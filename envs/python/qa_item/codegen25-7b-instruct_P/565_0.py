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
,
 
D
i
c
t






d
e
f
 
g
e
t
_
b
e
z
i
e
r
_
p
o
i
n
t
(
t
:
 
f
l
o
a
t
,
 
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
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
c
u
r
s
i
v
e
l
y
 
c
a
l
c
u
l
a
t
e
s
 
a
 
p
o
i
n
t
 
o
n
 
a
 
B
é
z
i
e
r
 
c
u
r
v
e
 
u
s
i
n
g
 
D
e
 
C
a
s
t
e
l
j
a
u
'
s
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
(
f
l
o
a
t
)
:
 
A
 
v
a
l
u
e
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
 
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
 
i
n
t
e
r
p
o
l
a
t
i
o
n
 
p
a
r
a
m
e
t
e
r
.


 
 
 
 
 
 
 
 
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
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
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
 
c
o
n
t
r
o
l
 
p
o
i
n
t
s
 
d
e
f
i
n
i
n
g
 
t
h
e
 
B
é
z
i
e
r
 
c
u
r
v
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


 
 
 
 
 
 
 
 
T
h
e
 
c
a
l
c
u
l
a
t
e
d
 
C
o
o
r
d
i
n
a
t
e
s
 
a
t
 
t
h
e
 
g
i
v
e
n
 
p
a
r
a
m
e
t
e
r
 
t
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
p
o
i
n
t
s
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
o
i
n
t
s
[
0
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
x
"
:
 
(
1
 
-
 
t
)
 
*
 
g
e
t
_
b
e
z
i
e
r
_
p
o
i
n
t
(
t
,
 
p
o
i
n
t
s
[
:
-
1
]
)
[
"
x
"
]
 
+
 
t
 
*
 
p
o
i
n
t
s
[
-
1
]
[
"
x
"
]
,


 
 
 
 
 
 
 
 
 
 
 
 
"
y
"
:
 
(
1
 
-
 
t
)
 
*
 
g
e
t
_
b
e
z
i
e
r
_
p
o
i
n
t
(
t
,
 
p
o
i
n
t
s
[
:
-
1
]
)
[
"
y
"
]
 
+
 
t
 
*
 
p
o
i
n
t
s
[
-
1
]
[
"
y
"
]
,


 
 
 
 
 
 
 
 
}






d
e
f
 
g
e
t
_
b
e
z
i
e
r
_
p
o
i
n
t
s
(


 
 
 
 
t
_
s
t
e
p
:
 
f
l
o
a
t
,
 
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
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
]


)
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
]
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
s
 
a
 
l
i
s
t
 
o
f
 
p
o
i
n
t
s
 
o
n
 
a
 
B
é
z
i
e
r
 
c
u
r
v
e
 
u
s
i
n
g
 
D
e
 
C
a
s
t
e
l
j
a
u
'
s
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
_
s
t
e
p
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
 
s
t
e
p
 
s
i
z
e
 
f
o
r
 
c
a
l
c
u
l
a
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
s
.


 
 
 
 
 
 
 
 
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
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
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
 
c
o
n
t
r
o
l
 
p
o
i
n
t
s
 
d
e
f
i
n
i
n
g
 
t
h
e
 
B
é
z
i
e
r
 
c
u
r
v
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


 
 
 
 
 
 
 
 
A
 
l
i
s
t
 
o
f
 
c
a
l
c
u
l
a
t
e
d
 
C
o
o
r
d
i
n
a
t
e
s
 
a
t
 
t
h
e
 
g
i
v
e
n
 
s
t
e
p
 
s
i
z
e
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
 
[
g
e
t
_
b
e
z
i
e
r
_
p
o
i
n
t
(
t
,
 
p
o
i
n
t
s
)
 
f
o
r
 
t
 
i
n
 
n
p
.
a
r
a
n
g
e
(
0
,
 
1
,
 
t
_
s
t
e
p
)
]






d
e
f
 
g
e
t
_
b
e
z
i
e
r
_
c
u
r
v
e
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
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
]
,
 
n
u
m
_
p
o
i
n
t
s
:
 
i
n
t
 
=
 
1
0
0


)
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
]
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
s
 
a
 
s
m
o
o
t
h
 
B
é
z
i
e
r
 
c
u
r
v
e
 
f
r
o
m
 
a
 
l
i
s
t
 
o
f
 
c
o
n
t
r
o
l
 
p
o
i
n
t
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
s
(
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
f
l
o
a
t
]
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
 
c
o
n
t
r
o
l
 
p
o
i
n
t
s
 
d
e
f
i
n
i
n
g
 
t
h
e
 
B
é
import unittest


class TestGetBezierPoint(unittest.TestCase):

    # Test case 1: Test with a simple linear curve
    def test_midpoint_of_two_points(self):
        points = [{'x': 0, 'y': 0}, {'x': 2, 'y': 2}]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 1, 'y': 1})

    # Test case 2: Test with three points (quadratic curve)
    def test_quadratic_bezier_curve(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 0}
        ]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 1, 'y': 1})

    # Test case 3: Test with four points (cubic curve)
    def test_cubic_bezier_curve(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 3},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 0}
        ]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 2, 'y': 1.5})

    # Test case 4: Test with a single point (edge case)
    def test_single_control_point(self):
        points = [{'x': 5, 'y': 5}]
        result = get_bezier_point(0.5, points)
        self.assertEqual(result, {'x': 5, 'y': 5})

    # Test case 5: Test with extreme t value (0)
    def test_extreme_t_value_zero(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 5}
        ]
        result = get_bezier_point(0, points)
        self.assertEqual(result, {'x': 0, 'y': 0})

    # Test case 6: Test with extreme t value (1)
    def test_extreme_t_value_one(self):
        points = [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 5}
        ]
        result = get_bezier_point(1, points)
        self.assertEqual(result, {'x': 5, 'y': 5})

if __name__ == '__main__':
    unittest.main()