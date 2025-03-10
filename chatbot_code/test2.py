import yfinance as yf
from yahooquery import search

def get_stock_symbol(company_name):
    result = search(company_name)
    quotes = result.get("quotes", [])
    if quotes:
        return quotes[0]["symbol"]
    return None

print(get_stock_symbol("APPLE"))