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
 
s
q
u
a
r
e
d
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
v
e
c
1
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
e
c
2
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
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
c
o
m
p
u
t
e
 
t
h
e
 
s
q
u
a
r
e
d
 
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
 
v
e
c
t
o
r
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
1
 
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
 
F
i
r
s
t
 
v
e
c
t
o
r
.


 
 
 
 
 
 
 
 
v
e
c
2
 
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
 
S
e
c
o
n
d
 
v
e
c
t
o
r
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
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
 
v
e
c
1
 
a
n
d
 
v
e
c
2
.


 
 
 
 
"
"
"


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
v
e
c
1
)
 
=
=
 
l
e
n
(
v
e
c
2
)


 
 
 
 
r
e
t
u
r
n
 
s
u
m
(
[
(
x
 
-
 
y
)
 
*
*
 
2
 
f
o
r
 
x
,
 
y
 
i
n
 
z
i
p
(
v
e
c
1
,
 
v
e
c
2
)
]
)






d
e
f
 
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
v
e
c
1
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
e
c
2
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
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
c
o
m
p
u
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
 
v
e
c
t
o
r
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
1
 
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
 
F
i
r
s
t
 
v
e
c
t
o
r
.


 
 
 
 
 
 
 
 
v
e
c
2
 
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
 
S
e
c
o
n
d
 
v
e
c
t
o
r
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
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
 
v
e
c
1
 
a
n
d
 
v
e
c
2
.


 
 
 
 
"
"
"


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
v
e
c
1
)
 
=
=
 
l
e
n
(
v
e
c
2
)


 
 
 
 
r
e
t
u
r
n
 
s
u
m
(
[
a
b
s
(
x
 
-
 
y
)
 
f
o
r
 
x
,
 
y
 
i
n
 
z
i
p
(
v
e
c
1
,
 
v
e
c
2
)
]
)






d
e
f
 
c
o
s
i
n
e
_
s
i
m
i
l
a
r
i
t
y
(
v
e
c
1
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
e
c
2
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
o
m
p
u
t
e
 
t
h
e
 
c
o
s
i
n
e
 
s
i
m
i
l
a
r
i
t
y
 
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
 
v
e
c
t
o
r
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
1
 
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
 
F
i
r
s
t
 
v
e
c
t
o
r
.


 
 
 
 
 
 
 
 
v
e
c
2
 
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
 
S
e
c
o
n
d
 
v
e
c
t
o
r
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
 
C
o
s
i
n
e
 
s
i
m
i
l
a
r
i
t
y
 
b
e
t
w
e
e
n
 
v
e
c
1
 
a
n
d
 
v
e
c
2
.


 
 
 
 
"
"
"


 
 
 
 
a
s
s
e
r
t
 
l
e
n
(
v
e
c
1
)
 
=
=
 
l
e
n
(
v
e
c
2
)


 
 
 
 
r
e
t
u
r
n
 
s
u
m
(
[
x
 
*
 
y
 
f
o
r
 
x
,
 
y
 
i
n
 
z
i
p
(
v
e
c
1
,
 
v
e
c
2
)
]
)
 
/
 
(


 
 
 
 
 
 
 
 
(
s
u
m
(
[
x
 
*
*
 
2
 
f
o
r
 
x
 
i
n
 
v
e
c
1
]
)
 
*
*
 
0
.
5
)
 
*
 
(
s
u
m
(
[
x
 
*
*
 
2
 
f
o
r
 
x
 
i
n
 
v
e
c
2
]
)
 
*
*
 
0
.
5
)


 
 
 
 
)






d
e
f
 
j
a
c
c
a
r
d
_
s
i
m
i
l
a
r
i
t
y
(
v
e
c
1
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
e
c
2
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
o
m
p
u
t
e
 
t
h
e
 
J
a
c
c
a
r
d
 
s
i
m
i
l
a
r
i
t
y
 
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
 
v
e
c
t
o
r
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
e
c
1
 
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
 
F
i
r
s
t
 
v
e
c
t
o
r
.


 
 
 
 
 
 
 
 
v
e
c
2
 
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
 
S
e
c
o
n
d
 
v
e
c
t
o
r
import unittest


class TestSquaredEuclideanDistance(unittest.TestCase):
    def test_standard_vectors(self):
        """Test squared distance calculation for typical vectors."""
        vec1 = [1, 2, 3]
        vec2 = [4, 5, 6]
        expected_result = 27  # (3^2 + 3^2 + 3^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_vectors_with_zeros(self):
        """Test vectors that include zero values."""
        vec1 = [0, 0, 0]
        vec2 = [0, 0, 0]
        expected_result = 0
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_vectors_with_negative_values(self):
        """Test vectors that include negative values."""
        vec1 = [-1, -2, -3]
        vec2 = [-4, -5, -6]
        expected_result = 27  # (3^2 + 3^2 + 3^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

    def test_single_element_vectors(self):
        """Test single element vectors."""
        vec1 = [5]
        vec2 = [-5]
        expected_result = 100  # (10^2)
        result = squared_euclidean_distance(vec1, vec2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()