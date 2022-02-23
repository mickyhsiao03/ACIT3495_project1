import connexion
from connexion import NoContent
import random
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import datetime
import yaml
import logging, logging.config
from grades import Grades
from DB_Operations import get_data

# with open('app_conf.yml', 'r') as f:
#     app_config = yaml.safe_load(f.read())
#     db_info = app_config["db"]

# with open('log_conf.yml', 'r') as f:
#     log_config = yaml.safe_load(f.read())
#     logging.config.dictConfig(log_config)
#     logger = logging.getLogger("basicLogger")

DB_ENGINE = create_engine("mysql+pymysql://root:Iforgot1!@localhost:3306/acit3495")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

# DB_ENGINE = create_engine("sqlite:///readings.sqlite")
# Base.metadata.bind = DB_ENGINE
# DB_SESSION = sessionmaker(bind=DB_ENGINE)

# def create_new_user(body):
#     """ Initialize a password manager user """

#     session = DB_SESSION()
#     password_user = Passworduser(body['user_id'],
#                        body['name'],
#                        body['password'],
#                        body['email'])


#     session.add(password_user)

#     session.commit()
#     session.close()

#     return NoContent, 201
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=20)],
                           render_kw={"placeholder": "Username"})
    password = PasswordField("Password", validators=[InputRequired(), Length(max=50)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

def post_grade(body):
    """ Initialize a password of a user """

    session = DB_SESSION()

    student = Grades(
                   body['first_name'],
                   body['last_name'],
                   body['course_name'],
                   body['grade'])


    session.add(student)

    session.commit()
    session.close()
    # logger.info("Stored event %s request with a unique id of %s"
    #             % ("User Passwords", body['trace_id']))

    return NoContent, 201


def get_grade():
    session = DB_SESSION()
    # timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    readings = session.query(Grades).all()
    results_list = []
    for reading in readings:
        results_list.append(reading.to_dict())
    session.close()
    
    return results_list, 200


@app.route('/', methods=['GET', 'POST'])
def home():
    username = 'root'
    password = 'password'
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'root' and form.password.data == 'password':
            return render_template("login.html", form=form)
    return render_template("dashboard.html")


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # posts = Grades.query.order_by(Grades.first_name.desc()).all()
    # return render_template("dashboard.html", posts=posts)
    posts = get_grade()
    all_text = get_data()
    print(all_text)
    print(posts)
    return render_template("dashboard.html", all_text=all_text)

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))
# def get_password_user(timestamp):
#     """ Gets user password readings after the timestamp """
    
#     session = DB_SESSION()
#     timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

#     readings = session.query(Passworduser).filter(Passworduser.date_created >= timestamp_datetime)
#     results_list = []
#     for reading in readings:
#         results_list.append(reading.to_dict())
#     session.close()

#     logger.info("Timestamp %s returns %d results" %
#     (timestamp, len(results_list)))
#     return results_list, 200


# def get_user_password(timestamp):
#     """ Gets user password readings after the timestamp """
    
#     session = DB_SESSION()
#     timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

#     readings = session.query(Userpasswords).filter(Userpasswords.date_created >= timestamp_datetime)
#     results_list = []
#     for reading in readings:
#         results_list.append(reading.to_dict())
#     session.close()

#     # logger.info("Timestamp %s returns %d results" %
#     # (timestamp, len(results_list)))
#     return results_list, 200


# app = connexion.FlaskApp(__name__, specification_dir='')
# app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(debug=True)
