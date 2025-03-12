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
 
e
u
l
e
r
_
t
o
_
r
o
t
a
t
i
o
n
_
m
a
t
r
i
x
(
r
o
l
l
:
 
f
l
o
a
t
,
 
p
i
t
c
h
:
 
f
l
o
a
t
,
 
y
a
w
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
p
.
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
o
n
v
e
r
t
 
E
u
l
e
r
 
a
n
g
l
e
s
 
(
r
o
l
l
,
 
p
i
t
c
h
,
 
y
a
w
)
 
t
o
 
a
 
r
o
t
a
t
i
o
n
 
m
a
t
r
i
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
l
l
 
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
r
o
u
n
d
 
t
h
e
 
x
-
a
x
i
s
 
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


 
 
 
 
 
 
 
 
p
i
t
c
h
 
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
r
o
u
n
d
 
t
h
e
 
y
-
a
x
i
s
 
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


 
 
 
 
 
 
 
 
y
a
w
 
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
r
o
u
n
d
 
t
h
e
 
z
-
a
x
i
s
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
n
p
.
a
r
r
a
y
:
 
A
 
3
x
3
 
r
o
t
a
t
i
o
n
 
m
a
t
r
i
x
.


 
 
 
 
"
"
"


 
 
 
 
r
o
l
l
 
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
r
o
l
l
)


 
 
 
 
p
i
t
c
h
 
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
p
i
t
c
h
)


 
 
 
 
y
a
w
 
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
y
a
w
)




 
 
 
 
#
 
C
r
e
a
t
e
 
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
 
m
a
t
r
i
x
 
u
s
i
n
g
 
t
h
e
 
E
u
l
e
r
 
a
n
g
l
e
s


 
 
 
 
R
_
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
r
o
l
l
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
r
o
l
l
)
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
r
o
l
l
)
,
 
n
p
.
c
o
s
(
r
o
l
l
)
]
,


 
 
 
 
 
 
 
 
]


 
 
 
 
)


 
 
 
 
R
_
y
 
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
p
i
t
c
h
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
p
i
t
c
h
)
]
,


 
 
 
 
 
 
 
 
 
 
 
 
[
0
,
 
1
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
p
i
t
c
h
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
p
i
t
c
h
)
]
,


 
 
 
 
 
 
 
 
]


 
 
 
 
)


 
 
 
 
R
_
z
 
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
y
a
w
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
y
a
w
)
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
y
a
w
)
,
 
n
p
.
c
o
s
(
y
a
w
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
 
1
]
,


 
 
 
 
 
 
 
 
]


 
 
 
 
)


 
 
 
 
R
 
=
 
n
p
.
d
o
t
(
R
_
z
,
 
n
p
.
d
o
t
(
R
_
y
,
 
R
_
x
)
)




 
 
 
 
r
e
t
u
r
n
 
R






d
e
f
 
r
o
t
a
t
i
o
n
_
m
a
t
r
i
x
_
t
o
_
e
u
l
e
r
(
R
:
 
n
p
.
a
r
r
a
y
)
 
-
>
 
n
p
.
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
o
n
v
e
r
t
 
a
 
r
o
t
a
t
i
o
n
 
m
a
t
r
i
x
 
t
o
 
E
u
l
e
r
 
a
n
g
l
e
s
 
(
r
o
l
l
,
 
p
i
t
c
h
,
 
y
a
w
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
R
 
(
n
p
.
a
r
r
a
y
)
:
 
A
 
3
x
3
 
r
o
t
a
t
i
o
n
 
m
a
t
r
i
x
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
p
.
a
r
r
a
y
:
 
A
 
1
x
3
 
a
r
r
a
y
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
E
u
l
e
r
 
a
n
g
l
e
s
 
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


 
 
 
 
"
"
"


 
 
 
 
r
o
l
l
 
=
 
n
p
.
a
r
c
t
a
n
import unittest
import numpy as np

class TestEulerToRotationMatrix(unittest.TestCase):
    def test_zero_rotation(self):
        # Test with zero rotation for all axes
        R = euler_to_rotation_matrix(0, 0, 0)
        np.testing.assert_array_almost_equal(R, np.identity(3))

    def test_rotation_about_x(self):
        # Test rotation about the x-axis
        R = euler_to_rotation_matrix(90, 0, 0)
        expected = np.array([
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_rotation_about_y(self):
        # Test rotation about the y-axis
        R = euler_to_rotation_matrix(0, 90, 0)
        expected = np.array([
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_rotation_about_z(self):
        # Test rotation about the z-axis
        R = euler_to_rotation_matrix(0, 0, 90)
        expected = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        np.testing.assert_array_almost_equal(R, expected)

    def test_combined_rotation(self):
        # Test combined rotation
        R = euler_to_rotation_matrix(30, 45, 60)
        # Expected model_answer_result manually calculated or verified via a reliable source
        expected = np.array([[ 0.35355339, -0.5732233,   0.73919892], [ 0.61237244 , 0.73919892,  0.28033009], [-0.70710678 , 0.35355339,  0.61237244]])
        np.testing.assert_array_almost_equal(R, np.array(expected), decimal=5)
if __name__ == '__main__':
    unittest.main()