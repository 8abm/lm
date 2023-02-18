import requests,random
import telebot
myid = str("1934060947")
token = input("enter token : ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['hunt'])
def user(message):
    name2 = message.from_user.first_name
    bot.reply_to(message,f" Hi {name2} \n send check")
    print(7)
@bot.message_handler(func=lambda m:True)
def info(message):
    bot.send_message(message.chat.id,'the check is start')
    inf = message.text
    if "check" in inf:
        while True:
            user1 = str("".join(random.choice('qwertyuioplkjhgfdsamnbvcxz_')for x in range(1)))
            user2 = str("".join(random.choice('qwert.yui.oplkjhgf_dsamn.bvcxz')for x in range(1)))
            user3 = str("".join(random.choice('abcdefghijklmnopqrstuvwxyz1234567_890._')for x in range(1)))
            user4 = str("".join(random.choice('qwert_yuioplkjhg_fdsamnbvcxz1234_567890')for x in range(1)))
            user = user1+user2+user3+user4
            req = requests.get(f"https://ip-info.aliasd5.repl.co/?user={user}").text
            if "True" in req:
                    bot.send_message(message.chat.id,f"{user}",reply_to_message_id=message.message_id)
                    print(f"{user} ✅")
            else:
                print(f"{user} ❌")
    else:
        bot.send_message(message.chat.id,f"ارسل الامر الصحيح",reply_to_message_id=message.message_id)
bot.polling(none_stop=False)