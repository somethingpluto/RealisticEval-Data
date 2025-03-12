i
m
p
o
r
t
 
n
u
m
p
y


i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p






d
e
f
 
c
r
e
a
t
e
_
r
o
t
_
m
a
t
r
i
x
(
a
n
g
l
e
_
d
e
g
:
 
f
l
o
a
t
,
 
a
x
i
s
:
 
s
t
r
)
 
-
>
 
n
u
m
p
y
.
n
d
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
C
r
e
a
t
e
 
a
 
p
o
s
e
 
m
a
t
r
i
x
 
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
 
a
 
r
o
t
a
t
i
o
n
 
a
b
o
u
t
 
a
 
g
i
v
e
n
 
a
x
i
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
n
g
l
e
_
d
e
g
 
(
f
l
o
a
t
)
:
 
R
o
t
a
t
i
o
n
 
a
n
g
l
e
 
i
n
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
a
x
i
s
 
(
s
t
r
)
:
 
A
x
i
s
 
t
o
 
r
o
t
a
t
e
 
a
b
o
u
t
,
 
m
u
s
t
 
b
e
 
o
n
e
 
o
f
 
'
X
'
,
 
'
Y
'
,
 
o
r
 
'
Z
'
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
n
u
m
p
y
.
n
d
a
r
r
a
y
:
 
4
x
4
 
p
o
s
e
 
m
a
t
r
i
x
 
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
 
r
o
t
a
t
i
o
n
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
a
x
i
s
 
n
o
t
 
i
n
 
[
'
X
'
,
 
'
Y
'
,
 
'
Z
'
]
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
'
I
n
v
a
l
i
d
 
a
x
i
s
 
s
p
e
c
i
f
i
e
d
'
)




 
 
 
 
a
n
g
l
e
_
r
a
d
 
=
 
n
p
.
d
e
g
2
r
a
d
(
a
n
g
l
e
_
d
e
g
)


 
 
 
 
i
f
 
a
x
i
s
 
=
=
 
'
X
'
:


 
 
 
 
 
 
 
 
r
o
t
_
m
a
t
r
i
x
 
=
 
n
p
.
a
r
r
a
y
(
[


 
 
 
 
 
 
 
 
 
 
 
 
[
1
,
 
0
,
 
0
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
-
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
0
,
 
0
,
 
1
]


 
 
 
 
 
 
 
 
]
)


 
 
 
 
e
l
i
f
 
a
x
i
s
 
=
=
 
'
Y
'
:


 
 
 
 
 
 
 
 
r
o
t
_
m
a
t
r
i
x
 
=
 
n
p
.
a
r
r
a
y
(
[


 
 
 
 
 
 
 
 
 
 
 
 
[
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
0
,
 
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
1
,
 
0
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
-
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
0
,
 
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
0
,
 
0
,
 
1
]


 
 
 
 
 
 
 
 
]
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
o
t
_
m
a
t
r
i
x
 
=
 
n
p
.
a
r
r
a
y
(
[


 
 
 
 
 
 
 
 
 
 
 
 
[
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
-
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
0
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
n
p
.
s
i
n
(
a
n
g
l
e
_
r
a
d
)
,
 
n
p
.
c
o
s
(
a
n
g
l
e
_
r
a
d
)
,
 
0
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
0
,
 
1
,
 
0
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
0
,
 
0
,
 
1
]


 
 
 
 
 
 
 
 
]
)




 
 
 
 
r
e
t
u
r
n
 
r
o
t
_
m
a
t
r
i
x






d
e
f
 
c
r
e
a
t
e
_
t
r
a
n
s
_
m
a
t
r
i
x
(
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
,
 
z
:
 
f
l
o
a
t
)
 
-
>
 
n
u
m
p
y
.
n
d
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
C
r
e
a
t
e
 
a
 
p
o
s
e
 
m
a
t
r
i
x
 
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
 
a
 
t
r
a
n
s
l
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
r
a
n
s
l
a
t
i
o
n
 
i
n
 
x
-
a
x
i
s
.


 
 
 
 
 
 
 
 
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
r
a
n
s
l
a
t
i
o
n
 
i
n
 
y
-
a
x
i
s
.


 
 
 
 
 
 
 
import unittest
import numpy as np
from numpy.testing import assert_array_almost_equal



class TestCreateRotMatrix(unittest.TestCase):
    def test_rotation_x_90_degrees(self):
        """ Test rotation around X-axis for 90 degrees """
        expected_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(90, 'x')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_rotation_y_180_degrees(self):
        """ Test rotation around Y-axis for 180 degrees """
        expected_matrix = np.array([
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(180, 'y')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_rotation_z_270_degrees(self):
        """ Test rotation around Z-axis for 270 degrees (or -90 degrees) """
        expected_matrix = np.array([
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        result_matrix = create_rot_matrix(270, 'z')
        assert_array_almost_equal(result_matrix, expected_matrix)

    def test_invalid_axis(self):
        """ Test behavior with invalid axis input """
        with self.assertRaises(ValueError):
            create_rot_matrix(90, 'a')

    def test_zero_rotation(self):
        """ Test zero degree rotation which should lead to identity matrix """
        expected_matrix = np.eye(4)
        result_matrix = create_rot_matrix(0, 'x')
        assert_array_almost_equal(result_matrix, expected_matrix)
if __name__ == '__main__':
    unittest.main()