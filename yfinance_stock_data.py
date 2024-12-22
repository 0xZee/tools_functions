# pip install yfinance
import yfinance as yf

def get_stock_data(tickers, list_keys):
  data = []
  data_0 = []
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    sel_info = {k: v for k, v in info.items() if k in list_keys}
    for key in to_drop:
      info.pop(key, None)
    data.append(sel_info)
    data_0.append(info)
  return data

tickers=["PLTR","IONQ", "NVDA", "ASTS", "RKLB", "QBTS", "RXRX", "AMD", "LAES", "GSAT", "LUNR"]

tickers_list = ["VHAI", "AVGO", "LUNR", "TLRY", "PL", "DQ", "OLO", "QBTS", "NTLA", "TSLA", "FSLY", "SDGR", "META", "TXG", "TDOC", "APLD", "ENPH", "PSN", "BYDDY", "MRVL", "EXAS", "XPEV", "NKE", "MU", "RBRK", "RKLB", "NKLA", "EDIT", "PANW", "OKTA", "RIVN", "NEE", "RTX", "ARM", "NTNX", "PLTR", "QCOM", "GE", "KC", "SMR", "GOOGL", "BEAM", "AMZN", "RGTI", "QS", "OKLO", "RXRX", "MDB", "PSTG", "AMD", "BABA", "GRAB", "SMCI", "IBM", "AFRM", "VLN", "NOW", "CSCO", "ADBE", "ACB", "IOT", "KO", "ARQQ", "MSFT", "NVDA", "ACHR", "AAPL", "CRSP", "ZS", "BKSY", "NET", "GSAT", "BRZE", "AVAV", "NNOX", "COST", "CGC", "VST", "ORCL", "AI", "VKTX", "BEPC", "BE", "LLAP", "DDOG", "SNOW", "CHPT", "DNA", "SOUN", "ASTS", "JD", "SERV", "PACB", "IONQ", "S", "PATH", "BBAI", "FTNT", "WMT", "COIN", "QUBT", "BHAT", "RDW", "INTC", "GTLB", "AES", "NIO", "CRWD", "RR", "PYPL", "NNE", "QMCO"]
keys_list = ['symbol', 'shortName','currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'targetMeanPrice', 'targetHighPrice', 'returnOnEquity', 'totalRevenue', 'freeCashflow', 'totalDebt', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'trailingPegRatio']

to_drop = ['address1', 'address2', 'industryDisp', 'industryKey', 'companyOfficers']
list_keys = ['symbol', 'currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'targetHighPrice', 'returnOnEquity' ]
stock_data = get_stock_data(tickers_list, keys_list)
stock_data[0]


##
# Create text list and metadata from stock data
texts = [str(stock) for stock in stock_data]
metadatas = [
    {
        "symbol": stock.get('symbol', 'N/A'),
        "shortName": stock.get('shortName', 'N/A'),
        "currentPrice": stock.get('currentPrice', 'N/A')
    } 
    for stock in stock_data
]

# Print example of the first few items
print("All Texts (first 3):")
for text in texts[:3]:
    print(text)

print("\nMetadatas (first 3):")
for metadata in metadatas[:3]:
    print(metadata)
