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
_
p
o
l
y
g
o
n
(
p
o
i
n
t
:
 
t
u
p
l
e
,
 
p
o
l
y
g
o
n
:
 
L
i
s
t
[
t
u
p
l
e
]
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
x
,
 
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
 
t
h
e
 
g
i
v
e
n
 
p
o
l
y
g
o
n
.


 
 
 
 
T
h
e
 
p
o
l
y
g
o
n
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
 
(
x
,
 
y
)
 
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
o
i
n
t
:
 
A
 
t
u
p
l
e
 
(
x
,
 
y
)
 
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
o
l
y
g
o
n
:
 
A
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
 
(
x
,
 
y
)
 
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
 
v
e
r
t
i
c
e
s
 
o
f
 
t
h
e
 
p
o
l
y
g
o
n
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
 
i
s
 
i
n
s
i
d
e
 
t
h
e
 
p
o
l
y
g
o
n
,
 
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
 
a
 
b
o
u
n
d
a
r
y


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
p
o
l
y
g
o
n
)
)
:


 
 
 
 
 
 
 
 
p
1
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
p
2
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
i
f
 
i
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
p
1
 
=
 
p
o
l
y
g
o
n
[
0
]


 
 
 
 
 
 
 
 
 
 
 
 
p
2
 
=
 
p
o
l
y
g
o
n
[
1
]


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
p
1
 
=
 
p
o
l
y
g
o
n
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
p
2
 
=
 
p
o
l
y
g
o
n
[
i
 
+
 
1
]


 
 
 
 
 
 
 
 
i
f
 
p
1
[
1
]
 
=
=
 
p
2
[
1
]
 
a
n
d
 
p
1
[
1
]
 
=
=
 
p
o
i
n
t
[
1
]
 
a
n
d
 
m
i
n
(
p
1
[
0
]
,
 
p
2
[
0
]
)
 
<
=
 
p
o
i
n
t
[
0
]
 
<
=
 
m
a
x
(
p
1
[
0
]
,
 
p
2
[
0
]
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
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
 
i
n
s
i
d
e
 
t
h
e
 
p
o
l
y
g
o
n


 
 
 
 
i
s
_
i
n
s
i
d
e
 
=
 
F
a
l
s
e


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
p
o
l
y
g
o
n
)
)
:


 
 
 
 
 
 
 
 
p
1
 
=
 
p
o
l
y
g
o
n
[
i
]


 
 
 
 
 
 
 
 
p
2
 
=
 
p
o
l
y
g
o
n
[
(
i
 
+
 
1
)
 
%
 
l
e
n
(
p
o
l
y
g
o
n
)
]


 
 
 
 
 
 
 
 
i
f
 
(
p
1
[
1
]
 
>
 
p
o
i
n
t
[
1
]
)
 
!
=
 
(
p
2
[
1
]
 
>
 
p
o
i
n
t
[
1
]
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
p
o
i
n
t
[
0
]
 
<
 
(
p
2
[
0
]
 
-
 
p
1
[
0
]
)
 
*
 
(
p
o
i
n
t
[
1
]
 
-
 
p
1
[
1
]
)
 
/
 
(
p
2
[
1
]
 
-
 
p
1
[
1
]
)
 
+
 
p
1
[
0
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
s
_
i
n
s
i
d
e
 
=
 
n
o
t
 
i
s
_
i
n
s
i
d
e


 
 
 
 
r
e
t
u
r
n
 
i
s
_
i
n
s
i
d
e






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
_
p
o
l
y
g
o
n
_
2
(
p
o
i
n
t
:
 
t
u
p
l
e
,
 
p
o
l
y
g
o
n
:
 
L
i
s
t
[
t
u
p
l
e
]
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
x
,
 
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
 
t
h
e
 
g
i
v
e
n
 
p
o
l
y
g
o
n
.


 
 
 
 
T
h
e
 
p
o
l
y
g
o
n
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
l
i
s
t
import unittest

class TestPointInPolygon(unittest.TestCase):
    def setUp(self):
        # Define some polygons to use in tests
        self.square = [(0, 0), (0, 10), (10, 10), (10, 0)]
        self.triangle = [(0, 0), (5, 10), (10, 0)]
        self.concave = [(0, 0), (5, 5), (10, 0), (5, 10), (0, 10)]

    def test_point_inside_square(self):
        # Point inside the square
        self.assertTrue(is_point_in_polygon((5, 5), self.square))

    def test_point_outside_square(self):
        # Point outside the square
        self.assertFalse(is_point_in_polygon((15, 5), self.square))

    def test_point_on_edge_of_triangle(self):
        # Point on the edge of the triangle
        self.assertFalse(is_point_in_polygon((5, 0), self.triangle))

    def test_point_inside_concave_polygon(self):
        # Point inside concave polygon
        self.assertTrue(is_point_in_polygon((5, 9), self.concave))

    def test_point_outside_concave_polygon(self):
        # Point outside concave polygon
        self.assertFalse(is_point_in_polygon((5, 1), self.concave))
if __name__ == '__main__':
    unittest.main()