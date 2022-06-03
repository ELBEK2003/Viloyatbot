from telegram.ext import  Updater,CommandHandler,CallbackQueryHandler, MessageHandler,Filters,CallbackContext,ConversationHandler
from telegram import Update
import logging
from functions import *



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


conv_handler=ConversationHandler(
    entry_points=[
        CommandHandler('start',start)
    ],
    states={
        'state_name': [
            CommandHandler('start',start),
            MessageHandler(Filters.text,command_name)


        ],
        'state_phone':[
            MessageHandler(Filters.text,command_phone),
            MessageHandler(Filters.contact,command_phone)
        ],
        'state_viloyat':[
            CommandHandler('start',start),
            MessageHandler(Filters.text,command_viloyat)
        ],
        'state_main':[
            CallbackQueryHandler(commandd_category)

        ]


    },
    fallbacks=[
        CommandHandler('start',start)

    ],
)

updater=Updater("5210102433:AAGHePETy_WihAJKmAkor8yvEOR3ywkf2f8")
updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()

# print(updater)
