from flask import *
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class Tariff_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(1000))

with app.app_context():
    db.create_all()

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(Tariff_list).order_by(Tariff_list.id_no)).scalars()
    return render_template("user/list.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        tariff_list = Tariff_list(
            id_no=request.form["id_no"],
            description=request.form["description"],
        )
        db.session.add(tariff_list)
        db.session.commit()
        return redirect(url_for("user_detail", id=tariff_list.id))

    return render_template("user/create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    tariff_list = db.get_or_404(Tariff_list, id)
    return render_template("user/detail.html", user=tariff_list)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    tariff_list = db.get_or_404(Tariff_list, id)

    if request.method == "POST":
        db.session.delete(tariff_list)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user/delete.html", user=tariff_list)