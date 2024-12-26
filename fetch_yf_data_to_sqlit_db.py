import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime

def get_stock_data(tickers_list, keys_list):
    # Initialize empty list to store data
    data_list = []
    
    # Fetch data for each ticker
    for ticker in tickers_list:
        try:
            # Get stock info
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Create a dictionary with requested keys
            stock_dict = {}
            for key in keys_list:
                stock_dict[key] = info.get(key, None)
            
            data_list.append(stock_dict)
            
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
    
    # Convert to DataFrame
    df = pd.DataFrame(data_list)
    return df

def save_to_sqlite(df, database_name='stocks_database.db'):
    # Create SQLite connection
    conn = sqlite3.connect(database_name)
    
    # Save data to SQLite with timestamp
    table_name = f'stocks_data_{datetime.now().strftime("%Y%m%d")}'
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    return conn, table_name

# List of tickers and fields :
############################
tickers_list = ["VHAI", "AVGO", "LUNR", "TLRY", "PL", "DQ", "OLO", "QBTS", "NTLA", "TSLA", "FSLY", "SDGR", "META", "TXG", "TDOC", "APLD", "ENPH", "PSN", "BYDDY", "MRVL", "EXAS", "XPEV", "NKE", "MU", "RBRK", "RKLB", "NKLA", "EDIT", "PANW", "OKTA", "RIVN", "NEE", "RTX", "ARM", "NTNX", "PLTR", "QCOM", "GE", "KC", "SMR", "GOOGL", "BEAM", "AMZN", "RGTI", "QS", "OKLO", "RXRX", "MDB", "PSTG", "AMD", "BABA", "GRAB", "SMCI", "IBM", "AFRM", "VLN", "NOW", "CSCO", "ADBE", "ACB", "IOT", "KO", "ARQQ", "MSFT", "NVDA", "ACHR", "AAPL", "CRSP", "ZS", "BKSY", "NET", "GSAT", "BRZE", "AVAV", "NNOX", "COST", "CGC", "VST", "ORCL", "AI", "VKTX", "BEPC", "BE", "LLAP", "DDOG", "SNOW", "CHPT", "DNA", "SOUN", "ASTS", "JD", "SERV", "PACB", "IONQ", "S", "PATH", "BBAI", "FTNT", "WMT", "COIN", "QUBT", "BHAT", "RDW", "INTC", "GTLB", "AES", "NIO", "CRWD", "RR", "PYPL", "NNE", "QMCO"]
keys_list = ['symbol', 'shortName', 'industryKey','currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'priceToBook', 'debtToEquity','shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'beta', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'targetMeanPrice', 'targetHighPrice', 'recommendationKey','returnOnEquity', 'totalRevenue', 'freeCashflow', 'totalDebt', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins','trailingPegRatio']

# database sqlite
############################
database_name='stocks_database.db'

# RUN
############################

# Get data
df = get_stock_data(tickers_list, keys_list)

# Save to SQLite
conn, table_name = save_to_sqlite(df, database_name)

# Example queries
def example_queries(conn, table_name):
    cursor = conn.cursor()
    
    # Example 1: Get stocks with market cap > 1B
    print("\nStocks with market cap > 1T:")
    query1 = f"SELECT symbol, shortName, marketCap FROM {table_name} WHERE marketCap > 1000000000000"
    print(pd.read_sql_query(query1, conn))
    
    # Example 2: Get top 5 stocks by current price
    print("\nTop 5 stocks by price:")
    query2 = f"SELECT symbol, currentPrice FROM {table_name} ORDER BY currentPrice DESC LIMIT 5"
    print(pd.read_sql_query(query2, conn))
    
    # Example 3: Get average PE ratio
    print("\nAverage PE ratio:")
    query3 = f"SELECT AVG(trailingPE) as avg_pe FROM {table_name} WHERE trailingPE IS NOT NULL"
    print(pd.read_sql_query(query3, conn))

# Print info
print(f"# SQLite3 Database : stocks_database.db")
print(f"# Data saved to Table : {table_name} in {conn}")
print("---------------------------------")
# Run example queries
example_queries(conn, table_name)

# Close connection
conn.close()
