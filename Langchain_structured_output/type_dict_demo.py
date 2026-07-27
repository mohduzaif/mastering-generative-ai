from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int 


new_person : Person = {'name' : 'David', 'age' : 26}

print(new_person)
print(type(new_person))