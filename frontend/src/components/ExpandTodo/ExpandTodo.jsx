import React from 'react'
import "./ExpandTodo.css"
import cross from "../../assets/cross.png"

const ExpandTodo = ({title, description, setTodoExpand}) => {
 
  return (
      <div className='expanded-todo'>
          <img src={cross} alt="" onClick={() => setTodoExpand(false)}/>
         <div>
              <label>Title</label>
              <p className="title">{title}</p>
        </div>
        
        <div>
            <label>Description</label>
            <p className="desc">{description}</p>
        </div>
        
    </div>
  )
}

export default ExpandTodo