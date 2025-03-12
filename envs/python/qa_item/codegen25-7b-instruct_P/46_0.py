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
u
e
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


 
 
 
 
 
 
 
 
p
a
s
s






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
 
r
o
o
t
=
N
o
n
e
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
=
N
o
n
e
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
=
N
o
n
e
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
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
p
a
s
s


import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """Setup basic tree structure for testing."""
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \
        #  4   5
        self.tree = BinaryTree(TreeNode(1))
        self.tree.root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        self.tree.root.right = TreeNode(3)

    def test_preorder_traversal(self):
        """Test preorder traversal."""
        result = self.tree.preorder_traversal(self.tree.root)
        self.assertEqual(result, [1, 2, 4, 5, 3])

    def test_inorder_traversal(self):
        """Test inorder traversal."""
        result = self.tree.inorder_traversal(self.tree.root)
        self.assertEqual(result, [4, 2, 5, 1, 3])

    def test_postorder_traversal(self):
        """Test postorder traversal."""
        result = self.tree.postorder_traversal(self.tree.root)
        self.assertEqual(result, [4, 5, 2, 3, 1])

    def test_empty_tree(self):
        """Test traversals on an empty tree."""
        empty_tree = BinaryTree()
        self.assertEqual(empty_tree.preorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.inorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.postorder_traversal(empty_tree.root), [])

    def test_single_node_tree(self):
        """Test all traversals on a tree with only one node."""
        single_node_tree = BinaryTree(TreeNode(10))
        self.assertEqual(single_node_tree.preorder_traversal(single_node_tree.root), [10])
        self.assertEqual(single_node_tree.inorder_traversal(single_node_tree.root), [10])
        self.assertEqual(single_node_tree.postorder_traversal(single_node_tree.root), [10])

if __name__ == '__main__':
    unittest.main()