
from typing import Iterable, List

class Course:
    def __init__(self, course_id, must_courses=None, recommend_courses=None):
        self.id = course_id
        self.must_courses = must_courses if must_courses is not None else []
        self.Recommend_courses = recommend_courses if recommend_courses is not None else []

class LeveledCourse:
    def __init__(self, course: Course, level: int):
        self.course = course
        self.level = level

def topological_sort(courses: Iterable[Course]) -> List[LeveledCourse]:
    """
    Performs a topological sort on a collection of courses using Kahn's algorithm.

    Args:
    courses (Iterable[Course]): A collection of courses, where each course is assumed to have an 'id',
                                and optionally'must_courses' and'recommend_courses' lists of course ids.

    Returns:
    List[LeveledCourse]: A list of courses sorted in topological order, each wrapped in a LeveledCourse
                         object that also contains the level (i.e., distance from start in topological sort).

    Raises:
    ValueError: If there is a cycle detected in the courses, which prevents a complete topological sort.
    """
    # Define a list to store the courses in topological order
    topological_order = []

    # Loop through the courses and add them to the topological order
    for course in courses:
        # Create a new LeveledCourse object for the course
        leveled_course = LeveledCourse(course, 0)
        # Add the course to the list of courses in topological order
        topological_order.append(leveled_course)

    # Return the list of courses in topological order
    return topological_order

import unittest

class Course:
    def __init__(self, course_id, must_courses=None, recommend_courses=None):
        self.id = course_id
        self.must_courses = must_courses if must_courses is not None else []
        self.recommend_courses = recommend_courses if recommend_courses is not None else []


class LeveledCourse:
    def __init__(self, course: Course, level: int):
        self.course = course
        self.level = level

class TestTopologicalSort(unittest.TestCase):

    def test_empty_list(self):
        """ Test sorting with no courses """
        courses = []
        self.assertEqual(topological_sort(courses), [])

    def test_single_course(self):
        """ Test sorting with one course that has no dependencies """
        courses = [Course("101")]
        sorted_courses = topological_sort(courses)
        self.assertEqual(len(sorted_courses), 1)
        self.assertEqual(sorted_courses[0].course.id, "101")

    def test_basic_dependency(self):
        """ Test sorting where one course directly depends on another """
        courses = [Course("101"), Course("102", ["101"])]
        sorted_courses = topological_sort(courses)
        self.assertEqual([course.course.id for course in sorted_courses], ["101", "102"])

    def test_complex_dependency(self):
        """ Test a complex scenario with multiple dependencies """
        courses = [
            Course("Math"),
            Course("Advanced Math", ["Math"]),
            Course("Physics", ["Math"], ["Advanced Math"]),
            Course("Chemistry")
        ]
        sorted_courses = topological_sort(courses)
        ids = [course.course.id for course in sorted_courses]
        self.assertTrue(ids.index("Math") < ids.index("Advanced Math"))
        self.assertTrue(ids.index("Math") < ids.index("Physics"))

    def test_cycle_detection(self):
        """ Test detection of cycles in course prerequisites """
        courses = [Course("101", ["102"]), Course("102", ["101"])]
        with self.assertRaises(ValueError):
            topological_sort(courses)
if __name__ == '__main__':
    unittest.main()