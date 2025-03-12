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
 
T
r
e
e
N
o
d
e
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
v
a
l
=
0
,
 
l
e
f
t
=
N
o
n
e
,
 
r
i
g
h
t
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
v
a
l
 
=
 
v
a
l


 
 
 
 
 
 
 
 
s
e
l
f
.
l
e
f
t
 
=
 
l
e
f
t


 
 
 
 
 
 
 
 
s
e
l
f
.
r
i
g
h
t
 
=
 
r
i
g
h
t






d
e
f
 
a
v
e
r
a
g
e
_
o
f
_
l
e
v
e
l
s
(
r
o
o
t
:
 
T
r
e
e
N
o
d
e
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


 
 
 
 
G
i
v
e
n
 
t
h
e
 
r
o
o
t
 
o
f
 
a
 
b
i
n
a
r
y
 
t
r
e
e
,
 
r
e
t
u
r
n
 
t
h
e
 
a
v
e
r
a
g
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
n
o
d
e
s
 
o
n
 
e
a
c
h
 
l
e
v
e
l
 
i
n
 
t
h
e
 
f
o
r
m
 
o
f
 
a
n
 
a
r
r
a
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
o
t
 
(
T
r
e
e
N
o
d
e
)
:
 
T
h
e
 
r
o
o
t
 
o
f
 
t
h
e
 
b
i
n
a
r
y
 
t
r
e
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
 
A
 
l
i
s
t
 
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
 
a
v
e
r
a
g
e
 
v
a
l
u
e
s
 
o
f
 
e
a
c
h
 
l
e
v
e
l
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
r
o
o
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
q
u
e
u
e
 
=
 
[
r
o
o
t
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




 
 
 
 
w
h
i
l
e
 
q
u
e
u
e
:


 
 
 
 
 
 
 
 
s
i
z
e
 
=
 
l
e
n
(
q
u
e
u
e
)


 
 
 
 
 
 
 
 
s
u
m
_
 
=
 
0


 
 
 
 
 
 
 
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
s
i
z
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
n
o
d
e
 
=
 
q
u
e
u
e
.
p
o
p
(
0
)


 
 
 
 
 
 
 
 
 
 
 
 
s
u
m
_
 
+
=
 
n
o
d
e
.
v
a
l


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
d
e
.
l
e
f
t
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
u
e
.
a
p
p
e
n
d
(
n
o
d
e
.
l
e
f
t
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
d
e
.
r
i
g
h
t
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
u
e
.
a
p
p
e
n
d
(
n
o
d
e
.
r
i
g
h
t
)


 
 
 
 
 
 
 
 
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
s
u
m
_
 
/
 
s
i
z
e
)




 
 
 
 
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
 
a
v
e
r
a
g
e
_
o
f
_
l
e
v
e
l
s
_
v
2
(
r
o
o
t
:
 
T
r
e
e
N
o
d
e
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


 
 
 
 
G
i
v
e
n
 
t
h
e
 
r
o
o
t
 
o
f
 
a
 
b
i
n
a
r
y
 
t
r
e
e
,
 
r
e
t
u
r
n
 
t
h
e
 
a
v
e
r
a
g
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
n
o
d
e
s
 
o
n
 
e
a
c
h
 
l
e
v
e
l
 
i
n
 
t
h
e
 
f
o
r
m
 
o
f
 
a
n
 
a
r
r
a
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
o
t
 
(
T
r
e
e
N
o
d
e
)
:
 
T
h
e
 
r
o
o
t
 
o
f
 
t
h
e
 
b
i
n
a
r
y
 
t
r
e
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
 
A
 
l
i
s
t
 
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
 
a
v
e
r
a
g
e
 
v
a
l
u
e
s
 
o
f
 
e
a
c
h
 
l
e
v
e
l
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
r
o
o
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
q
u
e
u
e
 
=
 
[
r
o
o
t
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




 
 
 
 
w
h
i
l
e
 
q
u
e
u
e
:


 
 
 
 
 
 
 
 
s
i
z
e
 
=
 
l
e
n
(
q
u
e
u
e
)


 
 
 
 
 
 
 
 
s
u
m
_
 
=
 
0


 
 
 
 
 
 
 
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
s
i
z
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
n
o
d
e
 
=
 
q
u
e
u
e
.
p
o
p
(
0
)


 
 
 
 
 
 
 
 
 
 
 
 
s
u
m
_
 
+
=
 
n
o
d
e
.
v
a
l


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
d
e
.
l
e
f
t
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
u
e
.
a
p
p
e
n
d
(
n
o
d
e
.
l
e
f
t
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
o
d
e
.
r
i
g
h
t
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
u
e
.
a
p
p
e
n
d
(
n
o
d
e
.
r
i
g
h
t
)


 
 
 
 
 
 
 
 
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
s
u
m
_
 
/
 
s
i
z
e
)




 
 
 
 
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
 
a
v
e
r
a
g
e
_
o
f
_
l
e
v
e
l
s
_
v
3
(
r
o
o
t
:
 
T
r
e
e
N
o
d
e
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


 
 
 
 
G
i
v
e
n
 
t
h
e
 
r
o
o
t
 
o
f
 
a
 
b
i
n
a
r
y
 
t
r
e
e
,
 
r
e
t
u
r
n
 
t
h
e
 
a
v
e
r
a
g
e
 
v
a
l
u
e
 
o
f
 
t
h
e
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestAverageOfLevels(unittest.TestCase):

    def test_empty_tree(self):
        root = None
        expected = []
        self.assertEqual(average_of_levels(root), expected)

    def test_single_node_tree(self):
        root = TreeNode(5)
        expected = [5.0]
        self.assertEqual(average_of_levels(root), expected)

    def test_balanced_tree_two_levels(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        expected = [3.0, 14.5]  # Level 0: 3; Level 1: (9+20)/2 = 14.5
        self.assertEqual(average_of_levels(root), expected)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [1.0, 2.0, 3.0]  # Level 0: 1; Level 1: 2; Level 2: 3
        self.assertEqual(average_of_levels(root), expected)

    def test_tree_multiple_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(8)
        expected = [1.0, 2.5, 5.67]  # Level 0: 1; Level 1: (2+3)/2 = 2.5; Level 2: (4+5+8)/3 ≈ 5.67
        self.assertAlmostEqual(average_of_levels(root)[2], expected[2], places=2)
        self.assertEqual(average_of_levels(root)[:2], expected[:2])
if __name__ == '__main__':
    unittest.main()