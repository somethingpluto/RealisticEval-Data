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
 
f
i
n
d
_
t
_
f
o
r
_
x
(
t
a
r
g
e
t
_
x
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
,
 
f
l
o
a
t
]
,
 
p
1
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
,
 
f
l
o
a
t
]
,
 
p
2
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
,
 
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


 
 
 
 
F
i
n
d
 
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
 
a
 
g
i
v
e
n
 
x
-
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
 
t
a
r
g
e
t
_
x


 
 
 
 
o
n
 
a
 
q
u
a
d
r
a
t
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
 
d
e
f
i
n
e
d
 
b
y
 
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
s
 
p
0
,
 
p
1
,
 
a
n
d
 
p
2
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
x
 
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
 
x
-
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
 
f
o
r
 
w
h
i
c
h
 
w
e
 
w
a
n
t
 
t
o
 
f
i
n
d
 
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


 
 
 
 
 
 
 
 
p
0
 
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
,
 
f
l
o
a
t
]
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
.


 
 
 
 
 
 
 
 
p
1
 
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
,
 
f
l
o
a
t
]
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
 
o
f
 
t
h
e
 
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
.


 
 
 
 
 
 
 
 
p
2
 
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
,
 
f
l
o
a
t
]
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
 
o
f
 
t
h
e
 
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
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
)
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
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
 
e
v
a
l
u
a
t
e
d
 
a
t
 
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
t
a
r
g
e
t
_
x
.


 
 
 
 
"
"
"


 
 
 
 
#
 
T
O
D
O
:
 
I
m
p
l
e
m
e
n
t
 
t
h
i
s
 
f
u
n
c
t
i
o
n
.


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
t
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
a
 
p
o
i
n
t
 
a
n
d
 
a
 
q
u
a
d
r
a
t
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
:


 
 
 
 
#
 
d
i
s
t
a
n
c
e
 
=
 
s
q
r
t
(
(
x
 
-
 
p
0
_
x
)
^
2
 
+
 
(
y
 
-
 
p
0
_
y
)
^
2
)


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
t
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
p
o
i
n
t
s
:


 
 
 
 
#
 
d
i
s
t
a
n
c
e
 
=
 
s
q
r
t
(
(
x
2
 
-
 
x
1
)
^
2
 
+
 
(
y
2
 
-
 
y
1
)
^
2
)


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
t
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
a
 
p
o
i
n
t
 
a
n
d
 
a
 
q
u
a
d
r
a
t
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
:


 
 
 
 
#
 
d
i
s
t
a
n
c
e
 
=
 
s
q
r
t
(
(
x
 
-
 
p
0
_
x
)
^
2
 
+
 
(
y
 
-
 
p
0
_
y
)
^
2
)


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
t
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
a
 
p
o
i
n
t
 
a
n
d
 
a
 
q
u
a
d
r
a
t
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
:


 
 
 
 
#
 
d
i
s
t
a
n
c
e
 
=
 
s
q
r
t
(
(
x
 
-
 
p
0
_
x
)
^
2
 
+
 
(
y
 
-
 
p
0
_
y
)
^
2
)


 
 
 
 
#
 
Y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
t
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
a
 
p
o
i
n
t
 
a
n
d
 
a
 
q
u
a
d
r
a
t
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
:


 
 
 
 
#
 
d
i
s
t
a
n
c
e
 
=
 
s
q
r
t
(
(
x
 
-
 
p
0
_
x
)
^
2
 
+
 
(
y
 
-
 
p
0
_
y
)
^
import unittest

class TestFindxTForX(unittest.TestCase):
    TOLERANCE = 1e-6

    def test_find_t_for_x_at_start(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.0, delta=self.TOLERANCE)

    def test_find_t_for_x_at_end(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 1.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 1.0, delta=self.TOLERANCE)

    def test_find_t_for_x_mid_curve(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.25
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.25, delta=self.TOLERANCE)

    def test_find_t_for_x_near_mid_curve(self):
        p0 = 0.0
        p1 = 1.0
        p2 = 2.0
        target_x = 1.5
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.75, delta=self.TOLERANCE)
if __name__ == '__main__':
    unittest.main()