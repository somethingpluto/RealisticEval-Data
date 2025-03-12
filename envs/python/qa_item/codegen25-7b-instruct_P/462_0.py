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
 
s
p
i
r
a
l
_
o
r
d
e
r
(
m
a
t
r
i
x
:
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
)
 
-
>
 
L
i
s
t
[
i
n
t
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
 
2
D
 
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
 
a
l
l
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
m
a
t
r
i
x
 
i
n
 
s
p
i
r
a
l
 
o
r
d
e
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
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
)
:
 
A
 
2
D
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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


 
 
 
 
 
 
 
 
L
i
s
t
[
i
n
t
]
:
 
A
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
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
 
m
a
t
r
i
x
 
e
l
e
m
e
n
t
s
 
i
n
 
s
p
i
r
a
l
 
o
r
d
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
m
a
t
r
i
x
 
o
r
 
n
o
t
 
m
a
t
r
i
x
[
0
]
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
r
e
s
u
l
t
 
=
 
[
]


 
 
 
 
t
o
p
,
 
b
o
t
t
o
m
 
=
 
0
,
 
l
e
n
(
m
a
t
r
i
x
)
 
-
 
1


 
 
 
 
l
e
f
t
,
 
r
i
g
h
t
 
=
 
0
,
 
l
e
n
(
m
a
t
r
i
x
[
0
]
)
 
-
 
1




 
 
 
 
w
h
i
l
e
 
t
o
p
 
<
=
 
b
o
t
t
o
m
 
a
n
d
 
l
e
f
t
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
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
f
t
,
 
r
i
g
h
t
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
m
a
t
r
i
x
[
t
o
p
]
[
i
]
)


 
 
 
 
 
 
 
 
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
t
o
p
 
+
 
1
,
 
b
o
t
t
o
m
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
m
a
t
r
i
x
[
i
]
[
r
i
g
h
t
]
)


 
 
 
 
 
 
 
 
i
f
 
t
o
p
 
!
=
 
b
o
t
t
o
m
:


 
 
 
 
 
 
 
 
 
 
 
 
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
r
i
g
h
t
 
-
 
1
,
 
l
e
f
t
 
-
 
1
,
 
-
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
m
a
t
r
i
x
[
b
o
t
t
o
m
]
[
i
]
)


 
 
 
 
 
 
 
 
i
f
 
l
e
f
t
 
!
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
 
 
 
 
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
b
o
t
t
o
m
 
-
 
1
,
 
t
o
p
,
 
-
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
m
a
t
r
i
x
[
i
]
[
l
e
f
t
]
)


 
 
 
 
 
 
 
 
t
o
p
 
+
=
 
1


 
 
 
 
 
 
 
 
b
o
t
t
o
m
 
-
=
 
1


 
 
 
 
 
 
 
 
l
e
f
t
 
+
=
 
1


 
 
 
 
 
 
 
 
r
i
g
h
t
 
-
=
 
1




 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t






d
e
f
 
s
p
i
r
a
l
_
o
r
d
e
r
_
v
2
(
m
a
t
r
i
x
:
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
)
 
-
>
 
L
i
s
t
[
i
n
t
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
 
2
D
 
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
 
a
l
l
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
m
a
t
r
i
x
 
i
n
 
s
p
i
r
a
l
 
o
r
d
e
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
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
)
:
 
A
 
2
D
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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


 
 
 
 
 
 
 
 
L
i
s
t
[
i
n
t
]
:
 
A
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
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
 
m
a
t
r
i
x
 
e
l
e
m
e
n
t
s
 
i
n
 
s
p
i
r
a
l
 
o
r
d
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
m
a
t
r
i
x
 
o
r
 
n
o
t
 
m
a
t
r
i
x
[
0
]
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
r
e
s
u
l
t
 
=
 
[
]


 
 
 
 
t
o
p
,
 
b
o
t
t
o
m
 
=
 
0
,
 
l
e
n
(
m
a
t
r
i
x
)
 
-
 
1


 
 
 
 
l
e
f
t
,
 
r
i
g
h
t
 
=
 
0
,
 
l
e
n
(
m
a
t
r
i
x
[
0
]
)
 
-
 
1




 
 
 
 
w
h
i
l
e
 
t
o
p
 
<
=
 
b
o
t
t
o
m
 
a
n
d
 
l
e
f
t
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
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
f
t
,
 
r
i
g
h
t
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
m
a
t
r
i
x
[
t
o
p
]
[
i
]
)


 
 
 
 
 
 
 
 
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
t
o
p
 
+
 
1
,
 
b
o
t
t
o
m
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
import unittest


class TestSpiralOrder(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(spiral_order([]), [])

    def test_single_row_matrix(self):
        self.assertEqual(spiral_order([[1, 2, 3]]), [1, 2, 3])

    def test_single_column_matrix(self):
        self.assertEqual(spiral_order([[1], [2], [3]]), [1, 2, 3])

    def test_square_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_rectangle_matrix(self):
        self.assertEqual(spiral_order([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
if __name__ == '__main__':
    unittest.main()