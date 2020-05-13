import sys
import matplotlib.pyplot as plt

import yfinance as yf

from plots import plot_price

sym = sys.argv[1].upper()
graph = sys.argv[2]

data = yf.download(sym, period="6mo", progress=False)

if graph == "price":
    fig, ax = plt.subplots(figsize=(12, 18))
    plot_price(ax, data)
elif graph == "volume":
    pass
plt.show()
