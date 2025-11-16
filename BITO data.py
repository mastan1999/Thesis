import yfinance as yf
import pandas as pd

# 1. تعریف نماد (Ticker) صندوق و بازه زمانی
ticker_symbol = "BITO"
start_date = "2023-01-01"
end_date = pd.Timestamp.now().strftime('%Y-%m-%d') # تاریخ امروز

print(f"در حال استخراج دیتای تاریخی برای نماد: {ticker_symbol} از تاریخ {start_date}...")

# 2. دریافت دیتای تاریخی
try:
    # yf.download به طور خودکار داده ها را از Yahoo Finance دانلود می کند
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    
    # 3. تمیزکاری و آماده سازی دیتا
    if not data.empty:
        # فقط ستون های مهم را نگه می داریم
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        # ستون Ticker را اضافه می کنیم
        data.insert(0, 'Ticker', ticker_symbol)
        
        print("\nنمونه ای از 5 سطر اول داده های استخراج شده:")
        print(data.head())
        
        # 4. ذخیره سازی دیتا در فایل CSV
        file_name = f"{ticker_symbol}_Closing_Prices.csv"
        data.to_csv(file_name)
        print(f"\nداده ها با موفقیت در فایل {file_name} ذخیره شدند.")
    else:
        print("خطا: دیتایی برای نماد مورد نظر یافت نشد.")
        
except Exception as e:
    print(f"یک خطا در حین اجرای کد رخ داد: {e}")