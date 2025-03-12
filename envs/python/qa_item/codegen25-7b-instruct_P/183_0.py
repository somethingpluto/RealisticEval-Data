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
,
 
y
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






c
l
a
s
s
 
R
a
y
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
 
o
r
i
g
i
n
,
 
d
i
r
e
c
t
i
o
n
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
o
r
i
g
i
n
 
=
 
o
r
i
g
i
n
 
 
#
 
S
t
a
r
t
i
n
g
 
p
o
i
n
t
 
o
f
 
t
h
e
 
r
a
y


 
 
 
 
 
 
 
 
s
e
l
f
.
d
i
r
e
c
t
i
o
n
 
=
 
d
i
r
e
c
t
i
o
n
 
 
#
 
D
i
r
e
c
t
i
o
n
 
o
f
 
t
h
e
 
r
a
y
 
(
s
h
o
u
l
d
 
b
e
 
n
o
r
m
a
l
i
z
e
d
)






c
l
a
s
s
 
C
i
r
c
l
e
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
 
c
e
n
t
e
r
,
 
r
a
d
i
u
s
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
c
e
n
t
e
r
 
=
 
c
e
n
t
e
r
 
 
#
 
C
e
n
t
e
r
 
o
f
 
t
h
e
 
c
i
r
c
l
e


 
 
 
 
 
 
 
 
s
e
l
f
.
r
a
d
i
u
s
 
=
 
r
a
d
i
u
s
 
 
#
 
R
a
d
i
u
s
 
o
f
 
t
h
e
 
c
i
r
c
l
e






d
e
f
 
i
n
t
e
r
s
e
c
t
s
(
r
a
y
:
 
R
a
y
,
 
c
i
r
c
l
e
:
 
C
i
r
c
l
e
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
a
 
r
a
y
 
i
n
t
e
r
s
e
c
t
s
 
w
i
t
h
 
a
 
c
i
r
c
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
a
y
 
(
R
a
y
)
:
 
T
h
e
 
r
a
y
 
t
o
 
b
e
 
t
e
s
t
e
d
 
f
o
r
 
i
n
t
e
r
s
e
c
t
i
o
n
.
 
I
t
 
i
s
 
a
s
s
u
m
e
d
 
t
o
 
c
o
n
t
a
i
n
 
p
r
o
p
e
r
t
i
e
s
 
s
u
c
h
 
a
s
 
a
n
 
o
r
i
g
i
n
 
p
o
i
n
t
 
(
x
,
 
y
)
 
a
n
d
 
a
 
d
i
r
e
c
t
i
o
n
 
v
e
c
t
o
r
 
(
d
x
,
 
d
y
)
.


 
 
 
 
 
 
 
 
c
i
r
c
l
e
 
(
C
i
r
c
l
e
)
:
 
T
h
e
 
c
i
r
c
l
e
 
t
o
 
c
h
e
c
k
 
f
o
r
 
i
n
t
e
r
s
e
c
t
i
o
n
.
 
I
t
 
i
s
 
a
s
s
u
m
e
d
 
t
o
 
c
o
n
t
a
i
n
 
p
r
o
p
e
r
t
i
e
s
 
s
u
c
h
 
a
s
 
a
 
c
e
n
t
e
r
 
p
o
i
n
t
 
(
h
,
 
k
)
 
a
n
d
 
a
 
r
a
d
i
u
s
 
r
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
r
a
y
 
i
n
t
e
r
s
e
c
t
s
 
t
h
e
 
c
i
r
c
l
e
;
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
c
e
n
t
e
r
 
o
f
 
t
h
e
 
c
i
r
c
l
e
 
a
n
d
 
t
h
e
 
o
r
i
g
i
n
 
o
f
 
t
h
e
 
r
a
y


 
 
 
 
d
i
s
t
a
n
c
e
 
=
 
(
(
r
a
y
.
o
r
i
g
i
n
.
x
 
-
 
c
i
r
c
l
e
.
c
e
n
t
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
r
a
y
.
o
r
i
g
i
n
.
y
 
-
 
c
i
r
c
l
e
.
c
e
n
t
e
r
.
y
)
 
*
*
 
2
)
 
*
*
 
0
.
5




 
 
 
 
#
 
I
f
 
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
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
t
h
e
 
r
a
d
i
u
s
,
 
t
h
e
n
 
t
h
e
 
r
a
y
 
d
o
e
s
 
n
o
t
 
i
n
t
e
r
s
e
c
t
 
t
h
e
 
c
i
r
c
l
e


 
 
 
 
i
f
 
d
i
s
t
a
n
c
e
 
>
 
c
i
r
c
l
e
.
r
a
d
i
u
s
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
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
 
p
r
o
j
e
c
t
i
o
n
 
o
f
 
t
h
e
 
r
a
y
 
o
n
t
o
 
t
h
e
 
c
i
r
c
l
e


 
 
 
 
p
r
o
j
e
c
t
i
o
n
 
=
 
d
i
s
t
a
n
c
e
 
-
 
c
i
r
c
l
e
.
r
a
d
i
u
s




 
 
 
 
#
 
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
o
r
i
g
i
n
 
o
f
 
t
h
e
 
r
a
y
 
a
n
d
 
t
h
e
 
i
n
t
e
r
s
e
c
t
i
o
n
 
p
o
i
n
t
 
o
f
 
t
h
e
 
r
a
y
 
w
i
t
h
 
t
h
e
 
c
i
r
c
l
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
_
i
n
t
e
r
s
e
c
t
i
o
n
 
=
 
(
(
r
a
y
.
o
r
i
g
i
n
.
x
 
-
 
c
i
r
c
l
e
.
c
e
n
t
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
r
a
y
.
o
r
i
g
i
n
.
y
 
-
 
c
i
r
c
l
e
.
c
e
n
t
e
r
.
y
)
 
*
*
 
2
)
 
*
*
 
0
.
5




 
 
 
 
#
 
I
f
 
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
 
b
e
t
w
e
e
n
 
t
h
e
 
o
r
i
g
i
n
 
o
f
 
t
h
e
 
r
a
y
 
a
n
d
 
t
h
e
 
i
n
t
e
r
s
e
c
t
i
o
n
 
p
o
i
n
t
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
t
h
e
 
p
r
o
j
e
c
t
i
o
n
,
 
t
h
e
n
 
t
h
e
 
r
a
y
 
d
o
e
s
 
n
o
t
 
i
n
t
e
r
s
e
c
t
 
t
h
e
 
c
i
r
c
l
e


 
 
 
 
i
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
_
i
n
t
e
r
s
e
c
t
i
o
n
 
>
 
p
r
o
j
e
c
t
i
o
n
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
i
n
t
e
r
s
e
c
t
i
o
n
 
p
o
i
n
t
 
o
f
 
t
h
e
 
r
a
y
 
a
n
d
 
t
h
e
 
c
i
r
c
l
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
_
c
i
r
c
l
e
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # Starting point of the ray
        self.direction = direction  # Direction of the ray (should be normalized)


class Circle:
    def __init__(self, center, radius):
        self.center = center  # Center of the circle
        self.radius = radius  # Radius of the circleimport unittest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # Starting point of the ray
        self.direction = direction  # Direction of the ray (should be normalized)


class Circle:
    def __init__(self, center, radius):
        self.center = center  # Center of the circle
        self.radius = radius  # Radius of the circle


class Tester(unittest.TestCase):
    def test_ray_circle_intersection(self):
        # Test Case 1: The ray intersects the circle at two points
        ray = Ray(Point(0, 0), Point(1, 1))  # Origin at (0, 0), direction (1, 1)
        circle = Circle(Point(3, 3), 2)  # Circle center at (3, 3), radius 2
        self.assertTrue(intersects(ray, circle))

        # Test Case 2: The ray is tangent to the circle (one intersection point)
        ray = Ray(Point(2, 0), Point(0, 1))  # Origin at (2, 0), direction (0, 1)
        circle = Circle(Point(2, 2), 1)  # Circle center at (2, 2), radius 1
        self.assertTrue(intersects(ray, circle))

        # Test Case 3: The ray starts inside the circle (one intersection point)
        ray = Ray(Point(2, 2), Point(1, 0))  # Origin at (2, 2), direction (1, 0)
        circle = Circle(Point(3, 2), 1)  # Circle center at (3, 2), radius 1
        self.assertTrue(intersects(ray, circle))

        # Test Case 4: The ray originates outside and goes away from the circle (no intersection)
        ray = Ray(Point(5, 5), Point(1, 0))  # Origin at (5, 5), direction (1, 0)
        circle = Circle(Point(3, 3), 1)  # Circle center at (3, 3), radius 1
        self.assertFalse(intersects(ray, circle))

        # Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
        ray = Ray(Point(0, 3), Point(1, 0))  # Origin at (0, 3), direction (1, 0)
        circle = Circle(Point(3, 3), 1)  # Circle center at (3, 3), radius 1
        self.assertFalse(intersects(ray, circle))

        # Test Case 6: The ray intersects the circle at one point when passing through the center
        ray = Ray(Point(3, 0), Point(0, 1))  # Origin at (3, 0), direction (0, 1)
        circle = Circle(Point(3, 3), 3)  # Circle center at (3, 3), radius 3
        self.assertTrue(intersects(ray, circle))

if __name__ == '__main__':
    unittest.main()