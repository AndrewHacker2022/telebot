import time
from telegram import Bot
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenc('CHAT_ID')

def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text='Я жив')
        except:
            print('Бот в коме')

        time.sleep(20 * 60)

if __name__ == '__main__':
    main()
