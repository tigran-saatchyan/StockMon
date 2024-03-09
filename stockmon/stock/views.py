from django.core.cache import cache
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from .models import Stock
from .services import Finance


def get_nasdaq_symbols(request):
    cached_data = cache.get('nasdaq_symbols')

    if not cached_data:
        data = Stock.objects.all()
        cache.set('nasdaq_symbols', data, 60 * 60)
    else:
        data = cached_data

    return render(
        request, "stock/symbols.html",
        {"symbols": data, "title": "Nasdaq Symbols"}
    )


def upload_csv(request):
    if request.method == "POST" and request.FILES["csv_file"]:
        csv_file = request.FILES["csv_file"]
        with transaction.atomic():
            Stock.objects.all().delete()
            Stock.create_from_csv(csv_file)
        cache.delete('nasdaq_symbols')
        return HttpResponse("CSV file uploaded successfully.")


def get_stock_info(request, symbol):
    if request.method == "GET":
        finance = Finance(symbol)
        info = finance.get_info()
        return render(
            request, "stock/company_profile.html",
            {"company_profile": info, "title": info.get("shortName")}
        )


def get_stock_history(request, symbol):
    if request.method == "GET":
        finance = Finance(symbol)
        history = finance.get_history()
        return render(
            request, "stock/history.html",
            {"history": history, "title": f"{symbol} History"}
        )

# msft = yf.Ticker("MSFT")

# # get all stock info
# msft.info
# print(msft.info)

# # get historical market data
# hist = msft.history(period="1mo")
# print(hist)

# # show meta information about the history (requires history() to be called
# first)
# msft.history_metadata

# # show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# # show share count
# msft.get_shares_full(start="2024-02-08", end=None)

# # show financials:
# # - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# # - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# # - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# # see `Ticker.get_income_stmt()` for more options

# # show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders
# msft.insider_transactions
# msft.insider_purchases
# msft.insider_roster_holders

# # show recommendations
# msft.recommendations
# msft.recommendations_summary
# msft.upgrades_downgrades

# # Show future and historic earnings dates, returns at most next 4 quarters
# and last 8 quarters by default.
# # Note: If more are needed use msft.get_earnings_dates(limit=XX) with
# increased limit argument.
# msft.earnings_dates

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin

# # show options expirations
# msft.options

# # show news
# msft.news

# # get option chain for specific expiration
# opt = msft.option_chain('2024-03-08')
# # data available via: opt.calls, opt.puts

# # Multiple tickers
# tickers = yf.Tickers('msft aapl goog')

# # access each ticker using (example)
# tickers.tickers['MSFT'].info
# tickers.tickers['AAPL'].history(period="1mo")
# tickers.tickers['GOOG'].actions
