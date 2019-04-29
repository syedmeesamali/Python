from telegram.ext import Updater, CommandHandler
import requests
import re
contents = requests.get('https://random.dog/woof.json').json()
image_url = contents['url']

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater('my_token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
