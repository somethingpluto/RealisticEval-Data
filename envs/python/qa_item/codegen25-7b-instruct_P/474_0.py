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
 
a
r
e
_
s
i
b
l
i
n
g
s
(
t
r
e
e
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
,
 
v
a
l
1
:
i
n
t
,
 
v
a
l
2
:
i
n
t
)
:


 
 
 
 
"
"
"


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
i
f
 
t
w
o
 
v
a
l
u
e
s
 
a
r
e
 
s
i
b
l
i
n
g
s
 
i
n
 
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
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
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


 
 
 
 
 
 
 
 
t
r
e
e
(
L
i
s
t
[
i
n
t
]
)
:
 
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
 
l
e
v
e
l
-
o
r
d
e
r
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n


 
 
 
 
 
 
 
 
v
a
l
1
(
i
n
t
)
:


 
 
 
 
 
 
 
 
v
a
l
2
(
i
n
t
)
:




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"




 
 
 
 
"
"
"


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
i
f
 
t
w
o
 
v
a
l
u
e
s
 
a
r
e
 
s
i
b
l
i
n
g
s
 
i
n
 
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
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
a
n
 
a
r
r
a
y
.




 
 
 
 
:
p
a
r
a
m
 
t
r
e
e
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
,
 
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
 
l
e
v
e
l
-
o
r
d
e
r
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n


 
 
 
 
:
p
a
r
a
m
 
v
a
l
1
:
 
i
n
t
,
 
f
i
r
s
t
 
v
a
l
u
e
 
t
o
 
c
h
e
c
k
 
f
o
r
 
s
i
b
l
i
n
g
 
r
e
l
a
t
i
o
n
s
h
i
p


 
 
 
 
:
p
a
r
a
m
 
v
a
l
2
:
 
i
n
t
,
 
s
e
c
o
n
d
 
v
a
l
u
e
 
t
o
 
c
h
e
c
k
 
f
o
r
 
s
i
b
l
i
n
g
 
r
e
l
a
t
i
o
n
s
h
i
p


 
 
 
 
:
r
e
t
u
r
n
:
 
b
o
o
l
,
 
T
r
u
e
 
i
f
 
v
a
l
1
 
a
n
d
 
v
a
l
2
 
a
r
e
 
s
i
b
l
i
n
g
s
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e


 
 
 
 
"
"
"




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
r
e
e
 
i
s
 
e
m
p
t
y


 
 
 
 
i
f
 
n
o
t
 
t
r
e
e
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




 
 
 
 
#
 
G
e
t
 
t
h
e
 
r
o
o
t
 
n
o
d
e


 
 
 
 
r
o
o
t
 
=
 
t
r
e
e
[
0
]




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
q
u
e
u
e
 
w
i
t
h
 
t
h
e
 
r
o
o
t
 
n
o
d
e


 
 
 
 
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




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
v
i
s
i
t
e
d
 
s
e
t


 
 
 
 
v
i
s
i
t
e
d
 
=
 
s
e
t
(
)




 
 
 
 
#
 
I
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
q
u
e
u
e


 
 
 
 
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




 
 
 
 
 
 
 
 
#
 
G
e
t
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e


 
 
 
 
 
 
 
 
c
u
r
r
 
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




 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
i
s
 
v
a
l
1
 
o
r
 
v
a
l
2


 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
 
=
=
 
v
a
l
1
 
o
r
 
c
u
r
r
 
=
=
 
v
a
l
2
:




 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
i
s
 
n
o
t
 
i
n
 
t
h
e
 
v
i
s
i
t
e
d
 
s
e
t


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
 
n
o
t
 
i
n
 
v
i
s
i
t
e
d
:




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
t
o
 
t
h
e
 
v
i
s
i
t
e
d
 
s
e
t


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
i
s
i
t
e
d
.
a
d
d
(
c
u
r
r
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
h
a
s
 
a
 
l
e
f
t
 
c
h
i
l
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
t
r
e
e
)
 
>
 
1
 
a
n
d
 
t
r
e
e
[
1
]
 
i
s
 
n
o
t
 
N
o
n
e
:




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
l
e
f
t
 
c
h
i
l
d
 
t
o
 
t
h
e
 
q
u
e
u
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
t
r
e
e
[
1
]
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
h
a
s
 
a
 
r
i
g
h
t
 
c
h
i
l
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
t
r
e
e
)
 
>
 
2
 
a
n
d
 
t
r
e
e
[
2
]
 
i
s
 
n
o
t
 
N
o
n
e
:




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
r
i
g
h
t
 
c
h
i
l
d
 
t
o
 
t
h
e
 
q
u
e
u
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
t
r
e
e
[
2
]
)




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
i
s
 
v
a
l
1


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
 
=
=
 
v
a
l
1
:




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
s
i
b
l
i
n
g
 
o
f
 
t
h
e
 
c
u
r
r
e
n
t
 
n
o
d
e
 
i
s
 
v
a
l
2


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
t
r
e
e
[
2
]
 
=
=
 
v
a
l
2
:




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
R
e
t
u
r
n
 
T
r
u
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




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
import unittest

class TestAreSiblings(unittest.TestCase):
    def setUp(self):
        # Setting up a binary tree used for all the test cases
        self.tree = [1, 2, 3, 4, 5, 6, 7]

    def test_basic_case(self):
        # Test with nodes 4 and 5, which are siblings
        result = are_siblings(self.tree, 4, 5)
        self.assertTrue(result)

    def test_non_sibling_case(self):
        # Test with nodes 4 and 6, which are not siblings
        result = are_siblings(self.tree, 4, 6)
        self.assertFalse(result)

    def test_root_node_case(self):
        # Test with node 1 (root) and any other node, should return False
        result = are_siblings(self.tree, 1, 2)
        self.assertFalse(result)

    def test_non_existent_values(self):
        # Test with non-existent values
        result = are_siblings(self.tree, 8, 9)
        self.assertFalse(result)

    def test_same_node_case(self):
        # Test with the same node for both values
        result = are_siblings(self.tree, 4, 4)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()