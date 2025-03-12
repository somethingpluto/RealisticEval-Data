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
 
L
i
s
t






d
e
f
 
i
s
_
p
o
i
n
t
_
o
n
_
l
i
n
e
(
A
:
 
L
i
s
t
[
i
n
t
]
,
 
B
:
 
L
i
s
t
[
i
n
t
]
,
 
C
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
b
o
o
l
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
 
A
 
p
o
i
n
t
 
i
s
 
o
n
 
a
 
l
i
n
e
 
f
o
r
m
e
d
 
b
y
 
t
w
o
 
p
o
i
n
t
s
,
 
s
u
c
h
 
a
s
 
p
o
i
n
t
 
C
 
i
s
 
o
n
 
a
 
l
i
n
e
 
f
o
r
m
e
d
 
b
y
 
p
o
i
n
t
s
 
A
 
a
n
d
 
B


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
A
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
A
 
x
y


 
 
 
 
 
 
 
 
B
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
B
 
x
y


 
 
 
 
 
 
 
 
C
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
C
 
x
y




 
 
 
 
R
e
t
u
r
n
s
:
 
i
s
 
C
 
i
n
 
l
i
n
e
 
o
f
 
A
 
B




 
 
 
 
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
C
[
1
]
 
-
 
A
[
1
]
)
 
*
 
(
B
[
0
]
 
-
 
A
[
0
]
)
 
=
=
 
(
B
[
1
]
 
-
 
A
[
1
]
)
 
*
 
(
C
[
0
]
 
-
 
A
[
0
]
)






d
e
f
 
i
s
_
p
o
i
n
t
_
i
n
_
t
r
i
a
n
g
l
e
(
A
:
 
L
i
s
t
[
i
n
t
]
,
 
B
:
 
L
i
s
t
[
i
n
t
]
,
 
C
:
 
L
i
s
t
[
i
n
t
]
,
 
D
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
b
o
o
l
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
 
a
 
p
o
i
n
t
 
i
s
 
i
n
 
a
 
t
r
i
a
n
g
l
e
 
f
o
r
m
e
d
 
b
y
 
t
h
r
e
e
 
p
o
i
n
t
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
A
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
A
 
x
y


 
 
 
 
 
 
 
 
B
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
B
 
x
y


 
 
 
 
 
 
 
 
C
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
C
 
x
y


 
 
 
 
 
 
 
 
D
 
(
L
i
s
t
[
i
n
t
]
)
:
 
p
o
i
n
t
 
D
 
x
y




 
 
 
 
R
e
t
u
r
n
s
:
 
i
s
 
D
 
i
n
 
t
r
i
a
n
g
l
e
 
o
f
 
A
 
B
 
C




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
i
s
_
p
o
i
n
t
_
o
n
_
l
i
n
e
(
A
,
 
B
,
 
D
)
 
a
n
d
 
i
s
_
p
o
i
n
t
_
o
n
_
l
i
n
e
(
B
,
 
C
,
 
D
)
 
a
n
d
 
i
s
_
p
o
i
n
t
_
o
n
_
l
i
n
e
(
C
,
 
A
,
 
D
)






d
e
f
 
i
s
_
p
o
i
n
t
_
i
n
_
p
o
l
y
g
o
n
(
A
:
 
L
i
s
t
[
i
n
t
]
,
 
B
:
 
L
i
s
t
[
i
n
t
]
,
 
C
:
 
L
i
s
t
[
i
n
t
]
,
 
D
:
 
L
i
s
t
[
i
n
t
]
,
 
E
:
 
L
i
s
t
[
i
n
t
]
,
 
F
:
 
L
i
s
t
[
i
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
:
 
L
i
s
t
[
i
n
t
]
,
 
H
:
 
L
i
s
t
[
i
n
t
]
,
 
I
:
 
L
i
s
t
[
i
n
t
]
,
 
J
:
 
L
i
s
t
[
i
n
t
]
,
 
K
:
 
L
i
s
t
[
i
n
t
]
,
 
L
:
 
L
i
s
t
[
i
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
M
:
 
L
i
s
t
[
i
n
t
]
,
 
N
:
 
L
i
s
t
[
i
n
t
]
,
 
O
:
 
L
i
s
t
[
i
n
t
]
,
 
P
:
 
L
i
s
t
[
i
n
t
]
,
 
Q
:
 
L
i
s
t
[
i
n
t
]
,
 
R
:
 
L
i
s
t
[
i
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
:
 
L
i
s
t
[
i
n
t
]
,
 
T
:
 
L
i
s
t
[
i
n
t
]
,
 
U
:
 
L
i
s
t
[
i
n
t
]
,
 
V
:
 
L
i
s
t
[
i
n
t
]
,
 
W
:
 
L
i
s
t
[
i
n
t
]
,
 
X
:
 
L
i
s
t
[
i
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Y
import unittest


def is_point_on_line(A, B, C):
    (x_a, y_a), (x_b, y_b), (x_c, y_c) = A, B, C
    if x_a == x_b:  # Check for vertical line
        return x_c == x_a
    return (y_c - y_a) * (x_b - x_a) == (y_b - y_a) * (x_c - x_a)


class TestPointOnLine(unittest.TestCase):
    def test_point_on_line(self):
        A = (0, 0)
        B = (10, 10)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_point_not_on_line(self):
        A = (0, 0)
        B = (10, 10)
        C = (5, 6)
        self.assertFalse(is_point_on_line(A, B, C))

    def test_vertical_line(self):
        A = (5, 0)
        B = (5, 10)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_horizontal_line(self):
        A = (0, 5)
        B = (10, 5)
        C = (5, 5)
        self.assertTrue(is_point_on_line(A, B, C))

    def test_point_not_on_vertical_line(self):
        A = (5, 0)
        B = (5, 10)
        C = (6, 5)
        self.assertFalse(is_point_on_line(A, B, C))

if __name__ == '__main__':
    unittest.main()