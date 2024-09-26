import unittest
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

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

class TestCanClassToDict(unittest.TestCase):

    def test_dataclass(self):
        person = Person(name="Alice", age=30)
        self.assertTrue(can_class_to_dict(person))

    def test_regular_class(self):
        car = Car(make="Toyota", model="Corolla")
        self.assertTrue(can_class_to_dict(car))

    def test_regular_class_with_private_attribute(self):
        dog = Dog(name="Buddy", breed="Golden Retriever")
        self.assertTrue(can_class_to_dict(dog))

    def test_empty_class(self):
        empty = EmptyClass()
        self.assertTrue(can_class_to_dict(empty))

    def test_class_with_class_variable(self):
        student = Student(name="John")
        self.assertTrue(can_class_to_dict(student))

    def test_non_class_object(self):
        number = 42
        self.assertFalse(can_class_to_dict(number))
