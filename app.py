from flask import Flask, render_template, request
from models import DB
app = Flask(__name__)

db = DB(app)

@app.route('/')
def index():


"""@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO name(firstname, lastname) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('list.html')"""


if __name__ == '__main__':
    app.run()