import connexion
from connexion import NoContent
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["3495Mongo"]
grade_table = mydb['grade_stats']

def get_stats():
    latest = ""
    for first in grade_table.find().sort("_id", -1).limit(1):
        latest = first

    reVal =  {'last_updated': latest['_id'], 'max_grade': latest['max_grade'], 'min_grade': latest['min_grade'], 'avg_grade': latest['avg_grade'], 'popular_course': latest['popular_course']}

    return reVal, 200

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("show.yaml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
   app.run(port=8200)