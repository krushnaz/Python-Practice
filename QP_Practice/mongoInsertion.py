import pymongo 
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["StudentDB"]
collection = database["Student"]

try : 
    student_Id = int(input("enter student id :"))
    name = input("enter student name :")
    course = input("enter student course :")
    mobile = int(input("enter student mobile :"))
        
    area = input("enter area :")
    city = input("enter city :")
    pin = input("enter pin :")
    country = input("enter country :")
    
    address = { 
             'area':area,
             'city':city,
             'pin':pin,
             'country':country
                    }
    document = { 
                'student_id':student_Id,
                'name':name,
                'course':course,
                'mobile':mobile,
                'address' : address
                }
    
    result = collection.insert_one(document)
    if result.inserted_id :
        print("document inserted sucessfully")
    else :
        print("error")
    
    collection.delete_one({'name':"krushna"})
except ValueError as e:
    print(e)