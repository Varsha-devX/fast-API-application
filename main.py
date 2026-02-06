from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()
class student(BaseModel):
    name: str
    email: str
    age: int  
    roll_number: str
    department:str
class studentResponse(BaseModel):
    id:int
    name: str
    email: str
    age: int  
    roll_number: str
    department:str
@app.get("/")
def read_root():
    return {"hello":"world"}
def create_student(student:student):
    return student

def read_student(id:int):
    return studentResponse(id=id,**student.dict())
def update_student(id:int,student:student):
    return studentResponse(id=id,**student.dict())
def delete_student(id:int):
    return studentResponse(id=id,**student.dict())




