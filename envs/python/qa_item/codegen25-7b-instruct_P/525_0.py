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
 
f
l
i
p
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
 
a
x
i
s
:
 
i
n
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


 
 
 
 
F
l
i
p
 
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
c
r
o
s
s
 
a
 
s
p
e
c
i
f
i
e
d
 
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


 
 
 
 
 
 
 
 
a
x
i
s
 
(
i
n
t
)
:
 
A
n
 
i
n
t
e
g
e
r
 
s
p
e
c
i
f
y
i
n
g
 
t
h
e
 
a
x
i
s
 
t
o
 
f
l
i
p
 
(
0
 
f
o
r
 
x
,
 
1
 
f
o
r
 
y
,
 
2
 
f
o
r
 
z
)
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
 
f
l
i
p
p
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


 
 
 
 
i
f
 
a
x
i
s
 
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
[
:
,
 
:
:
-
1
,
 
:
]


 
 
 
 
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
_
c
l
o
u
d
[
:
,
 
:
,
 
:
:
-
1
]


 
 
 
 
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
 
2
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
_
c
l
o
u
d
[
:
:
-
1
,
 
:
,
 
:
]


 
 
 
 
e
l
s
e
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
"
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
 
v
a
l
u
e
.
"
)






d
e
f
 
f
l
i
p
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
i
n
_
p
l
a
c
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
 
a
x
i
s
:
 
i
n
t
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
F
l
i
p
 
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
c
r
o
s
s
 
a
 
s
p
e
c
i
f
i
e
d
 
a
x
i
s
 
i
n
 
p
l
a
c
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


 
 
 
 
 
 
 
 
a
x
i
s
 
(
i
n
t
)
:
 
A
n
 
i
n
t
e
g
e
r
 
s
p
e
c
i
f
y
i
n
g
 
t
h
e
 
a
x
i
s
 
t
o
 
f
l
i
p
 
(
0
 
f
o
r
 
x
,
 
1
 
f
o
r
 
y
,
 
2
 
f
o
r
 
z
)
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
 
=
=
 
0
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
[
:
,
 
:
:
-
1
,
 
:
]
 
=
 
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
[
:
,
 
:
:
-
1
,
 
:
]


 
 
 
 
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
 
1
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
[
:
,
 
:
,
 
:
:
-
1
]
 
=
 
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
[
:
,
 
:
,
 
:
:
-
1
]


 
 
 
 
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
 
2
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
[
:
:
-
1
,
 
:
,
 
:
]
 
=
 
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
[
:
:
-
1
,
 
:
,
 
:
]


 
 
 
 
e
l
s
e
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
"
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
 
v
a
l
u
e
.
"
)






d
e
f
 
f
l
i
p
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
a
t
c
h
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
_
b
a
t
c
h
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
 
a
x
i
s
:
 
i
n
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


 
 
 
 
F
l
i
p
 
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
 
b
a
t
c
h
 
a
c
r
o
s
s
 
a
 
s
p
e
c
i
f
i
e
d
 
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
a
t
c
h
 
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
 
B
 
x
 
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
 
b
a
t
c
h
.


 
 
 
 
 
 
 
import unittest

import numpy as np


class TestFlipPointCloud(unittest.TestCase):

    def test_flip_x_axis(self):
        """Test flipping the point cloud across the x-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[1.0, -2.0, 3.0], [4.0, -5.0, 6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=1), expected_output)

    def test_flip_y_axis(self):
        """Test flipping the point cloud across the y-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[-1.0, 2.0, 3.0], [-4.0, 5.0, 6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=0), expected_output)

    def test_flip_z_axis(self):
        """Test flipping the point cloud across the z-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[1.0, 2.0, -3.0], [4.0, 5.0, -6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=2), expected_output)

    def test_invalid_axis(self):
        """Test handling of an invalid axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        self.assertRaises(Exception)


    def test_empty_point_cloud(self):
        """Test flipping an empty point cloud."""
        point_cloud = np.array([]).reshape(0, 3)  # Empty point cloud with shape (0, 3)
        expected_output = np.array([]).reshape(0, 3)  # Expect the output to be the same
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=0), expected_output)
if __name__ == '__main__':
    unittest.main()