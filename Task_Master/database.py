
import pymongo
 
HOSTNAME = "mongodb+srv://user_tasks_system:user_tasks_system@cluster0.7edplso.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "task_master"

client = pymongo.MongoClient(host = HOSTNAME)

task_master_database = client[DATABASE_NAME]
