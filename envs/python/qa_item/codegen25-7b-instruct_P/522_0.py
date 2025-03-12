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
 
r
o
t
a
t
e
_
p
o
i
n
t
_
c
l
o
u
d
(
p
o
i
n
t
_
c
l
o
u
d
:
 
n
p
.
n
d
a
r
r
a
y
,
 
r
o
t
a
t
i
o
n
_
a
n
g
l
e
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


 
 
 
 
R
o
t
a
t
e
 
t
h
e
 
p
o
i
n
t
 
c
l
o
u
d
 
a
r
o
u
n
d
 
t
h
e
 
Y
 
a
x
i
s
 
b
y
 
a
 
g
i
v
e
n
 
a
n
g
l
e
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
_
c
l
o
u
d
 
(
n
p
.
n
d
a
r
r
a
y
)
:
 
A
 
N
 
x
 
3
 
n
u
m
p
y
 
a
r
r
a
y
 
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
 
3
D
 
p
o
i
n
t
 
c
l
o
u
d
.


 
 
 
 
 
 
 
 
r
o
t
a
t
i
o
n
_
a
n
g
l
e
 
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
 
a
n
g
l
e
 
(
i
n
 
r
a
d
i
a
n
s
)
 
t
o
 
r
o
t
a
t
e
 
t
h
e
 
p
o
i
n
t
 
c
l
o
u
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


 
 
 
 
 
 
 
 
n
p
.
n
d
a
r
r
a
y
:
 
A
 
N
 
x
 
3
 
n
u
m
p
y
 
a
r
r
a
y
 
o
f
 
t
h
e
 
r
o
t
a
t
e
d
 
p
o
i
n
t
 
c
l
o
u
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
s
v
a
l
 
=
 
n
p
.
c
o
s
(
r
o
t
a
t
i
o
n
_
a
n
g
l
e
)


 
 
 
 
s
i
n
v
a
l
 
=
 
n
p
.
s
i
n
(
r
o
t
a
t
i
o
n
_
a
n
g
l
e
)


 
 
 
 
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
c
o
s
v
a
l
,
 
0
,
 
s
i
n
v
a
l
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
s
i
n
v
a
l
,
 
0
,
 
c
o
s
v
a
l
]
]
)


 
 
 
 
r
o
t
a
t
e
d
_
p
o
i
n
t
_
c
l
o
u
d
 
=
 
n
p
.
d
o
t
(
p
o
i
n
t
_
c
l
o
u
d
.
r
e
s
h
a
p
e
(
(
-
1
,
 
3
)
)
,
 
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
a
t
e
d
_
p
o
i
n
t
_
c
l
o
u
d






d
e
f
 
r
o
t
a
t
e
_
p
o
i
n
t
_
c
l
o
u
d
_
b
y
_
a
n
g
l
e
(
p
o
i
n
t
_
c
l
o
u
d
:
 
n
p
.
n
d
a
r
r
a
y
,
 
r
o
t
a
t
i
o
n
_
a
n
g
l
e
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


 
 
 
 
R
o
t
a
t
e
 
t
h
e
 
p
o
i
n
t
 
c
l
o
u
d
 
a
r
o
u
n
d
 
t
h
e
 
Y
 
a
x
i
s
 
b
y
 
a
 
g
i
v
e
n
 
a
n
g
l
e
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
_
c
l
o
u
d
 
(
n
p
.
n
d
a
r
r
a
y
)
:
 
A
 
N
 
x
 
3
 
n
u
m
p
y
 
a
r
r
a
y
 
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
 
3
D
 
p
o
i
n
t
 
c
l
o
u
d
.


 
 
 
 
 
 
 
 
r
o
t
a
t
i
o
n
_
a
n
g
l
e
 
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
 
a
n
g
l
e
 
(
i
n
 
r
a
d
i
a
n
s
)
 
t
o
 
r
o
t
a
t
e
 
t
h
e
 
p
o
i
n
t
 
c
l
o
u
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


 
 
 
 
 
 
 
 
n
p
.
n
d
a
r
r
a
y
:
 
A
 
N
 
x
 
3
 
n
u
m
p
y
 
a
r
r
a
y
 
o
f
 
t
h
e
 
r
o
t
a
t
e
d
 
p
o
i
n
t
 
c
l
o
u
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
s
v
a
l
 
=
 
n
p
.
c
o
s
(
r
o
t
a
t
i
o
n
_
a
n
g
l
e
)


 
 
 
 
s
i
n
v
a
l
 
=
 
n
p
.
s
i
n
(
r
o
t
a
t
i
o
n
_
a
n
g
l
e
)


 
 
 
 
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
c
o
s
v
a
l
,
 
0
,
 
s
i
n
v
a
l
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
s
i
n
v
a
l
,
 
0
,
 
c
o
s
v
a
l
]
]
)


 
 
 
 
r
o
t
a
t
e
d
_
p
o
i
n
t
_
c
l
o
u
d
 
=
 
n
p
.
d
o
t
(
p
o
i
n
t
_
c
l
o
u
d
.
r
e
s
h
a
p
e
(
(
-
1
,
 
3
)
)
,
 
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
a
t
e
d
_
p
o
i
n
t
_
c
l
o
u
d






d
e
f
 
r
o
t
a
t
e
_
p
o
i
n
t
_
c
l
o
u
d
_
b
y
_
e
u
l
e
r
_
a
n
g
l
e
s
(
p
o
i
n
t
_
c
l
o
u
d
:
 
n
p
.
n
d
a
r
r
a
y
,
 
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
n
d
a
r
r
a
y
:


import unittest

import numpy as np


class TestRotatePointCloud(unittest.TestCase):

    def test_no_rotation(self):
        """Test when rotation angle is 0 (should return the same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        rotation_angle = 0
        expected_output = point_cloud
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

    def test_180_degree_rotation(self):
        """Test rotation of 180 degrees (π radians) around Y axis."""
        point_cloud = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
        rotation_angle = np.pi  # 180 degrees
        expected_output = np.array([[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])  # [1,0,0] -> [-1,0,0]
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

    def test_full_rotation(self):
        """Test rotation of 360 degrees (2π radians) around Y axis (should return same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        rotation_angle = 2 * np.pi  # 360 degrees
        expected_output = point_cloud  # Should return the same point cloud
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

if __name__ == '__main__':
    unittest.main()