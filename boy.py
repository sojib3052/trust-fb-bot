import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# আপনার বটফাদারের টোকেনটি এখানে বসানো আছে
TOKEN = "8999014754:AAGyxpUaUn0A_14sNW0M3NOV8giTUkI-NvQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# বটের মূল মেনু (নিচের বাটনগুলো)
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 শপ"), KeyboardButton(text="💳 ডিপোজিট")],
        [KeyboardButton(text="👤 ব্যালেন্স"), KeyboardButton(text="📦 আমার অর্ডার")],
        [KeyboardButton(text="🎧 সাপোর্ট"), KeyboardButton(text="🎁 রেফার")]
    ],
    resize_keyboard=True
)

# /start কমান্ড দিলে বট যা উত্তর দিবে
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"✨ হ্যালো {user_name}!\n\n"
        f"স্বাগতম **Trust FB**-এ! নিচের মেনু থেকে অপশন বেছে নিন।"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=main_menu_keyboard)

# '🛍 শপ' বাটনে ক্লিক করলে প্রোডাক্ট ক্যাটাগরি দেখাবে
@dp.message(F.text == "🛍 শপ")
async def shop_menu(message: types.Message):
    shop_inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛍 Fb 0 friend cookies id (৳৭)", callback_data="buy_cookie_id")],
            [InlineKeyboardButton(text="📱 Mob Reg Facebook ID (৳১৫)", callback_data="buy_mob_id")]
        ]
    )
    await message.answer(
        "🛍 **প্রোডাক্ট লিস্ট**\n\nএকটি প্রোডাক্ট বেছে নিন 👇",
        parse_mode="Markdown",
        reply_markup=shop_inline_kb
    )

@dp.callback_query(F.data == "buy_cookie_id")
async def process_purchase_cookie(callback: types.CallbackQuery):
    await callback.message.answer("🛒 আপনার অর্ডারটি প্রসেস করা হচ্ছে...")
    await callback.answer()

@dp.callback_query(F.data == "buy_mob_id")
async def process_purchase_mob(callback: types.CallbackQuery):
    await callback.message.answer("🛒 আপনার অর্ডারটি প্রসেস করা হচ্ছে...")
    await callback.answer()

@dp.message(F.text == "👤 ব্যালেন্স")
async def check_balance(message: types.Message):
    await message.answer("👤 আপনার বর্তমান ব্যালেন্স: ৳০.০০\n\nটাকা যোগ করতে '💳 ডিপোজিট' এ ক্লিক করুন।")

@dp.message(F.text == "💳 ডিপোজিট")
async def deposit_money(message: types.Message):
    await message.answer("💳 ডিপোজিট করতে নিচের নাম্বারে Send Money করুন:\n\nবিকাশ/নগদ: `01XXXXXXXXX`", parse_mode="Markdown")

@dp.message(F.text == "📦 আমার অর্ডার")
async def my_orders(message: types.Message):
    await message.answer("📦 আপনার কোনো পূর্ববর্তী অর্ডার নেই।")

@dp.message(F.text == "🎧 সাপোর্ট")
async def support_info(message: types.Message):
    await message.answer("🎧 কোনো সমস্যা হলে আমাদের এডমিনকে নক করুন: @YourUsername")

@dp.message(F.text == "🎁 রেফার")
async def referral_info(message: types.Message):
    await message.answer("🎁 আপনার রেফারেল লিংক:\nhttps://t.me/TrustFB_shop_bot?start=ref12345")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Trust FB বট সফলভাবে চালু হয়েছে...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
