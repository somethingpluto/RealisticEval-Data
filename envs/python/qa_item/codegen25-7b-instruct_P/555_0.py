i
m
p
o
r
t
 
m
a
t
h


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
 
T
u
p
l
e






d
e
f
 
q
u
a
t
e
r
n
i
o
n
_
t
o
_
a
n
g
l
e
(
q
u
a
t
e
r
n
i
o
n
:
 
T
u
p
l
e
[
f
l
o
a
t
]
)
 
-
>
 
f
l
o
a
t
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
s
 
a
 
q
u
a
t
e
r
n
i
o
n
 
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
 
a
n
g
l
e
 
i
n
 
r
a
d
i
a
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
a
t
e
r
n
i
o
n
 
(
T
u
p
l
e
[
f
l
o
a
t
]
)
:
 
A
 
t
u
p
l
e
 
o
r
 
l
i
s
t
 
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
 
q
u
a
t
e
r
n
i
o
n
 
c
o
m
p
o
n
e
n
t
s
 
(
w
,
 
x
,
 
y
,
 
z
)




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
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
 
a
n
g
l
e
 
i
n
 
r
a
d
i
a
n
s


 
 
 
 
"
"
"


 
 
 
 
w
,
 
x
,
 
y
,
 
z
 
=
 
q
u
a
t
e
r
n
i
o
n


 
 
 
 
s
i
n
_
h
a
l
f
_
t
h
e
t
a
 
=
 
2
 
*
 
m
a
t
h
.
s
q
r
t
(
x
 
*
 
x
 
+
 
y
 
*
 
y
 
+
 
z
 
*
 
z
)


 
 
 
 
i
f
 
s
i
n
_
h
a
l
f
_
t
h
e
t
a
 
>
 
0
.
4
9
9
9
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
2
 
*
 
m
a
t
h
.
a
t
a
n
2
(
s
i
n
_
h
a
l
f
_
t
h
e
t
a
,
 
w
)


 
 
 
 
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
 
m
a
t
h
.
a
t
a
n
2
(
s
i
n
_
h
a
l
f
_
t
h
e
t
a
,
 
w
)






d
e
f
 
a
n
g
l
e
_
t
o
_
q
u
a
t
e
r
n
i
o
n
(
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
 
T
u
p
l
e
[
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


 
 
 
 
C
o
n
v
e
r
t
s
 
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
n
g
l
e
 
i
n
 
r
a
d
i
a
n
s
 
t
o
 
a
 
q
u
a
t
e
r
n
i
o
n
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
 
r
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
 
r
a
d
i
a
n
s




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
f
l
o
a
t
]
:
 
A
 
t
u
p
l
e
 
o
r
 
l
i
s
t
 
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
 
q
u
a
t
e
r
n
i
o
n
 
c
o
m
p
o
n
e
n
t
s
 
(
w
,
 
x
,
 
y
,
 
z
)


 
 
 
 
"
"
"


 
 
 
 
h
a
l
f
_
t
h
e
t
a
 
=
 
0
.
5
 
*
 
a
n
g
l
e


 
 
 
 
w
 
=
 
m
a
t
h
.
c
o
s
(
h
a
l
f
_
t
h
e
t
a
)


 
 
 
 
x
 
=
 
0


 
 
 
 
y
 
=
 
0


 
 
 
 
z
 
=
 
m
a
t
h
.
s
i
n
(
h
a
l
f
_
t
h
e
t
a
)


 
 
 
 
r
e
t
u
r
n
 
w
,
 
x
,
 
y
,
 
z






d
e
f
 
q
u
a
t
e
r
n
i
o
n
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
q
u
a
t
e
r
n
i
o
n
:
 
T
u
p
l
e
[
f
l
o
a
t
]
)
 
-
>
 
T
u
p
l
e
[
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
q
u
a
t
e
r
n
i
o
n
 
t
o
 
a
n
 
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
 
i
n
 
r
a
d
i
a
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
a
t
e
r
n
i
o
n
 
(
T
u
p
l
e
[
f
l
o
a
t
]
)
:
 
A
 
t
u
p
l
e
 
o
r
 
l
i
s
t
 
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
 
q
u
a
t
e
r
n
i
o
n
 
c
o
m
p
o
n
e
n
t
s
 
(
w
,
 
x
,
 
y
,
 
z
)




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
f
l
o
a
t
]
:
 
A
 
t
u
p
l
e
 
o
r
 
l
i
s
t
 
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
 
c
o
m
p
o
n
e
n
t
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
 
r
a
d
i
a
n
s


 
 
 
 
"
"
"


 
 
 
 
w
,
 
x
,
 
y
,
 
z
 
=
 
q
u
a
t
e
r
n
i
o
n


 
 
 
 
t
0
 
=
 
+
2
.
0
 
*
 
(
w
 
*
 
x
 
+
 
y
 
*
 
z
)


 
 
 
 
t
1
 
=
 
+
1
.
0
 
-
 
2
.
0
 
*
 
(
x
import math
import unittest


class TestQuaternionToAngle(unittest.TestCase):

    def test_identity_quaternion(self):
        """Test the identity quaternion (no rotation)."""
        quaternion = (1.0, 0.0, 0.0, 0.0)
        expected_angle = 0.0
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)


    def test_180_degrees_rotation(self):
        """Test a quaternion representing a 180-degree rotation."""
        quaternion = (0.0, 0.0, 1.0, 0.0)  # 180 degrees around Z axis
        expected_angle = math.pi  # 180 degrees in radians
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)

    def test_360_degrees_rotation(self):
        """Test a quaternion representing a full 360-degree rotation."""
        quaternion = (1.0, 0.0, 0.0, 0.0)  # Full rotation
        expected_angle = 0.0  # 360 degrees is equivalent to 0 degrees
        self.assertAlmostEqual(quaternion_to_angle(quaternion), expected_angle)


    def test_non_unit_quaternion(self):
        """Test a non-unit quaternion (should still give correct angle)."""
        quaternion = (0.5, 0.5, 0.5, 0.5)  # This is not normalized
        # Normalize the quaternion first
        norm = math.sqrt(sum(x ** 2 for x in quaternion))
        normalized_quaternion = tuple(x / norm for x in quaternion)
        expected_angle = 2 * math.acos(normalized_quaternion[0])  # Should be same angle
        self.assertAlmostEqual(quaternion_to_angle(normalized_quaternion), expected_angle)

    def test_invalid_quaternion(self):
        """Test that an invalid quaternion raises a ValueError."""
        with self.assertRaises(ValueError):
            quaternion_to_angle((1.0, 0.0, 0.0))  # Only 3 components
if __name__ == '__main__':
    unittest.main()