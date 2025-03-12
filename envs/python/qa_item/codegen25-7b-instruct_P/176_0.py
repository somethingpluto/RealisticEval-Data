i
m
p
o
r
t
 
m
a
t
h


f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
L
i
s
t






c
l
a
s
s
 
P
o
i
n
t
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
x
:
 
f
l
o
a
t
,
 
y
:
 
f
l
o
a
t
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
x
 
=
 
x


 
 
 
 
 
 
 
 
s
e
l
f
.
y
 
=
 
y




 
 
 
 
d
e
f
 
d
i
s
t
a
n
c
e
_
t
o
(
s
e
l
f
,
 
o
t
h
e
r
:
 
'
P
o
i
n
t
'
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
c
u
l
a
t
e
 
t
h
e
 
E
u
c
l
i
d
e
a
n
 
d
i
s
t
a
n
c
e
 
t
o
 
a
n
o
t
h
e
r
 
p
o
i
n
t
.
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
t
h
.
s
q
r
t
(
(
s
e
l
f
.
x
 
-
 
o
t
h
e
r
.
x
)
 
*
*
 
2
 
+
 
(
s
e
l
f
.
y
 
-
 
o
t
h
e
r
.
y
)
 
*
*
 
2
)






d
e
f
 
f
i
n
d
_
k
_
n
e
a
r
e
s
t
_
n
e
i
g
h
b
o
r
s
(
p
o
i
n
t
s
:
 
L
i
s
t
[
P
o
i
n
t
]
,
 
q
u
e
r
y
_
p
o
i
n
t
:
 
P
o
i
n
t
,
 
k
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
P
o
i
n
t
]
:


 
 
 
 
"
"
"
F
i
n
d
 
t
h
e
 
k
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
 
t
o
 
t
h
e
 
q
u
e
r
y
_
p
o
i
n
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
s
 
(
L
i
s
t
[
P
o
i
n
t
]
)
:
 
A
 
l
i
s
t
 
o
f
 
P
o
i
n
t
 
o
b
j
e
c
t
s
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
a
v
a
i
l
a
b
l
e
 
p
o
i
n
t
s
 
i
n
 
t
h
e
 
s
p
a
c
e
.


 
 
 
 
 
 
 
 
q
u
e
r
y
_
p
o
i
n
t
 
(
P
o
i
n
t
)
:
 
T
h
e
 
P
o
i
n
t
 
o
b
j
e
c
t
 
f
o
r
 
w
h
i
c
h
 
w
e
 
w
a
n
t
 
t
o
 
f
i
n
d
 
t
h
e
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
.


 
 
 
 
 
 
 
 
k
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
 
t
o
 
f
i
n
d
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
L
i
s
t
[
P
o
i
n
t
]
:
 
A
 
l
i
s
t
 
o
f
 
t
h
e
 
k
 
n
e
a
r
e
s
t
 
P
o
i
n
t
 
o
b
j
e
c
t
s
 
t
o
 
t
h
e
 
q
u
e
r
y
_
p
o
i
n
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
T
O
D
O
:
 
I
m
p
l
e
m
e
n
t
 
t
h
e
 
K
N
N
 
a
l
g
o
r
i
t
h
m
 
t
o
 
f
i
n
d
 
t
h
e
 
k
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
 
t
o
 
t
h
e
 
q
u
e
r
y
_
p
o
i
n
t
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
d
i
s
t
a
n
c
e
_
t
o
(
)
 
m
e
t
h
o
d
 
o
f
 
t
h
e
 
P
o
i
n
t
 
c
l
a
s
s
 
t
o
 
c
a
l
c
u
l
a
t
e
 
t
h
e
 
d
i
s
t
a
n
c
e


 
 
 
 
#
 
b
e
t
w
e
e
n
 
t
w
o
 
p
o
i
n
t
s
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
s
o
r
t
 
t
h
e
 
p
o
i
n
t
s
 
b
a
s
e
d
 
o
n
 
t
h
e
i
r
 
d
i
s
t
a
n
c
e
 
t
o
 
t
h
e
 
q
u
e
r
y
_
p
o
i
n
t
 
u
s
i
n
g
 
t
h
e
 
s
o
r
t
(
)
 
m
e
t
h
o
d


 
 
 
 
#
 
o
f
 
t
h
e
 
l
i
s
t
 
c
l
a
s
s
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
r
e
t
u
r
n
 
t
h
e
 
f
i
r
s
t
 
k
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
s
o
r
t
e
d
 
l
i
s
t
 
a
s
 
t
h
e
 
k
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
_
_
l
t
_
_
(
)
 
m
e
t
h
o
d
 
o
f
 
t
h
e
 
P
o
i
n
t
 
c
l
a
s
s
 
t
o
 
d
e
f
i
n
e
 
t
h
e
 
c
o
m
p
a
r
i
s
o
n
 
o
p
e
r
a
t
o
r


 
 
 
 
#
 
f
o
r
 
s
o
r
t
i
n
g
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
e
n
u
m
e
r
a
t
e
(
)
 
f
u
n
c
t
i
o
n
 
t
o
 
i
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
p
o
i
n
t
s
 
l
i
s
t
 
a
n
d
 
k
e
e
p
 
t
r
a
c
k
 
o
f


 
 
 
 
#
 
t
h
e
 
i
n
d
e
x
 
o
f
 
e
a
c
h
 
p
o
i
n
t
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
z
i
p
(
)
 
f
u
n
c
t
i
o
n
 
t
o
 
c
o
m
b
i
n
e
 
t
h
e
 
p
o
i
n
t
s
 
l
i
s
t
 
a
n
d
 
t
h
e
 
i
n
d
i
c
e
s
 
l
i
s
t
 
t
o
 
g
e
t


 
 
 
 
#
 
t
u
p
l
e
s
 
o
f
 
t
h
e
 
f
o
r
m
 
(
i
n
d
e
x
,
 
p
o
i
n
t
)
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
s
o
r
t
 
t
h
e
 
t
u
p
l
e
s
 
b
a
s
e
d
 
o
n
 
t
h
e
i
r
 
s
e
c
o
n
d
 
e
l
e
m
e
n
t
 
(
i
.
e
.
,
 
t
h
e
 
d
i
s
t
a
n
c
e
 
t
o
 
t
h
e
 
q
u
e
r
y
_
p
o
i
n
t
)


 
 
 
 
#
 
u
s
i
n
g
 
t
h
e
 
s
o
r
t
(
)
 
m
e
t
h
o
d
 
o
f
 
t
h
e
 
l
i
s
t
 
c
l
a
s
s
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
r
e
t
u
r
n
 
t
h
e
 
f
i
r
s
t
 
k
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
s
o
r
t
e
d
 
l
i
s
t
 
a
s
 
t
h
e
 
k
 
n
e
a
r
e
s
t
 
n
e
i
g
h
b
o
r
s
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
_
_
g
e
t
i
t
e
m
_
_
(
)
 
m
e
t
h
o
d
 
o
f
 
t
h
e
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)import math
import unittest


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Tester(unittest.TestCase):

    def test_find_k_nearest_neighbors_simple_case(self):
        points = [
            Point(1, 2),
            Point(3, 4),
            Point(1, -1),
            Point(5, 2)
        ]
        query_point = Point(2, 2)
        k = 2
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Point(1, 2)))
        self.assertTrue(self.contains_point(result, Point(3, 4)))

    def test_find_k_nearest_neighbors_exact_match(self):
        points = [
            Point(1, 2),
            Point(2, 2),
            Point(3, 3)
        ]
        query_point = Point(2, 2)
        k = 1
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0].x, 2.0, delta=0.001)
        self.assertAlmostEqual(result[0].y, 2.0, delta=0.001)

    def test_find_k_nearest_neighbors_larger_k(self):
        points = [
            Point(1, 2),
            Point(3, 4),
            Point(1, -1),
            Point(5, 2)
        ]
        query_point = Point(2, 2)
        k = 5  # k is larger than the number of points
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 4)

    def test_find_k_nearest_neighbors_empty_points(self):
        points = []
        query_point = Point(2, 2)
        k = 3
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 0)

    def test_find_k_nearest_neighbors_all_points_equidistant(self):
        points = [
            Point(2, 3),
            Point(3, 2),
            Point(1, 2),
            Point(2, 1)
        ]
        query_point = Point(2, 2)
        k = 2
        result = find_k_nearest_neighbors(points, query_point, k)

        self.assertEqual(len(result), 2)
        self.assertTrue(self.contains_point(result, Point(2, 3)))
        self.assertTrue(self.contains_point(result, Point(3, 2)))

    def contains_point(self, points, point):
        for p in points:
            if math.isclose(p.x, point.x, abs_tol=0.001) and math.isclose(p.y, point.y, abs_tol=0.001):
                return True
        return False

if __name__ == '__main__':
    unittest.main()