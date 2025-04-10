from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for a TODO item
class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# In-memory database (list) to store TODO items
todo_db: List[TodoItem] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the TODO app!"}

# Endpoint to get all TODO items
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todo_db

# Endpoint to get a single TODO item by ID
@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="TODO item not found")

# Endpoint to create a new TODO item
@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    for existing_todo in todo_db:
        if existing_todo.id == todo.id:
            raise HTTPException(status_code=400, detail="TODO item with this ID already exists")
    todo_db.append(todo)
    return todo

# Endpoint to update an existing TODO item
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            todo_db[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="TODO item not found")

# Endpoint to delete a TODO item
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[index]
            return {"message": "TODO item deleted successfully"}
    raise HTTPException(status_code=404, detail="TODO item not found")
