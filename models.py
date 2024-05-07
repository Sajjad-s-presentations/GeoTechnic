from flask_mysqldb import MySQL

class DB:

    def __init__(self, app):

        self.app = app
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = ''
        self.app.config['MYSQL_DB'] = 'administrator'

        self.mysql = MySQL(self.app)

    def connect_db(self):
        connection = self.mysql.connection.cursor()
        return connection

    def insert_to_tariff_list(self, id_no, description, unit, cost, tags):
        connection = self.connect_db()
        connection.execute("INSERT INTO tariff_list(id_no, description, unit, cost, tags) VALUES (%s, %s, %s, %s, %s)", (id_no, description, unit, cost, tags))
        self.mysql.connection.commit()
        connection.close()
        return 'success'