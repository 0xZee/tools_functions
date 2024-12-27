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
tickers_list = [
    'AAPL', 'NVDA', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'AVGO', 'WMT',
    'ORCL', 'COST', 'NFLX', 'CRM', 'KO', 'CSCO', 'NOW', 'IBM', 'DIS', 'BABA',
    'AMD', 'ADBE', 'GE', 'PLTR', 'QCOM', 'RTX', 'NEE', 'ANET', 'ARM', 'UBER',
    'PANW', 'NKE', 'BYDDY', 'MU', 'MRVL', 'SPOT', 'INTC', 'PYPL', 'CRWD',
    'MSTR', 'FTNT', 'WDAY', 'CEG', 'COIN', 'JD', 'SQ', 'SNOW', 'DDOG', 'VST',
    'NET', 'RDDT', 'ZS', 'IOT', 'ALAB', 'PSTG', 'AFRM', 'GRAB', 'MDB', 'SMCI',
    'NTNX', 'OKTA', 'RIVN', 'RKLB', 'RBRK', 'XPEV', 'MNDY', 'ROKU', 'EXAS',
    'PSN', 'IONQ', 'ENPH', 'GTLB', 'NIO', 'AES', 'SOUN', 'S', 'PATH', 'ASTS',
    'LYFT', 'ACHR', 'BE', 'BEPC', 'PONY', 'VKTX', 'AI', 'RGTI', 'AVAV', 'BRZE',
    'GSAT', 'CRSP', 'OKLO', 'QS', 'KC', 'RXRX', 'QBTS', 'QUBT', 'BEAM', 'SMR',
    'APLD', 'TXG', 'LUNR', 'TDOC', 'SDGR', 'FSLY', 'TLRY', 'PL', 'DQ', 'OLO',
    'NTLA', 'RDW', 'KULR', 'BBAI', 'NNE', 'RZLV', 'SERV', 'LAES', 'DNA', 'PACB',
    'ARQQ', 'CHPT', 'QSI', 'NNOX', 'CGC', 'QMCO', 'SPIR', 'BKSY', 'RR', 'VLN',
    'ACB', 'QNCCF', 'EDIT', 'NKLA', 'LLAP', 'MDAI'
]
tickers_list_old = ["AVGO", "LUNR", "TLRY", "PL", "DQ", "OLO", "QBTS", "NTLA", "TSLA", "FSLY", "SDGR", "META", "TXG", "TDOC", "APLD", "ENPH", "PSN", "BYDDY", "MRVL", "EXAS", "XPEV", "NKE", "MU", "RBRK", "RKLB", "NKLA", "EDIT", "PANW", "OKTA", "RIVN", "NEE", "RTX", "ARM", "NTNX", "PLTR", "QCOM", "GE", "KC", "SMR", "GOOGL", "BEAM", "AMZN", "RGTI", "QS", "OKLO", "RXRX", "MDB", "PSTG", "AMD", "BABA", "GRAB", "SMCI", "IBM", "AFRM", "VLN", "NOW", "CSCO", "ADBE", "ACB", "IOT", "KO", "ARQQ", "MSFT", "NVDA", "ACHR", "AAPL", "CRSP", "ZS", "BKSY", "NET", "GSAT", "BRZE", "AVAV", "NNOX", "COST", "CGC", "VST", "ORCL", "AI", "VKTX", "BEPC", "BE", "LLAP", "DDOG", "SNOW", "CHPT", "DNA", "SOUN", "ASTS", "JD", "SERV", "PACB", "IONQ", "S", "PATH", "BBAI", "FTNT", "WMT", "COIN", "QUBT", "BHAT", "RDW", "INTC", "GTLB", "AES", "NIO", "CRWD", "RR", "PYPL", "NNE", "QMCO", "LAES", ]
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
#job = client.load_table_from_dataframe(dataset, table_id)
#job.result()  # Wait for the job to complete

# upload df to table BigQuery
dataset.to_gbq(destination_table=table_id, project_id=project_id, if_exists='replace',  credentials=None)

# check table info
table = client.get_table(table_id)
print(f"# Loaded {table.num_rows} rows to Table : {table_id}")
print(f"# Table Schema : {table.schema}")
