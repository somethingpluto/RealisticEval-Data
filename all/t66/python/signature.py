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
