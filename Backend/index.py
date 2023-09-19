from fastapi import FastAPI
from config.configDB import client
from routers.todoRouters import todoApiRouter
from model.pydancticModel import todoModel
app = FastAPI()
app.include_router(todoApiRouter)


# @app.get("/")
# def show () :
#     print(f"clinet : {client}")
#
#     print("show route working ")
#     return {"msg" : "yes router is working and mongo db connected"}
