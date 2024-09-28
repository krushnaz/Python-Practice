from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Access a database (create it if it doesn't exist)
my_database = client['my_database']

# Accessing a collection (this step is optional)
my_collection = my_database['my_collection']

# Insert a document into the collection
my_collection.insert_one({"key": "value"})

# At this point, the database 'my_database' will be created if it doesn't exist
# and the collection 'my_collection' will be created if it doesn't exist.
# The document will be inserted into the collection.
