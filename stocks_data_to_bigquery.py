from google.cloud import bigquery
import yfinance as yf
import pandas as pd


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


# Example usage:
tickers_list = ["AVGO", "LUNR", "TLRY", "PL", "DQ", "OLO", "QBTS", "NTLA", "TSLA", "FSLY", "SDGR", "META", "TXG", "TDOC", "APLD", "ENPH", "PSN", "BYDDY", "MRVL", "EXAS", "XPEV", "NKE", "MU", "RBRK", "RKLB", "NKLA", "EDIT", "PANW", "OKTA", "RIVN", "NEE", "RTX", "ARM", "NTNX", "PLTR", "QCOM", "GE", "KC", "SMR", "GOOGL", "BEAM", "AMZN", "RGTI", "QS", "OKLO", "RXRX", "MDB", "PSTG", "AMD", "BABA", "GRAB", "SMCI", "IBM", "AFRM", "VLN", "NOW", "CSCO", "ADBE", "ACB", "IOT", "KO", "ARQQ", "MSFT", "NVDA", "ACHR", "AAPL", "CRSP", "ZS", "BKSY", "NET", "GSAT", "BRZE", "AVAV", "NNOX", "COST", "CGC", "VST", "ORCL", "AI", "VKTX", "BEPC", "BE", "LLAP", "DDOG", "SNOW", "CHPT", "DNA", "SOUN", "ASTS", "JD", "SERV", "PACB", "IONQ", "S", "PATH", "BBAI", "FTNT", "WMT", "COIN", "QUBT", "BHAT", "RDW", "INTC", "GTLB", "AES", "NIO", "CRWD", "RR", "PYPL", "NNE", "QMCO", "LAES", ]
keys_list = ['symbol', 'shortName', 'country','industry','sector','currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'priceToBook', 'debtToEquity','shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'beta', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'targetMeanPrice', 'targetHighPrice', 'recommendationKey','returnOnEquity', 'totalRevenue', 'freeCashflow', 'totalDebt', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins','trailingPegRatio']

# Get data
dataset = get_stock_data(tickers_list, keys_list)

###### BIGQURY - google Auth ######
#from google.colab import auth
#auth.authenticate_user()
# gcloud auth for webapp
#!gcloud auth application_default login

# bq client
client = bigquery.Client()

# Configure BigQuery dataset, table
project_id = GOOGLE_PROJ_ID # Replace with your Google Cloud project ID
dataset_name = 'ds_stx'    # Replace with your dataset name
table_name = 'table_stx_202412'        # Replace with your desired table name
# Full table ID
table_id = f"{project_id}.{dataset_name}.{table_name}"

# run ingesting job
job = client.load_table_from_dataframe(dataset, table_id)

job.result()  # Wait for the job to complete

# check table info
table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows to {table_id}")
print(table.schema)