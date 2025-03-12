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
 
U
n
i
o
n




d
e
f
 
f
i
n
d
_
s
h
o
r
t
e
s
t
_
p
a
t
h
s
_
b
y
_
f
l
o
y
d
_
w
a
r
s
h
a
l
l
(
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
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
 
F
l
o
y
d
-
W
a
r
s
h
a
l
l
 
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
s
 
b
e
t
w
e
e
n
 
a
l
l
 
p
a
i
r
s
 
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
 
a
 
g
r
a
p
h
 
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
 
b
y
 
a
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
)
:
 
T
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
 
m
a
t
r
i
x
 
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
 
g
r
a
p
h
,


 
 
 
 
 
 
 
 
w
h
e
r
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
_
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
 
i
s
 
t
h
e
 
w
e
i
g
h
t
 
o
f
 
t
h
e
 
e
d
g
e
 
f
r
o
m
 
v
e
r
t
e
x
 
i
 
t
o
 
v
e
r
t
e
x
 
j
.
 
I
f
 
t
h
e
r
e
 
i
s


 
 
 
 
 
 
 
 
n
o
 
e
d
g
e
,
 
t
h
e
 
w
e
i
g
h
t
 
s
h
o
u
l
d
 
b
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
:
 
T
h
e
 
m
a
t
r
i
x
 
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
 
b
e
t
w
e
e
n
 
a
l
l
 
p
a
i
r
s
 
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
.


 
 
 
 
 
 
 
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
i
]
[
j
]
 
w
i
l
l
 
h
o
l
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
 
v
e
r
t
e
x
 
i
 
t
o
 
v
e
r
t
e
x
 
j
.


 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
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
m
a
t
r
i
x
)


 
 
 
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
 
=
 
[
[
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
 
_
 
i
n
 
r
a
n
g
e
(
n
)
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
n
)
]


 
 
 
 
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
n
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
n
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
i
]
[
j
]
 
=
 
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


 
 
 
 
f
o
r
 
k
 
i
n
 
r
a
n
g
e
(
n
)
:


 
 
 
 
 
 
 
 
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
n
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
n
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
i
]
[
j
]
 
=
 
m
i
n
(
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
i
]
[
j
]
,
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
i
]
[
k
]
 
+
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s
[
k
]
[
j
]
)


 
 
 
 
r
e
t
u
r
n
 
s
h
o
r
t
e
s
t
_
p
a
t
h
s




d
e
f
 
f
i
n
d
_
s
h
o
r
t
e
s
t
_
p
a
t
h
s
_
b
y
_
d
i
j
k
s
t
r
a
(
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
,
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
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
s
 
b
e
t
w
e
e
n
 
a
l
l
 
p
a
i
r
s
 
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
 
a
 
g
r
a
p
h
 
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
 
b
y
 
a
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
]
)
:
 
T
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
 
m
a
t
r
i
x
 
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
 
g
r
a
p
h
import unittest

class TestFloydWarshallShortestPaths(unittest.TestCase):
    def test_basic_functionality(self):
        # Basic test.js case with a simple graph
        matrix = [
            [0, 3, float('inf'), 7],
            [8, 0, 2, float('inf')],
            [5, float('inf'), 0, 1],
            [2, float('inf'), float('inf'), 0]
        ]
        expected = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Basic functionality test.js failed")

    def test_single_vertex_graph(self):
        # Test case with a single vertex graph (1x1 matrix)
        matrix = [
            [0]
        ]
        expected = [
            [0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Single vertex graph test.js failed")

    def test_two_vertices_graph(self):
        # Test case with two vertices
        matrix = [
            [0, 1],
            [1, 0]
        ]
        expected = [
            [0, 1],
            [1, 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Two vertices graph test.js failed")

    def test_large_infinite_weights(self):
        # Test case with infinite weights
        matrix = [
            [0, float('inf')],
            [float('inf'), 0]
        ]
        expected = [
            [0, float('inf')],
            [float('inf'), 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Large infinite weights test.js failed")

    def test_negative_cycle(self):
        # Test case with a negative cycle
        matrix = [
            [0, 1, float('inf')],
            [float('inf'), 0, -1],
            [-1, float('inf'), 0]
        ]
        expected = [
            [-1, 0, -1],
            [-2, -1, -2],
            [-2, -1, -2]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Negative cycle test.js failed")



if __name__ == '__main__':
    unittest.main()