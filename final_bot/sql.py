import sqlite3
conn = sqlite3.connect('adminfile/database.sqlite')
cursor = conn.cursor()
cursor.execute('''
create table if not exists Users (TELEGRAM_ID integer, 
FIRST_NAME text, 
PHONE_NUMBER integer, 
CODE integer,
CODE_STADIA_ID integer)
''')
conn.commit()