# This file was originally created by GPT-4 (GPT UIO), and I've made som adjustments
# Designed for effective insert and delete at both ends of a deque
# Also designed for effective search (at the cost of memory usage)

from collections import deque

class CoordinateManager:
    def __init__(self):
        self.coordinates_deque = deque()
        self.coordinates_set = set()

    def add(self, x, y): # adds at end
        coord = (x, y)
        if coord not in self.coordinates_set:
            self.coordinates_deque.append(coord)
            self.coordinates_set.add(coord)

    def add_first(self, x, y):
        coord = (x, y)
        if coord not in self.coordinates_set:
            self.coordinates_deque.appendleft(coord)
            self.coordinates_set.add(coord)

    def remove_last(self):
        if self.coordinates_deque:
            coord = self.coordinates_deque.pop()
            self.coordinates_set.remove(coord)
            return coord

    # My comment: This method is unnecessary (head's pos is never removed_first)
    # def remove_first(self):
    #     if self.coordinates_deque:
    #         coord = self.coordinates_deque.popleft()
    #         self.coordinates_set.remove(coord)
    #         return coord

    def contains(self, x, y):
        return (x, y) in self.coordinates_set
    
    def clear(self):
        self.coordinates_deque.clear()
        self.coordinates_set.clear()

    def __repr__(self):
        return repr(self.coordinates_deque)