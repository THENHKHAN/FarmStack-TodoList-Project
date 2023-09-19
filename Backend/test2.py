from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# Assuming you have already set up your MongoDB client and collection
MONGODB_URL = "mongodb+srv://userName:<pwd>@fastapi-1stapidev.zsfoowr.mongodb.net/"
client = MongoClient(MONGODB_URL)
db = client.myTodoDB
collection_name = db["test2"]  # Change "test" to your desired collection name


class TodoModel(BaseModel):
    _id: str  # Required field for _id
    title: str
    description: str
    completed: bool


@app.post("/test/")
async def create_todo(todo: TodoModel):
    item_dict = todo.dict()
    result = collection_name.insert_one(item_dict)

    if result:
        return {"message": "Todo created successfully", "_id": str(result.inserted_id)}
    else:
        return {"error": "Failed to create todo"}
