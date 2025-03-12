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


 
 
 
 
G
i
v
e
n
 
a
 
3
x
3
 
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
n
d
a
r
r
a
y
:
 
A
 
2
-
e
l
e
m
e
n
t
 
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
x
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
y
)
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
 
3
x
3
 
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
 
3
x
3
 
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
 
3
x
3
 
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
m
a
t
r
i
x
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
:
 
f
l
o
a
t
,
 
s
c
a
l
e
:
 
f
l
o
a
t
,
 
s
h
e
a
r
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


 
 
 
 
G
i
v
e
n
 
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
,
 
r
o
t
a
t
i
o
n
,
 
s
c
a
l
e
,
 
a
n
d
 
s
h
e
a
r
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
 
3
x
3
 
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
-
e
l
e
m
e
n
t
 
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
x
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
y
)
.


 
 
 
 
 
 
 
 
r
o
t
a
t
i
o
n
 
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
.


import numpy as np
import unittest


# Assume the get_translation function is defined as provided

class TestGetTranslationFunction(unittest.TestCase):

    def test_identity_matrix(self):
        """ Test for the identity matrix (no translation) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_translation = np.array([0.0, 0.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)

    def test_translation_matrix(self):
        """ Test for a translation matrix (5 in x, 10 in y) """
        matrix = np.array([[1, 0, 5],
                           [0, 1, 10],
                           [0, 0, 1]])
        expected_translation = np.array([5.0, 10.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)

    def test_negative_translation(self):
        """ Test for a translation matrix with negative values """
        matrix = np.array([[1, 0, -3],
                           [0, 1, -6],
                           [0, 0, 1]])
        expected_translation = np.array([-3.0, -6.0])
        np.testing.assert_array_equal(get_translation(matrix), expected_translation)
if __name__ == '__main__':
    unittest.main()