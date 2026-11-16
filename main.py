import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import web

# আপনার টেলিগ্রাম বট টোকেন
TOKEN = "8999014754:AAGyxpUaUn0A_14sNW0M3NOV8giTUkI-NvQ"

# আপনার পেমেন্ট ও যোগাযোগের নম্বর
BKASH_NO = "01835328849"
NAGAD_NO = "01785283052"
ROCKET_NO = "01785283052"
WHATSAPP_NO = "01785283052"

# আপনার টেলিগ্রাম সাপোর্ট ইউজারনেম
SUPPORT_USERNAME = "Hmsojib52"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ১. ভাষা নির্বাচন মেনু (Language Selection)
def get_language_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
                InlineKeyboardButton(text="🇧🇩 বাংলা", callback_data="lang_bn")
            ]
        ]
    )
    return keyboard

# ২. ইংরেজি মূল মেনু
def get_main_menu_en():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📦 Products & Details", callback_data="shop_products_en")],
            [InlineKeyboardButton(text="💳 Payment Methods", callback_data="shop_payments_en")],
            [InlineKeyboardButton(text="📞 Support (Telegram)", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 Support (WhatsApp)", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="🌐 Change Language / ভাষা পরিবর্তন", callback_data="change_lang")]
        ]
    )
    return keyboard

# ৩. বাংলা মূল মেনু
def get_main_menu_bn():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📦 পণ্যের তালিকা ও বিবরণ", callback_data="shop_products_bn")],
            [InlineKeyboardButton(text="💳 পেমেন্ট মাধ্যম", callback_data="shop_payments_bn")],
            [InlineKeyboardButton(text="📞 সাপোর্টে যোগাযোগ (টেলিগ্রাম)", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 হোয়াটসঅ্যাপে যোগাযোগ", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="🌐 ভাষা পরিবর্তন / Change Language", callback_data="change_lang")]
        ]
    )
    return keyboard

# ৪. /start কমান্ড হ্যান্ডলার
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "🌐 **ভাষা নির্বাচন করুন (Select Language)**\n"
        "আপনার পছন্দের ভাষা নির্বাচন করুন:\n\n"
        "👇 নিচের বাটন চাপুন:"
    )
    await message.answer(text, reply_markup=get_language_menu(), parse_mode="Markdown")

# ৫. ভাষা পরিবর্তন বা ব্যাক টু ল্যাঙ্গুয়েজ
@dp.callback_query(F.data == "change_lang")
async def change_language(callback: types.CallbackQuery):
    text = (
        "🌐 **ভাষা নির্বাচন করুন (Select Language)**\n"
        "আপনার পছন্দের ভাষা নির্বাচন করুন:\n\n"
        "👇 নিচের বাটন চাপুন:"
    )
    await callback.message.edit_text(text, reply_markup=get_language_menu(), parse_mode="Markdown")
    await callback.answer()

# ৬. ইংরেজি ভাষা সিলেক্ট করলে
@dp.callback_query(F.data == "lang_en")
async def set_lang_english(callback: types.CallbackQuery):
    welcome_text = (
        "👋 Welcome to **Trust FB Shop**!\n\n"
        "Choose an option below to buy social media accounts safely:"
    )
    await callback.message.edit_text(welcome_text, reply_markup=get_main_menu_en(), parse_mode="Markdown")
    await callback.answer()

# ৭. বাংলা ভাষা সিলেক্ট করলে
@dp.callback_query(F.data == "lang_bn")
async def set_lang_bangla(callback: types.CallbackQuery):
    welcome_text = (
        "👋 স্বাগতম **Trust FB** শপে!\n\n"
        "নিরাপদ ও আস্থার সাথে সোশ্যাল মিডিয়া অ্যাকাউন্ট কিনতে নিচের অপশনগুলো থেকে বেছে নিন:"
    )
    await callback.message.edit_text(welcome_text, reply_markup=get_main_menu_bn(), parse_mode="Markdown")
    await callback.answer()

# --- English Section ---
@dp.callback_query(F.data == "shop_products_en")
async def show_products_en(callback: types.CallbackQuery):
    text = (
        "🛍️ **Our Products:**\n\n"
        "🔹 **New Number Cookies ID**\n"
        "   - **Price:** `8 BDT` per ID\n"
        "   - **What you will get:** `UID | Password | Cookies`\n"
        "   - **Details:** Fresh and trusted number cookies ID.\n\n"
        "Click below to order via Telegram or WhatsApp:"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Order via Telegram", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 Order via WhatsApp", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="⬅️ Back", callback_data="lang_en")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "shop_payments_en")
async def show_payments_en(callback: types.CallbackQuery):
    payment_text = (
        "💳 **Payment Methods (Personal Numbers):**\n\n"
        f"🔹 **Bkash (Personal):** `{BKASH_NO}`\n"
        f"🔹 **Nagad (Personal):** `{NAGAD_NO}`\n"
        f"🔹 **Rocket (Personal):** `{ROCKET_NO}`\n\n"
        "🟡 **Binance Payment:**\n"
        "If you want to pay with Binance, please contact support directly for the current rate.\n\n"
        "⚠️ After sending money, please send the TrxID or screenshot to support."
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Message Telegram Support", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 Message WhatsApp", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="⬅️ Back", callback_data="lang_en")]
        ]
    )
    await callback.message.edit_text(payment_text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# --- Bangla Section ---
@dp.callback_query(F.data == "shop_products_bn")
async def show_products_bn(callback: types.CallbackQuery):
    text = (
        "🛍️ **আমাদের বর্তমান পণ্যের তালিকা:**\n\n"
        "🔹 **New Number Cookies ID**\n"
        "   - **দাম:** প্রতি পিস `৮ টাকা`\n"
        "   - **আপনি যা যা পাবেন:** `UID | Password | Cookies`\n"
        "   - **বিবরণ:** ফ্রেশ এবং ট্রাস্টেড নাম্বার কুকিজ আইডি।\n\n"
        "অর্ডার করতে নিচের টেলিগ্রাম বা হোয়াটসঅ্যাপ বাটনে ক্লিক করুন:"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 টেলিগ্রামে অর্ডার করুন", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 হোয়াটসঅ্যাপে অর্ডার করুন", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="⬅️ ফিরে যান", callback_data="lang_bn")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "shop_payments_bn")
async def show_payments_bn(callback: types.CallbackQuery):
    payment_text = (
        "💳 **আমাদের পেমেন্ট মাধ্যম (Personal Numbers):**\n\n"
        f"🔹 **বিকাশ (Personal):** `{BKASH_NO}`\n"
        f"🔹 **নগদ (Personal):** `{NAGAD_NO}`\n"
        f"🔹 **রকেট (Personal):** `{ROCKET_NO}`\n\n"
        "🟡 **বাইনান্স (Binance) পেমেন্ট:**\n"
        "বাইনান্সে ডলার দিয়ে পেমেন্ট করতে চাইলে বর্তমান রেট ও পরিমাণের জন্য সরাসরি সাপোর্টে যোগাযোগ করুন।\n\n"
        "⚠️ টাকা পাঠানোর পর অবশ্যই ট্রানজাকশন আইডি (TrxID) বা স্ক্রিনশটসহ সাপোর্টে মেসেজ দিন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 টেলিগ্রাম সাপোর্টে মেসেজ দিন", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 হোয়াটসঅ্যাপে মেসেজ দিন", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="⬅️ ফিরে যান", callback_data="lang_bn")]
        ]
    )
    await callback.message.edit_text(payment_text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৮. রেন্ডারের জন্য ওয়েব সার্ভার
async def handle(request):
    return web.Response(text="Trust FB Bot is running successfully!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

# ৯. মূল এন্ট্রি পয়েন্ট
async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await start_web_server()
    print("Trust FB শপ বট সফলভাবে চালু হয়েছে...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
