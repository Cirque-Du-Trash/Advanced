

## Schema Comparison: airportdb.airline vs airportdb_mongo.airlines

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |


## Schema Comparison: airportdb.airplane vs airportdb_mongo.airplanes

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |


## Schema Comparison: airportdb.airplane_type vs airportdb_mongo.airplane_types

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |


## Schema Comparison: airportdb.airport vs airportdb_mongo.airports

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| airport_id | SMALLINT | Not present |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | Not present |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | Not present |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: airportdb.airport_geo vs airportdb_mongo.airport_geos

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| airport_id | SMALLINT | Not present |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| latitude | DECIMAL(11, 8) | Not present |
| longitude | DECIMAL(11, 8) | Not present |


## Schema Comparison: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| airport_id | SMALLINT | Not present |
| hops | INTEGER | Not present |


## Schema Comparison: airportdb.booking vs airportdb_mongo.bookings

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| booking_id | INTEGER | Not present |
| flight_id | INTEGER | Not present |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | Not present |
| passenger_id | INTEGER | Not present |
| price | DECIMAL(10, 2) | Not present |


## Schema Comparison: airportdb.employee vs airportdb_mongo.employees

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| employee_id | INTEGER | Not present |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| birthdate | DATE | Not present |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | Not present |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| zip | SMALLINT | Not present |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | Not present |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | Not present |
| salary | DECIMAL(8, 2) | Not present |
| department | ENUM | Not present |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | Not present |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: airportdb.flight vs airportdb_mongo.flights

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| flight_id | INTEGER | Not present |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | Not present |
| from | SMALLINT | Not present |
| to | SMALLINT | Not present |
| departure | DATETIME | Not present |
| arrival | DATETIME | Not present |
| airline_id | SMALLINT | Not present |
| airplane_id | INTEGER | Not present |


## Schema Comparison: airportdb.flight_log vs airportdb_mongo.flight_logs

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| flight_log_id | INTEGER | Not present |
| log_date | DATETIME | Not present |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| flight_id | INTEGER | Not present |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | Not present |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | Not present |
| from_old | SMALLINT | Not present |
| to_old | SMALLINT | Not present |
| from_new | SMALLINT | Not present |
| to_new | SMALLINT | Not present |
| departure_old | DATETIME | Not present |
| arrival_old | DATETIME | Not present |
| departure_new | DATETIME | Not present |
| arrival_new | DATETIME | Not present |
| airplane_id_old | INTEGER | Not present |
| airplane_id_new | INTEGER | Not present |
| airline_id_old | SMALLINT | Not present |
| airline_id_new | SMALLINT | Not present |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | Not present |
| from | SMALLINT | Not present |
| to | SMALLINT | Not present |
| departure | TIME | Not present |
| arrival | TIME | Not present |
| airline_id | SMALLINT | Not present |
| monday | TINYINT | Not present |
| tuesday | TINYINT | Not present |
| wednesday | TINYINT | Not present |
| thursday | TINYINT | Not present |
| friday | TINYINT | Not present |
| saturday | TINYINT | Not present |
| sunday | TINYINT | Not present |


## Schema Comparison: airportdb.passenger vs airportdb_mongo.passengers

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| passenger_id | INTEGER | Not present |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | Not present |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| passenger_id | INTEGER | Not present |
| birthdate | DATE | Not present |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | Not present |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| zip | SMALLINT | Not present |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | Not present |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: airportdb.weatherdata vs airportdb_mongo.weather_data

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| log_date | DATE | Not present |
| time | TIME | Not present |
| station | INTEGER | Not present |
| temp | DECIMAL(3, 1) | Not present |
| humidity | DECIMAL(4, 1) | Not present |
| airpressure | DECIMAL(10, 2) | Not present |
| wind | DECIMAL(5, 2) | Not present |
| weather | ENUM | Not present |
| winddirection | SMALLINT | Not present |


## Schema Comparison: oz.customers vs oz_mongo.customers

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| customer_id | INTEGER | Not present |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | Not present |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | Not present |
| date_of_birth | DATE | Not present |
| registration_date | TIMESTAMP | Not present |


## Schema Comparison: oz.departments vs oz_mongo.departments

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| department_id | INTEGER | Not present |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| manager_id | INTEGER | Not present |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| budget | DECIMAL(15, 2) | Not present |
| start_date | DATE | Not present |
| end_date | DATE | Not present |


## Schema Comparison: oz.employees vs oz_mongo.employees

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| employee_id | INTEGER | Not present |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | Not present |
| hire_date | DATE | Not present |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| salary | DECIMAL(10, 2) | Not present |


## Schema Comparison: oz.inventory vs oz_mongo.inventory

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| inventory_id | INTEGER | Not present |
| product_id | INTEGER | Not present |
| quantity | INTEGER | Not present |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| last_updated | TIMESTAMP | Not present |
| reorder_level | INTEGER | Not present |
| reorder_quantity | INTEGER | Not present |
| supplier_id | INTEGER | Not present |


## Schema Comparison: oz.invoices vs oz_mongo.invoices

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| invoice_id | INTEGER | Not present |
| order_id | INTEGER | Not present |
| invoice_date | DATE | Not present |
| due_date | DATE | Not present |
| total_amount | DECIMAL(10, 2) | Not present |
| tax_amount | DECIMAL(10, 2) | Not present |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| payment_date | DATE | Not present |


## Schema Comparison: oz.orders vs oz_mongo.orders

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| order_id | INTEGER | Not present |
| customer_id | INTEGER | Not present |
| order_date | DATE | Not present |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| total_amount | DECIMAL(10, 2) | Not present |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | Not present |
| delivery_date | DATE | Not present |


## Schema Comparison: oz.products vs oz_mongo.products

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| product_id | INTEGER | Not present |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| price | DECIMAL(10, 2) | Not present |
| stock_quantity | INTEGER | Not present |
| supplier_id | INTEGER | Not present |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | Not present |
| added_date | TIMESTAMP | Not present |


## Schema Comparison: oz.reviews vs oz_mongo.reviews

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| review_id | INTEGER | Not present |
| product_id | INTEGER | Not present |
| customer_id | INTEGER | Not present |
| rating | INTEGER | Not present |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | Not present |
| review_date | TIMESTAMP | Not present |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | Not present |


## Schema Comparison: oz.shipments vs oz_mongo.shipments

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| shipment_id | INTEGER | Not present |
| order_id | INTEGER | Not present |
| shipment_date | DATE | Not present |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| estimated_arrival | DATE | Not present |
| actual_arrival | DATE | Not present |


## Schema Comparison: oz.suppliers vs oz_mongo.suppliers

| Field | MySQL Type | MongoDB Type |
|-------|------------|---------------|
| supplier_id | INTEGER | Not present |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | Not present |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | Not present |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | Not present |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | Not present |
