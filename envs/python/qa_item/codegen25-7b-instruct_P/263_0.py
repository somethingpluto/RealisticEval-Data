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






c
l
a
s
s
 
M
a
t
r
i
x
T
r
a
v
e
r
s
a
l
:


 
 
 
 
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
t
r
a
v
e
r
s
a
l
(
s
e
l
f
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


 
 
 
 
 
 
 
 
T
r
a
v
e
r
s
e
 
a
 
g
i
v
e
n
 
m
 
x
 
n
 
m
a
t
r
i
x
 
i
n
 
a
 
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
 
a
n
d
 
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
 
a
s
 
a
 
l
i
s
t
.




 
 
 
 
 
 
 
 
T
h
e
 
f
u
n
c
t
i
o
n
 
s
t
a
r
t
s
 
a
t
 
t
h
e
 
t
o
p
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
 
t
r
a
v
e
r
s
e
s
 
i
t
 
i
n
 
a


 
 
 
 
 
 
 
 
c
l
o
c
k
w
i
s
e
 
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
,
 
m
o
v
i
n
g
 
r
i
g
h
t
 
a
c
r
o
s
s
 
t
h
e
 
t
o
p
 
r
o
w
,
 
d
o
w
n
 
t
h
e
 
r
i
g
h
t
 
c
o
l
u
m
n
,


 
 
 
 
 
 
 
 
l
e
f
t
 
a
c
r
o
s
s
 
t
h
e
 
b
o
t
t
o
m
 
r
o
w
,
 
a
n
d
 
u
p
 
t
h
e
 
l
e
f
t
 
c
o
l
u
m
n
,
 
r
e
p
e
a
t
i
n
g
 
t
h
i
s
 
p
r
o
c
e
s
s


 
 
 
 
 
 
 
 
u
n
t
i
l
 
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
 
a
r
e
 
t
r
a
v
e
r
s
e
d
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
 
w
i
t
h
 
m
 
r
o
w
s
 
a
n
d
 
n
 
c
o
l
u
m
n
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
 
t
h
e
 
o
r
d
e
r
 
t
h
e
y
 
w
e
r
e
 
t
r
a
v
e
r
s
e
d
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


 
 
 
 
 
 
 
 
r
o
w
_
s
t
a
r
t
 
=
 
0


 
 
 
 
 
 
 
 
r
o
w
_
e
n
d
 
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
 
-
 
1


 
 
 
 
 
 
 
 
c
o
l
_
s
t
a
r
t
 
=
 
0


 
 
 
 
 
 
 
 
c
o
l
_
e
n
d
 
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
 
r
o
w
_
s
t
a
r
t
 
<
=
 
r
o
w
_
e
n
d
 
a
n
d
 
c
o
l
_
s
t
a
r
t
 
<
=
 
c
o
l
_
e
n
d
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
T
r
a
v
e
r
s
e
 
r
i
g
h
t
 
a
c
r
o
s
s
 
t
h
e
 
t
o
p
 
r
o
w


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
r
a
n
g
e
(
c
o
l
_
s
t
a
r
t
,
 
c
o
l
_
e
n
d
 
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
r
o
w
_
s
t
a
r
t
]
[
c
o
l
]
)


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
_
s
t
a
r
t
 
+
=
 
1




 
 
 
 
 
 
 
 
 
 
 
 
#
 
T
r
a
v
e
r
s
e
 
d
o
w
n
 
a
c
r
o
s
s
 
t
h
e
 
r
i
g
h
t
 
c
o
l
u
m
n


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
a
n
g
e
(
r
o
w
_
s
t
a
r
t
,
 
r
o
w
_
e
n
d
 
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
r
o
w
]
[
c
o
l
_
e
n
d
]
)


 
 
 
 
 
 
 
 
 
 
 
 
c
o
l
_
e
n
d
 
-
=
 
1




 
 
 
 
 
 
 
 
 
 
 
 
#
 
T
r
a
v
e
r
s
e
 
l
e
f
t
 
a
c
r
o
s
s
 
t
h
e
 
b
o
t
t
o
m
 
r
o
w


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
r
o
w
_
s
t
a
r
t
 
<
=
 
r
o
w
_
e
n
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
r
a
n
g
e
(
c
o
l
_
e
n
d
,
 
c
o
l
_
s
t
a
r
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
r
o
w
_
e
n
d
]
[
c
o
l
]
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
_
e
n
d
 
-
=
 
1




 
 
 
 
 
 
 
 
 
 
 
 
#
 
T
r
a
v
e
r
s
e
 
u
p
 
a
c
r
o
s
s
 
t
h
e
 
l
e
f
t
 
c
o
l
u
m
n


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
o
l
_
s
t
a
r
t
 
<
=
 
c
o
l
_
e
n
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
a
n
g
e
(
r
o
w
_
e
n
d
,
 
r
o
w
_
s
t
a
r
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
r
o
w
]
[
c
o
l
_
s
t
a
r
t
]
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
l
_
s
t
a
r
t
 
+
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
t
r
a
v
e
r
s
a
l
_
2
(
s
e
l
f
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
import unittest

class TestMatrixTraversal(unittest.TestCase):
    def setUp(self):
        self.mt = MatrixTraversal()

    def test_empty_matrix(self):
        # 异常值测试：空矩阵
        self.assertEqual(self.mt.spiral_traversal([]), [], "Should return an empty list for an empty matrix")

    def test_single_element_matrix(self):
        # 基本逻辑功能测试：单元素矩阵
        matrix = [[42]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [42], "Should return the single element in the matrix")

    def test_single_row_matrix(self):
        # 边界值测试：单行矩阵
        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 4, 5], "Should return all elements in a single row")

    def test_single_column_matrix(self):
        # 边界值测试：单列矩阵
        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 4, 5], "Should return all elements in a single column")

    def test_general_case(self):
        # 基本逻辑功能测试：多行多列矩阵
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.mt.spiral_traversal(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5], "Should return elements in spiral order for a general case matrix")

if __name__ == '__main__':
    unittest.main()