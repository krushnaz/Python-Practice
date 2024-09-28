import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
# print(client)

# create database as crud_op
database = client['crud_op']
# print(database)
collection = database['student_info']
# print(collection)

# document = {"name":"krushna zarekar",
#             "course":"MCA",
#             "age":22}

# inserted_doc = collection.insert_one(document)
# print(inserted_doc)
# find_doc = collection.find({})
# for x in find_doc :
#     print(x)

# delete_doc = collection.delete_many({})
# print(delete_doc)

# insert 10 records of student 
document = []
for i in range(11) :
    document.append({"studentId" : 100+i,"studentName":f"student{i}","course":"MCA","age":20+i})

result = collection.insert_many(document)
print(result.inserted_ids)
# query = {"age" :{"$lte":25}}
# find_all = collection.find(query)
# for i in find_all :
#     print(i)
# print()
# delete_query = {"studentId":{"$lte":104}}
# find_and_delete = collection.find_one_and_delete(delete_query)
# print(find_and_delete)

# delete_all = collection.delete_many({})
# print(delete_all)

# update 
# update_query = {"studentId":102}
# value = {"$set":{"age" : 19}}
# update = collection.update_one(update_query,value)
# print(update)