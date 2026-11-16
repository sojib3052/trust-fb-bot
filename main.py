import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import web

TOKEN = "8999014754:AAGyxpUaUn0A_14sNW0M3NOV8giTUkI-NvQ"

BKASH_NO = "01835328849"
NAGAD_NO = "01785283052"
ROCKET_NO = "01785283052"
WHATSAPP_NO = "01785283052"
SUPPORT_USERNAME = "Hmsojib52"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 New Number Cookies ID (8 BDT)", callback_data="buy_cookies")],
            [InlineKeyboardButton(text="💳 Payment Methods", callback_data="payment_info")],
            [InlineKeyboardButton(text="📞 Support (Telegram)", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 Support (WhatsApp)", url=f"https://wa.me/88{WHATSAPP_NO}")]
        ]
    )
    return keyboard

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "🔥 **Welcome to Trust FB Shop** 🔥\n\n"
        "আস্থার সাথে ফ্রেশ নাম্বার কুকিজ আইডি কিনতে নিচের অপশনগুলো ব্যবহার করুন:\n\n"
        "👇 আপনার পছন্দের অপশনে ক্লিক করুন:"
    )
    await message.answer(text, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "buy_cookies")
async def show_product_details(callback: types.CallbackQuery):
    text = (
        "🛍️ **Product Details:**\n\n"
        "🔹 **Item:** New Number Cookies ID\n"
        "🔹 **Price:** `8 BDT` per ID\n"
        "🔹 **Format:** `UID | Password | Cookies`\n\n"
        "🛒 **অর্ডার করার নিয়ম:**\n"
        "প্রথমে নিচের পেমেন্ট মাধ্যম থেকে টাকা পাঠিয়ে ট্রানজাকশন আইডি (TrxID) সহ সরাসরি আমাদের সাপোর্টে মেসেজ দিন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💳 Payment Methods", callback_data="payment_info")],
            [InlineKeyboardButton(text="🛒 Order via Telegram", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="💬 Order via WhatsApp", url=f"https://wa.me/88{WHATSAPP_NO}")],
            [InlineKeyboardButton(text="⬅️ Back to Home", callback_data="back_home")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "payment_info")
async def show_payments(callback: types.CallbackQuery):
    text = (
        "💳 **Our Payment Methods (Personal):**\n\n"
        f"🔹 **Bkash:** `{BKASH_NO}`\n"
        f"🔹 **Nagad:** `{NAGAD_NO}`\n"
        f"🔹 **Rocket:** `{ROCKET_NO}`\n\n"
        "🟡 **Binance:** ডলার বা বাইনান্সের মাধ্যমে পেমেন্ট করতে চাইলে সরাসরি সাপোর্টে যোগাযোগ করুন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Contact Support", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="⬅️ Back to Home", callback_data="back_home")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "back_home")
async def back_to_home(callback: types.CallbackQuery):
    text = (
        "🔥 **Welcome to Trust FB Shop** 🔥\n\n"
        "আস্থার সাথে ফ্রেশ নাম্বার কুকিজ আইডি কিনতে নিচের অপশনগুলো ব্যবহার করুন:\n\n"
        "👇 আপনার পছন্দের অপশনে ক্লিক করুন:"
    )
    await callback.message.edit_text(text, reply_markup=get_main_menu(), parse_mode="Markdown")
    await callback.answer()

async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await start_web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
