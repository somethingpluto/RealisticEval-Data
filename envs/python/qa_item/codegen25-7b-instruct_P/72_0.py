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
o
n
v
e
r
t
_
p
i
x
e
l
_
t
o
_
3
d
_
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
s
(
K
:
 
n
p
.
a
r
r
a
y
,
 
d
:
 
f
l
o
a
t
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
 
2
D
 
p
i
x
e
l
 
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
s
 
i
n
t
o
 
3
D
 
w
o
r
l
d
 
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
s
 
u
s
i
n
g
 
c
a
m
e
r
a
 
i
n
t
r
i
n
s
i
c
 
p
a
r
a
m
e
t
e
r
s
 
a
n
d
 
d
e
p
t
h
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
K
 
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
 
(
3
,
 
3
)
 
c
a
m
e
r
a
 
i
n
t
r
i
n
s
i
c
 
m
a
t
r
i
x
,
 
w
h
i
c
h
 
i
n
c
l
u
d
e
s
 
f
o
c
a
l
 
l
e
n
g
t
h
s
 
a
n
d
 
o
p
t
i
c
a
l
 
c
e
n
t
e
r
.


 
 
 
 
 
 
 
 
d
 
(
f
l
o
a
t
)
:
 
D
e
p
t
h
 
(
d
i
s
t
a
n
c
e
 
a
l
o
n
g
 
t
h
e
 
z
-
a
x
i
s
)
 
f
r
o
m
 
t
h
e
 
c
a
m
e
r
a
 
t
o
 
t
h
e
 
p
o
i
n
t
 
i
n
 
3
D
 
s
p
a
c
e
.


 
 
 
 
 
 
 
 
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
i
x
e
l
 
i
n
 
2
D
 
i
m
a
g
e
 
s
p
a
c
e
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
h
e
 
y
 
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
i
x
e
l
 
i
n
 
2
D
 
i
m
a
g
e
 
s
p
a
c
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
 
3
D
 
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
s
 
(
x
,
 
y
,
 
z
)
 
i
n
 
t
h
e
 
c
a
m
e
r
a
'
s
 
r
i
g
h
t
-
h
a
n
d
e
d
 
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
 
f
r
a
m
e
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
 
c
o
n
v
e
r
s
i
o
n
 
f
r
o
m
 
p
i
x
e
l
 
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
s
 
t
o
 
3
D
 
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
 
p
r
o
v
i
d
e
d
 
h
e
l
p
e
r
 
f
u
n
c
t
i
o
n
s
 
t
o
 
c
o
m
p
u
t
e
 
t
h
e
 
3
D
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
 
p
r
o
v
i
d
e
d
 
h
e
l
p
e
r
 
f
u
n
c
t
i
o
n
s
 
t
o
 
c
o
m
p
u
t
e
 
t
h
e
 
3
D
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.


 
 
 
 
#
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
p
t
h
 
d
 
i
s
 
g
i
v
e
n
 
i
n
 
t
h
e
 
s
a
m
e
 
u
n
i
t
 
a
s
 
t
h
e
 
x
,
 
y
,
 
a
n
d
 
z
 
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
s
.
import unittest

import numpy as np


class TestGet3DCoordinates(unittest.TestCase):
    def setUp(self):
        # Define a common intrinsic matrix for testing
        self.K = np.array([[1000, 0, 320],
                           [0, 1000, 240],
                           [0, 0, 1]])

    def test_center_coordinates(self):
        """ Test with center pixel coordinates where x and y should map to zero in NDC. """
        result = convert_pixel_to_3d_coordinates(self.K, 100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 100]))

    def test_boundary_coordinates(self):
        """ Test with boundary values in the image frame. """
        result = convert_pixel_to_3d_coordinates(self.K, 50, 640, 480)
        expected_x = (640 - 320) / 1000 * 50
        expected_y = (480 - 240) / 1000 * 50
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 50]))

    def test_negative_depth(self):
        """ Test with a negative depth to see if it handles incorrect input properly. """
        result = convert_pixel_to_3d_coordinates(self.K, -100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, -100]))

    def test_zero_depth(self):
        """ Test with zero depth which should lead to a zero-length vector. """
        result = convert_pixel_to_3d_coordinates(self.K, 0, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 0.0]))

    def test_non_integer_values(self):
        """ Test with non-integer pixel coordinates. """
        result = convert_pixel_to_3d_coordinates(self.K, 100, 320.5, 240.5)
        expected_x = (320.5 - 320) / 1000 * 100
        expected_y = (240.5 - 240) / 1000 * 100
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 100]))

if __name__ == '__main__':
    unittest.main()