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
v
e
c
t
o
r
_
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
f
l
o
a
t
]
]
,
 
v
e
c
t
o
r
:
 
L
i
s
t
[
f
l
o
a
t
]
)
 
-
>
 
L
i
s
t
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


 
 
 
 
M
u
l
t
i
p
l
i
e
s
 
a
 
m
a
t
r
i
x
 
b
y
 
a
 
v
e
c
t
o
r
 
a
n
d
 
r
e
t
u
r
n
s
 
t
h
e
 
r
e
s
u
l
t
i
n
g
 
v
e
c
t
o
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
f
l
o
a
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
.


 
 
 
 
 
 
 
 
v
e
c
t
o
r
 
(
L
i
s
t
[
f
l
o
a
t
]
)
:
 
A
 
1
D
 
l
i
s
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
 
v
e
c
t
o
r
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
 
r
e
s
u
l
t
i
n
g
 
v
e
c
t
o
r
 
a
f
t
e
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
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
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
 
a
n
d
 
v
e
c
t
o
r
 
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
 
!
=
 
l
e
n
(
v
e
c
t
o
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
M
a
t
r
i
x
 
a
n
d
 
v
e
c
t
o
r
 
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
.
"
)




 
 
 
 
r
e
s
u
l
t
 
=
 
[
0
.
0
]
 
*
 
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
v
e
c
t
o
r
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
[
i
]
 
+
=
 
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
j
]
 
*
 
v
e
c
t
o
r
[
j
]




 
 
 
 
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
 
v
e
c
t
o
r
_
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
i
c
a
t
i
o
n
(
v
e
c
t
o
r
:
 
L
i
s
t
[
f
l
o
a
t
]
,
 
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
f
l
o
a
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


 
 
 
 
M
u
l
t
i
p
l
i
e
s
 
a
 
v
e
c
t
o
r
 
b
y
 
a
 
m
a
t
r
i
x
 
a
n
d
 
r
e
t
u
r
n
s
 
t
h
e
 
r
e
s
u
l
t
i
n
g
 
v
e
c
t
o
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
t
o
r
 
(
L
i
s
t
[
f
l
o
a
t
]
)
:
 
A
 
1
D
 
l
i
s
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
 
v
e
c
t
o
r
.


 
 
 
 
 
 
 
 
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
f
l
o
a
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
 
r
e
s
u
l
t
i
n
g
 
v
e
c
t
o
r
 
a
f
t
e
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
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
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
 
o
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
 
a
n
d
 
m
a
t
r
i
x
 
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
t
o
r
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
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
V
e
c
t
o
r
 
a
n
d
 
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
.
"
)




 
 
 
 
r
e
s
u
l
t
 
=
 
[
0
.
0
]
 
*
 
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
[
0
]
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
v
e
c
t
o
r
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
[
i
]
 
+
=
 
v
e
c
t
o
r
[
j
]
 
*
 
m
a
t
r
i
x
[
j
]
[
i
]




 
 
 
 
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
 
m
a
t
r
i
x
_
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
i
c
a
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
_
a
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
f
l
o
a
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
_
b
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
f
l
o
a
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
f
l
o
a
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
M
u
l
t
i
p
l
i
e
s
 
t
w
o
 
m
a
t
import unittest


class TestMatrixVectorMultiplication(unittest.TestCase):

    def test_non_square_matrix(self):
        """Test case for a non-square matrix and a compatible vector."""
        matrix = [[1, 2], [3, 4], [5, 6]]
        vector = [2, 3]
        expected_result = [8.0, 18.0, 28.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_zero_vector(self):
        """Test case for a matrix and a zero vector."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        vector = [0, 0, 0]
        expected_result = [0.0, 0.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_single_element(self):
        """Test case for a single element matrix and vector."""
        matrix = [[5]]
        vector = [3]
        expected_result = [15.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_single_element_matrix_and_vector(self):
        # Test case with a single element in the matrix and vector
        matrix = [[3]]
        vector = [4]
        expected = [12]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected)

    def test_compatible_sizes(self):
        # Test case with compatible sizes but different dimensions
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        vector = [1, 1, 1]
        expected = [6, 15, 24]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected)

if __name__ == '__main__':
    unittest.main()