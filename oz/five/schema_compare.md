# 스키마 비교 결과

## 스키마 비교: airportdb.airline vs airportdb_mongo.airlines

| 필드 | MySQL 타입 | MongoDB 타입 |
|-------|------------|---------------|
| airline_id | SMALLINT | int |
| iata | CHAR(2) COLLATE "utf8mb4_unicode_ci" | str |
| airlinename | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| base_airport | SMALLINT | int |
| airplane_id | INTEGER | int |
| capacity | MEDIUMINT | int |
| type_id | INTEGER | int |
| airline_id | INTEGER | int |
| type_id | INTEGER | int |
| identifier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| airport_id | SMALLINT | int |
| iata | CHAR(3) COLLATE "utf8mb4_unicode_ci" | str |
| icao | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| airport_id | SMALLINT | int |
| name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| latitude | DECIMAL(11, 8) | float |
| longitude | DECIMAL(11, 8) | float |
| airport_id | SMALLINT | int |
| hops | INTEGER | int |
| booking_id | INTEGER | int |
| flight_id | INTEGER | int |
| seat | CHAR(4) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| price | DECIMAL(10, 2) | float |
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
| flight_id | INTEGER | int |
| flightno | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from | SMALLINT | int |
| to | SMALLINT | int |
| departure | DATETIME | str |
| arrival | DATETIME | str |
| airline_id | SMALLINT | int |
| airplane_id | INTEGER | int |
| flight_log_id | INTEGER | int |
| log_date | DATETIME | str |
| user | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| flight_id | INTEGER | int |
| flightno_old | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| flightno_new | CHAR(8) COLLATE "utf8mb4_unicode_ci" | str |
| from_old | SMALLINT | int |
| to_old | SMALLINT | int |
| from_new | SMALLINT | int |
| to_new | SMALLINT | int |
| departure_old | DATETIME | str |
| arrival_old | DATETIME | str |
| departure_new | DATETIME | str |
| arrival_new | DATETIME | str |
| airplane_id_old | INTEGER | int |
| airplane_id_new | INTEGER | int |
| airline_id_old | SMALLINT | int |
| airline_id_new | SMALLINT | int |
| comment | VARCHAR(200) COLLATE "utf8mb4_unicode_ci" | str |
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
| passenger_id | INTEGER | int |
| passportno | CHAR(9) COLLATE "utf8mb4_unicode_ci" | str |
| firstname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| lastname | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| passenger_id | INTEGER | int |
| birthdate | DATE | str |
| sex | CHAR(1) COLLATE "utf8mb4_unicode_ci" | str |
| street | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| zip | SMALLINT | int |
| country | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| emailaddress | VARCHAR(120) COLLATE "utf8mb4_unicode_ci" | str |
| telephoneno | VARCHAR(30) COLLATE "utf8mb4_unicode_ci" | str |
| log_date | DATE | str |
| time | TIME | int |
| station | INTEGER | int |
| temp | DECIMAL(3, 1) | float |
| humidity | DECIMAL(4, 1) | float |
| airpressure | DECIMAL(10, 2) | float |
| wind | DECIMAL(5, 2) | float |
| weather | ENUM | str |
| winddirection | SMALLINT | int |
| customer_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| date_of_birth | DATE | str |
| registration_date | TIMESTAMP | str |
| department_id | INTEGER | int |
| department_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| manager_id | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| budget | DECIMAL(15, 2) | float |
| start_date | DATE | str |
| end_date | DATE | str |
| employee_id | INTEGER | int |
| first_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| hire_date | DATE | str |
| department | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| salary | DECIMAL(10, 2) | float |
| inventory_id | INTEGER | int |
| product_id | INTEGER | int |
| quantity | INTEGER | int |
| location | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| last_updated | TIMESTAMP | str |
| reorder_level | INTEGER | int |
| reorder_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| invoice_id | INTEGER | int |
| order_id | INTEGER | int |
| invoice_date | DATE | str |
| due_date | DATE | str |
| total_amount | DECIMAL(10, 2) | float |
| tax_amount | DECIMAL(10, 2) | float |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| payment_date | DATE | str |
| order_id | INTEGER | int |
| customer_id | INTEGER | int |
| order_date | DATE | str |
| order_status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| total_amount | DECIMAL(10, 2) | float |
| payment_method | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| shipping_address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| delivery_date | DATE | str |
| product_id | INTEGER | int |
| product_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| category | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| price | DECIMAL(10, 2) | float |
| stock_quantity | INTEGER | int |
| supplier_id | INTEGER | int |
| description | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| added_date | TIMESTAMP | str |
| review_id | INTEGER | int |
| product_id | INTEGER | int |
| customer_id | INTEGER | int |
| rating | INTEGER | int |
| review_text | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| review_date | TIMESTAMP | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| response | TEXT COLLATE "utf8mb4_unicode_ci" | str |
| shipment_id | INTEGER | int |
| order_id | INTEGER | int |
| shipment_date | DATE | str |
| carrier | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| tracking_number | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| status | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| estimated_arrival | DATE | str |
| actual_arrival | DATE | str |
| supplier_id | INTEGER | int |
| supplier_name | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| contact_name | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| contact_email | VARCHAR(100) COLLATE "utf8mb4_unicode_ci" | str |
| phone_number | VARCHAR(20) COLLATE "utf8mb4_unicode_ci" | str |
| address | VARCHAR(255) COLLATE "utf8mb4_unicode_ci" | str |
| city | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |
| country | VARCHAR(50) COLLATE "utf8mb4_unicode_ci" | str |