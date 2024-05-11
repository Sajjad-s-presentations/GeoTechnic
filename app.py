from flask import Flask, render_template, session, request, redirect, url_for
from functions import Administrator
from models import DB

app = Flask(__name__)
db = DB(app)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def create_account():
    if request.method == "POST":
        admin = Administrator(app, db)
        details = request.form
        id_no = details['account_id_no']
        name = details['account_name']
        state = details['account_state']
        phone = details['account_phone']
        result = admin.account_creator(id_no, name, state, phone)
        return result
    #else:
        #return render_template('administrator/create_account.html')
        #return render_template('administrator/home.html')

@app.route('/administrator', methods=['GET', 'POST'])
def administrator_index():
    msg = ''
    if request.method == 'GET' and "home" in request.form:
        return render_template("administrator/index.html")
    # Check if the user is logged in
    if 'loggedin' in session:
        return render_template('administrator/home.html')
    else:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            administrator = Administrator(app, db)
            msg = administrator.login(username, password)
            if msg == "4012c84cf11195274ec652190afb90d4":
                return render_template('administrator/home.html')
        return render_template('administrator/index.html', msg=msg)

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return "done"

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