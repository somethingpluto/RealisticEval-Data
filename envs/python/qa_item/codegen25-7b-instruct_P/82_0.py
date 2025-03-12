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
 
D
i
c
t
,
 
A
n
y




i
m
p
o
r
t
 
n
e
t
w
o
r
k
x
 
a
s
 
n
x






c
l
a
s
s
 
G
r
a
p
h
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
 
e
d
g
e
s
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
g
r
a
p
h
 
=
 
n
x
.
D
i
G
r
a
p
h
(
e
d
g
e
s
)




 
 
 
 
d
e
f
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
(
s
e
l
f
,
 
f
i
l
t
e
r
_
r
e
p
e
a
t
_
n
o
d
e
s
=
T
r
u
e
)
 
-
>
 
D
i
c
t
[
A
n
y
,
 
L
i
s
t
]
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
F
i
n
d
s
 
a
l
l
 
u
n
i
q
u
e
 
c
y
c
l
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
 
t
h
a
t
 
a
r
e
 
l
a
r
g
e
r
 
t
h
a
n
 
s
i
z
e
 
2
,
 
o
p
t
i
o
n
a
l
l
y
 
f
i
l
t
e
r
i
n
g
 
o
u
t
 
c
y
c
l
e
s
 
w
i
t
h
 
r
e
p
e
a
t
e
d
 
n
o
d
e
s
.




 
 
 
 
 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
_
r
e
p
e
a
t
_
n
o
d
e
s
 
(
b
o
o
l
)
:
 
I
f
 
T
r
u
e
,
 
f
i
l
t
e
r
s
 
o
u
t
 
c
y
c
l
e
s
 
w
h
e
r
e
 
a
n
y
 
n
o
d
e
 
a
p
p
e
a
r
s
 
m
o
r
e
 
t
h
a
n
 
o
n
c
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


 
 
 
 
 
 
 
 
 
 
 
 
D
i
c
t
[
i
n
t
,
 
L
i
s
t
[
n
x
.
G
r
a
p
h
]
]
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
 
m
a
p
p
i
n
g
 
e
a
c
h
 
c
y
c
l
e
 
s
i
z
e
 
t
o
 
a
 
l
i
s
t
 
o
f
 
s
u
b
g
r
a
p
h
 
o
b
j
e
c
t
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
a
c
h
 
u
n
i
q
u
e
 
c
y
c
l
e
 
o
f
 
t
h
a
t
 
s
i
z
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
c
y
c
l
e
s
 
=
 
n
x
.
s
i
m
p
l
e
_
c
y
c
l
e
s
(
s
e
l
f
.
g
r
a
p
h
)


 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
 
=
 
{
}


 
 
 
 
 
 
 
 
f
o
r
 
c
y
c
l
e
 
i
n
 
c
y
c
l
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
f
i
l
t
e
r
_
r
e
p
e
a
t
_
n
o
d
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
s
e
t
(
c
y
c
l
e
)
)
 
=
=
 
l
e
n
(
c
y
c
l
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
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
c
y
c
l
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
y
c
l
e
_
s
i
z
e
 
n
o
t
 
i
n
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
[
c
y
c
l
e
_
s
i
z
e
]
 
=
 
[
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
[
c
y
c
l
e
_
s
i
z
e
]
.
a
p
p
e
n
d
(
c
y
c
l
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
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
c
y
c
l
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
y
c
l
e
_
s
i
z
e
 
n
o
t
 
i
n
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
[
c
y
c
l
e
_
s
i
z
e
]
 
=
 
[
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
[
c
y
c
l
e
_
s
i
z
e
]
.
a
p
p
e
n
d
(
c
y
c
l
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e




 
 
 
 
d
e
f
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
_
w
i
t
h
_
r
e
p
e
a
t
e
d
_
n
o
d
e
s
(
s
e
l
f
)
 
-
>
 
D
i
c
t
[
A
n
y
,
 
L
i
s
t
]
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
F
i
n
d
s
 
a
l
l
 
u
n
i
q
u
e
 
c
y
c
l
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
 
t
h
a
t
 
a
r
e
 
l
a
r
g
e
r
 
t
h
a
n
 
s
i
z
e
 
2
,
 
i
n
c
l
u
d
i
n
g
 
c
y
c
l
e
s
 
w
i
t
h
 
r
e
p
e
a
t
e
d
 
n
o
d
e
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


 
 
 
 
 
 
 
 
 
 
 
 
D
i
c
t
[
i
n
t
,
 
L
i
s
t
[
n
x
.
G
r
a
p
h
]
]
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
 
m
a
p
p
i
n
g
 
e
a
c
h
 
c
y
c
l
e
 
s
i
z
e
 
t
o
 
a
 
l
i
s
t
 
o
f
 
s
u
b
g
r
a
p
h
 
o
b
j
e
c
t
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
a
c
h
 
u
n
i
q
u
e
 
c
y
c
l
e
 
o
f
 
t
h
a
t
 
s
i
z
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
c
y
c
l
e
s
 
=
 
n
x
.
s
i
m
p
l
e
_
c
y
c
l
e
s
(
s
e
l
f
.
g
r
a
p
h
)


 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
 
=
 
{
}


 
 
 
 
 
 
 
 
f
o
r
 
c
y
c
l
e
 
i
n
 
c
y
c
l
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
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
c
y
c
l
e
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
y
c
l
e
_
s
i
z
e
 
n
o
t
 
i
n
 
c
y
c
l
e
s
_
b
y
_
s
i
z
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
y
c
l
e
s
_
b
y
import unittest
from collections import defaultdict


class TestGraphCycles(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph([])
        self.assertEqual(g.cycles_by_size(), defaultdict(list),
                         "Failed: Expected an empty defaultdict for an empty graph.")

    def test_graph_no_cycles(self):
        g = Graph([(1, 2), (2, 3)])
        self.assertEqual(g.cycles_by_size(), defaultdict(list),
                         "Failed: Expected an empty defaultdict for a graph with no cycles.")

    def test_simple_cycles(self):
        g = Graph([(1, 2), (2, 3), (3, 1)])
        results = g.cycles_by_size()
        self.assertEqual(len(results[3]), 1, "Failed: Expected one cycle of length 3.")
        self.assertIn(list(results[3][0].nodes()), [[1, 2, 3]], "Failed: Expected cycle nodes to match.")

    def test_multiple_cycles(self):
        g = Graph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1)])
        results = g.cycles_by_size()
        self.assertEqual(len(results[3]), 1, "Failed: Expected one cycle of length 3.")
        self.assertEqual(len(results[4]), 1, "Failed: Expected one cycle of length 4.")

if __name__ == '__main__':
    unittest.main()