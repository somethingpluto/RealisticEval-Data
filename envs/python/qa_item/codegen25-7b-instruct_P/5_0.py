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
 
m
a
t
r
i
x
_
m
u
l
t
i
p
l
y
(
m
a
t
r
i
x
A
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
,
 
m
a
t
r
i
x
B
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
i
n
g
 
m
a
t
r
i
x
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n




 
 
 
 
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
A
 
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
 
m
a
t
r
i
x
 
A


 
 
 
 
 
 
 
 
m
a
t
r
i
x
B
 
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
 
m
a
t
r
i
x
 
B




 
 
 
 
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
:
 
m
a
t
r
i
x
A
 
m
a
t
r
i
x
B
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
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
A
[
0
]
)
 
!
=
 
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
B
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
E
r
r
o
r
:
 
m
a
t
r
i
x
 
d
i
m
e
n
s
i
o
n
s
 
a
r
e
 
n
o
t
 
c
o
m
p
a
t
i
b
l
e
 
f
o
r
 
m
u
l
t
i
p
l
i
c
a
t
i
o
n
"


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
=
 
[
[
0
 
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
m
a
t
r
i
x
B
[
0
]
)
)
]
 
f
o
r
 
j
 
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
m
a
t
r
i
x
A
)
)
]


 
 
 
 
 
 
 
 
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
m
a
t
r
i
x
A
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
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
m
a
t
r
i
x
B
[
0
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
k
 
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
m
a
t
r
i
x
B
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
[
i
]
[
j
]
 
+
=
 
m
a
t
r
i
x
A
[
i
]
[
k
]
 
*
 
m
a
t
r
i
x
B
[
k
]
[
j
]


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t






d
e
f
 
m
a
t
r
i
x
_
a
d
d
i
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
A
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
,
 
m
a
t
r
i
x
B
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
i
n
g
 
m
a
t
r
i
x
 
a
d
d
i
t
i
o
n




 
 
 
 
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
A
 
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
 
m
a
t
r
i
x
 
A


 
 
 
 
 
 
 
 
m
a
t
r
i
x
B
 
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
 
m
a
t
r
i
x
 
B




 
 
 
 
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
:
 
m
a
t
r
i
x
A
 
m
a
t
r
i
x
B
 
a
d
d
i
t
i
o
n
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
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
A
)
 
!
=
 
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
B
)
 
o
r
 
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
A
[
0
]
)
 
!
=
 
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
B
[
0
]
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
E
r
r
o
r
:
 
m
a
t
r
i
x
 
d
i
m
e
n
s
i
o
n
s
 
a
r
e
 
n
o
t
 
c
o
m
p
a
t
i
b
l
e
 
f
o
r
 
a
d
d
i
t
i
o
n
"


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
=
 
[
[
0
 
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
m
a
t
r
i
x
B
[
0
]
)
)
]
 
f
o
r
 
j
 
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
m
a
t
r
i
x
A
)
)
]


 
 
 
 
 
 
 
 
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
m
a
t
r
i
x
A
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
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
m
a
t
r
i
x
B
[
0
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
[
i
]
[
j
]
 
=
 
m
a
t
r
i
x
A
[
i
]
[
j
]
 
+
 
m
a
t
r
i
x
B
[
import unittest


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should correctly multiply standard matrices")

    def test_identity_matrix(self):
        mat1 = [[1, 0], [0, 1]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the identity matrix should yield the answer.py matrix")

    def test_zero_matrix(self):
        mat1 = [[0, 0], [0, 0]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the zero matrix should yield a zero matrix")

    def test_square_matrix_multiplication(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "The multiplication of two square matrices should yield the correct product")

    def test_large_identity_matrix(self):
        mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the larger identity matrix should yield the answer matrix")

if __name__ == '__main__':
    unittest.main()