from dataclasses import is_dataclass
from typing import Any, Dict


def class_to_dict(obj: Any) -> Dict[str, Any]:
    """
    Converts a dataclass or class instance to a dictionary.

    Args:
        obj: An instance of a dataclass or a class.

    Returns:
        A dictionary representation of the class or dataclass.
    """
    if is_dataclass(obj):
        return obj.__dict__
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}
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