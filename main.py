# main.py

import logging
import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TOKEN
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.menu_handler import handle_menu  # وارد کردن handle_menu از فایل جدید
import nest_asyncio
from menus import MENU_OPTIONS

nest_asyncio.apply()

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# هندلر برای شروع ربات
async def start(update, context):
    keyboard = MENU_OPTIONS["main_menu"]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)

# تابع اصلی ربات
async def main():
    # ایجاد شیء برنامه
    application = Application.builder().token(TOKEN).build()

    # افزودن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_menu))  # استفاده از هندلر جدید

    # اجرای ربات
    await application.run_polling()

if __name__ == "__main__":
    import sys

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == "Cannot close a running event loop":
            loop = asyncio.get_event_loop()
            loop.create_task(main())
        else:
            raise
