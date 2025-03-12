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
 
g
e
t
_
r
o
t
a
t
i
o
n
(
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
a
r
r
a
y
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


 
 
 
 
G
i
v
e
n
 
a
n
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
r
e
t
u
r
n
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
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
a
r
r
a
y
)
:
 
A
 
2
D
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
a
f
f
i
n
e
 
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
e
t
u
r
n
 
n
p
.
a
r
c
t
a
n
2
(
m
a
t
r
i
x
[
1
,
0
]
,
 
m
a
t
r
i
x
[
0
,
0
]
)




d
e
f
 
g
e
t
_
s
c
a
l
e
(
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
a
r
r
a
y
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


 
 
 
 
G
i
v
e
n
 
a
n
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
r
e
t
u
r
n
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
s
c
a
l
e
 
f
a
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
a
r
r
a
y
)
:
 
A
 
2
D
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
s
c
a
l
e
 
f
a
c
t
o
r
,
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
a
f
f
i
n
e
 
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
e
t
u
r
n
 
n
p
.
s
q
r
t
(
m
a
t
r
i
x
[
0
,
0
]
*
*
2
 
+
 
m
a
t
r
i
x
[
1
,
0
]
*
*
2
)




d
e
f
 
g
e
t
_
s
h
e
a
r
(
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
a
r
r
a
y
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


 
 
 
 
G
i
v
e
n
 
a
n
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
r
e
t
u
r
n
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
s
h
e
a
r
 
f
a
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
a
r
r
a
y
)
:
 
A
 
2
D
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
s
h
e
a
r
 
f
a
c
t
o
r
,
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
a
f
f
i
n
e
 
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
e
t
u
r
n
 
m
a
t
r
i
x
[
0
,
1
]




d
e
f
 
g
e
t
_
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
(
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


 
 
 
 
G
i
v
e
n
 
a
n
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
r
e
t
u
r
n
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
a
r
r
a
y
)
:
 
A
 
2
D
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
 
T
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
,
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
a
f
f
i
n
e
 
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
e
t
u
r
n
 
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
m
a
t
r
i
x
[
0
,
2
]
,
 
m
a
t
r
i
x
[
1
,
2
]
]
)




d
e
f
 
g
e
t
_
c
e
n
t
e
r
(
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


 
 
 
 
G
i
v
e
n
 
a
n
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
,
 
r
e
t
u
r
n
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
c
e
n
t
e
r
 
o
f
 
r
o
t
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
a
r
r
a
y
)
:
 
A
 
2
D
 
a
f
f
i
n
e
 
t
r
a
n
s
f
o
r
m
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
 
T
h
e
 
c
e
n
t
e
r
 
o
f
 
r
o
t
a
t
i
o
n
,
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
a
f
f
i
n
e
 
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
e
t
u
r
n
 
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
m
a
t
r
i
x
[
0
,
2
]
,
 
m
a
t
r
i
x
[
1
import numpy as np
import unittest


class TestGetRotationFunction(unittest.TestCase):

    def test_rotation_0_degrees(self):
        """ Test for a rotation of 0 degrees (identity matrix) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_rotation = 0.0
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_90_degrees(self):
        """ Test for a rotation of 90 degrees """
        matrix = np.array([[0, -1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi / 2  # 90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_180_degrees(self):
        """ Test for a rotation of 180 degrees """
        matrix = np.array([[-1, 0, 0],
                           [0, -1, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi  # 180 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_negative_90_degrees(self):
        """ Test for a rotation of -90 degrees """
        matrix = np.array([[0, 1, 0],
                           [-1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = -np.pi / 2  # -90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

if __name__ == '__main__':
    unittest.main()