import connexion
from connexion import NoContent

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from grades import Grades
from base import Base

DB_ENGINE = create_engine('mysql+pymysql://root:2705895a@localhost:3306/acit3495')
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def enter_grade(body):

    session = DB_SESSION()

    grade_data = Grades(body['first_name'],
                    body['last_name'],
                    body['course_name'],
                    body['grade']
                    )

    session.add(grade_data)

    session.commit()
    session.close()



    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("enter.yaml", strict_validation=True, validate_responses=True)
if __name__ == "__main__":
    app.run(port=8100)