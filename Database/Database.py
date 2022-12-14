from config import USER, PASSWORD
import psycopg2
from loguru import logger


class Database:

    def __init__(self, user=USER, password=PASSWORD, host='127.0.0.1', port='5432', db='postgres'):
        self.conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=db)
        self.cur = self.conn.cursor()

    def create(self, table):
        self.cur.execute(table)
        self.conn.commit()
        logger.info("Таблица успешно создана в PostgreSQL")

    def insert(self, insert, *args):
        self.cur.execute(insert, (args))
        self.conn.commit()
        logger.info("В таблицу успешно добавлены новые данные")

    def get_admins(self):
        ADMINS = []
        self.cur.execute('select * from admin')
        admins_records = self.cur.fetchall()
        for i in admins_records:
            ADMINS.append(i[1])
        return ADMINS

    def admin_allow_to_mute(self):
        self.cur.execute('select * from admin')
        admin_permission = self.cur.fetchall()
        for i in admin_permission:
            return i[3]

    def get_chats(self):
        CHAT_LIST = []
        self.cur.execute('select * from chats')
        chat_records = self.cur.fetchall()
        for i in chat_records:
            CHAT_LIST.append(i[1])
        return CHAT_LIST

    def close(self):
        self.cur.close()
        self.conn.close()
        logger.info("Соединение с PostgreSQL закрыто")


class CreateTables:
    def __init__(self):
        self.db = Database()

        self.db.create("""
            CREATE TABLE IF NOT EXISTS admin (
                id serial PRIMARY KEY,
                id_tg integer,
                privilege integer,
                can_mute BOOLEAN)
            """)

        self.db.create("""
            CREATE TABLE IF NOT EXISTS chats (

            id_chat_tg BIGINT PRIMARY KEY NOT NULL,
            chat_name text NOT NULL,
            chat_members_count integer,
            subscription BOOLEAN,
            subscription_length integer)""")


class TablesModerate:
    def __init__(self):
        self.db = Database()

    def add_new_admin(self, id_tg, privilege):
        global can_mute
        if int(privilege) == 2:
            can_mute = True
        self.db.insert("""
        INSERT INTO admin (id_tg, privilege, can_mute)
        VALUES (%s, %s, %s);
        
        """, id_tg, privilege, can_mute)

    def add_new_chat(self, id_chat_tg, chat_name, chat_members_count):
        self.db.insert("""
        INSERT INTO chats (id_chat_tg, chat_name, chat_members_count)
        VALUES (%s, %s, %s);
        """, id_chat_tg, chat_name, chat_members_count)

