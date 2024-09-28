import pymongo 
import datetime
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Hospital_DB']

hospital_col = db['Hospital']
doctor_col = db['Doctor']

def insert_hospital_records() :
    hospital_details = []
    
    hospital_data = [
    {"Hospital_Id": 1, "Hospital_Name": "Hospital A", "Bed_Count": 100},
    {"Hospital_Id": 2, "Hospital_Name": "Hospital B", "Bed_Count": 150},
    {"Hospital_Id": 3, "Hospital_Name": "Hospital C", "Bed_Count": 200},
    {"Hospital_Id": 4, "Hospital_Name": "Hospital D", "Bed_Count": 120},
    {"Hospital_Id": 5, "Hospital_Name": "Hospital E", "Bed_Count": 180},
    {"Hospital_Id": 6, "Hospital_Name": "Hospital F", "Bed_Count": 90},
    {"Hospital_Id": 7, "Hospital_Name": "Hospital G", "Bed_Count": 210},
    {"Hospital_Id": 8, "Hospital_Name": "Hospital H", "Bed_Count": 170},
    {"Hospital_Id": 9, "Hospital_Name": "Hospital I", "Bed_Count": 140},
    {"Hospital_Id": 10, "Hospital_Name": "Hospital J", "Bed_Count": 160},
]


    hospital_col.insert_many(hospital_data)


def insert_doctor_records() :

    doctor_data = [
    {"doctor_id": 1, "doctor_name": "doctor1", "hospital_id": 1, "joining_date": datetime.datetime.now(), "speciality": "speciality1", "salary": 6000, "experience": 6},
    {"doctor_id": 2, "doctor_name": "doctor2", "hospital_id": 2, "joining_date": datetime.datetime.now(), "speciality": "speciality2", "salary": 7000, "experience": 7},
    {"doctor_id": 3, "doctor_name": "doctor3", "hospital_id": 3, "joining_date": datetime.datetime.now(), "speciality": "speciality3", "salary": 8000, "experience": 8},
    {"doctor_id": 4, "doctor_name": "doctor4", "hospital_id": 4, "joining_date": datetime.datetime.now(), "speciality": "speciality4", "salary": 9000, "experience": 9},
    {"doctor_id": 5, "doctor_name": "doctor5", "hospital_id": 5, "joining_date": datetime.datetime.now(), "speciality": "speciality4", "salary": 10000, "experience": 10},
    {"doctor_id": 6, "doctor_name": "doctor6", "hospital_id": 6, "joining_date": datetime.datetime.now(), "speciality": "speciality4", "salary": 11000, "experience": 11},
    {"doctor_id": 7, "doctor_name": "doctor7", "hospital_id": 7, "joining_date": datetime.datetime.now(), "speciality": "speciality4", "salary": 12000, "experience": 12},
    {"doctor_id": 8, "doctor_name": "doctor8", "hospital_id": 8, "joining_date": datetime.datetime.now(), "speciality": "speciality4", "salary": 13000, "experience": 13},
    {"doctor_id": 9, "doctor_name": "doctor9", "hospital_id": 9, "joining_date": datetime.datetime.now(), "speciality": "speciality9", "salary": 14000, "experience": 14},
    {"doctor_id": 10, "doctor_name": "doctor10", "hospital_id": 10, "joining_date": datetime.datetime.now(), "speciality": "speciality10", "salary": 15000, "experience": 15}
]

    
    doctor_col.insert_many(doctor_data)

def fetch_hospital_doctor_info(hospital_id,doctor_id):
  
    print("\nHospital information :\n")
    hospital_info = hospital_col.find_one({"Hospital_Id" : hospital_id})
    print(hospital_info)
   
    print("\n doctor inoformation :\n")
    doctor_info = doctor_col.find_one({"doctor_id":doctor_id})
    print(doctor_info)

def fetch_doctors(salary,speciality) :
   
    print("\nprinting doctor with salary :",salary,"and speciality :",speciality)
    doctors = doctor_col.find_one({"salary":{"$gt":salary}, "speciality" :speciality})
    print(doctors)

def update_doctor_experience(doctor_id,experience) :
    
    print("\nupdating doctor experience as ",experience,"where doctor_id is :",doctor_id)
    update_ex = doctor_col.update_one({"doctor_id":doctor_id},{"$set":{"experience":experience}})
    print("\ndoctor experience updated successfully")



# 10 record insertion

insert_hospital_records()
insert_doctor_records()

# Fectch hospital and doctor -----
print("\n ------------------------------------------------------")
hospital_id = int(input("enter hospital id :"))
doctor_id = int(input("enter doctor id :"))
fetch_hospital_doctor_info(hospital_id,doctor_id)

# Fetch all doctors 
print("\n ------------------------------------------------------")
salary = int(input("enter salary :"))
speciality = input("enter speciality :")
fetch_doctors(salary,speciality)

# update experience 
print("\n ------------------------------------------------------")
doctor_id = int(input("enter doctor id :"))
experience = int(input("enter experience :"))
update_doctor_experience(doctor_id,experience)
