d
e
f
 
c
u
b
i
c
_
b
e
z
i
e
r
(
t
:
 
f
l
o
a
t
,
 
p
0
:
 
l
i
s
t
,
 
p
1
:
 
l
i
s
t
,
 
p
2
:
 
l
i
s
t
,
 
p
3
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
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
 
a
 
c
u
b
i
c
 
B
é
z
i
e
r
 
c
u
r
v
e
 
a
t
 
a
 
g
i
v
e
n
 
p
a
r
a
m
e
t
e
r
 
t
 
(
t
y
p
i
c
a
l
l
y
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
 
(
f
l
o
a
t
)
:
 
A
 
f
l
o
a
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
 
p
a
r
a
m
e
t
e
r
 
a
l
o
n
g
 
t
h
e
 
c
u
r
v
e
,
 
w
h
e
r
e
 
0
 
<
=
 
t
 
<
=
 
1
.


 
 
 
 
 
 
 
 
p
0
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
s
t
a
r
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
1
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
f
i
r
s
t
 
c
o
n
t
r
o
l
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
2
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
c
o
n
t
r
o
l
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
3
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
e
n
d
 
p
o
i
n
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
p
o
i
n
t
 
o
n
 
t
h
e
 
c
u
r
v
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
o
 
t
h
e
 
p
a
r
a
m
e
t
e
r
 
t
.


 
 
 
 
"
"
"


 
 
 
 
x
 
=
 
(
1
 
-
 
t
)
 
*
*
 
3
 
*
 
p
0
[
0
]
 
+
 
3
 
*
 
(
1
 
-
 
t
)
 
*
*
 
2
 
*
 
t
 
*
 
p
1
[
0
]
 
+
 
3
 
*
 
(
1
 
-
 
t
)
 
*
 
t
 
*
*
 
2
 
*
 
p
2
[
0
]
 
+
 
t
 
*
*
 
3
 
*
 
p
3
[
0
]


 
 
 
 
y
 
=
 
(
1
 
-
 
t
)
 
*
*
 
3
 
*
 
p
0
[
1
]
 
+
 
3
 
*
 
(
1
 
-
 
t
)
 
*
*
 
2
 
*
 
t
 
*
 
p
1
[
1
]
 
+
 
3
 
*
 
(
1
 
-
 
t
)
 
*
 
t
 
*
*
 
2
 
*
 
p
2
[
1
]
 
+
 
t
 
*
*
 
3
 
*
 
p
3
[
1
]


 
 
 
 
r
e
t
u
r
n
 
[
x
,
 
y
]






d
e
f
 
b
e
z
i
e
r
_
c
u
r
v
e
_
r
a
n
g
e
(
n
:
 
i
n
t
,
 
p
0
:
 
l
i
s
t
,
 
p
1
:
 
l
i
s
t
,
 
p
2
:
 
l
i
s
t
,
 
p
3
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
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
 
a
 
c
u
b
i
c
 
B
é
z
i
e
r
 
c
u
r
v
e
 
o
v
e
r
 
a
 
r
a
n
g
e
 
o
f
 
p
a
r
a
m
e
t
e
r
 
v
a
l
u
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
p
o
i
n
t
s
 
t
o
 
c
a
l
c
u
l
a
t
e
.


 
 
 
 
 
 
 
 
p
0
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
s
t
a
r
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
1
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
f
i
r
s
t
 
c
o
n
t
r
o
l
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
2
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
i
z
e
 
2
 
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
 
x
 
a
n
d
 
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
s
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
c
o
n
t
r
o
l
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
3
 
(
l
i
s
t
)
:
 
A
import unittest
from typing import List

class TestCubicBezier(unittest.TestCase):
    def test_cubic_bezier_t0(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 0.0
        expected = [0.0, 0.0]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected)

    def test_cubic_bezier_t1(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 1.0
        expected = [1.0, 0.0]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected)

    def test_cubic_bezier_t0_5(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 1.0]
        p2 = [1.0, 1.0]
        p3 = [1.0, 0.0]
        t = 0.5
        expected = [0.5, 0.75]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)

    def test_cubic_bezier_mid_point(self):
        p0 = [0.0, 0.0]
        p1 = [1.0, 1.0]
        p2 = [2.0, 1.0]
        p3 = [3.0, 0.0]
        t = 0.5
        expected = [1.5, 0.75]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)

    def test_cubic_bezier_arbitrary_t(self):
        p0 = [0.0, 0.0]
        p1 = [0.0, 2.0]
        p2 = [2.0, 2.0]
        p3 = [2.0, 0.0]
        t = 0.75
        expected = [1.6875, 1.125]
        self.assertAlmostEqual(cubic_bezier(t, p0, p1, p2, p3), expected, places=9)
if __name__ == '__main__':
    unittest.main()