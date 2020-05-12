import sys

import yfinance as yf

from plots import plot_price

sym = sys.argv[1].upper()
graph = sys.argv[2]

data = yf.download(sym, period="6mo", progress=False)

if graph == "price":
    plot_price(data)
