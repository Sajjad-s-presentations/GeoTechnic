from flask import session, render_template, redirect, url_for
from datetime import datetime
class Administrator:
    def __init__(self, app, db):
        self.app = app
        self.db = db

    def login(self, username, password):
        # Output a message if something goes wrong...
        msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
        # Create variables for easy access

        # Check if account exists using MySQL
        connection = self.db.connect_db()
        connection.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = connection.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('administrator'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
        # Show the login form with message (if any)
        return msg

    def account_creator(self, id_no, name, state, phone):
        now = datetime.now()
        current_time = now.strftime("%y-%m-%d %H:%M:%S")

        connection = self.db.connect_db()
        connection.execute("INSERT INTO accounts(id_no, name, state, phone, start_date) VALUES (%s, %s, %s, %s, %s)",
                           (id_no, name, state, phone, current_time))
        self.db.mysql.connection.commit()
        connection.close()
        return 'success'
