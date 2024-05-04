from flask_mysqldb import MySQL

class DB:

    def __init__(self, app):

        self.app = app
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = ''
        self.app.config['MYSQL_DB'] = 'test'

        self.mysql = MySQL(self.app)

    def connect_db(self):
        connection = self.mysql.connection.cursor()
        return connection

