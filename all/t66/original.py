from typing import Iterable


def topological_sort(courses: Iterable[Course]) -> Iterable[Course]:
    '''
    This function was written by ChatGPT.

    Performs a topological sort on a collection of courses.
    This function uses the Kahn's algorithm to perform a topological sort, which has a time complexity of O(n + m),
    where n is the number of courses and m is the number of prerequisites.
    '''
    graph = {course.id: [] for course in courses}
    indegrees = {course.id: 0 for course in courses}

    # Build the graph and calculate the indegrees
    for course in courses:
        for prereq in course.must_courses + course.recommend_courses:
            graph[prereq].append(course.id)
            indegrees[course.id] += 1

    # Perform a topological sort using a queue
    queue = deque(
        [course.id for course in courses if indegrees[course.id] == 0])
    levels = {course.id: 0 for course in courses}
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                levels[neighbor] = levels[curr] + 1

    return [LeveledCourse(course, level=levels[course.id]) for course in courses]