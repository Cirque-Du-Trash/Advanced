from sqlalchemy import inspect

def get_schemas(engine):
    return inspect(engine).get_schema_names()

def get_tables(engine, schema):
    return inspect(engine).get_table_names(schema=schema)

def get_views(engine, schema):
    return inspect(engine).get_view_names(schema=schema)

def _get_columns_info(inspector, table_name, schema):
    return [
        {
            "name": col['name'],
            "type": str(col['type']),
            "nullable": col['nullable'],
            "primary_key": col.get('primary_key', False),
            "comment": col.get('comment', '')
        }
        for col in inspector.get_columns(table_name, schema=schema)
    ]

def get_table_info(engine, schema):
    inspector = inspect(engine)
    return {
        table_name: {
            "columns": _get_columns_info(inspector, table_name, schema),
            "indexes": inspector.get_indexes(table_name, schema=schema)
        }
        for table_name in inspector.get_table_names(schema=schema)
    }

def get_view_info(engine, schema):
    inspector = inspect(engine)
    return {
        view_name: {
            "columns": _get_columns_info(inspector, view_name, schema)
        }
        for view_name in inspector.get_view_names(schema=schema)
    }

def get_column_info(engine, table_name, schema):
    return _get_columns_info(inspect(engine), table_name, schema)

def get_ddl(engine, table_name, schema):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name, schema=schema)
    column_defs = []
    
    for col in columns:
        col_def = f"  {col['name']} {col['type']}"
        if not col['nullable']:
            col_def += " NOT NULL"
        if col.get('primary_key', False):
            col_def += " PRIMARY KEY"
        column_defs.append(col_def)
    
    return f"CREATE TABLE {schema}.{table_name} (\n" + ',\n'.join(column_defs) + "\n);"