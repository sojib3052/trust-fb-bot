import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import web  # রেন্ডারের টাইমআউট রোধ করার জন্য

# আপনার টেলিগ্রাম বট টোকেন
TOKEN = "8999014754:AAGyxpUaUn0A_14sNW0M3NOV8giTUkI-NvQ"

# আপনার পেমেন্ট নম্বর ও বাইনান্স আইডি
BKASH_NO = "01835328849"
NAGAD_NO = "01785283052"
ROCKET_NO = "01785283052"
BINANCE_ID = "902145970"

# আপনার টেলিগ্রাম সাপোর্ট ইউজারনেম
SUPPORT_USERNAME = "Hmsojib52"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ১. মূল মেনু
def get_main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📦 পণ্যের তালিকা ও দাম", callback_data="shop_products")],
            [InlineKeyboardButton(text="💳 পেমেন্ট মাধ্যম (বিকাশ/নগদ/বাইনান্স)", callback_data="shop_payments")],
            [InlineKeyboardButton(text="📞 সাপোর্টে যোগাযোগ", url=f"https://t.me/{SUPPORT_USERNAME}")],
        ]
    )
    return keyboard

# ২. /start কমান্ড হ্যান্ডলার
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "👋 স্বাগতম **Trust FB** শপে!\n\n"
        "নিরাপদ ও আস্থার সাথে সোশ্যাল মিডিয়া অ্যাকাউন্ট কিনতে নিচের অপশনগুলো থেকে বেছে নিন:"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")

# ৩. পণ্যের তালিকা প্রদর্শন
@dp.callback_query(F.data == "shop_products")
async def show_products(callback: types.CallbackQuery):
    text = (
        "🛍️ **আমাদের বর্তমান পণ্যের তালিকা:**\n\n"
        "🔹 **New Number Cookies ID**\n"
        "   - বিবরণ: ফ্রেশ এবং ট্রাস্টেড নাম্বার কুকিজ আইডি।\n"
        "   - অর্ডার করতে বা দাম জানতে সরাসরি সাপোর্টে যোগাযোগ করুন।\n\n"
        "পছন্দের পণ্যটি নিতে নিচের বাটনে ক্লিক করুন:"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 অর্ডার করতে যোগাযোগ করুন", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="⬅️ ফিরে যান", callback_data="back_home")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৪. পেমেন্ট নম্বর ও বাইনান্স আইডি প্রদর্শন
@dp.callback_query(F.data == "shop_payments")
async def show_payments(callback: types.CallbackQuery):
    payment_text = (
        "💳 **আমাদের পেমেন্ট মাধ্যম (Personal Numbers & Binance):**\n\n"
        f"🔹 **বিকাশ (Bkash Personal):** `{BKASH_NO}`\n"
        f"🔹 **নগদ (Nagad Personal):** `{NAGAD_NO}`\n"
        f"🔹 **রকেট (Rocket Personal):** `{ROCKET_NO}`\n"
        f"🔹 **বাইনান্স আইডি (Binance ID):** `{BINANCE_ID}`\n\n"
        "⚠️ টাকা পাঠানোর পর অবশ্যই ট্রানজাকশন আইডি (TrxID) বা পেমেন্টের স্ক্রিনশটসহ সাপোর্টে মেসেজ দিন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 পেমেন্ট করে সাপোর্টে মেসেজ দিন", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="⬅️ মূল মেনুতে ফিরে যান", callback_data="back_home")]
        ]
    )
    await callback.message.edit_text(payment_text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৫. হোম মেনুতে ফেরার হ্যান্ডলার
@dp.callback_query(F.data == "back_home")
async def back_to_home(callback: types.CallbackQuery):
    welcome_text = (
        "👋 স্বাগতম **Trust FB** শপে!\n\n"
        "নিরাপদ ও আস্থার সাথে সোশ্যাল মিডিয়া অ্যাকাউন্ট কিনতে নিচের অপশনগুলো থেকে বেছে নিন:"
    )
    await callback.message.edit_text(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")
    await callback.answer()

# ৬. ডামি ওয়েব সার্ভার (রেন্ডার টাইমআউট ঠেকানোর জন্য)
async def handle(request):
    return web.Response(text="Trust FB Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

# ৭. মূল রান ফাংশন
async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # ওয়েব সার্ভার এবং টেলিগ্রাম পুলিং একসাথে রান করবে
    await asyncio.gather(web_server(), dp.start_polling(bot))

if __name__ == "__main__":
    asyncio.run(main())
    
