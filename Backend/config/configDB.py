from pymongo import MongoClient

MONGODB_URL = "mongodb_ConnectionString"

client = MongoClient(MONGODB_URL)
db = client.myTodoDB
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
