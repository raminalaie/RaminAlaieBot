# handlers/menu_handler.py
from utils.price import get_usdt_price
from menus import MENU_OPTIONS
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # مدیریت تغییرات منو بر اساس انتخاب کاربر
    if query.data in MENU_OPTIONS:
        keyboard = MENU_OPTIONS[query.data]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if query.data == "currency":
            await query.edit_message_text("لطفاً یکی از گزینه‌های ارز را انتخاب کنید:", reply_markup=reply_markup)
        elif query.data == "usdt":
            price = get_usdt_price()
            await query.edit_message_text(price, reply_markup=reply_markup)
        elif query.data == "help":
            help_message = "برای ارتباط با سازنده ربات، لطفاً با آیدی @aramin79 تماس بگیرید."
            await query.edit_message_text(help_message, reply_markup=reply_markup)
        elif query.data == "about":
            about_message = (
                "این ربات در زمینه‌های مختلف فعالیت می‌کند، از جمله دریافت قیمت لحظه‌ای ارزها. "
                "به زودی ویژگی‌های جدیدی به ربات اضافه خواهند شد."
            )
            await query.edit_message_text(about_message, reply_markup=reply_markup)
        else:
            await query.edit_message_text("لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)
