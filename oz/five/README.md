# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane vs airportdb_mongo.airplanes

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.airplane_type vs airportdb_mongo.airplane_types

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport vs airportdb_mongo.airports

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_geo vs airportdb_mongo.airport_geos

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.airport_reachable vs airportdb_mongo.airport_reachables

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.booking vs airportdb_mongo.bookings

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: airportdb.employee vs airportdb_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(8, 2) | float |
| department | ENUM | str |
| username | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| password | CHAR(32) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight vs airportdb_mongo.flights

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | datetime |
| arrival | DATETIME | datetime |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.flight_log vs airportdb_mongo.flight_logs

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flight_log_id | INTEGER | int |
| log_date | DATETIME | datetime |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | datetime |
| arrival_old | DATETIME | datetime |
| departure_new | DATETIME | datetime |
| arrival_new | DATETIME | datetime |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.flightschedule vs airportdb_mongo.flight_schedules

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | TIME | int |
| arrival | TIME | int |
| airline_id | SMALLINT | int |
| monday | TINYINT | int |
| tuesday | TINYINT | int |
| wednesday | TINYINT | int |
| thursday | TINYINT | int |
| friday | TINYINT | int |
| saturday | TINYINT | int |
| sunday | TINYINT | int |
# 스키마 비교 결과

## 스키마 비교: airportdb.passenger vs airportdb_mongo.passengers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.passengerdetails vs airportdb_mongo.passenger_details

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: airportdb.weatherdata vs airportdb_mongo.weather_data

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
# 스키마 비교 결과

## 스키마 비교: oz.customers vs oz_mongo.customers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
# 스키마 비교 결과

## 스키마 비교: oz.departments vs oz_mongo.departments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.employees vs oz_mongo.employees

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
# 스키마 비교 결과

## 스키마 비교: oz.inventory vs oz_mongo.inventory

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | datetime |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
# 스키마 비교 결과

## 스키마 비교: oz.invoices vs oz_mongo.invoices

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.orders vs oz_mongo.orders

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.products vs oz_mongo.products

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | datetime |
# 스키마 비교 결과

## 스키마 비교: oz.reviews vs oz_mongo.reviews

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | datetime |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
# 스키마 비교 결과

## 스키마 비교: oz.shipments vs oz_mongo.shipments

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
# 스키마 비교 결과

## 스키마 비교: oz.suppliers vs oz_mongo.suppliers

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
