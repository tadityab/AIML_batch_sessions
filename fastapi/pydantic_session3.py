# Numeric constraints 

from ipaddress import _BaseAddress
from decimal import Decimal
from pydantic import BaseModel, Field, ValidationError, PositiveInt


class TrainingPydantic(BaseModel):
    id: int = Field(gt=0, le=1000)
    batch_size: int = Field(gt=0, multiple_of=8)
    learning_rate: float = Field(gt=0.0, lt=1.0, allow_inf_nan=False)
    budget_used: Decimal = Field(gt=0,max_digits=8, decimal_places=2)

# valid 
t = TrainingPydantic(id=10,batch_size=32, learning_rate=0.001, budget_used=150.50)
print(t)

# Invalid 
try:
    TrainingPydantic(id=10,batch_size=15, learning_rate=2.001, budget_used=150.50)
except ValidationError as e:
    print(e.error_count())
    for err in e.errors():
        print(err['loc'], " --> ", err['msg'])


print("-"*50)

# String Contraints 

from typing import Annotated
from pydantic import BaseModel, Field, ValidationError, StringConstraints

CleanStringContraint = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
RollNumberVal = Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, pattern=r"^[A-Za-z]{2,5}-\d{3}$")]

# AB-102

class BWTClass(BaseModel):
    name: CleanStringContraint
    roll_no: RollNumberVal 

# Valid senario 
b = BWTClass(name="  Ram  ", roll_no=" ab-123")
print(b)

# invalid scenario 
try:
    BWTClass(name="  ", roll_no="xyzlksajflksj")
except ValidationError as e:
    print(e.error_count())
    for err in e.errors():
        print(err['loc'], " --> ", err['msg'])


print("-"*50)

# List Constraints 

from typing import Annotated
from pydantic import BaseModel, Field, ValidationError, PositiveInt

ProbVal = Annotated[float, Field(ge=0.0, le=1.0, allow_inf_nan=False)]

class NewClass(BaseModel):
    request_id: PositiveInt
    class_prob: list[ProbVal]= Field(min_length=2, max_length=10)
    embedding: list[ProbVal] = Field(min_length=3, max_length=6, repr=False)

# valid
n = NewClass(request_id=101, class_prob=[0.5,0.8],embedding=[0.12,0.44,0.44])
print(n)
print(n.embedding)

c=n
print(c)
print(c.embedding)

# Invalid 
try:
    NewClass(request_id=-1101, class_prob=[1.5,0.8],embedding=[0.12,0.44])
except ValidationError as e:
    print(e.error_count())
    for err in e.errors():
        print(err['loc'], " --> ", err['msg'])

print("-"*50)

# Strict and Frozen 
from pydantic import BaseModel, Field, ValidationError

class StrictUser(BaseModel):
    user_id: int = Field(strict=True, frozen=True)
    val:int 

u = StrictUser(user_id=10,val="10")
print(u)

print("-"*50)

# Strict and Frozen 
from pydantic import BaseModel, Field, ValidationError

class Session(BaseModel):
    username: str
    api_key: str = Field(exclude=True)

s = Session(username="ram",api_key="bacdad")
print(s)
print(s.api_key)
print(s.model_dump())





