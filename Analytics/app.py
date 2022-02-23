from audioop import avg
import connexion
from connexion import NoContent
import pymongo
import requests
from collections import Counter
import statistics
import uuid
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://deployment-mongo-db-1:27017/")
mydb = myclient["3495Mongo"]
grade_table = mydb['grade_stats']

def populate():
    grade_response = requests.get('http://deployment-enter-1:8100/grades')

    #make sure connection is valid
    if grade_response.status_code == 200:
        print('got response')
    else:
        print('failed to get response')
    

    #convert response to json
    grade_received = grade_response.json()

    #calculations
    grades = []
    popular_course = []
    for i in grade_received:
        grades.append(i['grade'])
        popular_course.append(i['course_name'])
    
    max_grade = max(grades)
    min_grade = min(grades)
    avg_grade = statistics.mean(grades)    
    course_list = []
    count = []
    x = Counter(popular_course).keys()
    y = Counter(popular_course).values()
    for i in x:
        course_list.append(i)
    for i in y:
        count.append(i)

    max_count = max(count)
    max_index = count.index(max_count)
    trans_id = str(uuid.uuid4())

    #insert into mongo db
    toInsert = {'_id': datetime.now(), 'max_grade': max_grade, 'min_grade': min_grade, 'avg_grade': int(avg_grade), 'popular_course': course_list[max_index]}
    grade_table.insert_one(toInsert)

    return toInsert, 200



app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("analytics.yaml")
if __name__ == "__main__":
    app.run(port=8090)