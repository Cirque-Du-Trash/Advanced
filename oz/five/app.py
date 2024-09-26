from flask import Flask, jsonify, request
from sqlalchemy import create_engine, inspect, Table, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, DateTime, Boolean, SmallInteger, DECIMAL, Enum, Time, TIMESTAMP
from flask_restx import Api, Resource
from faker import Faker
import random
import string

faker = Faker()

app = Flask(__name__)

api = Api(app, version='1.0', title='Database API',
          description='A simple Database API for metadata retrieval')

db_config = {
    'username': 'root',
    'password': 'root', 
    'host': 'localhost',
    'port': '3306',
    'database_name': 'oz'
}

DATABASE_URI = f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}"
engine = create_engine(DATABASE_URI)

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

def generate_unique_string(existing_values, length=10):
    while True:
        unique_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if unique_str not in existing_values:
            return unique_str

def generate_unique_integer(existing_values, max_value=30000):
    unique_int = faker.random_int(min=0, max=max_value)
    while unique_int in existing_values:
        unique_int = faker.random_int(min=0, max=max_value)
    return unique_int

def generate_column_data(col_type, existing_values):
    if isinstance(col_type, Enum):
        return random.choice(col_type.enums)
    
    elif isinstance(col_type, String):
        length = col_type.length
        if length:
            if existing_values is not None:
                return generate_unique_string(existing_values, length)
            else:
                if length < 5:
                    return faker.word()[:length]
                else:
                    return faker.text(max_nb_chars=length)
        return faker.text(max_nb_chars=50)
    
    elif isinstance(col_type, (Integer, Float, SmallInteger)):
        return (generate_unique_integer(existing_values) if existing_values 
                else random.choice([0, 1]) if 'TINYINT' in str(col_type) 
                else faker.random_int(min=0, max=30000))
    
    elif isinstance(col_type, DECIMAL):
        return faker.latitude()
    
    elif isinstance(col_type, Boolean):
        return faker.boolean()
    
    elif isinstance(col_type, Date):
        return faker.date()
    
    elif isinstance(col_type, DateTime):
        return faker.date_time()
    
    elif isinstance(col_type, Time):
        return faker.time()
    
    return faker.text()

def generate_dummy_data(table, num_rows):
    data = []
    existing_values = {col.name: set() for col in table.columns}
    unique_columns = {col.name for col in table.primary_key.columns}
    
    for index in table.indexes:
        if index.unique:
            unique_columns.update(col.name for col in index.columns)
            
    for _ in range(num_rows):
        row = {}
        for col in table.columns:
            if col.autoincrement == True:
                continue
            elif isinstance(col.type, TIMESTAMP): #autoincrement와 CURRENT_TIME 속성을 가진 컬럼들은 skip
                continue
            else:
                if col.name in unique_columns:
                    row[col.name] = generate_column_data(col.type, existing_values[col.name])
                else:
                    row[col.name] = generate_column_data(col.type, None)

            existing_values[col.name].add(row[col.name])
        data.append(row)
        
        print(f"테이블 {table.name}에 대해 {len(data)}개의 데이터가 생성됨.")
    return data

# Swagger 문서화된 엔드포인트 추가
@api.route('/schemas')
class Schemas(Resource):
    def get(self):
        """Get all schemas"""
        return jsonify(get_schemas(engine))

@api.route('/schemas/<schema>/tables')
class Tables(Resource):
    def get(self, schema):
        """Get all tables in a schema"""
        return jsonify(get_tables(engine, schema))

@api.route('/schemas/<schema>/views')
class Views(Resource):
    def get(self, schema):
        """Get all views in a schema"""
        return jsonify(get_views(engine, schema))

@api.route('/schemas/<schema>/tables/<table_name>')
class TableInfo(Resource):
    def get(self, schema, table_name):
        """Get table info including columns and indexes"""
        return jsonify(get_table_info(engine, schema).get(table_name))

@api.route('/schemas/<schema>/views/<view_name>')
class ViewInfo(Resource):
    def get(self, schema, view_name):
        """Get view info including columns"""
        return jsonify(get_view_info(engine, schema).get(view_name))

@api.route('/schemas/<schema>/tables/<table_name>/columns')
class ColumnInfo(Resource):
    def get(self, schema, table_name):
        """Get column info for a table"""
        return jsonify(get_column_info(engine, table_name, schema))

@api.route('/schemas/<schema>/tables/<table_name>/ddl')
class DDL(Resource):
    def get(self, schema, table_name):
        """Get DDL for a table"""
        return jsonify(get_ddl(engine, table_name, schema))
    
@api.route('/schemas/<schema>/tables/<table_name>/dummy/<int:num_rows>')
class DummyData(Resource):
    def post(self, schema, table_name, num_rows):
        """Generate dummy data for a specific table"""
        metadata = MetaData()
        table = Table(table_name, metadata, autoload_with=engine, schema=schema)

        if table is None:
            return {"error": "Table not found"}, 404

        dummy_data = generate_dummy_data(table, num_rows)
        return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)
