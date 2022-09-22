from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import os
import json

# telegram token
TOKEN = os.environ.get("TELEGRAM_ID")
from flask import Flask, request
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       Welcome to NLP bot
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)



# commandhandler for start command
# def start(update, context):
#     yourname = update.message.chat.first_name

#     msg = "Hi " + yourname + "! Welcome to mimic bot."
#     context.bot.send_message(update.message.chat.id, msg)


# # Message handler for texts only
# def mimic(update, context):
#     context.bot.send_message(update.message.chat.id, update.message.text)


# # commandhandler for details command
# def details(update, context):
#     context.bot.send_message(update.message.chat.id, str(update))


# # Error handler
# def error(update, context):
#     context.bot.send_message(update.message.chat.id, "Oops! Error encountered!")


# main logic
def main():
#     # to get the updates from bot
#     updater = Updater(token=TOKEN, use_context=True)

#     # to dispatch the updates to respective handlers
#     dp = updater.dispatcher

#     # handlers
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("details", details))

#     dp.add_handler(MessageHandler(Filters.text, mimic))

#     dp.add_error_handler(error)
    app.run(threaded=True)


    # to start webhook
    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 443),
                          url_path=TOKEN,
                          webhook_url="https://impyimpy.herokuapp.com/" + TOKEN)
    updater.idle()


# start application with main function
if __name__ == '__main__':
    main()
