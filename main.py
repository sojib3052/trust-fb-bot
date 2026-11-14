import asyncio
import logging
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
            [InlineKeyboardButton(text="💬 হোয়াটসঅ্যাপে যোগাযোগ", url
                                  
