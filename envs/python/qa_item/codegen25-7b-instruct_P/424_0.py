i
m
p
o
r
t
 
h
e
a
p
q


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
 
D
i
c
t






d
e
f
 
d
i
j
k
s
t
r
a
(
g
r
a
p
h
:
 
D
i
c
t
,
 
s
t
a
r
t
:
 
s
t
r
)
 
-
>
 
D
i
c
t
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
s
 
D
i
j
k
s
t
r
a
'
s
 
a
l
g
o
r
i
t
h
m
 
t
o
 
f
i
n
d
 
t
h
e
 
s
h
o
r
t
e
s
t
 
p
a
t
h
 
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
r
t
 
n
o
d
e
 
t
o
 
a
l
l
 
o
t
h
e
r
 
n
o
d
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


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
g
r
a
p
h
(
D
i
c
t
)
:
 
A
 
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
 
k
e
y
 
i
s
 
a
 
n
o
d
e
,
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
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
 
(
n
e
i
g
h
b
o
r
,
 
w
e
i
g
h
t
)
.


 
 
 
 
 
 
 
 
s
t
a
r
t
(
s
t
r
)
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
n
o
d
e
 
f
o
r
 
t
h
e
 
s
h
o
r
t
e
s
t
 
p
a
t
h
 
s
e
a
r
c
h
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
D
i
c
t
:
 
A
 
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
 
w
i
t
h
 
t
h
e
 
s
h
o
r
t
e
s
t
 
d
i
s
t
a
n
c
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
r
t
 
n
o
d
e
 
t
o
 
e
a
c
h
 
n
o
d
e
.


 
 
 
 
"
"
"


 
 
 
 
d
i
s
t
a
n
c
e
s
 
=
 
{
n
o
d
e
:
 
f
l
o
a
t
(
'
i
n
f
'
)
 
f
o
r
 
n
o
d
e
 
i
n
 
g
r
a
p
h
}


 
 
 
 
d
i
s
t
a
n
c
e
s
[
s
t
a
r
t
]
 
=
 
0


 
 
 
 
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


 
 
 
 
u
n
v
i
s
i
t
e
d
 
=
 
[
(
0
,
 
s
t
a
r
t
)
]




 
 
 
 
w
h
i
l
e
 
u
n
v
i
s
i
t
e
d
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
d
i
s
t
a
n
c
e
,
 
c
u
r
r
e
n
t
_
n
o
d
e
 
=
 
h
e
a
p
q
.
h
e
a
p
p
o
p
(
u
n
v
i
s
i
t
e
d
)


 
 
 
 
 
 
 
 
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
e
n
t
_
n
o
d
e
)




 
 
 
 
 
 
 
 
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
,
 
w
e
i
g
h
t
 
i
n
 
g
r
a
p
h
[
c
u
r
r
e
n
t
_
n
o
d
e
]
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
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
 
v
i
s
i
t
e
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e




 
 
 
 
 
 
 
 
 
 
 
 
n
e
w
_
d
i
s
t
a
n
c
e
 
=
 
c
u
r
r
e
n
t
_
d
i
s
t
a
n
c
e
 
+
 
w
e
i
g
h
t




 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
e
w
_
d
i
s
t
a
n
c
e
 
<
 
d
i
s
t
a
n
c
e
s
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
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
s
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
 
n
e
w
_
d
i
s
t
a
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
h
e
a
p
q
.
h
e
a
p
p
u
s
h
(
u
n
v
i
s
i
t
e
d
,
 
(
n
e
w
_
d
i
s
t
a
n
c
e
,
 
n
e
i
g
h
b
o
r
)
)




 
 
 
 
r
e
t
u
r
n
 
d
i
s
t
a
n
c
e
s






d
e
f
 
d
i
j
k
s
t
r
a
_
w
i
t
h
_
p
a
t
h
(
g
r
a
p
h
:
 
D
i
c
t
,
 
s
t
a
r
t
:
 
s
t
r
)
 
-
>
 
D
i
c
t
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
s
 
D
i
j
k
s
t
r
a
'
s
 
a
l
g
o
r
i
t
h
m
 
t
o
 
f
i
n
d
 
t
h
e
 
s
h
o
r
t
e
s
t
 
p
a
t
h
 
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
r
t
 
n
o
d
e
 
t
o
 
a
l
l
 
o
t
h
e
r
 
n
o
d
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


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
g
r
a
p
h
(
D
i
c
t
)
:
 
A
 
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
 
k
e
y
 
i
s
 
a
 
n
o
d
e
,
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
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
 
(
n
e
i
g
h
b
o
r
,
 
w
e
i
g
h
t
)
.


 
 
 
 
 
 
 
 
s
t
a
r
t
(
s
t
r
)
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
n
o
d
e
 
f
o
r
 
t
h
e
 
s
h
o
r
t
e
s
t
 
p
a
t
h
 
s
e
a
r
c
h
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
D
i
c
t
:
 
A
 
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
 
w
i
t
h
 
t
h
e
 
s
h
o
r
t
e
s
t
 
d
i
s
t
a
n
c
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
r
t
 
n
o
d
e
 
t
o
 
e
a
c
h
 
n
o
d
e
,
 
a
n
d
 
t
h
e
 
p
a
t
h
 
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
r
t
 
n
o
d
e
 
t
o
 
e
a
c
h
 
n
o
d
e
.


 
 
 
 
"
"
"


 
 
 
 
d
i
s
t
a
n
c
e
s
 
=
 
{
n
o
d
e
:
 
f
l
o
a
t
(
'
i
n
f
'
)
 
f
o
r
 
n
o
d
e
 
i
n
 
g
r
a
p
h
}


 
 
 
 
d
i
s
t
a
n
c
e
s
[
s
t
a
r
t
]
 
=
 
0


 
 
 
 
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


 
 
 
 
u
n
v
i
s
i
t
e
d
 
=
 
[
(
0
,
 
s
t
a
r
t
)
]




 
 
 
 
p
a
t
h
s
 
=
 
{
n
o
d
e
:
 
[
]
 
f
o
r
import unittest

class TestDijkstraAlgorithm(unittest.TestCase):

    def setUp(self):
        # Sample graphs for testing
        self.graph1 = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)],
        }

        self.graph2 = {
            'A': [('B', 2)],
            'B': [('A', 2), ('C', 3)],
            'C': [('B', 3), ('D', 1)],
            'D': [('C', 1)],
        }

        self.graph_with_isolated_node = {
            'A': [('B', 1)],
            'B': [('A', 1)],
            'C': [],  # Isolated node
        }

        self.graph_with_negative_weight = {
            'A': [('B', 2), ('C', 1)],
            'B': [('D', 3)],
            'C': [('B', -1), ('D', 4)],
            'D': [],
        }

    def test_shortest_paths_graph1(self):
        """Test shortest paths in a normal graph."""
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
        result = dijkstra(self.graph1, 'A')
        self.assertEqual(result, expected)

    def test_shortest_paths_graph2(self):
        """Test shortest paths in a different normal graph."""
        expected = {'A': 0, 'B': 2, 'C': 5, 'D': 6}
        result = dijkstra(self.graph2, 'A')
        self.assertEqual(result, expected)

    def test_shortest_paths_with_isolated_node(self):
        """Test shortest paths with an isolated node."""
        expected = {'A': 0, 'B': 1, 'C': float('inf')}
        result = dijkstra(self.graph_with_isolated_node, 'A')
        self.assertEqual(result, expected)


    def test_starting_at_isolated_node(self):
        """Test when starting at an isolated node."""
        expected = {'C': 0, 'A': float('inf'), 'B': float('inf')}
        result = dijkstra(self.graph_with_isolated_node, 'C')
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()