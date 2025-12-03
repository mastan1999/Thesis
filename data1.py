import yfinance as yf
import pandas as pd

# نماد صندوق BITO
ticker = "BITO"

# دانلود داده از یاهو فایننس
data = yf.download(ticker, start="2021-10-01", end="2025-01-01")

# ذخیره در فایل CSV
data.to_csv("BITO.csv")

print("BITO data saved!")