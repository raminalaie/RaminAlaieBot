# handlers/menu_handler.py
from utils.price import get_usdt_price
from utils.validation import validate_national_code
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

        elif query.data == "validate_national_code":
            # درخواست از کاربر برای وارد کردن کد ملی
            await query.edit_message_text("لطفاً کد ملی خود را وارد کنید:")
            # تنظیم وضعیت برای دریافت کد ملی و بررسی اعتبار آن
            context.user_data['waiting_for_national_code'] = True

        else:
            await query.edit_message_text("لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)



# هندلر برای اعتبارسنجی مجدد کد ملی
async def revalidate_national_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # فعال‌سازی وضعیت منتظر برای کد ملی دوباره
    context.user_data['waiting_for_national_code'] = True
    await update.message.reply_text(
        "لطفاً کد ملی خود را مجدداً وارد کنید:",
        reply_markup=InlineKeyboardMarkup(MENU_OPTIONS["validate_national_code"])  # دکمه‌ها برای ادامه
    )

# هندلر برای دریافت کد ملی و اعتبارسنجی آن
async def handle_national_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # بررسی وضعیت منتظر برای کد ملی
    if 'waiting_for_national_code' in context.user_data and context.user_data['waiting_for_national_code']:
        national_code = update.message.text
        is_valid = validate_national_code(national_code)  # تابع اعتبارسنجی کد ملی

        if is_valid:
            # کد ملی معتبر است
            await update.message.reply_text(
                "کد ملی وارد شده معتبر است. ✅",
                reply_markup=InlineKeyboardMarkup(MENU_OPTIONS["validate_national_code"])  # دکمه‌ها بعد از اعتبارسنجی
            )
        else:
            # کد ملی نامعتبر است
            await update.message.reply_text(
                "کد ملی وارد شده نامعتبر است. ❌ لطفاً مجدداً تلاش کنید.",
                reply_markup=InlineKeyboardMarkup(MENU_OPTIONS["validate_national_code"])  # دکمه‌ها بعد از اعتبارسنجی
            )

        # حذف وضعیت منتظر برای کد ملی پس از اعتبارسنجی
        context.user_data['waiting_for_national_code'] = False
    else:
        # اگر وضعیت منتظر وجود نداشته باشد
        await update.message.reply_text(
            "لطفاً ابتدا روی دکمه 'اعتبارسنجی کد ملی' کلیک کنید.",
            reply_markup=InlineKeyboardMarkup(MENU_OPTIONS["main_menu"])  # بازگشت به منو اصلی
        )
