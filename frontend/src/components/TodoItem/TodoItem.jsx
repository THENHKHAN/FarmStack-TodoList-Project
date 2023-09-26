import React, { useEffect, useState } from 'react'
import "./TodoItem.css"
import ExpandTodo from '../ExpandTodo/ExpandTodo'
import AddTaskForm from '../AddTaskForm/AddTaskForm'

const TodoItem = ({title,description}) => {

    const [todoExpand, setTodoExpand] = useState(false)
    const [editTodo, setEditTodo] = useState(false)



  return (
    <>
   
        <div className="todo-item">
            {/* to expand the title by clicking on the title */}
            {/* <p className="todo-title" onClick={() => setTodoExpand(true)}>Kal Noorul ke 20 thappad marne hain</p> */}
            <p className="todo-title" onClick={() => setTodoExpand(true)}>{title}</p>
            <div className="todo-btns">

                    <div className='edit_btn' onClick = {() => setEditTodo(true)}>
                        {/* Edit btn */}
                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 72 72">
                            <path d="M38.406 22.234l11.36 11.36L28.784 54.576l-12.876 4.307c-1.725.577-3.367-1.065-2.791-2.79l4.307-12.876L38.406 22.234zM41.234 19.406l5.234-5.234c1.562-1.562 4.095-1.562 5.657 0l5.703 5.703c1.562 1.562 1.562 4.095 0 5.657l-5.234 5.234L41.234 19.406z"></path>
                            </svg>
                    </div>
            {/* delete btn */}
                    <div className='delete_btn' onClick = {()=>"delete"}>
                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 24 24">
                                <path d="M 10 2 L 9 3 L 5 3 C 4.448 3 4 3.448 4 4 C 4 4.552 4.448 5 5 5 L 7 5 L 17 5 L 19 5 C 19.552 5 20 4.552 20 4 C 20 3.448 19.552 3 19 3 L 15 3 L 14 2 L 10 2 z M 5 7 L 5 20 C 5 21.105 5.895 22 7 22 L 17 22 C 18.105 22 19 21.105 19 20 L 19 7 L 5 7 z"></path>
                            </svg>
                    </div>
            </div>
        </div>
        {todoExpand && 
        
            <div className="modal">
                <ExpandTodo title={title} description = {description} setTodoExpand = {setTodoExpand}/>
            </div>
        }
        {editTodo && 
        
        <div className="modal">
            <AddTaskForm title={"Kal Noorul ke 20 thappad marne hain"} desc = {""} setEditTodo = {setEditTodo} editTodo = {editTodo}/>
        </div>
    }
    </>
    
  )
}

export default TodoItem