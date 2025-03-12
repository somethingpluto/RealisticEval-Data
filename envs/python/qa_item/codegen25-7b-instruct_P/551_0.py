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
m
i
d
s
_
f
r
o
m
_
e
d
g
e
s
(
e
d
g
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
:


 
 
 
 
"
"
"


 
 
 
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
m
i
d
p
o
i
n
t
s
 
f
r
o
m
 
a
 
g
i
v
e
n
 
a
r
r
a
y
 
o
f
 
e
d
g
e
s
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
0
,
 
1
,
 
2
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
[
0
.
5
,
 
1
.
5
]




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
d
g
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
n
 
a
r
r
a
y
 
o
f
 
e
d
g
e
 
v
a
l
u
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
n
 
a
r
r
a
y
 
o
f
 
m
i
d
p
o
i
n
t
s
 
c
a
l
c
u
l
a
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
 
e
d
g
e
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
 
(
e
d
g
e
s
[
1
:
]
 
+
 
e
d
g
e
s
[
:
-
1
]
)
 
/
 
2






d
e
f
 
g
e
t
_
e
d
g
e
s
_
f
r
o
m
_
m
i
d
s
(
m
i
d
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
:


 
 
 
 
"
"
"


 
 
 
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
e
d
g
e
s
 
f
r
o
m
 
a
 
g
i
v
e
n
 
a
r
r
a
y
 
o
f
 
m
i
d
p
o
i
n
t
s
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
0
,
 
1
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
[
0
,
 
0
.
5
,
 
1
]




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
i
d
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
n
 
a
r
r
a
y
 
o
f
 
m
i
d
p
o
i
n
t
 
v
a
l
u
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
n
 
a
r
r
a
y
 
o
f
 
e
d
g
e
s
 
c
a
l
c
u
l
a
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
 
m
i
d
p
o
i
n
t
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
c
o
n
c
a
t
e
n
a
t
e
(
[
m
i
d
s
[
:
-
1
]
,
 
[
m
i
d
s
[
-
1
]
 
+
 
(
m
i
d
s
[
-
1
]
 
-
 
m
i
d
s
[
-
2
]
)
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
e
d
g
e
s
_
f
r
o
m
_
m
i
d
s
_
a
n
d
_
w
i
d
t
h
s
(
m
i
d
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
,
 
w
i
d
t
h
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
:


 
 
 
 
"
"
"


 
 
 
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
e
d
g
e
s
 
f
r
o
m
 
a
 
g
i
v
e
n
 
a
r
r
a
y
 
o
f
 
m
i
d
p
o
i
n
t
s
 
a
n
d
 
w
i
d
t
h
s
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
0
,
 
1
]
,
 
[
0
.
5
,
 
0
.
5
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
[
0
,
 
0
.
5
,
 
1
]




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
i
d
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
n
 
a
r
r
a
y
 
o
f
 
m
i
d
p
o
i
n
t
 
v
a
l
u
e
s
.


 
 
 
 
 
 
 
 
w
i
d
t
h
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
n
 
a
r
r
a
y
 
o
f
 
w
i
d
t
h
 
v
a
l
u
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
n
 
a
r
r
a
y
 
o
f
 
e
d
g
e
s
 
c
a
l
c
u
l
a
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
 
m
i
d
p
o
i
n
t
s
 
a
n
d
 
w
i
d
t
h
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
c
o
n
c
a
t
e
n
a
t
e
(
[
m
i
d
s
[
:
-
1
]
 
-
 
w
i
d
t
h
s
[
:
-
1
]
 
/
 
2
,
 
[
m
i
d
s
[
-
1
]
 
+
 
w
i
d
t
h
s
[
-
1
]
 
/
 
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
m
i
d
s
_
f
r
o
m
_
e
d
g
e
s
_
a
n
d
_
w
i
d
t
h
s
(
e
d
g
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
,
 
w
i
d
t
h
s
:
 
n
p
.
n
d
import unittest

import numpy as np


class TestGetMidsFromEdges(unittest.TestCase):

    def test_basic_case(self):
        """Test with a standard range of edges."""
        edges = np.array([1, 2, 3, 4])
        expected_mids = np.array([1.5, 2.5, 3.5])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_single_interval(self):
        """Test with two edges (single interval)."""
        edges = np.array([5, 10])
        expected_mids = np.array([7.5])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_multiple_intervals(self):
        """Test with multiple intervals."""
        edges = np.array([0, 1, 2, 3, 4, 5])
        expected_mids = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_negative_edges(self):
        """Test with negative edges."""
        edges = np.array([-5, -3, -1, 1])
        expected_mids = np.array([-4.0, -2.0, 0.0])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_zero_edges(self):
        """Test with edges including zero."""
        edges = np.array([0, 1, 2])
        expected_mids = np.array([0.5, 1.5])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_float_edges(self):
        """Test with floating-point edges."""
        edges = np.array([0.0, 1.5, 3.0])
        expected_mids = np.array([0.75, 2.25])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)

    def test_empty_array(self):
        """Test with an empty array."""
        edges = np.array([])
        expected_mids = np.array([])
        np.testing.assert_array_equal(get_mids_from_edges(edges), expected_mids)
if __name__ == '__main__':
    unittest.main()