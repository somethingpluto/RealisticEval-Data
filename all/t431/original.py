import collections
import unittest


class TestPath(unittest.TestCase):

    def test_path(self):
        expect = [
            [(0, 0, 2, 2), (1, 1, 3, 3), (3, 0, 5, 2), (4, 1, 6, 3)],
            [(0, 0, 2, 2), (1, 1, 3, 3), (4, 1, 6, 3)],
            [(0, 0, 2, 2), (3, 0, 5, 2), (1, 1, 3, 3), (4, 1, 6, 3)],
            [(0, 0, 2, 2), (3, 0, 5, 2), (4, 1, 6, 3)],
            [(0, 0, 2, 2), (4, 1, 6, 3)]
        ]
        rectangles = [(0, 0, 2, 2), (1, 1, 3, 3), (3, 0, 5, 2), (4, 1, 6, 3)]
        nodes, relations = create_rectangles_and_relations(rectangles)
        start_rect = (0, 0, 2, 2)
        end_rect = (4, 1, 6, 3)
        paths = find_paths_between_rectangles(nodes, relations, start_rect, end_rect)
        self.assertEqual(paths, expect)


def intersect_horizontally(rect1, rect2):
    return not (rect1[2] < rect2[0] or rect2[2] < rect1[0])


def intersect_vertically(rect1, rect2):
    return not (rect1[3] < rect2[1] or rect2[3] < rect1[1])


def create_rectangles_and_relations(rectangles):
    """
    Create nodes for rectangles and establish relations based on whether they
    touch each other.

    Args:
    rectangles: A list of rectangles represented by tuples (left, top, right, bottom).

    Returns:
    nodes: A dictionary representing nodes (rectangles).
    relations: A dictionary representing relations between rectangles.
    """
    nodes = {}
    relations = collections.defaultdict(list)

    def establish_relations(rect1, rect2):
        if (
                intersect_horizontally(rect1, rect2)
                or intersect_vertically(rect1, rect2)
        ):
            relations[rect1].append(rect2)
            relations[rect2].append(rect1)

    # Create nodes for rectangles
    for rect in rectangles:
        nodes[rect] = {
            'left': rect[0],
            'top': rect[1],
            'right': rect[2],
            'bottom': rect[3]
        }

    # Establish relations between rectangles
    for i, rect1 in enumerate(rectangles):
        for rect2 in rectangles[i + 1:]:
            establish_relations(rect1, rect2)

    return nodes, relations


def find_paths_between_rectangles(
        nodes,
        relations,
        start_rect,
        end_rect,
        visited=None,
        path=None,
):
    """
    Find paths between two rectangles using depth-first search.

    Args:
    nodes: A dictionary of nodes representing rectangles.
    relations: A dictionary representing relations between rectangles.
    start_rect: The starting rectangle.
    end_rect: The ending rectangle.
    visited: A set of visited rectangles to avoid cycles (default None).
    path: The current path being explored (default None).

    Returns:
    paths: A list of paths between start_rect and end_rect.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start_rect)
    path.append(start_rect)

    paths = []
    if start_rect == end_rect:
        paths.append(path.copy())
    else:
        for neighbor in relations.get(start_rect, []):
            if neighbor in visited:
                continue
            paths.extend(
                find_paths_between_rectangles(
                    nodes,
                    relations,
                    neighbor,
                    end_rect,
                    visited,
                    path,
                )
            )
    path.pop()
    visited.remove(start_rect)
    return paths
