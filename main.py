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

# ১. মূল শপ ইন্টারফেস (Clean & Minimalist Design)
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

# ২. /start কমান্ড হ্যান্ডলার
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "🔥 **Welcome to Trust FB Shop** 🔥\n\n"
        "আস্থার সাথে ফ্রেশ নাম্বার কুকিজ আইডি কিনতে নিচের অপশনগুলো ব্যবহার করুন:\n\n"
        "👇 আপনার পছন্দের অপশনে ক্লিক করুন:"
    )
    await message.answer(text, reply_markup=get_main_menu(), parse_mode="Markdown")

# ৩. পণ্য কেনার বিবরণ ও অর্ডার নির্দেশিকা
@dp.callback_query(F.data == "buy_cookies")
async def show_product_details(callback: types.CallbackQuery):
    text = (
        "🛍️ **Product Details:**\n\n"
        "🔹 **Item:** New Number Cookies ID\n"
        "🔹 **Price:** `8 BDT` per ID\n"
        "🔹 **Format:** `UID | Password | Cookies`\n\n"
        "🛒 **অর্ডার করার নিয়ম:**\n"
        "প্রথমে নিচের পেমেন্ট মাধ্যম থেকে টাকা পাঠিয়ে ট্রানজাকশন আইডি (TrxID) সহ সরাসরি আমাদের সাপোর্টে মেসেজ দিন। সাথে সাথে আইডি পেয়ে যাবেন!"
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

# ৪. পেমেন্ট মাধ্যম
@dp.callback_query(F.data == "payment_info")
async def show_payments(callback: types.CallbackQuery):
    text = (
        "💳 **Our Payment Methods (Personal):**\n\n"
        f"🔹 **Bkash:** `{BKASH_NO}`\n"
        f"🔹 **Nagad:** `{NAGAD_NO}`\n"
        f"🔹 **Rocket:** `{ROCKET_NO}`\n\n"
        "🟡 **Binance:** ডলার বা বাইনান্সের মাধ্যমে পেমেন্ট করতে চাইলে সরাসরি সাপোর্টে যোগাযোগ করুন।\n\n"
        "⚠️ টাকা পাঠানোর পর স্ক্রিনশট বা TrxID দিয়ে সাপোর্টে নক দিন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Contact Support", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="⬅️ Back to Home", callback_data="back_home
    
