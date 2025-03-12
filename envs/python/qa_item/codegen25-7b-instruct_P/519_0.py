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
 
t
r
a
n
s
p
o
s
e
_
m
a
t
r
i
x
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


 
 
 
 
T
r
a
n
s
p
o
s
e
 
a
 
g
i
v
e
n
 
m
a
t
r
i
x
 
(
2
D
 
a
r
r
a
y
)
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
 
T
h
e
 
i
n
p
u
t
 
2
D
 
a
r
r
a
y
 
t
o
 
b
e
 
t
r
a
n
s
p
o
s
e
d
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
 
T
h
e
 
t
r
a
n
s
p
o
s
e
d
 
2
D
 
a
r
r
a
y
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
 
l
i
s
t
(
m
a
p
(
l
i
s
t
,
 
z
i
p
(
*
m
a
t
r
i
x
)
)
)




d
e
f
 
g
e
t
_
m
a
t
r
i
x
_
m
i
n
o
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
,
 
i
:
 
i
n
t
,
 
j
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
 
m
i
n
o
r
 
o
f
 
a
 
g
i
v
e
n
 
m
a
t
r
i
x
 
(
2
D
 
a
r
r
a
y
)
 
b
y
 
r
e
m
o
v
i
n
g
 
t
h
e
 
i
-
t
h
 
r
o
w
 
a
n
d
 
j
-
t
h
 
c
o
l
u
m
n
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
 
T
h
e
 
i
n
p
u
t
 
2
D
 
a
r
r
a
y
.


 
 
 
 
 
 
 
 
i
 
(
i
n
t
)
:
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
r
o
w
 
t
o
 
b
e
 
r
e
m
o
v
e
d
.


 
 
 
 
 
 
 
 
j
 
(
i
n
t
)
:
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
o
l
u
m
n
 
t
o
 
b
e
 
r
e
m
o
v
e
d
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
 
T
h
e
 
m
i
n
o
r
 
o
f
 
t
h
e
 
2
D
 
a
r
r
a
y
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
 
[
r
o
w
[
:
j
]
 
+
 
r
o
w
[
j
+
1
:
]
 
f
o
r
 
r
o
w
 
i
n
 
(
m
a
t
r
i
x
[
:
i
]
 
+
 
m
a
t
r
i
x
[
i
+
1
:
]
)
]




d
e
f
 
g
e
t
_
m
a
t
r
i
x
_
d
e
t
e
r
m
i
n
a
n
t
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
 
i
n
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
 
d
e
t
e
r
m
i
n
a
n
t
 
o
f
 
a
 
g
i
v
e
n
 
m
a
t
r
i
x
 
(
2
D
 
a
r
r
a
y
)
 
b
y
 
r
e
c
u
r
s
i
v
e
l
y
 
r
e
d
u
c
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
 
i
n
t
o
 
a
 
s
m
a
l
l
e
r
 
2
x
2
 
m
a
t
r
i
x
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
 
T
h
e
 
i
n
p
u
t
 
2
D
 
a
r
r
a
y
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
d
e
t
e
r
m
i
n
a
n
t
 
o
f
 
t
h
e
 
2
D
 
a
r
r
a
y
.


 
 
 
 
"
"
"


 
 
 
 
#
 
b
a
s
e
 
c
a
s
e
:
 
2
x
2
 
m
a
t
r
i
x


 
 
 
 
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
)
 
=
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
t
r
i
x
[
0
]
[
0
]
 
*
 
m
a
t
r
i
x
[
1
]
[
1
]
 
-
 
m
a
t
r
i
x
[
0
]
[
1
]
 
*
 
m
a
t
r
i
x
[
1
]
[
0
]




 
 
 
 
#
 
r
e
c
u
r
s
i
v
e
 
c
a
s
e
:
 
n
x
n
 
m
a
t
r
i
x


 
 
 
 
d
e
t
e
r
m
i
n
a
n
t
 
=
 
0


 
 
 
 
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
)
)
:


 
 
 
 
 
 
 
 
d
e
t
e
r
m
i
n
a
n
t
 
+
=
 
(
(
-
1
)
 
*
*
 
j
)
 
*
 
m
a
t
r
i
x
[
0
]
[
j
]
 
*
 
g
e
t
_
m
a
t
r
i
x
_
d
e
t
e
r
m
i
n
a
n
t
(
g
e
t
_
m
a
t
r
i
x
_
m
i
n
o
r
(
m
a
t
r
i
x
,
 
0
,
 
j
import unittest


class TestTransposeMatrix(unittest.TestCase):

    def test_square_matrix(self):
        """Test transposing a square matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)

    def test_rectangular_matrix(self):
        """Test transposing a rectangular matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)


    def test_matrix_with_empty_rows(self):
        """Test transposing a matrix with an empty row."""
        matrix = [[], []]
        expected = []
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)

    def test_single_element_matrix(self):
        """Test transposing a matrix with a single element."""
        matrix = [[5]]
        expected = [[5]]
        result = transpose_matrix(matrix)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()