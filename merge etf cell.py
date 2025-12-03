import pandas as pd

df_bito = pd.read_csv('BITO.csv')
df_bft = pd.read_csv('BTF.csv')

print(df_bito.columns)
print(df_bft.columns)

df_bito = pd.read_csv('BITO.csv')
df_bft = pd.read_csv('BTF.csv') 

# ستون مشترک فرضی: timestamp
merged = pd.merge(df_bito, df_bft, on=['Price', 'Close', 'High', 'Low', 'Open', 'Volume'], how='inner')

# ذخیره فایل مرج شده
merged.to_csv('merged.csv', index=False)
import pandas as pd
#برای مرج کردن داده‌های مالی، باید روی timestamp / date مرج کنی، نه روی قیمت‌ها.
df_bito = pd.read_csv('BITO.csv')
df_bft = pd.read_csv('BTF.csv')

print(df_bito.head())
print(df_bft.head())
