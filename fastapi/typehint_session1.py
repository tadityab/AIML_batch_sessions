

# str = "Ram"

# print(type(str))


a = 10 

print(type(a))

a = '10'

print(type(a))

print("-"*20)

text: str = "Ram"

text1: str = "100"

print(type(text))
print(type(text1))

text2: str = 100

print(type(text2))


print("-" * 20)

def fun(param):
    param.reverse()
    return param

print(fun(['1','2']))


def fun1(param: list[str]) -> list[str]:
    param.reverse()
    return param 


print(fun1(['1','2']))

def full_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()

print(full_name("ram","patil"))


def full_name1(first_name: str, last_name:str) -> str:
    return first_name.title() + " " + last_name.title()

print(full_name1("sham","patil"))

print("-"*20)

"""
Types in Type Hint
1. str
2. int
3. bool
4. bytes
5. float 
"""

def get_items(item_a: str, item_b: int, item_c: bool, item_d: bytes, item_e: float):
    return item_a, item_b, item_c, item_d, item_e

print(get_items('Ram', 100, True, b"a", 10.2))

print("-"*20)

from typing  import Any

def random_func(data: Any):
    return data 

print(random_func("Ram"))
print(random_func(100))

print("-"*20)

"""Generic Type

1. list[str]
2. tuple[int, int, int]
3. set[bytes]
4. dict[str, str]
"""

def process_list(items: list[str]) -> None:
    for item in items:
        print(item)

process_list(['1','2','3'])

print("-"*10)

def proces_tuple_and_set(item_t:tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s

print(proces_tuple_and_set((1,2,'a'),{b'a'}))

print("-"*10)

def process_dict(prices: dict[str, int]):
    for item_name, item_price in prices.items():
        print(item_name," -> ", item_price)

process_dict({"chair":100,"table":250})

print("-"*20)

"""Union
Declare variables accepting multiple types using '|'
"""

def process_id(item: str | int):
    print("ID : ", item, "of type : ", type(item))

process_id(100)
process_id("Ram")


def bwt_hi(name: str | None = None):
    if name is not None:
        print("Hello ",name)
    else:
        print("Hello BWT Class...!")

bwt_hi("Ram")
bwt_hi()

print("-" * 20)

from collections.abc import Iterable

def reverse_array(items: Iterable[str]) -> list[str]:
    return list(items)[::-1]

print(reverse_array(['1','2']))

print("-" * 20)

class Person:
    def __init__(self, name: str):
        self.name = name 

def get_person_name(one_person: Person)-> str:
    return one_person.name

p = Person("Ram")

print(get_person_name(p))

print("-" * 20)
 
# Literal in TypeHint 

from typing import Literal 

def set_access(name: str, role: Literal["admin","editor","viewer"]) -> str:
    return f"{name} has a {role} permission"

print(set_access("Ram","admin"))
print(set_access("Sham","viewer"))
print(set_access("Kiran","xyz"))

print("-" * 20)

# Enum in TypeHint 

from enum import Enum 

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

def assign_role(user: str, role: Role) -> str:
    return f"{user} has a role name = {role.name}, role value = {role.value}"

print(assign_role("Ram",Role.ADMIN))

