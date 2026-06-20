from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    employee_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100))

    last_name = db.Column(db.String(100))

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    mobile = db.Column(db.String(20))

    dept_id = db.Column(db.Integer)

    role_id = db.Column(db.Integer)

    reporting_manager_id = db.Column(db.Integer)

    date_of_joining = db.Column(db.Date)

    created_at = db.Column(db.DateTime)

    updated_at = db.Column(db.DateTime)