from telegram.ext import Updater, CommandHandler

uzb_dct = {'Salam' : 'Salam-Salam)',
       'Qaleysan?': 'Yahshi. Qandaysan? Yaxshimisan?',
       'Yahshi': 'Bu juda yaxshi!'}
rus_dct = {'Привет' : 'И тебе привет) ',
        'Прив' : 'И тебе привет) ',
        'привет': 'И тебе привет) ',
        'прив': 'И тебе привет) ',
        'Как дела?': 'У меня всё хорошо. Ты как?',
        'Хорошо': 'Хорошо - это же замечательно!'}
eng_dct = {'Hello': 'Hi',
       'Hi': 'Hello',
        'hello': 'Hi',
        'hi': 'Hello',
       'How are you?': 'I am fine, tnx)',
       'how are you?': 'I am fine, tnx)'}

TOKEN = '1450570162:AAGOGtyKrmTxuuU8dPByC3LIiqTYnLkoD98'

updater = Updater(TOKEN, use_context=True)

def uz(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Salom Alekum ' + name)
    def uzbek(update, context):
        def start_u(update, context):
            name = update.message.from_user.first_name
            context.bot.send_message(chat_id=update.message.chat_id, text='Assalom Alekum ' + name)

        def a_u(update, context):
            f = open('text.txt', 'a')
            name = update.message.from_user.first_name
            f.write(name + '\n')
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Malumotlar bazasiga sizning ismingiz qoshildi,  ' + name)
            f.close()

        def d_u(update, context):
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
            context.bot.send_message(chat_id=update.message.chat_id, text='Hop.')

        dispatcher.add_handler(CommandHandler('go', start_u))

        dispatcher.add_handler(CommandHandler('adduser', a_u))

        dispatcher.add_handler(CommandHandler('deluser', d_u))

    dispatcher.add_handler(CommandHandler('uz', uz))

    dispatcher.add_handler(CommandHandler('ru', rus))

    dispatcher.add_handler(CommandHandler('en', en))

    uzbek(update, context)

def rus(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Доброго дня ' + name)

    def russian(update, context):
        def start_r(update, context):
            name = update.message.from_user.first_name
            context.bot.send_message(chat_id=update.message.chat_id, text='Приветствую вас ' + name)

        def a_r(update, context):
            f = open('text.txt', 'a')
            name = update.message.from_user.first_name
            f.write(name + '\n')
            context.bot.send_message(chat_id=update.message.chat_id, text='Мы запомнили ваше имя,  ' + name)
            f.close()

        def d_r(update, context):
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

        dispatcher.add_handler(CommandHandler('go', start_r))

        dispatcher.add_handler(CommandHandler('adduser', a_r))

        dispatcher.add_handler(CommandHandler('deluser', d_r))

    dispatcher.add_handler(CommandHandler('uz', uz))

    dispatcher.add_handler(CommandHandler('ru', rus))

    dispatcher.add_handler(CommandHandler('en', en))

    russian(update, context)

def en(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Hello, dear ' + name)

    def english(update, context):
        def start_e(update, context):
            name = update.message.from_user.first_name
            context.bot.send_message(chat_id=update.message.chat_id, text='Hello ' + name)

        def a_e(update, context):
            f = open('text.txt', 'a')
            name = update.message.from_user.first_name
            f.write(name + '\n')
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Your name has been added to the database,  ' + name)
            f.close()

        def d_e(update, context):
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
            context.bot.send_message(chat_id=update.message.chat_id, text='Name removed. Goodbye agent 007')

        dispatcher.add_handler(CommandHandler('go', start_e))

        dispatcher.add_handler(CommandHandler('adduser', a_e))

        dispatcher.add_handler(CommandHandler('deluser', d_e))

    dispatcher.add_handler(CommandHandler('uz', uz))

    dispatcher.add_handler(CommandHandler('ru', rus))

    dispatcher.add_handler(CommandHandler('en', en))

    english(update, context)
dispatcher = updater.dispatcher

def strt(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Assalom! Iltimos, tilni tanlang : /uz\n Доброго дня! Для начала работы выберите язык : /ru\n Hello, Please select а language : /en')

dispatcher.add_handler(CommandHandler('uz', uz))

dispatcher.add_handler(CommandHandler('ru', rus))

dispatcher.add_handler(CommandHandler('en', en))

dispatcher.add_handler(CommandHandler('start', strt))

updater.start_polling(clean=True)
updater.idle()