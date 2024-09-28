import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client['CustInfo']
collection = database['Customer']  # We create the collection outside of the functions

def createCollection() :
    colName = input("Enter collection name: ")
    global collection  # Access the global collection variable
    collection = database[colName]
    print(f"Collection '{colName}' has been created successfully")

def insertDocument(collection) :
    n = int(input("Enter document size: "))
    for i in range(n):
        cid = int(input(f"Enter customer {i+1} ID: "))
        cname = input(f"Enter customer {i+1} name: ")
        cmobile = int(input(f"Enter customer {i+1} mobile no: "))
        caddress = input(f"Enter customer {i+1} address: ")
        
        records = {'cid': cid, 'cname': cname, 'cmobile': cmobile, 'caddress': caddress}
        result = collection.insert_one(records)
        if result.inserted_id:
            print(f"Document {i+1} inserted successfully")

def updateMobById(collection, cid):
    mobileNo = int(input("Enter new mobile no: "))
    query = {"cid": cid}
    new_values = {"$set": {"cmobile": mobileNo}}
    result = collection.update_one(query, new_values)
    if result.modified_count > 0:
        print("Mobile number updated successfully")
    else:
        print("Unable to update mobile number")

def deleteCustByMob(collection, mob):
    query = {"cmobile": mob}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        print("Customer deleted successfully")
    else:
        print("Unable to delete customer")

def main():
    while True:
        print("\nMenu:")
        print("1. Create Collection")
        print("2. Insert Document")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")

        ch = int(input("Enter choice: "))
        
        if ch == 1:
            createCollection()
        
        elif ch == 2:
            insertDocument(collection)
        
        elif ch == 3:
            cid = int(input("Enter customer ID: "))
            updateMobById(collection, cid)
        
        elif ch == 4:
            mob = int(input("Enter customer mobile: "))
            deleteCustByMob(collection, mob)
        
        elif ch == 5:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
