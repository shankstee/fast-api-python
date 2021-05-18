from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Todo(BaseModel):
    todo: str

@app.get('/todos')
def getAllTodos():
    return db

@app.get('/todos/{todoId}')
def getTodo(todoId: int):
    return db[todoId-1]

@app.post('/todos')
def createTodo(todo: Todo):
    db.append(todo.dict())
    return db[-1]

@app.delete('/todos/{todoId}')
def deleteTodo(todoId: int):
    db.pop(todoId-1)
    return {}


