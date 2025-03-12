f
r
o
m
 
d
a
t
a
c
l
a
s
s
e
s
 
i
m
p
o
r
t
 
i
s
_
d
a
t
a
c
l
a
s
s


f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
A
n
y
,
 
D
i
c
t






d
e
f
 
c
l
a
s
s
_
t
o
_
d
i
c
t
(
o
b
j
:
 
A
n
y
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
d
a
t
a
c
l
a
s
s
 
o
r
 
c
l
a
s
s
 
i
n
s
t
a
n
c
e
 
t
o
 
a
 
d
i
c
t
i
o
n
a
r
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
b
j
:
 
A
n
 
i
n
s
t
a
n
c
e
 
o
f
 
a
 
d
a
t
a
c
l
a
s
s
 
o
r
 
a
 
c
l
a
s
s
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
d
i
c
t
i
o
n
a
r
y
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
c
l
a
s
s
 
o
r
 
d
a
t
a
c
l
a
s
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
s
_
d
a
t
a
c
l
a
s
s
(
o
b
j
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
{
f
.
n
a
m
e
:
 
g
e
t
a
t
t
r
(
o
b
j
,
 
f
.
n
a
m
e
)
 
f
o
r
 
f
 
i
n
 
f
i
e
l
d
s
(
o
b
j
)
}


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
o
b
j
.
_
_
d
i
c
t
_
_


import unittest
from dataclasses import dataclass


# The class_to_dict function should already be defined above.

@dataclass
class Person:
    name: str
    age: int


class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.year = 2020


class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        self._age = 5  # Private attribute


class EmptyClass:
    pass


class Student:
    school_name = "Example School"

    def __init__(self, name: str):
        self.name = name
        self.grade = "A"


class TestClassToDict(unittest.TestCase):

    def test_dataclass(self):
        person = Person(name="Alice", age=30)
        self.assertEqual(class_to_dict(person), {'name': 'Alice', 'age': 30})

    def test_regular_class(self):
        car = Car(make="Toyota", model="Corolla")
        self.assertEqual(class_to_dict(car), {'make': 'Toyota', 'model': 'Corolla', 'year': 2020})

    def test_empty_class(self):
        empty = EmptyClass()
        self.assertEqual(class_to_dict(empty), {})

    def test_class_with_class_variable(self):
        student = Student(name="John")
        self.assertEqual(class_to_dict(student), {'name': 'John', 'grade': 'A'})

if __name__ == '__main__':
    unittest.main()