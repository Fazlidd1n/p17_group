import psycopg2

config = {
    "DB_name": 'monitoradmin',
    "DB_user": 'postgres',
    "DB_password": '1',
    "DB_port": 5432,
    "DB_host": 'localhost'
}


class DB:
    con = psycopg2.connect(**config)
    cur = con.cursor()
    def select(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass

