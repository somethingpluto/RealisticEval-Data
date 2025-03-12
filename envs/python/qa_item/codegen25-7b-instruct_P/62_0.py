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
 
k
e
y
)
:


 
 
 
 
 
 
 
 
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
 
N
o
n
e


 
 
 
 
 
 
 
 
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
 
N
o
n
e


 
 
 
 
 
 
 
 
s
e
l
f
.
v
a
l
 
=
 
k
e
y






c
l
a
s
s
 
B
i
n
a
r
y
T
r
e
e
:


 
 
 
 
"
"
"


 
 
 
 
i
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
e
 
t
r
e
e
 
i
n
 
t
h
e
 
q
u
e
s
t
i
o
n
 
s
t
r
u
c
t
u
r
e
 
a
n
d
 
i
m
p
l
e
m
e
n
t
 
i
t
s
 
t
h
r
e
e
 
t
r
a
v
e
r
s
a
l
 
m
e
t
h
o
d
s


 
 
 
 
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
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
r
o
o
t
 
=
 
N
o
n
e




 
 
 
 
d
e
f
 
i
n
s
e
r
t
(
s
e
l
f
,
 
k
e
y
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
_
i
n
s
e
r
t
(
s
e
l
f
,
 
n
o
d
e
,
 
k
e
y
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
i
n
o
r
d
e
r
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
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
_
i
n
o
r
d
e
r
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
 
n
o
d
e
,
 
r
e
s
u
l
t
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
p
r
e
o
r
d
e
r
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
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
_
p
r
e
o
r
d
e
r
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
 
n
o
d
e
,
 
r
e
s
u
l
t
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
p
o
s
t
o
r
d
e
r
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
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
_
p
o
s
t
o
r
d
e
r
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
 
n
o
d
e
,
 
r
e
s
u
l
t
)
:


 
 
 
 
 
 
 
 
p
a
s
s


import unittest


class TestBinaryTree(unittest.TestCase):

    def test_empty_tree(self):
        bt = BinaryTree()
        self.assertEqual(bt.inorder_traversal(), [])
        self.assertEqual(bt.preorder_traversal(), [])
        self.assertEqual(bt.postorder_traversal(), [])

    def test_single_node_tree(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [10])
        self.assertEqual(bt.preorder_traversal(), [10])
        self.assertEqual(bt.postorder_traversal(), [10])

    def test_balanced_tree(self):
        bt = BinaryTree()
        elements = [8, 3, 10, 1, 6, 9, 14]
        for elem in elements:
            bt.insert(elem)
        self.assertEqual(bt.inorder_traversal(), [1, 3, 6, 8, 9, 10, 14])
        self.assertEqual(bt.preorder_traversal(), [8, 3, 1, 6, 10, 9, 14])
        self.assertEqual(bt.postorder_traversal(), [1, 6, 3, 9, 14, 10, 8])

    def test_left_heavy_tree(self):
        bt = BinaryTree()
        for i in range(10, 0, -1):  # Inserts 10, 9, ..., 1
            bt.insert(i)
        self.assertEqual(bt.inorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.preorder_traversal(), [10-i for i in range(10)])
        self.assertEqual(bt.postorder_traversal(), [i for i in range(1, 11)])

    def test_right_heavy_tree(self):
        bt = BinaryTree()
        for i in range(1, 11):  # Inserts 1, 2, ..., 10
            bt.insert(i)
        self.assertEqual(bt.inorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.preorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.postorder_traversal(), [i for i in range(10, 0, -1)])
if __name__ == '__main__':
    unittest.main()