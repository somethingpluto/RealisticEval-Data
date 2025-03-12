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
r
e
_
s
e
t
s
_
e
q
u
a
l
(
s
e
t
1
,
 
s
e
t
2
,
 
r
t
o
l
=
1
e
-
5
,
 
a
t
o
l
=
1
e
-
6
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
a
r
e
s
 
t
w
o
 
s
e
t
s
 
o
f
 
f
l
o
a
t
s
 
f
o
r
 
e
q
u
a
l
i
t
y
 
w
i
t
h
i
n
 
a
 
r
e
l
a
t
i
v
e
 
a
n
d
 
a
b
s
o
l
u
t
e
 
t
o
l
e
r
a
n
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
t
1
:
 
T
h
e
 
f
i
r
s
t
 
s
e
t
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
s
e
t
2
:
 
T
h
e
 
s
e
c
o
n
d
 
s
e
t
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
r
t
o
l
:
 
T
h
e
 
r
e
l
a
t
i
v
e
 
t
o
l
e
r
a
n
c
e
 
(
d
e
f
a
u
l
t
:
 
1
e
-
5
)
.


 
 
 
 
 
 
 
 
a
t
o
l
:
 
T
h
e
 
a
b
s
o
l
u
t
e
 
t
o
l
e
r
a
n
c
e
 
(
d
e
f
a
u
l
t
:
 
1
e
-
6
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


 
 
 
 
 
 
 
 
T
r
u
e
 
i
f
 
t
h
e
 
s
e
t
s
 
a
r
e
 
e
q
u
a
l
 
w
i
t
h
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
t
o
l
e
r
a
n
c
e
s
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
s
e
t
1
)
 
!
=
 
l
e
n
(
s
e
t
2
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
s
e
t
1
)
)
:


 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
n
p
.
i
s
c
l
o
s
e
(
s
e
t
1
[
i
]
,
 
s
e
t
2
[
i
]
,
 
r
t
o
l
=
r
t
o
l
,
 
a
t
o
l
=
a
t
o
l
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
a
r
e
_
v
e
c
t
o
r
s
_
e
q
u
a
l
(
v
e
c
1
,
 
v
e
c
2
,
 
r
t
o
l
=
1
e
-
5
,
 
a
t
o
l
=
1
e
-
6
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
a
r
e
s
 
t
w
o
 
v
e
c
t
o
r
s
 
o
f
 
f
l
o
a
t
s
 
f
o
r
 
e
q
u
a
l
i
t
y
 
w
i
t
h
i
n
 
a
 
r
e
l
a
t
i
v
e
 
a
n
d
 
a
b
s
o
l
u
t
e
 
t
o
l
e
r
a
n
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
1
:
 
T
h
e
 
f
i
r
s
t
 
v
e
c
t
o
r
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
v
e
c
2
:
 
T
h
e
 
s
e
c
o
n
d
 
v
e
c
t
o
r
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
r
t
o
l
:
 
T
h
e
 
r
e
l
a
t
i
v
e
 
t
o
l
e
r
a
n
c
e
 
(
d
e
f
a
u
l
t
:
 
1
e
-
5
)
.


 
 
 
 
 
 
 
 
a
t
o
l
:
 
T
h
e
 
a
b
s
o
l
u
t
e
 
t
o
l
e
r
a
n
c
e
 
(
d
e
f
a
u
l
t
:
 
1
e
-
6
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


 
 
 
 
 
 
 
 
T
r
u
e
 
i
f
 
t
h
e
 
v
e
c
t
o
r
s
 
a
r
e
 
e
q
u
a
l
 
w
i
t
h
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
t
o
l
e
r
a
n
c
e
s
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
v
e
c
1
)
 
!
=
 
l
e
n
(
v
e
c
2
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
v
e
c
1
)
)
:


 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
n
p
.
i
s
c
l
o
s
e
(
v
e
c
1
[
i
]
,
 
v
e
c
2
[
i
]
,
 
r
t
o
l
=
r
t
o
l
,
 
a
t
o
l
=
a
t
o
l
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
a
r
e
_
m
a
t
r
i
c
e
s
_
e
q
u
a
l
(
m
a
t
1
,
 
m
a
t
2
,
 
r
t
o
l
=
1
e
-
5
,
 
a
t
o
l
=
1
e
-
6
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
a
r
e
s
 
t
w
o
 
m
a
t
r
i
c
e
s
 
o
f
 
f
l
o
a
t
s
 
f
o
r
 
e
q
u
a
l
i
t
y
 
w
i
t
h
i
n
 
a
 
r
e
l
a
t
i
v
e
 
a
n
d
 
a
b
s
o
l
u
t
e
 
t
o
l
e
r
a
n
c
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
1
:
 
T
h
e
 
f
i
r
s
t
 
m
a
t
r
i
x
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
m
a
t
2
:
 
T
h
e
 
s
e
c
o
n
d
 
m
a
t
r
i
x
 
o
f
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
r
t
o
l
:
 
T
h
e
 
r
e
l
a
t
i
v
e
 
t
o
l
e
r
a
n
c
e
 
(
d
e
f
a
u
l
t
import unittest


class TestAreSetsEqual(unittest.TestCase):

    def test_identical_sets(self):
        """Test with two identical sets of floats."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.0, 3.0}
        self.assertTrue(are_sets_equal(set1, set2))

    def test_sets_with_close_values(self):
        """Test with two sets that are close within the tolerance."""
        set1 = {1.0, 2.00001, 3.0}
        set2 = {1.0, 2.00002, 3.0}
        self.assertTrue(are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6))

    def test_sets_with_large_difference(self):
        """Test with two sets that have large differences beyond tolerance."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.5, 3.0}
        self.assertFalse(are_sets_equal(set1, set2))

    def test_sets_with_one_different_values(self):
        """Test with two sets containing one different floats."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.000001, 3.0}
        self.assertTrue(are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6))

    def test_empty_sets(self):
        """Test with two empty sets."""
        set1 = set()
        set2 = set()
        self.assertTrue(are_sets_equal(set1, set2))

if __name__ == '__main__':
    unittest.main()