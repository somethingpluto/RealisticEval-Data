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
 
p
o
w
e
r
(
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
i
n
t
]
]
,
 
n
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
i
n
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
u
t
e
s
 
t
h
e
 
n
-
t
h
 
p
o
w
e
r
 
o
f
 
a
 
m
a
t
r
i
x
 
u
s
i
n
g
 
t
h
e
 
f
a
s
t
 
e
x
p
o
n
e
n
t
i
a
t
i
o
n
 
m
e
t
h
o
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
i
n
t
]
]
)
:
 
A
 
s
q
u
a
r
e
 
m
a
t
r
i
x
 
t
o
 
b
e
 
e
x
p
o
n
e
n
t
i
a
t
e
d
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
h
e
 
e
x
p
o
n
e
n
t
 
t
o
 
r
a
i
s
e
 
t
h
e
 
m
a
t
r
i
x
 
t
o
.
 
M
u
s
t
 
b
e
 
a
 
n
o
n
-
n
e
g
a
t
i
v
e
 
i
n
t
e
g
e
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
i
n
t
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
a
i
s
e
d
 
t
o
 
t
h
e
 
p
o
w
e
r
 
o
f
 
n
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
n
 
i
s
 
n
e
g
a
t
i
v
e
.


 
 
 
 
 
 
 
 
T
y
p
e
E
r
r
o
r
:
 
I
f
 
m
a
t
r
i
x
 
i
s
 
n
o
t
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s
 
o
r
 
n
 
i
s
 
n
o
t
 
a
n
 
i
n
t
e
g
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
m
a
t
r
i
x
,
 
l
i
s
t
)
 
o
r
 
n
o
t
 
a
l
l
(
i
s
i
n
s
t
a
n
c
e
(
r
o
w
,
 
l
i
s
t
)
 
f
o
r
 
r
o
w
 
i
n
 
m
a
t
r
i
x
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
m
a
t
r
i
x
 
m
u
s
t
 
b
e
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s
"
)


 
 
 
 
i
f
 
n
o
t
 
a
l
l
(
i
s
i
n
s
t
a
n
c
e
(
e
l
e
m
,
 
i
n
t
)
 
f
o
r
 
r
o
w
 
i
n
 
m
a
t
r
i
x
 
f
o
r
 
e
l
e
m
 
i
n
 
r
o
w
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
m
a
t
r
i
x
 
m
u
s
t
 
b
e
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s
 
o
f
 
i
n
t
e
g
e
r
s
"
)


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
n
,
 
i
n
t
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
n
 
m
u
s
t
 
b
e
 
a
n
 
i
n
t
e
g
e
r
"
)


 
 
 
 
i
f
 
n
 
<
 
0
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
n
 
m
u
s
t
 
b
e
 
n
o
n
-
n
e
g
a
t
i
v
e
"
)


 
 
 
 
i
f
 
n
o
t
 
i
s
_
s
q
u
a
r
e
(
m
a
t
r
i
x
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
m
a
t
r
i
x
 
m
u
s
t
 
b
e
 
a
 
s
q
u
a
r
e
 
m
a
t
r
i
x
"
)




 
 
 
 
#
 
B
a
s
e
 
c
a
s
e


 
 
 
 
i
f
 
n
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
[
i
n
t
(
r
o
w
 
=
=
 
c
o
l
)
 
f
o
r
 
c
o
l
 
i
n
 
r
a
n
g
e
(
l
e
n
(
m
a
t
r
i
x
)
)
]
 
f
o
r
 
r
o
w
 
i
n
 
r
a
n
g
e
(
l
e
n
(
m
a
t
r
i
x
)
)
]


 
 
 
 
i
f
 
n
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
t
r
i
x




 
 
 
 
#
 
R
e
c
u
r
s
i
v
e
 
c
a
s
e


 
 
 
 
i
f
 
n
 
%
 
2
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
u
l
t
i
p
l
y
(
p
o
w
e
r
(
m
a
t
r
i
x
,
 
n
 
/
/
 
2
)
,
 
p
o
w
e
r
(
m
a
t
r
i
x
,
 
n
 
/
/
 
2
)
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
u
l
t
i
p
l
y
(
m
a
t
r
i
x
,
 
p
o
w
e
r
(
p
o
w
e
r
(
m
a
t
r
i
x
,
 
n
 
/
/
 
2
)
,
 
2
)
)






d
e
f
 
m
u
l
t
i
p
l
y
(
m
a
t
r
i
x
_
a
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
i
n
t
]
]
,
 
m
a
t
r
i
x
_
b
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
i
n
t
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
i
n
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
M
u
l
t
i
p
l
i
e
s
 
t
w
o
 
m
a
t
r
i
c
e
s
 
t
o
g
e
t
h
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
t
r
i
x
_
a
 
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
i
n
t
]
]
)
:
 
A
 
m
a
t
r
i
x
.


 
 
 
 
 
 
 
 
m
a
t
r
i
x
_
b
 
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
i
n
t
]
]
)
:
import unittest

class TestMatrixPower(unittest.TestCase):

    def test_identity_matrix(self):
        # Testing the power function with an identity matrix
        matrix = [[1, 0], [0, 1]]
        expected = [[1, 0], [0, 1]]
        result = power(matrix, 1)
        self.assertEqual(result, expected)

    def test_zero_power(self):
        # Testing matrix to the power of zero (should return identity)
        matrix = [[2, 3], [1, 4]]
        expected = [[1, 0], [0, 1]]
        result = power(matrix, 0)
        self.assertEqual(result, expected)

    def test_positive_power(self):
        # Testing matrix to a positive power
        matrix = [[2, 1], [1, 3]]
        expected = [[5, 5], [5, 10]]  # This is the result of matrix^2
        result = power(matrix, 2)
        self.assertEqual(result, expected)

    def test_negative_power(self):
        # Testing matrix to a negative power (should raise ValueError)
        matrix = [[2, 1], [1, 3]]
        with self.assertRaises(ValueError):
            power(matrix, -1)
if __name__ == '__main__':
    unittest.main()