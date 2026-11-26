print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str = "Ram"

# Optional and non-nullable 
# what happens when value is not provided in dict 
value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
    

print("-"*20)
# Optional and non-nullable 
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


print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str | None = None

# Optional and nullable 
# what happens when value is not passed
value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
    
print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str | None = None

# Optional and nullable 
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

print("-"*20)

# pydantic does not validate default value by itself.
class Product(BaseModel):
    product_id: int = "abc"

p = Product()
print(p)

print("-"* 50 )

from datetime import datetime, UTC
import time

class BadExample(BaseModel):
    created_dt: datetime = datetime.now(UTC)

b1 = BadExample()
b2 = BadExample()

print(b1)
time.sleep(2)
print(b2)
print(b1.created_dt == b2.created_dt) # always True 
print("-"*20)

# correct example 
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
import time

class GoodExample(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

g1 = GoodExample()
time.sleep(2)
g2 = GoodExample()

print(g1)
print(g2)
print(g1.created_at == g2.created_at) # always false 

print("-"*50)

from datetime import datetime, UTC 
from uuid import UUID, uuid4 
from pydantic import BaseModel, Field 

class LLMChatRequest(BaseModel):
    # Required
    prompt: str

    # Optional with sensible production defaults
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int | None = None          # None = let provider use model default
    system_prompt: str | None = None       # Optional system instruction
    stop_sequences: list[str] = Field(default_factory=list)

    # Auto-generated metadata per request
    trace_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

req = LLMChatRequest(prompt="Explain RAG in 2 sentences.")
print(req)

req.stop_sequences.append("hello stop")

print(req)

print("-"* 50 )

class Prompt(BaseModel):
    text: str = Field(description="User text value")
    user_id: str = Field(...,description="Caller user id")
    value: str | None = Field(default=None, description="randome value")

print(Prompt(text="abc",user_id="pqr",value=None))

print("-"*50)
# How to validate default value 
class ValidateVal(BaseModel):
    product_id: int = Field(default="xyz", validate_default=True)

try: 
    ValidateVal()
except ValidationError as e:
    print(e.errors()[0]['msg'])

print("-"*50)

# Dynamic data assign 
class ModelData(BaseModel):
    model_name : str
    version: int = 1 
    attribute_val: str = Field(
        default_factory=lambda data:f"{data['model_name']}:{data['version']}"
    )

a = ModelData(model_name="gpt")
print(a)

# Question for students 
"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via default_factory)

Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""

