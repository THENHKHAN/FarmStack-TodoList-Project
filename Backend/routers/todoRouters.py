from fastapi import APIRouter , HTTPException
from typing import List
from model.pydancticModel import todoModel
from config.configDB import myTestCollection
from schemas.Todoschema import myTodoSerializer, myTodosSerializer
from bson import ObjectId

todoApiRouter = APIRouter()


# retrieve all todos
@todoApiRouter.get("/api/")
async def getAllTodos():
    myTodos = myTestCollection.find({})  # leaving empty means we need all document/records
    # now we need to serialize so that we can send as response.
    serializeData = myTodosSerializer(myTodos)  # it will send a  list of serialize dictionary
    #     since todos hences myTodosSerializer USED
    return {"TodoList": serializeData}


# retrieve single todo w.r.t id
@todoApiRouter.get("/api/{title}")
async def getTodo(title: str):
    # mytodo = myTestCollection.find_one({"_id": ObjectId(id)})  # filtering
    mytodo = myTestCollection.find_one({"title": title})  # filtering
    print(mytodo)  # get record whose id is matching wth provided id
    response = myTodoSerializer(mytodo)
    #     since only single todo hences myTodoSerializer USED
    return {"Response": response}


# retrieve single todo w.r.t id
@todoApiRouter.post("/api/todo")  # Read the body of the request as JSON.
async def createTodo(todo: todoModel):  # fastapi automatically deserialize the body request based on model
    item_dict = todo.dict()  # we have to convert it into dictionary to insert into mongodb
    todoId = myTestCollection.insert_one(item_dict)  # since mongodb store in this format
    # print(todoId.inserted_id)
    print(todo.title)
    if todoId:
        return {"message": "Todo created successfully", "title":item_dict["title"], "Desc" : item_dict["description"] }
        # return {"message": "Todo created successfully", "_id": str(todoId.inserted_id)}
    else:
        return {"error": "Failed to create note"}


# retrieve single todo w.r.t id
@todoApiRouter.post("/api/todos")
async def createTodos(todos: List[todoModel]):
    todos = [todo.dict() for todo in
             todos]  # it will give list of todos i.e.we are making it so that we can insert into mongo
    todoIds = myTestCollection.insert_many(todos)  # since mongodb store in this format
    print(todoIds.inserted_ids)  # it will print list of inserted todo ids
    if todos:  # checking if inserted or not
        inserted_ids = [str(_id) for _id in todoIds.inserted_ids]
        return {"message": "Todos created successfully", "_id": inserted_ids}
    else:
        return {"error": "Failed to create note"}


# update
@todoApiRouter.put("/api/{title}")
async def updateTodo(title: str, todo: todoModel):  # we need id and body (which value want to update)

    # Create a query to find the document with the specified ObjectId
    query = {"title": title}
    # Create an update operation using the fields from updated_todo
    update_operation = {"$set": todo.dict()}  # converting again to dict
    # Use the find_one_and_update method to find and update the document
    updated_document = myTestCollection.find_one_and_update(query, update_operation, return_document=True)

    if updated_document:
        response = myTodoSerializer(updated_document)
        return {"message": "Todo updated successfully", "updated_todo": response}
    else:
        raise HTTPException(status_code=404, detail="Todo not found")


@todoApiRouter.delete("/api/{title}")
async def deleteTodo(title:str):
    query = {"title": title}
    res = myTestCollection.find_one_and_delete(query)
    return {"status":"todo deleted" , "deleted todo" : myTodoSerializer(res)}


'''

IMP*****************

async def createTodo(todo: todoModel):# fastapi automatically deserialize the body request based on model
    print(todo) #Parsed and become class obj: title='My 1st todo' description='My 1st todo inserted from postman. ' completed=False
    item_dict = todo.dict() # we have to convert it into dictionary o insert into mongodb
    # print(typeitem_dict) # {'title': 'My 1st todo', 'description': 'My 1st todo inserted from postman. ', 'completed': False}
    print(item_dict["description"]) # My 1st todo inserted from postman.
    todoId = collection_name.insert_one(item_dict) # since mongodb store in this format
    print(todoId.inserted_id) # 65080e0cbf10e10d627227b6.



'''
