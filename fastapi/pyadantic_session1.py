# before pydantic 

class Student:
    def __init__(self, name: str, age: int, gpa: float):
        self.name = name 
        self.age = age 
        self.gpa = gpa 

s = Student(name = 99, age = "Twenty", gpa = False)
print(s.name, " ", s.age, " ", s.gpa)

print("-" * 20)

# after pydantic 

from pydantic import BaseModel 

class Student(BaseModel):
    name:str 
    age:int
    gpa:float

s1 = Student(name = "Ram", age=21, gpa=2.9)
print(s1)

print("-"*10)

# s2 =  Student(name = 99, age = "Twenty", gpa = "excellent")
# print(s2)
"""
Traceback (most recent call last):
  File "D:\BWT2026\AIML_batch_sessions\fastapi\pyadantic_session1.py", line 28, in <module>
    s2 =  Student(name = 99, age = "Twenty", gpa = "excellent")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\BWT2026\AIML_batch_sessions\.venv\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 3 validation errors for Student
name
  Input should be a valid string [type=string_type, input_value=99, input_type=int]
    For further information visit https://errors.pydantic.dev/2.14/v/string_type
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Twenty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.14/v/int_parsing
gpa
  Input should be a valid number, unable to parse string as a number [type=float_parsing, input_value='excellent', input_type=str]
    For further information visit https://errors.pydantic.dev/2.14/v/float_parsing
"""

print("-"*20)

# Real world approach, in API data will arrives in Dictionary format. 

raw_data = {
    "name":"Sham",
    "age":20,
    "gpa":3.5
}

s2 = Student(**raw_data)
print(s2)

print("-"*20)

raw_data1 = {
    "name":"Sham",
    "age":"21",
    "gpa":"21.5"
}

s3 = Student(**raw_data1)
print(s3)
print(type(s3.name), type(s3.age), type(s3.gpa))


raw_data2 = {
    "name":"Sham",
    "age":21.5,
    "gpa":"21.5"
}

# s3 = Student(**raw_data2)
# print(s3)
"""
<class 'str'> <class 'int'> <class 'float'>
Traceback (most recent call last):
  File "D:\BWT2026\AIML_batch_sessions\fastapi\pyadantic_session1.py", line 82, in <module>
    s3 = Student(**raw_data2)
         ^^^^^^^^^^^^^^^^^^^^
  File "D:\BWT2026\AIML_batch_sessions\.venv\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
age
  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=21.5, input_type=float]
    For further information visit https://errors.pydantic.dev/2.14/v/int_from_float
"""
# print(type(s3.name), type(s3.age), type(s3.gpa))


print("-"*20)


# ValidationError 

from pydantic import ValidationError 

raw_data4 = {
    "name" : 1234, 
    "age":"Twenty"
}

try:
    s4 = Student(**raw_data4)
except ValidationError as e: 
    print(f"Total number of errors found: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")


print("-"* 20)

"""
Try writing a small Product(BaseModel) in your notebook with fields: 
product_id: int, name: str, price: float, in_stock: bool, 
and test it with:

Valid coerced inputs (product_id="50", price="199.99", in_stock="1").
A broken input inside try / except ValidationError as e: and print e.error_count().
"""

print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str 

# Required and Non-nullable 
# what happens when value is not provided in dict 
value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
    

print("-"*20)
# Required and Non-nullable 
# what happens if value is None
value = {
    "product_id" : "50",
    "name": None
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")

print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str | None

# Required and nullable 
# what happens when value is not provided in dict 
value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
    

print("-"*20)
# Required and nullable 
# what happens if value is None
value = {
    "product_id" : "50",
    "name": None
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
    






