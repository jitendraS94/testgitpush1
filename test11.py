import pymongo


client = pymongo.MongoClient("mongodb+srv://jitendra1:sharma4403@cluster0.pl901.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "emp_id" : 124652,
    "mob_no" : 75698565,
    "job_loc": "gwalior"
}
db1 = client["Mongodb123"]
coll = db1['test2']
coll.insert_one(d )