d
e
f
 
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
 
f
l
o
a
t
,
 
p
1
:
 
f
l
o
a
t
,
 
p
2
:
 
f
l
o
a
t
,
 
p
3
:
 
f
l
o
a
t
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
a
l
c
u
l
a
t
e
s
 
t
h
e
 
v
a
l
u
e
 
o
f
 
a
 
c
u
b
i
c
 
B
e
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
 
T
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
 
v
a
l
u
e
 
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
 
t
h
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
s
 
a
 
p
o
s
i
t
i
o
n
 
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
.


 
 
 
 
 
 
 
 
p
0
 
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
 
o
f
 
t
h
e
 
c
u
r
v
e
,
 
t
y
p
i
c
a
l
l
y
 
w
h
e
r
e
 
t
h
e
 
c
u
r
v
e
 
s
t
a
r
t
s
.


 
 
 
 
 
 
 
 
p
1
 
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
,
 
w
h
i
c
h
 
i
n
f
l
u
e
n
c
e
s
 
t
h
e
 
t
a
n
g
e
n
t
 
a
t
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
t
h
e
 
c
u
r
v
e
.


 
 
 
 
 
 
 
 
p
2
 
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
 
t
h
i
r
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
,
 
w
h
i
c
h
 
i
n
f
l
u
e
n
c
e
s
 
t
h
e
 
t
a
n
g
e
n
t
 
a
t
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
c
u
r
v
e
.


 
 
 
 
 
 
 
 
p
3
 
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
o
u
r
t
h
 
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
,
 
t
y
p
i
c
a
l
l
y
 
w
h
e
r
e
 
t
h
e
 
c
u
r
v
e
 
e
n
d
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
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
 
B
e
z
i
e
r
 
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


 
 
 
 
r
e
t
u
r
n
 
(


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
+
 
t
 
*
*
 
3
 
*
 
p
3


 
 
 
 
)






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
r
a
n
g
e
(


 
 
 
 
p
0
:
 
f
l
o
a
t
,
 
p
1
:
 
f
l
o
a
t
,
 
p
2
:
 
f
l
o
a
t
,
 
p
3
:
 
f
l
o
a
t
,
 
n
:
 
i
n
t
 
=
 
1
0
0


)
 
-
>
 
I
t
e
r
a
t
o
r
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


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
 
r
a
n
g
e
 
o
f
 
p
o
i
n
t
s
 
a
l
o
n
g
 
a
 
c
u
b
i
c
 
B
e
z
i
e
r
 
c
u
r
v
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
0
 
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
 
o
f
 
t
h
e
 
c
u
r
v
e
,
 
t
y
p
i
c
a
l
l
y
 
w
h
e
r
e
 
t
h
e
 
c
u
r
v
e
 
s
t
a
r
t
s
.


 
 
 
 
 
 
 
 
p
1
 
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
,
 
w
h
i
c
h
 
i
n
f
l
u
e
n
c
e
s
 
t
h
e
 
t
a
n
g
e
n
t
 
a
t
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
t
h
e
 
c
u
r
v
e
.


 
 
 
 
 
 
 
 
p
2
 
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
 
t
h
i
r
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
,
 
w
h
i
c
h
 
i
n
f
l
u
e
n
c
e
s
 
t
h
e
 
t
a
n
g
e
n
t
 
a
t
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
c
u
r
v
e
.


 
 
 
 
 
 
 
 
p
3
 
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
o
u
r
t
h
 
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
,
 
t
y
p
i
c
a
l
l
y
 
w
h
e
r
e
 
t
h
e
 
c
u
r
v
e
 
e
n
d
s
.


 
 
 
 
 
 
 
 
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
 
g
e
n
e
r
a
t
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


 
 
 
 
 
 
 
 
I
t
e
r
a
t
o
r
[
f
l
o
a
t
]
:
 
T
h
e
 
p
o
i
n
t
s
 
a
l
o
n
g
 
t
h
e
 
B
e
z
i
e
r
 
c
u
r
v
e
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
t
 
i
n
 
l
i
n
s
p
a
c
e
(
0
,
 
1
,
 
n
)
:


 
 
 
 
 
 
 
 
y
i
e
l
d
 
b
e
z
i
e
r
(
t
,
 
p
0
,
 
p
1
,
 
p
2
,
 
p
3
)






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
(


 
 
 
 
p
0
:
 
f
l
o
a
t
,
 
p
1
:
 
f
l
o
a
t
,
 
p
2
:
 
f
l
o
a
t
,
 
p
3
:
 
f
l
o
a
t
import unittest

class TestAnswer(unittest.TestCase):

    def test_bezier_at_start(self):
        self.assertAlmostEqual(bezier(0, 1, 3, 3, 1), 1.0,
                               msg="Bezier at t=0 should return the first control point p0")

    def test_bezier_at_end(self):
        self.assertAlmostEqual(bezier(1, 1, 3, 3, 1), 1.0,
                               msg="Bezier at t=1 should return the last control point p3")

    def test_bezier_at_middle(self):
        expected = 1.0 * 0.125 + 3 * 0.375 + 3 * 0.375 + 1 * 0.125  # Calculate manually for t=0.5
        self.assertAlmostEqual(bezier(0.5, 1, 3, 3, 1), expected,
                               delta=0.001,
                               msg="Bezier at t=0.5 should return the correct middle value")

    def test_bezier_with_identical_control_points(self):
        self.assertAlmostEqual(bezier(0.5, 2, 2, 2, 2), 2.0,
                               msg="Bezier with all control points the same should return that value")

if __name__ == '__main__':
    unittest.main()