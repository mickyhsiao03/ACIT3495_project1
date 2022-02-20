from sqlalchemy import Column, Integer, String
from base import Base



class Grades(Base):
    """ Grades """

    __tablename__ = "student_grades"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(100), nullable=False)
    course_name = Column(String(50), nullable=False)
    grade = Column(Integer, nullable=False)

    def __init__(self, first_name, last_name, course_name, grade):
        """ Initializes a grades detail """
        self.first_name = first_name
        self.last_name = last_name
        self.course_name = course_name
        self.grade = grade

    def to_dict(self):
        """ Dictionary Representation of a grades detail"""
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['course_name'] = self.course_name
        dict['grade'] = self.grade

        return dict
