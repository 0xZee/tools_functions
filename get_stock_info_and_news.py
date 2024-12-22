def get_stock_info_and_news(tickers):
    """
    Fetch stock info and news for a list of stock tickers and return as a DataFrame.

    Args:
        tickers (list): List of stock tickers.

    Returns:
        pd.DataFrame: DataFrame containing stock info and news.
    """
    data = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        news = stock.news

        data.append({
            "Ticker": ticker,
            "Info": info,
            "News": news
        })

    return pd.DataFrame(data)
