from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
# client = MongoClient("mongodb+srv://root:<root>@cluster0.3azg3xb.mongodb.net/")

print(client)
print("List of databases before creating new one")
print(client.list_database_names())  # Call list_database_names as a method

Student = client['Student']
# record = {
#     'Name': "krushna",
#     'roll number': '23260',
#     'courseName': 'MCA'
# }

# rec = Student.Student_Collection.insert_many([record])

# print("Document inserted successfully.")

my_query = { 
    'name':{'$gt' : 'K'}
}

mydoc = Student.Student_Collection.find({})

for x in mydoc :
    print(x)