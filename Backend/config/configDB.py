from dotenv import load_dotenv
import os
from pymongo import MongoClient

dotenv_path = "config/.env"  # this path is a rltive pathe with respect to working direcotry(mainFile) and our working directory is index.py

# Load environment variables from the specified path
load_dotenv(dotenv_path)

# Access the MongoDB Atlas URI
mongoDbUri = os.environ.get("MONGODB_URI")

client = MongoClient(mongoDbUri)
db = client.myTodoDB # myTodoDB is the database Name.
myTestCollection = db["test"]  # collection_name , here test is table/collection name
myTestCollection2 = db["test1"]  # collection_name , here test1 is table/collection name

# print(f"DB collection...........{myTestCollection}")
print("DB connected...........")

'''
MongoClient() :
The MongoClient class is used to establish a connection to a MongoDB database.
MoreInfo: The client variable will hold an instance of the MongoClient class, which represents a connection to the MongoDB server specified by the URL parameter. This connection allows you to interact with the MongoDB database,
 including performing operations like querying for data, inserting data, updating data, and more.

EX:
db = client.my_database  # Replace "my_database" with the name of your database
collection = db.my_collection  # Replace "my_collection" with the name of your collection

# Perform a query
result = collection.find({"key": "value"})

# Iterate over the query results
for document in result:
    print(document)



In this example, client is used to connect to a database named "my_database," and then we access a specific collection
within that database. Finally, we perform a query on the collection using the find method. The result variable holds the
query results,which can be iterated over to retrieve documents from the collection.

'''
