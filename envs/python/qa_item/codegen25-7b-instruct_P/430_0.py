d
e
f
 
i
n
t
e
r
s
e
c
t
_
v
e
r
t
i
c
a
l
l
y
(
r
e
c
t
1
,
 
r
e
c
t
2
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
w
h
e
t
h
e
r
 
t
w
o
 
r
e
c
t
a
n
g
l
e
s
 
i
n
t
e
r
s
e
c
t
 
i
n
 
t
h
e
 
v
e
r
t
i
c
a
l
 
d
i
r
e
c
t
i
o
n




 
 
 
 
E
a
c
h
 
r
e
c
t
a
n
g
l
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
a
 
t
u
p
l
e
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
)
,
 
w
h
e
r
e
:


 
 
 
 
-
 
(
x
1
,
 
y
1
)
 
a
r
e
 
t
h
e
 
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
 
o
f
 
t
h
e
 
b
o
t
t
o
m
-
l
e
f
t
 
c
o
r
n
e
r
.


 
 
 
 
-
 
(
x
2
,
 
y
2
)
 
a
r
e
 
t
h
e
 
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
 
o
f
 
t
h
e
 
t
o
p
-
r
i
g
h
t
 
c
o
r
n
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
e
c
t
1
 
(
t
u
p
l
e
)
:
 
T
h
e
 
f
i
r
s
t
 
r
e
c
t
a
n
g
l
e
 
d
e
f
i
n
e
d
 
b
y
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
)
.


 
 
 
 
 
 
 
 
r
e
c
t
2
 
(
t
u
p
l
e
)
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
 
r
e
c
t
a
n
g
l
e
 
d
e
f
i
n
e
d
 
b
y
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
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


 
 
 
 
 
 
 
 
b
o
o
l
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
 
r
e
c
t
a
n
g
l
e
s
 
i
n
t
e
r
s
e
c
t
 
v
e
r
t
i
c
a
l
l
y
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


 
 
 
 
x
1
,
 
y
1
,
 
x
2
,
 
y
2
 
=
 
r
e
c
t
1


 
 
 
 
x
3
,
 
y
3
,
 
x
4
,
 
y
4
 
=
 
r
e
c
t
2


 
 
 
 
r
e
t
u
r
n
 
(
x
1
 
<
=
 
x
4
 
a
n
d
 
x
3
 
<
=
 
x
2
 
a
n
d
 
y
1
 
<
=
 
y
4
 
a
n
d
 
y
3
 
<
=
 
y
2
)






d
e
f
 
i
n
t
e
r
s
e
c
t
_
h
o
r
i
z
o
n
t
a
l
l
y
(
r
e
c
t
1
,
 
r
e
c
t
2
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
w
h
e
t
h
e
r
 
t
w
o
 
r
e
c
t
a
n
g
l
e
s
 
i
n
t
e
r
s
e
c
t
 
i
n
 
t
h
e
 
h
o
r
i
z
o
n
t
a
l
 
d
i
r
e
c
t
i
o
n




 
 
 
 
E
a
c
h
 
r
e
c
t
a
n
g
l
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
a
 
t
u
p
l
e
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
)
,
 
w
h
e
r
e
:


 
 
 
 
-
 
(
x
1
,
 
y
1
)
 
a
r
e
 
t
h
e
 
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
 
o
f
 
t
h
e
 
b
o
t
t
o
m
-
l
e
f
t
 
c
o
r
n
e
r
.


 
 
 
 
-
 
(
x
2
,
 
y
2
)
 
a
r
e
 
t
h
e
 
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
 
o
f
 
t
h
e
 
t
o
p
-
r
i
g
h
t
 
c
o
r
n
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
e
c
t
1
 
(
t
u
p
l
e
)
:
 
T
h
e
 
f
i
r
s
t
 
r
e
c
t
a
n
g
l
e
 
d
e
f
i
n
e
d
 
b
y
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
)
.


 
 
 
 
 
 
 
 
r
e
c
t
2
 
(
t
u
p
l
e
)
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
 
r
e
c
t
a
n
g
l
e
 
d
e
f
i
n
e
d
 
b
y
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
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


 
 
 
 
 
 
 
 
b
o
o
l
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
 
r
e
c
t
a
n
g
l
e
s
 
i
n
t
e
r
s
e
c
t
 
h
o
r
i
z
o
n
t
a
l
l
y
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


 
 
 
 
x
1
,
 
y
1
,
 
x
2
,
 
y
2
 
=
 
r
e
c
t
1


 
 
 
 
x
3
,
 
y
3
,
 
x
4
,
 
y
4
 
=
 
r
e
c
t
2


 
 
 
 
r
e
t
u
r
n
 
(
y
1
 
<
=
 
y
4
 
a
n
d
 
y
3
 
<
=
 
y
2
 
a
n
d
 
x
1
 
<
=
 
x
4
 
a
n
d
 
x
3
 
<
=
 
x
2
)






d
e
f
 
i
n
t
e
r
s
e
c
t
(
r
e
c
t
1
,
 
r
e
c
t
2
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
w
h
e
t
h
e
r
 
t
w
o
 
r
e
c
t
a
n
g
l
e
s
 
i
n
t
e
r
s
e
c
t




 
 
 
 
E
a
c
h
 
r
e
c
t
a
n
g
l
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
a
 
t
u
p
l
e
 
(
x
1
,
 
y
1
,
 
x
2
,
 
y
2
)
,
 
w
h
e
r
e
:


 
 
 
 
-
import unittest


class TestIntersectVertically(unittest.TestCase):

    def test_case1(self):
        """Test with overlapping rectangles."""
        rect1 = (0, 0, 2, 2)
        rect2 = (1, 1, 3, 3)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case2(self):
        """Test with overlapping rectangles."""
        rect1 = (-1, -1, 1, 1)
        rect2 = (0, 0, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case3(self):
        # Test case where rectangles partially overlap vertically
        rect1 = (0, 1, 2, 4)
        rect2 = (1, 0, 3, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case4(self):
        # Test case where rectangles are identical
        rect1 = (0, 0, 2, 2)
        rect2 = (0, 0, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

    def test_case5(self):
        # Test case where one rectangle is completely inside the other
        rect1 = (0, 0, 4, 4)
        rect2 = (1, 1, 2, 2)
        self.assertTrue(intersect_vertically(rect1, rect2))

if __name__ == '__main__':
    unittest.main()