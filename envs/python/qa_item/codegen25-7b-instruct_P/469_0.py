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
 
T
u
p
l
e
[
n
p
.
f
l
o
a
t
6
4
,
 
n
p
.
f
l
o
a
t
6
4
]
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
 
3
x
3
 
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
i
n
g
 
f
a
c
t
o
r
s


 
 
 
 
a
l
o
n
g
 
t
h
e
 
x
 
a
n
d
 
y
 
a
x
e
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
 
3
x
3
 
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
n
p
.
f
l
o
a
t
6
4
,
 
n
p
.
f
l
o
a
t
6
4
]
:
 
A
 
t
u
p
l
e
 
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
s
 
(
s
c
a
l
e
_
x
,
 
s
c
a
l
e
_
y
)
.


 
 
 
 
"
"
"


 
 
 
 
s
c
a
l
e
_
x
 
=
 
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


 
 
 
 
s
c
a
l
e
_
y
 
=
 
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
 
1
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
 
1
]
 
*
*
 
2
)


 
 
 
 
r
e
t
u
r
n
 
s
c
a
l
e
_
x
,
 
s
c
a
l
e
_
y






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
 
T
u
p
l
e
[
n
p
.
f
l
o
a
t
6
4
,
 
n
p
.
f
l
o
a
t
6
4
]
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
 
3
x
3
 
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
s


 
 
 
 
a
l
o
n
g
 
t
h
e
 
x
 
a
n
d
 
y
 
a
x
e
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
 
3
x
3
 
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
n
p
.
f
l
o
a
t
6
4
,
 
n
p
.
f
l
o
a
t
6
4
]
:
 
A
 
t
u
p
l
e
 
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
s
 
(
s
h
e
a
r
_
x
,
 
s
h
e
a
r
_
y
)
.


 
 
 
 
"
"
"


 
 
 
 
s
h
e
a
r
_
x
 
=
 
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


 
 
 
 
s
h
e
a
r
_
y
 
=
 
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


 
 
 
 
r
e
t
u
r
n
 
s
h
e
a
r
_
x
,
 
s
h
e
a
r
_
y






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
f
l
o
a
t
6
4
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
 
3
x
3
 
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
 
d
e
g
r
e
e
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
 
3
x
3
 
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
f
l
o
a
t
6
4
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


 
 
 
 
d
e
t
 
=
 
n
p
.
l
i
n
a
l
g
.
d
e
t
(
m
a
t
r
i
x
)


 
 
 
 
i
f
 
d
e
t
 
<
 
0
:


 
 
 
 
 
 
 
 
d
e
t
 
=
 
-
d
e
t


 
 
 
 
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
c
o
s
(
d
e
t
)
 
*
 
1
8
0
 
/
 
n
p
.
p
i






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
import numpy as np
import unittest


# Assume the get_scale function is defined as provided

class TestGetScaleFunction(unittest.TestCase):

    def test_identity_matrix(self):
        """ Test for the identity matrix (no scaling) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_scale = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected_scale)

    def test_scaling_matrix(self):
        """ Test for a scaling matrix (2x in x and 3x in y) """
        matrix = np.array([[2, 0, 0],
                           [0, 3, 0],
                           [0, 0, 1]])
        expected_scale = (2.0, 3.0)
        self.assertEqual(get_scale(matrix), expected_scale)


    def test_uniform_scaling(self):
        # Test case with uniform scaling
        matrix = np.array([[2, 0, 0],
                           [0, 2, 0],
                           [0, 0, 1]])
        expected = (2.0, 2.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_non_uniform_scaling(self):
        # Test case with non-uniform scaling
        matrix = np.array([[3, 0, 0],
                           [0, 5, 0],
                           [0, 0, 1]])
        expected = (3.0, 5.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_reflection_matrix(self):
        # Test case with reflection matrix
        matrix = np.array([[-1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected)
if __name__ == '__main__':
    unittest.main()