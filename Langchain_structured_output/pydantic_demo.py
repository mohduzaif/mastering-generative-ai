from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str 
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0, le = 10, default = 5)
    address : Optional[str] = Field(max_length = 50, default = None, description = "Address filed represent the address of the student.")


my_dict = {
    'name' : 'David',
    'age' : '26', 
    'email' : 'abc@gmail.com',
    'cgpa' : 9
}

student = Student(**my_dict)

print(student)
# print(student.name)
# print(student.age)

student_dict = dict(student)
print(type(student_dict))
print(student_dict)

student_json = student.model_dump_json()
print(type(student_json))
print(student_json)