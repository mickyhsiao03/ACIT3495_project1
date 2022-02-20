import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["3495Mongo"]

# mongoDB needs at least one table and one value to create database
grade_table = mydb["grade_stats"]
table_default = {'max_grade':"default_initialize", 'min_grade':"default_initialize", 'avg_grade':"default_initialize", 'popular_course':"default_initialize"}
grade_table.insert_one(table_default)


dblist = myclient.list_database_names()

if "3495Mongo" in dblist:
  print("Database created")