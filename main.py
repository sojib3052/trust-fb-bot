import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8999014754:AAGyxpUaUn0A_14sNW0M3NOV8giTUkI-NvQ"

ADMIN_ID = 512345678  # <--- এখানে তোমার টেলিগ্রাম Admin ID বসিয়ে দিবে (যেখানে পেমেন্ট নোটিফিকেশন যাবে)

BKASH_NO = "01835328849"
NAGAD_NO = "01785283052"
ROCKET_NO = "01785283052"
SUPPORT_USERNAME = "Hmsojib52"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# সাময়িক ডাটাবেজ (টেস্ট ও পরিচালনার জন্য - পরবর্তীতে ডাটাবেজে যুক্ত করা যাবে)
user_balances = {}  # {user_id: balance}
stock_ids = [
    "100012345678901 | pass123 | c_user=123; xs=abc;",
    "100098765432109 | pass456 | c_user=456; xs=def;",
    "100055555555555 | pass789 | c_user=789; xs=ghi;"
]  # স্টক আইডির লিস্ট (৮ টাকা করে প্রতি পিস)

# ১. মূল মেনু
def get_main_menu(user_id):
    balance = user_balances.get(user_id, 0)
    stock_count = len(stock_ids)
    
    text = (
        f"🔥 **Trust FB Shop** 🔥\n\n"
        f"👤 আপনার ব্যালেন্স: `৳ {balance}`\n"
        f"📦 বর্তমান স্টক: `اپ {stock_count} পিস` (প্রতি পিস ৮ টাকা)\n\n"
        "👇 নিচে থেকে আপনার পছন্দমতো অপশন সিলেক্ট করুন:"
    )
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"🛒 Buy Cookies ID (Stock: {stock_count})", callback_data="buy_menu")],
            [InlineKeyboardButton(text="💳 Add Balance / Deposit", callback_data="add_balance")],
            [InlineKeyboardButton(text="👤 My Profile & Balance", callback_data="my_profile")],
            [InlineKeyboardButton(text="📞 Support", url=f"https://t.me/{SUPPORT_USERNAME}")]
        ]
    )
    return text, keyboard

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text, keyboard = get_main_menu(message.from_user.id)
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

# ২. বাই মেনু ও স্টক চেক
@dp.callback_query(F.data == "buy_menu")
async def buy_menu_handler(callback: types.CallbackQuery):
    stock_count = len(stock_ids)
    user_id = callback.from_user.id
    balance = user_balances.get(user_id, 0)
    
    if stock_count == 0:
        text = "❌ দুঃখিত, বর্তমানে কোনো স্টক নেই! দয়া করে পরে চেষ্টা করুন।"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Back", callback_data="back_home")]])
    else:
        text = (
            f"🛍️ **New Number Cookies ID**\n"
            f"💵 দাম: `৮ টাকা` প্রতি পিস\n"
            f"📦 এভেইলেবল স্টক: `পিস {stock_count}`\n\n"
            f"আপনার বর্তমান ব্যালেন্স: `৳ {balance}`\n"
            f"আইডি কিনতে নিচে 'Confirm Buy' এ ক্লিক করুন।"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="✅ Confirm Buy (8 BDT)", callback_data="confirm_buy")],
                [InlineKeyboardButton(text="⬅️ Back", callback_data="back_home")]
            ]
        )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৩. আইডি কেনা কনফার্মেশন ও অটো ডেলিভারি
@dp.callback_query(F.data == "confirm_buy")
async def confirm_buy_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    balance = user_balances.get(user_id, 0)
    price = 8
    
    if balance < price:
        await callback.answer("❌ আপনার পর্যাপ্ত ব্যালেন্স নেই! আগে ডিপোজিট করে ব্যালেন্স যোগ করুন।", show_alert=True)
        return
    
    if len(stock_ids) == 0:
        await callback.answer("❌ স্টক শেষ হয়ে গেছে!", show_alert=True)
        return
    
    # ব্যালেন্স কাটুন এবং স্টক থেকে একটি আইডি দিন
    user_balances[user_id] = balance - price
    bought_id = stock_ids.pop(0)  # স্টক থেকে প্রথম আইডি রিমুভ করে দিয়ে দেওয়া হলো
    
    success_text = (
        "🎉 **সফলভাবে আইডি কেনা সম্পন্ন হয়েছে!**\n\n"
        f"আপনার কেনা আইডি নিচে দেওয়া হলো:\n`{bought_id}`\n\n"
        "⚠️ এটি নিরাপদ জায়গায় সংরক্ষণ করুন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🏠 Home Menu", callback_data="back_home")]]
    )
    await callback.message.edit_text(success_text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৪. ব্যালেন্স বা ডিপোজিট অপশন
@dp.callback_query(F.data == "add_balance")
async def add_balance_handler(callback: types.CallbackQuery):
    text = (
        "💳 **Balance Deposit System:**\n\n"
        f"🔹 **Bkash Personal:** `{BKASH_NO}`\n"
        f"🔹 **Nagad Personal:** `{NAGAD_NO}`\n"
        f"🔹 **Rocket Personal:** `{ROCKET_NO}`\n\n"
        "💡 টাকা পাঠানোর পর আপনার **TrxID** এবং আপনার **User ID** সাপোর্টে পাঠান অথবা অ্যাডমিনকে জানান, অ্যাডমিন চেক করে ব্যালেন্স অ্যাড করে দেবেন।"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Contact Admin to Add Balance", url=f"https://t.me/{SUPPORT_USERNAME}")],
            [InlineKeyboardButton(text="⬅️ Back", callback_data="back_home")]
        ]
    )
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৫. প্রোফাইল
@dp.callback_query(F.data == "my_profile")
async def profile_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    balance = user_balances.get(user_id, 0)
    text = (
        f"👤 **Your Profile:**\n\n"
        f"🆔 Telegram ID: `{user_id}`\n"
        f"💰 Current Balance: `৳ {balance}`"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Back", callback_data="back_home")]])
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

# ৬. হোম মেনু ব্যাক
@dp.callback_query(F.data == "back_home")
async def back_home_handler(callback: types.CallbackQuery):
    text, keyboard = get_main_menu(callback.from_user.id)
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    print("Trust FB Shop Bot (Stock & Balance System) started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
