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
 
b
r
e
s
e
n
h
a
m
_
l
i
n
e
(
x
1
:
 
i
n
t
,
 
y
1
:
 
i
n
t
,
 
x
2
:
 
i
n
t
,
 
y
2
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
t
u
p
l
e
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
 
i
n
t
e
g
e
r
 
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
n
 
t
h
e
 
l
i
n
e
 
f
r
o
m
 
(
x
1
,
 
y
1
)
 
t
o
 
(
x
2
,
 
y
2
)
 
u
s
i
n
g
 
B
r
e
s
e
n
h
a
m
'
s
 
l
i
n
e
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
B
r
e
s
e
n
h
a
m
'
s
 
a
l
g
o
r
i
t
h
m
 
c
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
 
p
o
i
n
t
s
 
o
f
 
a
n
 
a
p
p
r
o
x
i
m
a
t
e
l
y
 
s
t
r
a
i
g
h
t
 
l
i
n
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
 
g
i
v
e
n
 
p
o
i
n
t
s
 
o
n
 
a
 
g
r
i
d
.


 
 
 
 
I
t
 
i
s
 
p
a
r
t
i
c
u
l
a
r
l
y
 
w
e
l
l
-
s
u
i
t
e
d
 
f
o
r
 
c
o
m
p
u
t
e
r
 
g
r
a
p
h
i
c
s
 
w
h
e
r
e
 
a
n
 
e
f
f
i
c
i
e
n
t
,
 
i
n
t
e
g
e
r
-
b
a
s
e
d
 
a
l
g
o
r
i
t
h
m
 
i
s
 
n
e
e
d
e
d
 
t
o


 
 
 
 
d
e
t
e
r
m
i
n
e
 
w
h
i
c
h
 
p
o
i
n
t
s
 
s
h
o
u
l
d
 
b
e
 
r
a
s
t
e
r
i
z
e
d
 
t
o
 
r
e
p
r
e
s
e
n
t
 
t
h
e
 
l
i
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
1
 
(
i
n
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
i
n
g
 
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
 
l
i
n
e
.


 
 
 
 
 
 
 
 
y
1
 
(
i
n
t
)
:
 
T
h
e
 
y
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
i
n
g
 
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
 
l
i
n
e
.


 
 
 
 
 
 
 
 
x
2
 
(
i
n
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
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
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
 
l
i
n
e
.


 
 
 
 
 
 
 
 
y
2
 
(
i
n
t
)
:
 
T
h
e
 
y
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
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
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
 
l
i
n
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


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
:
 
A
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
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
s
 
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
 
a
 
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
 
l
i
n
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
E
n
s
u
r
e
 
t
h
a
t
 
t
h
e
 
s
t
a
r
t
i
n
g
 
a
n
d
 
e
n
d
i
n
g
 
p
o
i
n
t
s
 
a
r
e
 
i
n
 
t
h
e
 
c
o
r
r
e
c
t
 
o
r
d
e
r


 
 
 
 
i
f
 
x
1
 
>
 
x
2
:


 
 
 
 
 
 
 
 
x
1
,
 
x
2
 
=
 
x
2
,
 
x
1


 
 
 
 
 
 
 
 
y
1
,
 
y
2
 
=
 
y
2
,
 
y
1




 
 
 
 
#
 
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
 
s
t
e
e
p
n
e
s
s
 
o
f
 
t
h
e
 
l
i
n
e


 
 
 
 
i
s
_
s
t
e
e
p
 
=
 
a
b
s
(
y
2
 
-
 
y
1
)
 
>
 
a
b
s
(
x
2
 
-
 
x
1
)




 
 
 
 
#
 
S
t
o
r
e
 
t
h
e
 
p
o
i
n
t
s
 
i
n
 
a
 
l
i
s
t


 
 
 
 
p
o
i
n
t
s
 
=
 
[
]




 
 
 
 
#
 
S
w
a
p
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
p
o
i
n
t
s
 
i
f
 
n
e
c
e
s
s
a
r
y


 
 
 
 
i
f
 
i
s
_
s
t
e
e
p
:


 
 
 
 
 
 
 
 
x
1
,
 
y
1
 
=
 
y
1
,
 
x
1


 
 
 
 
 
 
 
 
x
2
,
 
y
2
 
=
 
y
2
,
 
x
2




 
 
 
 
#
 
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
 
a
b
s
o
l
u
t
e
 
d
i
f
f
e
r
e
n
c
e
s
 
b
e
t
w
e
e
n
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
p
o
i
n
t
s


 
 
 
 
d
x
 
=
 
x
2
 
-
 
x
1


 
 
 
 
d
y
 
=
 
a
b
s
(
y
2
 
-
 
y
1
)




 
 
 
 
#
 
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
r
r
o
r
 
v
a
l
u
e
 
f
o
r
 
e
a
c
h
 
s
t
e
p


 
 
 
 
e
r
r
o
r
 
=
 
d
x
 
/
 
2
.
0




 
 
 
 
#
 
L
o
o
p
 
o
v
e
r
 
t
h
e
 
p
o
i
n
t
s
 
i
n
 
t
h
e
 
l
i
n
e


 
 
 
 
y
 
=
 
y
1


 
 
 
 
y
s
t
e
p
 
=
 
1
 
i
f
 
y
1
 
<
 
y
2
 
e
l
s
e
 
-
1




 
 
 
 
f
o
r
 
x
 
i
n
 
r
a
n
g
e
(
x
1
,
 
x
2
 
+
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
s
t
e
e
p
:


 
 
 
 
 
 
 
 
 
 
 
 
p
o
i
n
t
s
import unittest


class TestBresenhamLineAlgorithm(unittest.TestCase):
    def test_horizontal_line(self):
        self.assertEqual(bresenham_line(1, 5, 5, 5), [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])

    def test_vertical_line(self):
        self.assertEqual(bresenham_line(3, 2, 3, 6), [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])

    def test_diagonal_line(self):
        self.assertEqual(bresenham_line(2, 2, 6, 6), [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])

    def test_steep_slope(self):
        self.assertEqual(bresenham_line(1, 1, 4, 6), [(1, 1), (2, 2), (2, 3), (3, 4), (3, 5), (4, 6)])

    def test_negative_slope(self):
        self.assertEqual(bresenham_line(5, 1, 1, 5), [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)])

if __name__ == '__main__':
    unittest.main()