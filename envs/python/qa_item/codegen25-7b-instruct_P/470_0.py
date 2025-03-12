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
 
a
p
p
l
y
_
s
h
e
a
r
_
x
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
,
 
s
h
e
a
r
_
f
a
c
t
o
r
:
 
f
l
o
a
t
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
i
e
s
 
a
 
s
h
e
a
r
 
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
 
t
o
 
a
 
2
D
 
m
a
t
r
i
x
 
a
l
o
n
g
 
t
h
e
 
x
-
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
 
2
D
 
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
 
o
r
i
g
i
n
a
l
 
m
a
t
r
i
x
.


 
 
 
 
s
h
e
a
r
_
f
a
c
t
o
r
 
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
 
f
a
c
t
o
r
 
b
y
 
w
h
i
c
h
 
t
h
e
 
m
a
t
r
i
x
 
i
s
 
s
h
e
a
r
e
d
 
a
l
o
n
g
 
t
h
e
 
x
-
a
x
i
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
 
T
h
e
 
s
h
e
a
r
e
d
 
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


 
 
 
 
m
a
t
r
i
x
[
:
,
 
1
]
 
+
=
 
s
h
e
a
r
_
f
a
c
t
o
r
 
*
 
m
a
t
r
i
x
[
:
,
 
0
]


 
 
 
 
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






d
e
f
 
a
p
p
l
y
_
s
h
e
a
r
_
y
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
,
 
s
h
e
a
r
_
f
a
c
t
o
r
:
 
f
l
o
a
t
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
i
e
s
 
a
 
s
h
e
a
r
 
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
 
t
o
 
a
 
2
D
 
m
a
t
r
i
x
 
a
l
o
n
g
 
t
h
e
 
y
-
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
 
2
D
 
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
 
o
r
i
g
i
n
a
l
 
m
a
t
r
i
x
.


 
 
 
 
s
h
e
a
r
_
f
a
c
t
o
r
 
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
 
f
a
c
t
o
r
 
b
y
 
w
h
i
c
h
 
t
h
e
 
m
a
t
r
i
x
 
i
s
 
s
h
e
a
r
e
d
 
a
l
o
n
g
 
t
h
e
 
y
-
a
x
i
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
 
T
h
e
 
s
h
e
a
r
e
d
 
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


 
 
 
 
m
a
t
r
i
x
[
:
,
 
0
]
 
+
=
 
s
h
e
a
r
_
f
a
c
t
o
r
 
*
 
m
a
t
r
i
x
[
:
,
 
1
]


 
 
 
 
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






d
e
f
 
a
p
p
l
y
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
,
 
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
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
i
e
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
 
t
o
 
a
 
2
D
 
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
 
2
D
 
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
 
o
r
i
g
i
n
a
l
 
m
a
t
r
i
x
.


 
 
 
 
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
 
b
y
 
w
h
i
c
h
 
t
h
e
 
m
a
t
r
i
x
 
i
s
 
r
o
t
a
t
e
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
 
T
h
e
 
r
o
t
a
t
e
d
 
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


 
 
 
 
c
o
s
_
t
h
e
t
a
 
=
 
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
)


 
 
 
 
s
i
n
_
t
h
e
t
a
 
=
 
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
_
t
h
e
t
a
,
 
-
s
i
n
_
t
h
e
t
a
]
,
 
[
s
i
n
_
t
h
e
t
a
,
 
c
o
s
_
t
h
e
t
a
]
]
)


 
 
 
 
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
m
a
t
m
u
l
(
m
a
t
r
i
x
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
 
m
a
t
r
i
x






d
e
f
 
a
p
p
l
y
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
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
i
e
s
 
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
 
t
o
 
a
 
2
D
 
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
 
2
D
 
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
 
o
r
i
g
i
n
a
l
import numpy as np
import unittest

class TestShearTransformation(unittest.TestCase):
    def test_identity_shear(self):
        """ Test with zero shear factor which should return the original matrix unchanged. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = 0
        expected_output = np.array([[1, 2], [3, 4]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should remain unchanged with zero shear factor.")

    def test_positive_shear(self):
        """ Test with a positive shear factor. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = 1
        expected_output = np.array([[1, 3], [3, 7]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared.")

    def test_negative_shear(self):
        """ Test with a negative shear factor. """
        matrix = np.array([[1, 2], [3, 4]])
        shear_factor = -1
        expected_output = np.array([[1, 1], [3, 1]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared negatively.")


    def test_high_shear_factor(self):
        """ Test with a high shear factor to see how the matrix adapts to extreme transformations. """
        matrix = np.array([[1, 1], [1, 1]])
        shear_factor = 10
        expected_output = np.array([[1, 11], [1, 11]])
        result = apply_shear_x(matrix, shear_factor)
        np.testing.assert_array_equal(result, expected_output, "The matrix should be correctly sheared with a high shear factor.")
if __name__ == '__main__':
    unittest.main()