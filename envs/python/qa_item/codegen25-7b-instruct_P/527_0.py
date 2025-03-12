d
e
f
 
i
s
_
p
o
i
n
t
_
i
n
s
i
d
e
_
t
r
i
a
n
g
l
e
(
p
x
:
 
f
l
o
a
t
,
 
p
y
:
 
f
l
o
a
t
,
 
x
1
:
 
f
l
o
a
t
,
 
y
1
:
 
f
l
o
a
t
,
 
x
2
:
 
f
l
o
a
t
,
 
y
2
:
 
f
l
o
a
t
,
 
x
3
:
 
f
l
o
a
t
,
 
y
3
:
 
f
l
o
a
t
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
i
f
 
a
 
p
o
i
n
t
 
i
s
 
i
n
s
i
d
e
 
a
 
t
r
i
a
n
g
l
e
 
d
e
f
i
n
e
d
 
b
y
 
t
h
r
e
e
 
v
e
r
t
i
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
x
 
(
f
l
o
a
t
)
:
 
T
h
e
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
p
o
i
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
p
y
 
(
f
l
o
a
t
)
:
 
T
h
e
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
p
o
i
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
x
1
 
(
f
l
o
a
t
)
:
 
T
h
e
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
.


 
 
 
 
 
 
 
 
y
1
 
(
f
l
o
a
t
)
:
 
T
h
e
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
.


 
 
 
 
 
 
 
 
x
2
 
(
f
l
o
a
t
)
:
 
T
h
e
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
.


 
 
 
 
 
 
 
 
y
2
 
(
f
l
o
a
t
)
:
 
T
h
e
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
.


 
 
 
 
 
 
 
 
x
3
 
(
f
l
o
a
t
)
:
 
T
h
e
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
t
h
i
r
d
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
.


 
 
 
 
 
 
 
 
y
3
 
(
f
l
o
a
t
)
:
 
T
h
e
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
t
h
i
r
d
 
v
e
r
t
e
x
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
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
 
p
o
i
n
t
 
(
p
x
,
 
p
y
)
 
i
s
 
i
n
s
i
d
e
 
o
r
 
o
n
 
t
h
e
 
e
d
g
e
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e
 
f
o
r
m
e
d
 
b
y
 
t
h
e
 
v
e
r
t
i
c
e
s
 
(
x
1
,
 
y
1
)
,
 
(
x
2
,
 
y
2
)
,
 
(
x
3
,
 
y
3
)
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
h
e
c
k
 
i
f
 
t
h
e
 
p
o
i
n
t
 
i
s
 
o
n
 
t
h
e
 
e
d
g
e
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e


 
 
 
 
i
f
 
(
x
1
 
=
=
 
x
2
 
a
n
d
 
y
1
 
=
=
 
y
2
)
 
o
r
 
(
x
1
 
=
=
 
x
3
 
a
n
d
 
y
1
 
=
=
 
y
3
)
 
o
r
 
(
x
2
 
=
=
 
x
3
 
a
n
d
 
y
2
 
=
=
 
y
3
)
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
h
e
c
k
 
i
f
 
t
h
e
 
p
o
i
n
t
 
i
s
 
o
n
 
t
h
e
 
e
d
g
e
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e


 
 
 
 
i
f
 
(
x
2
 
-
 
x
1
)
 
*
 
(
y
3
 
-
 
y
1
)
 
-
 
(
x
3
 
-
 
x
1
)
 
*
 
(
y
2
 
-
 
y
1
)
 
=
=
 
0
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
h
e
c
k
 
i
f
 
t
h
e
 
p
o
i
n
t
 
i
s
 
o
n
 
t
h
e
 
e
d
g
e
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e


 
 
 
 
i
f
 
(
x
3
 
-
 
x
1
)
 
*
 
(
y
2
 
-
 
y
1
)
 
-
 
(
x
2
 
-
 
x
1
)
 
*
 
(
y
3
 
-
 
y
1
)
 
=
=
 
0
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
h
e
c
k
 
i
f
 
t
h
e
 
p
o
i
n
t
 
i
s
 
o
n
 
t
h
e
 
e
d
g
e
 
o
f
 
t
h
e
 
t
r
i
a
n
g
l
e


 
 
 
 
i
f
 
(
x
3
 
-
 
x
2
)
 
*
 
(
y
1
 
-
 
y
2
)
 
-
 
(
x
1
 
-
 
x
2
)
 
*
 
(
y
3
 
-
 
y
2
)
 
=
=
 
0
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
import unittest


class TestPointInsideTriangle(unittest.TestCase):

    def test_point_inside_triangle(self):
        """Test case where point is inside the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (2.5, 2)  # Inside the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_on_edge(self):
        """Test case where point is on the edge of the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (2.5, 0)  # On the edge of the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_outside_triangle(self):
        """Test case where point is outside the triangle."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (6, 2)  # Outside the triangle
        self.assertFalse(is_point_inside_triangle(point[0], point[1], *triangle_vertices))

    def test_point_at_vertex(self):
        """Test case where point is at one of the triangle's vertices."""
        triangle_vertices = (0, 0, 5, 0, 2.5, 5)
        point = (0, 0)  # At the vertex of the triangle
        self.assertTrue(is_point_inside_triangle(point[0], point[1], *triangle_vertices))
if __name__ == '__main__':
    unittest.main()