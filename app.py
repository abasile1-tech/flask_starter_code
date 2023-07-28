from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models

app = Flask(__name__)

# TODO: Fill in username/password and database_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{user}:{password}@localhost:5432/{database_name}"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and Register Controllers

@app.route("/")
def home():
    return render_template("index.html", title="Hello World")
