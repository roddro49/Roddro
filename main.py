import telebot
import json

TOKEN = 'YOUR_BOTFATHER_TOKEN'  # এখানে আপনার টেলিগ্রাম বট টোকেন বসান
bot = telebot.TeleBot(TOKEN)

with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

with open('problems.json', 'r', encoding='utf-8') as f:
    problems = json.load(f)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Boss, মডেল নম্বর দিন অথবা সমস্যা লিখুন।")

@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    text = message.text.strip()

    if text in products:
        p = products[text]
        reply = f"Model: {text}\nPrice: {p['price']}\nPower: {p['power']}\nBrand: {p['brand']}\nWarranty: {p['warranty']}"
        bot.send_photo(message.chat.id, photo=open(p['image'], 'rb'))
        bot.send_message(message.chat.id, reply)

    elif text in problems:
        bot.send_message(message.chat.id, f"সমাধান:\n{problems[text]}")

    else:
        bot.reply_to(message, "Boss, এই মডেল বা সমস্যা আমার ডেটাবেজে নাই।")

bot.polling()
