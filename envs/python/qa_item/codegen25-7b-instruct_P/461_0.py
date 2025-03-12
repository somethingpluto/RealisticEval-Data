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
,
 
O
p
t
i
o
n
a
l


f
r
o
m
 
c
o
l
l
e
c
t
i
o
n
s
 
i
m
p
o
r
t
 
d
e
q
u
e






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


 
 
 
 
"
"
"
D
e
f
i
n
i
t
i
o
n
 
f
o
r
 
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
 
n
o
d
e
.
"
"
"




 
 
 
 
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
 
O
p
t
i
o
n
a
l
[
T
r
e
e
N
o
d
e
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
 
n
o
d
e
s
 
a
t
 
e
a
c
h
 
l
e
v
e
l
 
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
O
p
t
i
o
n
a
l
[
T
r
e
e
N
o
d
e
]
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
 
o
f
 
a
v
e
r
a
g
e
s
 
f
o
r
 
e
a
c
h
 
l
e
v
e
l
 
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




 
 
 
 
a
v
e
r
a
g
e
s
 
=
 
[
]


 
 
 
 
q
u
e
u
e
 
=
 
d
e
q
u
e
(
[
r
o
o
t
]
)




 
 
 
 
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


 
 
 
 
 
 
 
 
l
e
v
e
l
_
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


 
 
 
 
 
 
 
 
l
e
v
e
l
_
s
u
m
 
=
 
0
.
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
l
e
v
e
l
_
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
l
e
f
t
(
)


 
 
 
 
 
 
 
 
 
 
 
 
l
e
v
e
l
_
s
u
m
 
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


 
 
 
 
 
 
 
 
a
v
e
r
a
g
e
s
.
a
p
p
e
n
d
(
l
e
v
e
l
_
s
u
m
 
/
 
l
e
v
e
l
_
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
 
a
v
e
r
a
g
e
s






d
e
f
 
i
s
_
s
y
m
m
e
t
r
i
c
(
r
o
o
t
:
 
O
p
t
i
o
n
a
l
[
T
r
e
e
N
o
d
e
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
 
i
s
 
a
 
m
i
r
r
o
r
 
o
f
 
i
t
s
e
l
f
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
O
p
t
i
o
n
a
l
[
T
r
e
e
N
o
d
e
]
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
W
h
e
t
h
e
r
 
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
 
i
s
 
a
 
m
i
r
r
o
r
 
o
f
 
i
t
s
e
l
f
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
 
T
r
u
e




 
 
 
 
q
u
e
u
e
 
=
 
d
e
q
u
e
(
[
r
o
o
t
]
)




 
 
 
 
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


 
 
 
 
 
 
 
 
l
e
v
e
l
_
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


 
 
 
 
 
 
 
 
l
e
v
e
l
_
v
a
l
u
e
s
 
=
 
[
]


 
 
 
 
 
 
 
 
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
l
e
v
e
l
_
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
l
e
f
t
(
)


 
 
 
 
 
 
 
 
 
 
 
 
l
e
v
e
l
_
v
a
l
u
e
s
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
v
a
l
)


 
 
 
 
 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
i
f
 
l
e
v
e
l
_
v
a
l
u
e
s
 
!
=
 
l
e
v
e
l
_
v
a
l
u
e
s
[
:
:
-
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
i
s
_
s
u
b
t
r
e
e
(
s
:
 
O
p
t
i
o
n
a
l
[
T
r
e
e
N
o
d
e
import unittest


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestAverageOfLevels(unittest.TestCase):
    def test_empty_tree(self):
        """Test case for an empty tree."""
        self.assertEqual(average_of_levels(None), [])

    def test_single_node(self):
        """Test case for a tree with a single node."""
        root = TreeNode(5)
        self.assertEqual(average_of_levels(root), [5.0])

    def test_three_levels(self):
        """Test case for a tree with three levels."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(average_of_levels(root), [1.0, 2.5, 5.0])  # (1), (2, 3) -> [1.0, (2+3)/2], (4, 5, 6) -> [5.0]

if __name__ == '__main__':
    unittest.main()