import React from 'react'
import "./AddTaskForm.css"
import cross from "../../assets/cross.png"

const AddTaskForm = (prop) => {   // setModalActive =prop.setModalActive = setModalActive(true)

  const { setModalActive, title, desc, setEditTodo, editTodo } = prop //{setModalActive : setModalActive()}

  const handleClose = () => {
    if(editTodo) setEditTodo(false)
    else setModalActive(false)
  }

  return (
    <div className='add-form'>
        <img src={cross} alt="" onClick={handleClose}/>
        <div className="form-div">
            <input type="text" placeholder='My Todo Title' value = {editTodo ? {title} : ""}/>
        </div>
        <div className="form-div">
            <input type="text" placeholder='My Todo Description' value = {editTodo ? {desc} : ""}/>
        </div>
        <button className="btn-form">{editTodo ? "Save Changes" : "Add Task"}</button>
        
    </div>
  )
}

export default AddTaskForm