import yfinance as yf
import pandas as pd

print("Initializing professional financial data pull...")

# 1. Target Ticker
ticker_symbol = "INFY.NS"
company = yf.Ticker(ticker_symbol)

# 2. Fetch Statements
inc_stmt = company.financials
bal_sheet = company.balance_sheet

# 3. Shape Data for Power BI (Transpose: Years become rows)
df_inc = inc_stmt.T.reset_index().rename(columns={'index': 'Date'})
df_bal = bal_sheet.T.reset_index().rename(columns={'index': 'Date'})

# 4. Clean Dates & Extract Year
df_inc['Year'] = pd.to_datetime(df_inc['Date']).dt.year
df_bal['Year'] = pd.to_datetime(df_bal['Date']).dt.year

# 5. Extract core metrics safely (Units will match company reporting - typically Crores/Millions)
inc_cols = ['Year', 'Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income']
bal_cols = ['Year', 'Current Assets', 'Current Liabilities', 'Stockholders Equity', 'Total Debt']

df_inc_filtered = df_inc[[col for col in inc_cols if col in df_inc.columns]].copy()
df_bal_filtered = df_bal[[col for col in bal_cols if col in df_bal.columns]].copy()

# 6. Merge into a clean Fact Table
master_fact_table = pd.merge(df_inc_filtered, df_bal_filtered, on='Year', how='outer')
master_fact_table['Company'] = "Infosys"

# Save uncleaned raw master dataset
master_fact_table.to_csv("infosys_powerbi_master.csv", index=False)
print("\n[SUCCESS] 'infosys_powerbi_master.csv' generated for Power BI modeling!")