# Data Dictionary

## Customers Table
| Field | Type | Description |
|-------|------|-------------|
| customer_id | int | Unique customer identifier |
| age | int | Customer age in years |
| gender | str | Customer gender (M/F) |
| location | str | Customer location (Urban/Suburban/Rural) |
| registration_date | date | Date of customer registration |

## Transactions Table  
| Field | Type | Description |
|-------|------|-------------|
| transaction_id | int | Unique transaction identifier |
| customer_id | int | Foreign key to customers table |
| product_category | str | Product category |
| channel | str | Sales channel (Online/Mobile/Store) |
| price | float | Product price |
| quantity | int | Quantity purchased |
| transaction_date | date | Date of transaction |
| discount_applied | float | Discount percentage applied |
| revenue | float | Total revenue (calculated field) |
