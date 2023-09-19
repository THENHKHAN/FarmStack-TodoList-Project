#  it is work like a Serializer. Because we had to send response as serializer to browser.
# and whatever field we need to send as response


#  HERE we'll define pydantic Models called schema. This will map with the request data.


#  used to serialize one todo and return as dictionary

def myTodoSerializer(todo) -> dict:
    return {
            # the left key is of python and rhs: it will be stored with the same name(in mongodb)
            "id": str(todo["_id"]),
            "title": str(todo["title"]),
            "description": str(todo["description"]),
            "completed": str(todo["completed"]),
           }


# this is going to be used for multiple todo or list of dictionary means we'll have to return list
# and we we need to pass each todo to myTodo to serialize each todo 1st then saved as a list of todo(dict)
# that's why its better to use list comprehension rather that simple for loop and append

def myTodosSerializer(todos) -> list: # list of todo will receive
    listOfTodo = [myTodoSerializer(todo) for todo in todos] #todo in this one by one each dict will come and send to myTodo fun.
    return  listOfTodo

# EX: str = "hello"
# l = [i  for i in str] # print (l)  ----> ['h', 'e', 'l', 'l', 'o']
