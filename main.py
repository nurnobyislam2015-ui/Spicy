import telebot
from telebot import types

# আপনার বটের টোকেন এখানে দিন
API_TOKEN='8504169863:AAERbU9KX5xjQiQlwmmU8ziYfD2VPtAybEU'
bot = telebot.TeleBot(API_TOKEN)

# আপনার নিউজপেপার বা অ্যাড লিঙ্কটি এখানে দিন
# লিঙ্কের শেষে অবশ্যই ?start=verify যুক্ত করে দেবেন আপনার সাইটের বাটনে
AD_LINK = "https://bdviralnews24hub.blogspot.com"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # যদি ইউজার ভেরিফাই করে ফিরে আসে (যেমন: /start verify)
    if len(message.text) > 7 and "verify" in message.text:
        bot.reply_to(message, "✅ ভেরিফিকেশন সফল! আপনি এখন মিডিয়া অ্যাক্সেস করতে পারবেন।")
        # এখানে আপনি আপনার ভিডিও বা ফাইল পাঠাতে পারেন
        # bot.send_video(message.chat.id, 'FILE_ID_OR_URL')
    else:
        # সাধারণ স্টার্ট মেসেজ
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🔓 Unlock Media (Wait 30s)", url=AD_LINK)
        markup.add(btn)
        
        text = ("স্বাগতম! ভিডিওটি দেখতে নিচের বাটনে ক্লিক করে ৩০ সেকেন্ড অপেক্ষা করুন।\n"
                "সময় শেষ হলে 'Get Access' বাটনে ক্লিক করে ফিরে আসুন।")
        bot.send_message(message.chat.id, text, reply_markup=markup)

print("Bot is running...")
bot.polling()
