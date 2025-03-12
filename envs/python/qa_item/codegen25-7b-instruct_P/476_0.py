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
 
T
u
p
l
e






d
e
f
 
t
o
p
o
l
o
g
i
c
a
l
_
s
o
r
t
_
d
f
s
(
v
e
r
t
i
c
e
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
,
 
e
d
g
e
s
:
 
L
i
s
t
[
T
u
p
l
e
]
)
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
a
c
h
i
e
v
e
 
t
o
p
o
l
o
g
i
c
a
l
 
s
o
r
t
i
n
g
,
 
b
a
s
e
d
 
o
n
 
d
e
p
t
h
 
p
r
i
o
r
i
t
y
 
s
e
a
r
c
h




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
r
t
i
c
e
s
 
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
 
A
 
l
i
s
t
 
o
f
 
v
e
r
t
i
c
e
s
 
i
n
 
t
h
e
 
g
r
a
p
h
.
 
E
a
c
h
 
v
e
r
t
e
x
 
s
h
o
u
l
d
 
b
e
 
a
 
u
n
i
q
u
e
 
i
n
t
e
g
e
r
.


 
 
 
 
 
 
 
 
e
d
g
e
s
 
(
L
i
s
t
[
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
]
)
:
 
A
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
 
w
h
e
r
e
 
e
a
c
h
 
t
u
p
l
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
s
 
a
 
d
i
r
e
c
t
e
d
 
e
d
g
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
g
r
a
p
h
 
a
n
d
 
i
s
 
f
o
r
m
e
d
 
a
s
 
(
s
t
a
r
t
_
v
e
r
t
e
x
,
 
e
n
d
_
v
e
r
t
e
x
)
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
 
v
e
r
t
i
c
e
s
 
i
n
 
t
o
p
o
l
o
g
i
c
a
l
 
o
r
d
e
r
.
 
I
f
 
t
h
e
 
g
r
a
p
h
 
c
o
n
t
a
i
n
s
 
a
 
c
y
c
l
e
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
t
h
u
s
 
c
a
n
n
o
t
 
h
a
v
e
 
a
 
v
a
l
i
d
 
t
o
p
o
l
o
g
i
c
a
l
 
o
r
d
e
r
i
n
g
,
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
i
s
 
r
e
t
u
r
n
e
d
.


 
 
 
 
"
"
"


 
 
 
 
#
 
i
n
i
t
i
a
l
i
z
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
s
t
o
r
e
 
t
h
e
 
i
n
-
d
e
g
r
e
e
 
o
f
 
e
a
c
h
 
v
e
r
t
e
x


 
 
 
 
i
n
_
d
e
g
r
e
e
 
=
 
{
v
e
r
t
e
x
:
 
0
 
f
o
r
 
v
e
r
t
e
x
 
i
n
 
v
e
r
t
i
c
e
s
}


 
 
 
 
#
 
i
n
i
t
i
a
l
i
z
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
s
t
o
r
e
 
t
h
e
 
a
d
j
a
c
e
n
c
y
 
l
i
s
t
 
o
f
 
e
a
c
h
 
v
e
r
t
e
x


 
 
 
 
a
d
j
a
c
e
n
c
y
_
l
i
s
t
 
=
 
{
v
e
r
t
e
x
:
 
[
]
 
f
o
r
 
v
e
r
t
e
x
 
i
n
 
v
e
r
t
i
c
e
s
}


 
 
 
 
#
 
p
o
p
u
l
a
t
e
 
t
h
e
 
a
d
j
a
c
e
n
c
y
 
l
i
s
t
 
a
n
d
 
i
n
-
d
e
g
r
e
e
 
d
i
c
t
i
o
n
a
r
y


 
 
 
 
f
o
r
 
s
t
a
r
t
_
v
e
r
t
e
x
,
 
e
n
d
_
v
e
r
t
e
x
 
i
n
 
e
d
g
e
s
:


 
 
 
 
 
 
 
 
i
n
_
d
e
g
r
e
e
[
e
n
d
_
v
e
r
t
e
x
]
 
+
=
 
1


 
 
 
 
 
 
 
 
a
d
j
a
c
e
n
c
y
_
l
i
s
t
[
s
t
a
r
t
_
v
e
r
t
e
x
]
.
a
p
p
e
n
d
(
e
n
d
_
v
e
r
t
e
x
)


 
 
 
 
#
 
i
n
i
t
i
a
l
i
z
e
 
a
 
s
t
a
c
k
 
t
o
 
s
t
o
r
e
 
t
h
e
 
v
e
r
t
i
c
e
s
 
w
i
t
h
 
z
e
r
o
 
i
n
-
d
e
g
r
e
e


 
 
 
 
s
t
a
c
k
 
=
 
[
v
e
r
t
e
x
 
f
o
r
 
v
e
r
t
e
x
 
i
n
 
v
e
r
t
i
c
e
s
 
i
f
 
i
n
_
d
e
g
r
e
e
[
v
e
r
t
e
x
]
 
=
=
 
0
]


 
 
 
 
#
 
i
n
i
t
i
a
l
i
z
e
 
a
 
l
i
s
t
 
t
o
 
s
t
o
r
e
 
t
h
e
 
t
o
p
o
l
o
g
i
c
a
l
 
o
r
d
e
r


 
 
 
 
t
o
p
o
l
o
g
i
c
a
l
_
o
r
d
e
r
 
=
 
[
]


 
 
 
 
#
 
p
e
r
f
o
r
m
 
a
 
d
e
p
t
h
-
f
i
r
s
t
 
s
e
a
r
c
h


 
 
 
 
w
h
i
l
e
 
s
t
a
c
k
:


 
 
 
 
 
 
 
 
#
 
p
o
p
 
a
 
v
e
r
t
e
x
 
w
i
t
h
 
z
e
r
o
 
i
n
-
d
e
g
r
e
e
 
f
r
o
m
 
t
h
e
 
s
t
a
c
k


 
 
 
 
 
 
 
 
v
e
r
t
e
x
 
=
 
s
t
a
c
k
.
p
o
p
(
)


 
 
 
 
 
 
 
 
#
 
a
d
d
 
t
h
e
 
v
e
r
t
e
x
 
t
o
 
t
h
e
 
t
o
p
o
l
o
g
i
c
a
l
 
o
r
d
e
r


 
 
 
 
 
 
 
 
t
o
p
o
l
o
g
i
c
a
l
_
o
r
d
e
r
.
a
p
p
e
n
d
(
v
e
r
t
e
x
)


 
 
 
 
 
 
 
 
#
 
i
t
e
r
a
t
e
 
t
h
r
o
u
g
h
 
t
h
e
 
a
d
j
a
c
e
n
c
y
 
l
i
s
t
 
o
f
 
t
h
e
 
v
e
r
t
e
x


 
 
 
 
 
 
 
 
f
o
r
 
n
e
i
g
h
b
o
r
 
i
n
 
a
d
j
a
c
e
n
c
y
_
l
i
s
t
[
v
e
r
t
e
x
]
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
r
e
d
u
c
e
 
t
h
e
 
i
n
-
d
e
g
r
e
e
 
o
f
 
t
h
e
 
n
e
i
g
h
b
o
r
 
b
y
 
1


 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
d
e
g
r
e
e
[
n
e
i
g
h
b
o
r
]
 
-
=
 
1


 
 
 
 
 
 
 
 
 
 
 
 
#
 
i
f
 
t
h
e
 
n
e
i
g
h
b
o
r
 
h
a
s
 
z
e
r
o
 
i
n
-
d
e
g
r
e
e
,
 
a
d
d
 
i
t
 
t
o
 
t
h
e
 
s
t
a
c
k


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
i
n
_
d
e
g
r
e
e
[
n
e
i
g
h
b
o
r
]
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
c
k
.
import unittest


class TestTopologicalSortDFS(unittest.TestCase):
    def test_simple_chain(self):
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3)]
        self.assertEqual(topological_sort_dfs(vertices, edges), [1, 2, 3])


    def test_disconnected_graph(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2)]
        # There are multiple correct answers possible
        result = topological_sort_dfs(vertices, edges)
        self.assertTrue(result.index(1) < result.index(2))
        self.assertTrue(3 in result and 4 in result)

    def test_complex_graph(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (6, 1)]
        result = topological_sort_dfs(vertices, edges)
        self.assertTrue(result.index(1) < result.index(2))
        self.assertTrue(result.index(1) < result.index(3))
        self.assertTrue(result.index(2) < result.index(4))
        self.assertTrue(result.index(3) < result.index(4))
        self.assertTrue(result.index(4) < result.index(5))
        self.assertTrue(result.index(6) < result.index(1))

    def test_single_vertex(self):
        vertices = [1]
        edges = []
        self.assertEqual(topological_sort_dfs(vertices, edges), [1])
if __name__ == '__main__':
    unittest.main()