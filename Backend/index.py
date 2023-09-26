from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from config.configDB import client
from routers.todoRouters import todoApiRouter
from model.pydancticModel import todoModel
app = FastAPI()
app.include_router(todoApiRouter)


# Define a list of allowed origins (replace with your frontend URL)
origins = [
    "http://localhost:5173",  # Add your frontend URL here
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict HTTP methods if needed
    allow_headers=["*"],  # You can restrict headers if needed
)

# Your FastAPI routes and application setup go here

if __name__ == "__main__":

    print("helllooo Frontend I am Backend")
    uvicorn.run(app, host="127.0.0.1", port=8000)

# @app.get("/")
# def show () :
#     print(f"clinet : {client}")
#
#     print("show route working ")
#     return {"msg" : "yes router is working and mongo db connected"}
