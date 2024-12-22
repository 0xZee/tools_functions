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
to_drop = ['address1', 'address2', 'industryDisp', 'industryKey', 'companyOfficers']
list_keys = ['symbol', 'currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'targetHighPrice', 'returnOnEquity' ]
stock_data = get_stock_data(tickers, list_keys)
stock_data[0]
