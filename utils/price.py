# utils/price.py

import requests
import logging

logger = logging.getLogger(__name__)

def get_usdt_price():
    try:
        url = "https://api.nobitex.ir/v3/orderbook/USDTIRT"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok":
            # دریافت قیمت و فرمت کردن آن
            last_trade_price = int(data.get("lastTradePrice"))
            formatted_price = f"{last_trade_price:,}"  # سه‌رقم سه‌رقم با کاما
            return f"قیمت لحظه‌ای دلار/تتر: {formatted_price} ریال"
        else:
            return "خطا در دریافت اطلاعات قیمت!"
    except Exception as e:
        logger.error(f"Error fetching price: {e}")
        return "خطا در ارتباط با سرور!"
