# Data Directory

## Structure
- `raw/` - Original, unprocessed data files
- `processed/` - Cleaned and processed datasets
- `sample/` - Sample data for testing and demos

## Data Sources
- Synthetic e-commerce transaction data generated for analysis
- Customer demographics and behavior patterns
- Product categories and pricing information

## Data Dictionary
See `docs/data_dictionary.md` for detailed field descriptions.

## Usage
```python
# Load processed data
customers = pd.read_csv('data/processed/customers_clean.csv')
transactions = pd.read_csv('data/processed/transactions_clean.csv')
```
