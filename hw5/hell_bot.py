from telegram.ext import Updater, CommandHandler

TOKEN = '1450570162:AAGOGtyKrmTxuuU8dPByC3LIiqTYnLkoD98'



updater = Updater(TOKEN, use_context=True)
def start (update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Приветствую вас ' + name)

def a (update, context):
    f = open('text.txt', 'a')
    name = update.message.from_user.first_name
    f.write(name + '\n')
    context.bot.send_message(chat_id=update.message.chat_id, text='Мы запомнили ваше имя,  ' + name)
    f.close()

def d (update, context):
    name = update.message.from_user.first_name
    l = []
    x = ()
    f = open('text.txt', 'r')
    for i in f:
        l.append(i)
        x = str(i)
    l.remove(x)
    f.close()
    f = open('text.txt', 'w')
    for i in l:
        f.write(i)
        f.close()
    context.bot.send_message(chat_id=update.message.chat_id, text='Мы забыли ваше имя, Агент 007')




dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('adduser', a))

dispatcher.add_handler(CommandHandler('deluser', d))



updater.start_polling(clean=True)
updater.idle()