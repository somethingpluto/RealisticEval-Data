from typing import Iterable, List

class Course:
    def __init__(self, course_id, must_courses=None, recommend_courses=None):
        self.id = course_id
        self.must_courses = must_courses if must_courses is not None else []
        self.recommend_courses = recommend_courses if recommend_courses is not None else []

class LeveledCourse:
    def __init__(self, course: Course, level: int):
        self.course = course
        self.level = level

def topological_sort(courses: Iterable[Course]) -> List[LeveledCourse]:
    from collections import defaultdict, deque

    # Create a graph from the courses
    graph = defaultdict(list)
    in_degree = {course.id: 0 for course in courses}

    # Populate the graph and in_degree map
    for course in courses:
        for must_course_id in course.must_courses:
            graph[course.id].append(must_course_id)
            in_degree[must_course_id] += 1

    # Initialize the queue with courses having zero in-degree
    zero_in_degree_queue = deque([course.id for course in courses if in_degree[course.id] == 0])

    # List to store the topological order
    topological_order = []

    # Perform Kahn's algorithm
    while zero_in_degree_queue:
        course_id = zero_in_degree_queue.popleft()
        topological_order.append(course_id)

        # Decrease the in-degree of neighboring nodes
        for neighbor in graph[course_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)

    # Check if topological sort is possible (i.e., graph has a cycle)
    if len(topological_order) != len(courses):
        raise ValueError("Cycle detected in the courses, topological sort is not possible.")

    # Assign levels to each course in the topological order
    level_map = {course_id: i for i, course_id in enumerate(topological_order)}
    leveled_courses = [LeveledCourse(course, level_map[course.id]) for course in courses]

    return leveled_courses
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