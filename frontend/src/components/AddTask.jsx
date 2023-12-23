import React, { useEffect, useState } from "react";
import axios from 'axios';
import './AddTask.css'
import AddTaskForm from "./AddTaskForm/AddTaskForm";
import TodoItem from "./TodoItem/TodoItem";


function AddTask () {

    const [modalActive, setModalActive] = useState(false)
    const [todoData, setTodoData] = useState([])

    // calling API 
//    const getApi= "http://127.0.0.1:8000/api/"
   const getApi= "http://127.0.0.1:8000/api/"

   useEffect(() => {
    axios
      .get(getApi)
      .then((response) => {
        // Check the response status code
        if (response.status === 200) {
          console.log("res.data: ", response.data); // Log the response data
          console.log("res.Data.TodoList: ", response.data.TodoList); // Log the TodoList data
        setTodoData(response.data.TodoList)

        } else {
          console.log("Unexpected status code: ", response.status);
        }
      })
      .catch((err) => {
        console.error("Error: ", err);
      });
  }, []);

//   just to check whether data are getting stored from backend to todoData or not
  useEffect(() => {
    todoData.map((elem) => {
        // console.log(elem);
    })
  }, [todoData])

   return ( 

    <>
        <div class="container" >      
            <h1>Reorganize your life. Make a todo</h1>
            <button className="btn" onClick = {() => setModalActive(true)}>Add Todo</button>
        </div>
        
        {
          todoData.map( ( todoObj )=>{
           return(
            <TodoItem  todoObj={todoObj} setTodoData={setTodoData} />
              )   // return end   
             }  )   // map end
             
        } 
        

        {
            modalActive && <div className="modal">
                <AddTaskForm setModalActive = {setModalActive}/>
            </div>
        }
      
    </>
);
} 

export default AddTask ;

