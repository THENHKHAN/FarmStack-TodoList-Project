import React, { useState } from 'react'
import "./AddTaskForm.css"
import cross from "../../assets/cross.png"
import axios from 'axios';

const AddTaskForm = (prop) => {   // setModalActive = prop.setModalActive = setModalActive(true).true bcz user clikced on add button

  const { setModalActive, setConfirmation, title, desc, setEditTodo, editTodo } = prop // object destructuring-//{setModalActive : setModalActive()}
// for clicking on add button  title, desc, setEditTodo, editTodo will be undefined since in prop only setModalActive function is comming
  const formData = {title:"", description: ""}
  const [inputData, setInputData] = useState(formData)

const handleClose = () => {
    if(editTodo)
      setEditTodo(false)
    else 
      setModalActive(false)
  }

  const inputHandler = (e)=>{
    setInputData ({...inputData, [e.target.name] : e.target.value }) //  [e.target.name]. It's a way to dynamically set a property name in an object. Always in list format
    console.log(inputData)
  }

  const addItem =async (e)=>{
    console.log("Object that we wanna send: ", inputData)
    e.preventDefault()
    if (!inputData.title || !inputData.description ){
      alert("All fields are mendatory!!!")
    }
   else{
    console.log(inputData);
    setModalActive(false)

    setConfirmation(true);
    setTimeout(()=>{
      setConfirmation(false)
    },2000)

    // api for post
  const postReqApi = "http://127.0.0.1:8000/api/todo"
    try {
      
      // Send data to the FastAPI backend
      const response = await axios.post(postReqApi, inputData);
      // Handle the response if needed
      console.log("--------->    ",response.data);
      // console.log(response.message);
    } catch (error) {
      // Handle errors
      console.error('Error sending data to backend:', error);
    }
    
     }

  }

  return (
    <div className='add-form'>
        <img src={cross} alt="" onClick={handleClose}/>

        <div className="form-div">
            <input type="text" name="title" placeholder='My Todo Title' value = {editTodo ? title : inputData.title } onChange={inputHandler}/>
        </div>
        <div className="form-div">
            <input type="text" name="description" placeholder='My Todo Description' value = {editTodo ? desc : inputData.description} onChange={inputHandler}/>
        </div>
        <button className="btn-form" onClick={editTodo? editItem : addItem} > {editTodo ? "Save Changes" : "Add Task"}</button>
        
    </div>
  )
}

export default AddTaskForm