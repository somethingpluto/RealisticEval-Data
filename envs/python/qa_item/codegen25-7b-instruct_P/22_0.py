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
 
T
u
p
l
e






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
e
u
c
l
i
d
e
a
n
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
p
o
i
n
t
1
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
,
 
p
o
i
n
t
2
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
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


 
 
 
 
c
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
 
p
o
i
n
t
s
 
i
n
 
a
 
2
D
 
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
1
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
f
i
r
s
t
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
1
,
 
y
1
)
.


 
 
 
 
 
 
 
 
p
o
i
n
t
2
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
2
,
 
y
2
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
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
h
e
 
t
w
o
 
p
o
i
n
t
s
.




 
 
 
 
"
"
"


 
 
 
 
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
p
o
i
n
t
1
[
0
]
 
-
 
p
o
i
n
t
2
[
0
]
)
 
*
*
 
2
 
+
 
(
p
o
i
n
t
1
[
1
]
 
-
 
p
o
i
n
t
2
[
1
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
m
a
n
h
a
t
t
a
n
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
p
o
i
n
t
1
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
,
 
p
o
i
n
t
2
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
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


 
 
 
 
c
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
 
M
a
n
h
a
t
t
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
 
p
o
i
n
t
s
 
i
n
 
a
 
2
D
 
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
1
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
f
i
r
s
t
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
1
,
 
y
1
)
.


 
 
 
 
 
 
 
 
p
o
i
n
t
2
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
2
,
 
y
2
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
M
a
n
h
a
t
t
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
 
p
o
i
n
t
s
.




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
a
b
s
(
p
o
i
n
t
1
[
0
]
 
-
 
p
o
i
n
t
2
[
0
]
)
 
+
 
a
b
s
(
p
o
i
n
t
1
[
1
]
 
-
 
p
o
i
n
t
2
[
1
]
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
c
h
e
b
y
s
h
e
v
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
p
o
i
n
t
1
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
,
 
p
o
i
n
t
2
:
 
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
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


 
 
 
 
c
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
 
C
h
e
b
y
s
h
e
v
 
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
 
p
o
i
n
t
s
 
i
n
 
a
 
2
D
 
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
1
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
f
i
r
s
t
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
1
,
 
y
1
)
.


 
 
 
 
 
 
 
 
p
o
i
n
t
2
 
(
T
u
p
l
e
[
f
l
o
a
t
,
 
f
l
o
a
t
]
)
:
 
T
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
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
 
(
x
2
,
 
y
2
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
C
h
e
b
y
s
h
e
v
 
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
 
p
o
i
n
t
s
.




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
a
x
(
a
b
s
(
p
o
i
n
t
1
[
0
]
 
-
 
p
o
i
n
t
2
[
0
]
)
,
 
a
b
s
(
p
o
i
n
t
1
[
1
]
 
-
 
p
o
i
n
t
2
[
1
]
)
)




import unittest
from typing import Tuple

class TestCalculateEuclideanDistance(unittest.TestCase):

    def test_basic_functionality(self):
        # Basic logic functionality test.js
        point1 = (0, 0)
        point2 = (3, 4)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should calculate the distance correctly")

    def test_negative_coordinates(self):
        # Test with negative coordinates
        point1 = (-1, -1)
        point2 = (-4, -5)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should handle negative coordinates correctly")

    def test_zero_distance(self):
        # Boundary test.js: points are the same
        point1 = (2, 3)
        point2 = (2, 3)
        expected_distance = 0.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should return 0 when both points are the same")

    def test_large_coordinates(self):
        # Boundary test.js: large coordinates
        point1 = (1e6, 1e6)
        point2 = (1e6 + 3, 1e6 + 4)
        expected_distance = 5.0
        self.assertEqual(calculate_euclidean_distance(point1, point2), expected_distance, "Should handle large coordinates correctly")

    def test_invalid_input(self):
        # Exception handling test.js: invalid input (non-tuple)
        with self.assertRaises(TypeError):
            calculate_euclidean_distance("invalid", (0, 0))

if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()