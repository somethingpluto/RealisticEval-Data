from collections import deque
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
    """
    Performs a topological sort on a collection of courses using Kahn's algorithm.

    Args:
    courses (Iterable[Course]): A collection of courses, where each course is assumed to have an 'id',
                                and optionally 'must_courses' and 'recommend_courses' lists of course ids.

    Returns:
    List[LeveledCourse]: A list of courses sorted in topological order, each wrapped in a LeveledCourse
                         object that also contains the level (i.e., distance from start in topological sort).

    Raises:
    ValueError: If there is a cycle detected in the courses, which prevents a complete topological sort.
    """
    graph = {course.id: [] for course in courses}
    indegrees = {course.id: 0 for course in courses}

    # Build the graph and calculate the indegrees
    for course in courses:
        for prereq in course.must_courses + course.recommend_courses:
            graph[prereq].append(course.id)
            indegrees[course.id] += 1

    # Perform a topological sort using a queue
    queue = deque([course.id for course in courses if indegrees[course.id] == 0])
    levels = {course.id: 0 for course in courses}
    sorted_courses = []

    while queue:
        curr = queue.popleft()
        sorted_courses.append(curr)
        for neighbor in graph[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                levels[neighbor] = levels[curr] + 1

    if len(sorted_courses) != len(courses):
        raise ValueError("There is a cycle in the courses")

    return [LeveledCourse(course, level=levels[course.id]) for course in courses if course.id in levels]
