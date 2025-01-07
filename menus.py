# menus.py

from telegram import InlineKeyboardButton

# تابع برای ساخت دکمه بازگشت
def back_button(target_menu):
    return [InlineKeyboardButton("🔙 بازگشت", callback_data=target_menu)]

# تعریف منوها به صورت دیکشنری
MENU_OPTIONS = {
    "main_menu": [
        [InlineKeyboardButton("💸 ارز", callback_data="currency")],
        [InlineKeyboardButton("ℹ️ درباره ربات", callback_data="about")],
        [InlineKeyboardButton("📞 ارتباط باما", callback_data="help")],
    ],
    "currency": [
        [InlineKeyboardButton("💵 دلار/تتر", callback_data="usdt")],
        back_button("main_menu"),  # دکمه بازگشت
    ],
    "usdt": [
        back_button("currency"),  # دکمه بازگشت
    ],
    "about": [
        back_button("main_menu"),  # دکمه بازگشت
    ],
    "help": [
        back_button("main_menu"),  # دکمه بازگشت
    ],
}
