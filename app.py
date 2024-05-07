from flask import Flask, render_template, session, request
from functions import Administrator
from models import DB

app = Flask(__name__)
db = DB(app)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def administrator_index():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        administrator = Administrator(app, db)
        msg = administrator.login(username, password)
    return render_template('administrator/index.html', msg=msg)

@app.route('/jjjjlguvgfol')
def index():
    id_no = "0123"
    description = "این یک نمونه از توضیحات است"
    unit = "متر مکعب"
    cost = "1230000"
    tags = "حفاری"
    result = db.insert_to_tariff_list(id_no, description, unit, cost, tags)
    return result


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