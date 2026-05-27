from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def getmessage():
    return {"message":"Hello World"}

@app.get('/greet')
def greet():
    return {'message':'namaste'}

@app.get('/greet/{name}')
def greet_name_age(name:str,age:Optional[int]=None):
    return {'message':f'namaste {name} your age is {age}'}

class Student(BaseModel):
    name : str
    age : int
    rollno : int

@app.post('/create')
def create_student(student : Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "rollno" : student.rollno,
        "message" : "student created successfully"
    }