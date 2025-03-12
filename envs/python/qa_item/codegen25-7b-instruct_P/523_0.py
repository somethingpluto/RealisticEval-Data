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
 
t
r
a
n
s
l
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
_
v
e
c
t
o
r
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


 
 
 
 
T
r
a
n
s
l
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
 
b
y
 
a
 
g
i
v
e
n
 
v
e
c
t
o
r
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
_
v
e
c
t
o
r
 
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
 
1
 
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
r
 
l
i
s
t
 
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
 
v
e
c
t
o
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
 
t
r
a
n
s
l
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
_
v
e
c
t
o
r
 
=
 
n
p
.
a
s
a
r
r
a
y
(
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
_
v
e
c
t
o
r
)


 
 
 
 
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
 
+
 
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
_
v
e
c
t
o
r






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
m
a
t
r
i
x
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
 
b
y
 
a
 
g
i
v
e
n
 
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
m
a
t
r
i
x
 
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
 
3
 
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


 
 
 
 
r
e
t
u
r
n
 
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
.
T
)






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
 
b
y
 
a
 
g
i
v
e
n
 
s
e
t
 
o
f
 
e
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
 
1
 
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
r
 
l
i
s
t
 
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
 
e
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






d
e
f
 
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
import unittest

import numpy as np


class TestTranslatePointCloud(unittest.TestCase):

    def test_simple_translation(self):
        """Test a simple translation of a single point."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        translation_vector = np.array([1.0, 1.0, 1.0])
        expected_output = np.array([[2.0, 3.0, 4.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_multiple_points_translation(self):
        """Test translation of multiple points."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        translation_vector = np.array([1.0, 2.0, 3.0])
        expected_output = np.array([[2.0, 4.0, 6.0], [5.0, 7.0, 9.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_zero_translation(self):
        """Test translation by a zero vector (should return the same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        translation_vector = np.array([0.0, 0.0, 0.0])
        expected_output = point_cloud  # No change expected
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_negative_translation(self):
        """Test translation with negative values."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        translation_vector = np.array([-1.0, -2.0, -3.0])
        expected_output = np.array([[0.0, 0.0, 0.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)
if __name__ == '__main__':
    unittest.main()