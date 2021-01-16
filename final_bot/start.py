from telegram.ext import Filters, CommandHandler, MessageHandler, Updater, CallbackQueryHandler

from functions import *

from constants import *

updater = Updater(token=TOKEN, workers=20)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('buttons', buttons, run_async=True))

# dispatcher.add_handler(CallbackQueryHandler(pattern='contact', callback=contacting))

dispatcher.add_handler(CallbackQueryHandler(pattern='pht1',callback=pht1))

dispatcher.add_handler(CallbackQueryHandler(pattern='pht2',callback=pht2))

dispatcher.add_handler(CallbackQueryHandler(pattern='pht3',callback=pht3))

dispatcher.add_handler(CallbackQueryHandler(pattern='pht4',callback=pht4))

dispatcher.add_handler(CallbackQueryHandler(pattern='pht5',callback=pht5))

dispatcher.add_handler(CallbackQueryHandler(pattern='rand1',callback=rand1))

dispatcher.add_handler(CallbackQueryHandler(pattern='rand2',callback=rand2))

dispatcher.add_handler(CallbackQueryHandler(pattern='rand3',callback=rand3))

dispatcher.add_handler(CallbackQueryHandler(pattern='randomize',callback=randomize, run_async=True))

dispatcher.add_handler(CallbackQueryHandler(pattern='gallery',callback=buttons_pht, run_async=True))

dispatcher.add_handler(CallbackQueryHandler(pattern='name',callback=name))



dispatcher.add_handler(CommandHandler('start', hello, run_async=True))

dispatcher.add_handler(CommandHandler('photo', buttons_pht))

dispatcher.add_handler(CommandHandler('verification', checking, run_async=True))

dispatcher.add_handler(CommandHandler('admin88005553535', admin))

dispatcher.add_handler(MessageHandler(Filters.text, t_answ, run_async=True))

dispatcher.add_handler(MessageHandler(Filters.photo, p_answ, run_async=True))

updater.start_polling(clean=True)
updater.idle()