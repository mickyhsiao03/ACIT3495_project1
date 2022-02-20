from audioop import avg
import connexion
from connexion import NoContent
import pymongo
import requests
from collections import Counter
import statistics

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["3495Mongo"]
grade_table = mydb['grade_stats']

def populate():
    grade_response = requests.get('http://localhost:8100/grades')

    #make sure connection is valid
    if grade_response.status_code == 200:
        print('got')
    else:
        print('failed to get')
    

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

    print(course_list[max_index])
    print('max', max_grade)
    print('min', min_grade)
    print('avg', avg_grade)

    toInsert = {'max_grade': max_grade, 'min_grade': min_grade, 'avg_grade': avg_grade, 'popular_course': course_list[max_index]}
    grade_table.insert_one(toInsert)

    






    return NoContent, 200

def get_stats():
    return

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("analytics.yaml", strict_validation=True, validate_responses=True)
if __name__ == "__main__":
    populate()
    app.run(port=8090)