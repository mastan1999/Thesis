import pandas as pd

# نام فایل اصلی اکسل (نه CSV)
FILE_NAME = "672e88c7-dac6-4fcd-9069-18eef01a2c73-33.xlsx"
OUTPUT_FILE = "gbtc_premium_discount_result.csv"

def calculate_gbtc_premium(file_name, output_file):
    """ فایل GBTC را خوانده و ستون Premium/Discount را محاسبه می کند. """
    try:
        # ۱. بارگذاری فایل اکسل (.xlsx) و مشخص کردن شیت مورد نظر
        # شیت "Daily Performance" شامل NAV و Market Price است
        df = pd.read_excel(file_name, sheet_name='Daily Performance')

        print(f"فایل اکسل {file_name} و شیت 'Daily Performance' با موفقیت بارگذاری شد.")
        print("-" * 30)

        # ۲. تمیزکاری و آماده سازی ستون‌ها
        df = df.rename(columns={
            'Date': 'Date',
            'NAV Per Share': 'NAV_Per_Share',
            'Market Price Per Share': 'Market_Price'
        })

        # فیلتر کردن فقط برای نماد GBTC و ستون‌های مورد نیاز
        df_gbtc = df[df['OTC Ticker'] == 'GBTC'][['Date', 'NAV_Per_Share', 'Market_Price']].copy()
        
        # تبدیل ستون‌های قیمت و NAV به عدد و حذف ردیف‌های خالی
        df_gbtc['NAV_Per_Share'] = pd.to_numeric(df_gbtc['NAV_Per_Share'], errors='coerce')
        df_gbtc['Market_Price'] = pd.to_numeric(df_gbtc['Market_Price'], errors='coerce')
        df_gbtc.dropna(inplace=True)
        
        print(f"تعداد رکوردهای تمیز شده و آماده برای محاسبه: {len(df_gbtc)}")
        
        # ۳. محاسبه Premium/Discount
        # فرمول: (قیمت بازار - NAV) / NAV * 100
        df_gbtc['Premium_Discount_Pct'] = (
            (df_gbtc['Market_Price'] - df_gbtc['NAV_Per_Share']) / df_gbtc['NAV_Per_Share']
        ) * 100
        
        print("\nمحاسبه Premium/Discount با موفقیت انجام شد.")

        # ۴. ذخیره سازی نتیجه
        df_gbtc.to_csv(output_file, index=False) 
        
        print("-" * 30)
        print("✅ ۵ سطر آخر داده های محاسبه شده:")
        print(df_gbtc[['Date', 'Premium_Discount_Pct']].tail())
        print(f"✅ فایل نهایی شامل Premium/Discount در این مسیر ذخیره شد: {output_file}")

    except FileNotFoundError:
        print(f"❌ خطا: فایل {file_name} در مسیر پروژه یافت نشد.")
    except KeyError:
        print("❌ خطا: نام ستون‌ها یا شیت 'Daily Performance' اشتباه است. لطفاً نام شیت را در فایل اکسل بررسی کنید.")
    except Exception as e:
        print(f"❌ یک خطای عمومی رخ داد: {e}")

# اجرای تابع اصلی
calculate_gbtc_premium(FILE_NAME, OUTPUT_FILE)