from flask import session
from models import DB
class Administrator:
    def __init__(self, app):
        self.db = DB(app)

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
            msg = 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
        # Show the login form with message (if any)
        return msg