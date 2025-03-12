d
e
f
 
c
a
l
c
u
l
a
t
e
_
d
i
s
t
a
n
c
e
(
a
g
e
n
t
1
:
 
s
t
r
,
 
a
g
e
n
t
2
:
 
s
t
r
,
 
o
b
s
e
r
v
a
t
i
o
n
s
:
 
d
i
c
t
)
 
-
>
 
f
l
o
a
t
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
s
 
t
h
e
 
E
u
c
l
i
d
e
a
n
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
a
g
e
n
t
s
 
b
a
s
e
d
 
o
n
 
t
h
e
i
r
 
c
o
o
r
d
i
n
a
t
e
s
 
i
n
 
t
h
e
 
o
b
s
e
r
v
a
t
i
o
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
g
e
n
t
1
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
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
 
o
f
 
a
g
e
n
t
1
'
s
 
i
d
e
n
t
i
f
i
e
r
.


 
 
 
 
 
 
 
 
a
g
e
n
t
2
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
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
 
o
f
 
a
g
e
n
t
2
'
s
 
i
d
e
n
t
i
f
i
e
r
.


 
 
 
 
 
 
 
 
o
b
s
e
r
v
a
t
i
o
n
s
 
(
d
i
c
t
)
:
 
D
i
c
t
i
o
n
a
r
y
 
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
 
o
b
s
e
r
v
a
t
i
o
n
 
q
u
e
s
t
i
o
n
 
w
i
t
h
 
a
g
e
n
t
 
i
d
e
n
t
i
f
i
e
r
s
 
a
s
 
k
e
y
s
.
E
a
c
h
 
v
a
l
u
e
 
i
s
 
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
 
w
i
t
h
 
'
x
'
 
a
n
d
 
'
y
'
 
k
e
y
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
 
c
o
o
r
d
i
n
a
t
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
E
u
c
l
i
d
e
a
n
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
t
w
o
 
a
g
e
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
a
g
e
n
t
1
_
c
o
o
r
d
i
n
a
t
e
s
 
=
 
o
b
s
e
r
v
a
t
i
o
n
s
[
a
g
e
n
t
1
]


 
 
 
 
a
g
e
n
t
2
_
c
o
o
r
d
i
n
a
t
e
s
 
=
 
o
b
s
e
r
v
a
t
i
o
n
s
[
a
g
e
n
t
2
]


 
 
 
 
r
e
t
u
r
n
 
m
a
t
h
.
s
q
r
t
(


 
 
 
 
 
 
 
 
(
a
g
e
n
t
1
_
c
o
o
r
d
i
n
a
t
e
s
[
"
x
"
]
 
-
 
a
g
e
n
t
2
_
c
o
o
r
d
i
n
a
t
e
s
[
"
x
"
]
)
 
*
*
 
2


 
 
 
 
 
 
 
 
+
 
(
a
g
e
n
t
1
_
c
o
o
r
d
i
n
a
t
e
s
[
"
y
"
]
 
-
 
a
g
e
n
t
2
_
c
o
o
r
d
i
n
a
t
e
s
[
"
y
"
]
)
 
*
*
 
2


 
 
 
 
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
(
o
b
s
e
r
v
a
t
i
o
n
s
:
 
d
i
c
t
)
 
-
>
 
n
p
.
n
d
a
r
r
a
y
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
s
 
t
h
e
 
d
i
s
t
a
n
c
e
 
m
a
t
r
i
x
 
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
 
a
g
e
n
t
s
 
b
a
s
e
d
 
o
n
 
t
h
e
i
r
 
c
o
o
r
d
i
n
a
t
e
s
 
i
n
 
t
h
e
 
o
b
s
e
r
v
a
t
i
o
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
b
s
e
r
v
a
t
i
o
n
s
 
(
d
i
c
t
)
:
 
D
i
c
t
i
o
n
a
r
y
 
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
 
o
b
s
e
r
v
a
t
i
o
n
 
q
u
e
s
t
i
o
n
 
w
i
t
h
 
a
g
e
n
t
 
i
d
e
n
t
i
f
i
e
r
s
 
a
s
 
k
e
y
s
.
E
a
c
h
 
v
a
l
u
e
 
i
s
 
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
 
w
i
t
h
 
'
x
'
 
a
n
d
 
'
y
'
 
k
e
y
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
 
c
o
o
r
d
i
n
a
t
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


 
 
 
 
 
 
 
 
n
p
.
n
d
a
r
r
a
y
:
 
D
i
s
t
a
n
c
e
 
m
a
t
r
i
x
 
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
 
a
g
e
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
n
u
m
_
a
g
e
n
t
s
 
=
 
l
e
n
(
o
b
s
e
r
v
a
t
i
o
n
s
)


 
 
 
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
 
=
 
n
p
.
z
e
r
o
s
(
(
n
u
m
_
a
g
e
n
t
s
,
 
n
u
m
_
a
g
e
n
t
s
)
)


 
 
 
 
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
u
m
_
a
g
e
n
t
s
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
i
 
+
 
1
,
 
n
u
m
_
a
g
e
n
t
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
[
i
,
 
j
]
 
=
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
[
j
,
 
i
]
 
=
 
c
a
l
c
u
l
a
t
e
_
d
i
s
t
a
n
c
e
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
g
e
n
t
1
=
l
i
s
t
(
o
b
s
e
r
v
a
t
i
o
n
s
.
k
e
y
s
(
)
)
[
i
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
g
e
n
t
2
=
l
i
s
t
(
o
b
s
e
r
v
a
t
i
o
n
s
.
k
e
y
s
(
)
)
[
j
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
b
s
e
r
v
a
t
i
o
n
s
=
o
b
s
e
r
v
a
t
i
o
n
s
,


 
 
 
 
 
 
 
 
 
 
 
 
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
_
m
a
t
r
i
x






d
e
f
 
c
a
l
c
u
l
a
t
e
_
c
l
o
s
e
n
e
s
s
_
c
e
n
t
r
a
l
i
t
y
(


 
 
 
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
:
 
n
p
.
n
d
a
r
r
a
y
,


)
 
-
>
 
n
p
.
n
d
a
r
r
a
y
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
s
 
t
h
e
 
c
l
o
s
e
n
e
s
s
 
c
e
n
t
r
a
l
i
t
y
 
o
f
 
e
a
c
h
 
a
g
e
n
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
d
i
s
t
a
n
c
e
 
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


 
 
 
 
 
 
 
import unittest

import numpy as np


class TestCalculateDistance(unittest.TestCase):

    def test_same_point(self):
        # Both agents are at the same point
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 0, "y": 0}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 0.0)

    def test_horizontal_distance(self):
        # Agents are horizontally apart
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 3, "y": 0}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 3.0)

    def test_vertical_distance(self):
        # Agents are vertically apart
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 0, "y": 4}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 4.0)

    def test_diagonal_distance(self):
        # Agents are diagonally apart
        observations = {
            "agent1": {"x": 1, "y": 2},
            "agent2": {"x": 4, "y": 6}
        }
        expected_distance = np.sqrt((4 - 1) ** 2 + (6 - 2) ** 2)
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), expected_distance)

    def test_negative_coordinates(self):
        # Agents have negative coordinates
        observations = {
            "agent1": {"x": -1, "y": -1},
            "agent2": {"x": -4, "y": -5}
        }
        expected_distance = np.sqrt((-4 + 1) ** 2 + (-5 + 1) ** 2)
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), expected_distance)
if __name__ == '__main__':
    unittest.main()