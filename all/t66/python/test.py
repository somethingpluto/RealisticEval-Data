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