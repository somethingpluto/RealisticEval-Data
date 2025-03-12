from collections import deque, defaultdict
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
    # Create a mapping from course id to Course object
    course_map = {course.id: course for course in courses}
    
    # Create a mapping from course id to its in-degree (number of prerequisites)
    in_degree = defaultdict(int)
    
    # Create a mapping from course id to its direct successors
    graph = defaultdict(list)
    
    # Initialize in-degree and graph
    for course in courses:
        if course.id not in in_degree:
            in_degree[course.id] = 0
        for prereq_id in course.must_courses:
            if prereq_id in course_map:
                graph[prereq_id].append(course.id)
                in_degree[course.id] += 1
    
    # Initialize the queue with all courses that have no prerequisites
    queue = deque([course_id for course_id in in_degree if in_degree[course_id] == 0])
    
    # List to store the result
    result = []
    
    # Level counter
    level = 0
    
    while queue:
        level += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            course_id = queue.popleft()
            course = course_map[course_id]
            result.append(LeveledCourse(course, level))
            
            for successor_id in graph[course_id]:
                in_degree[successor_id] -= 1
                if in_degree[successor_id] == 0:
                    queue.append(successor_id)
    
    # If the result does not contain all courses, there must be a cycle
    if len(result) != len(courses):
        raise ValueError("Cycle detected in the course prerequisites")
    
    return result
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