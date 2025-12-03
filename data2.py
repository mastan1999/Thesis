import yfinance as yf
import pandas as pd

ticker = "BTF"

data = yf.download(ticker, start="2021-10-01", end="2025-01-01")
data.to_csv("BTF.csv")

print("BTF data saved!")
