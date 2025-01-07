import yfinance as yf
from datetime import datetime

def get_ticker_data(symbol: str) -> str:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    text = f"""---- {info.get('shortName', 'N/A')} ({symbol}) Financial Sheet ----

** Date : {current_date}

# Company Overview:
Symbol: {info.get('symbol', 'N/A')}
Company Name: {info.get('shortName', 'N/A')}
Current Price: ${info.get('currentPrice', 'N/A')}
Market Cap: ${info.get('marketCap', 'N/A')}
Industry: {info.get('industry', 'N/A')}
Sector: {info.get('sector', 'N/A')}
Country: {info.get('country', 'N/A')}
Employees: {info.get('fullTimeEmployees', 'N/A')}

# Financial Ratios:
Trailing P/E: {info.get('trailingPE', 'N/A')}
Forward P/E: {info.get('forwardPE', 'N/A')}
Price to Sales (TTM): {info.get('priceToSalesTrailing12Months', 'N/A')}
Enterprise/Revenue: {info.get('enterpriseToRevenue', 'N/A')}
Enterprise/EBITDA: {info.get('enterpriseToEbitda', 'N/A')}
Return on Assets: {info.get('returnOnAssets', 'N/A')}
Return on Equity: {info.get('returnOnEquity', 'N/A')}
Price to Book: {info.get('priceToBook', 'N/A')}

# Company Valuation:
Total Revenue: ${info.get('totalRevenue', 'N/A')}
Net Income: ${info.get('netIncomeToCommon', 'N/A')}``
Revenue Per Share: ${info.get('revenuePerShare', 'N/A')}
Total Cash: ${info.get('totalCash', 'N/A')}
Free cash flow: ${info.get('freeCashflow', 'N/A')}
Enterprise Value: ${info.get('enterpriseValue', 'N/A')}
Book Value: {info.get('bookValue', 'N/A')}

# Financial Profitabilty and Growth :
Quarterly Revenue Growth: {info.get('revenueGrowth', 'N/A')}
Revenue Growth: {info.get('revenueGrowth', 'N/A')}
Earnings Growth: {info.get('earningsGrowth', 'N/A')}
Gross Margins: {info.get('grossMargins', 'N/A')}
Operating Margins: {info.get('operatingMargins', 'N/A')}
EBITDA Margins: {info.get('ebitdaMargins', 'N/A')}
Profit Margins: {info.get('profitMargins', 'N/A')}

# Market Price Action :
Price: ${info.get('currentPrice', 'N/A')}
Year Range: ${info.get('fiftyTwoWeekLow', 'N/A')} - ${info.get('fiftyTwoWeekHigh', 'N/A')}
Beta: {info.get('beta', 'N/A')}
Volume: {info.get('volume', 'N/A')}
Average Volume: {info.get('averageVolume', 'N/A')}

# Dividend Information:
Dividend Rate: ${info.get('dividendRate', 'N/A')}
Dividend Yield: {info.get('dividendYield', 'N/A')}
Payout Ratio: {info.get('payoutRatio', 'N/A')}
5Y Avg Dividend Yield: {info.get('fiveYearAvgDividendYield', 'N/A')}

# Debt Overview:
Total Debt: ${info.get('totalDebt', 'N/A')}
Quick Ratio: {info.get('quickRatio', 'N/A')}
Current Ratio: {info.get('currentRatio', 'N/A')}
Debt to Equity: {info.get('debtToEquity', 'N/A')}

# Analyst Recommendations:
Target Price Range (low - high): ${info.get('targetLowPrice', 'N/A')} - ${info.get('targetHighPrice', 'N/A')}
Mean Target: ${info.get('targetMeanPrice', 'N/A')}
Recommendation: {info.get('recommendationKey', 'N/A')}
Number of Analysts: {info.get('numberOfAnalystOpinions', 'N/A')}

# Risk :
Audit Risk: {info.get('auditRisk', 'N/A')}
Board Risk: {info.get('boardRisk', 'N/A')}
Compensation Risk: {info.get('compensationRisk', 'N/A')}
DhareHolder Rights Risk: {info.get('shareHolderRightsRisk', 'N/A')}
Overall Risk: {info.get('overallRisk', 'N/A')}

# Short Interest:
Float Shares: {info.get('floatShares', 'N/A')}
Shares Outstanding: {info.get('sharesOutstanding', 'N/A')}
Shares Short: {info.get('sharesShort', 'N/A')}
Short Ratio: {info.get('shortRatio', 'N/A')}
Short % of Float: {info.get('shortPercentOfFloat', 'N/A')}
Institutional Holdings: {info.get('heldPercentInstitutions', 'N/A')}"""

    return text
