d
e
f
 
c
r
e
a
t
e
_
m
a
t
r
i
x
(
r
o
w
s
:
 
i
n
t
,
 
c
o
l
u
m
n
s
:
 
i
n
t
,
 
i
n
i
t
i
a
l
_
v
a
l
u
e
:
 
a
n
y
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
m
a
t
r
i
x
 
w
i
t
h
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
n
u
m
b
e
r
 
o
f
 
r
o
w
s
 
a
n
d
 
c
o
l
u
m
n
s
,


 
 
 
 
f
i
l
l
e
d
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
i
n
i
t
i
a
l
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
s
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
r
o
w
s
 
i
n
 
t
h
e
 
m
a
t
r
i
x
.


 
 
 
 
 
 
 
 
c
o
l
u
m
n
s
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
c
o
l
u
m
n
s
 
i
n
 
t
h
e
 
m
a
t
r
i
x
.


 
 
 
 
 
 
 
 
i
n
i
t
i
a
l
_
v
a
l
u
e
 
(
a
n
y
)
:
 
T
h
e
 
v
a
l
u
e
 
t
o
 
f
i
l
l
 
t
h
e
 
m
a
t
r
i
x
 
w
i
t
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
I
t
 
c
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
e
 
(
n
u
m
b
e
r
,
 
s
t
r
i
n
g
,
 
o
b
j
e
c
t
,
 
e
t
c
.
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
l
i
s
t
 
(
m
a
t
r
i
x
)
 
f
i
l
l
e
d
 
w
i
t
h
 
t
h
e
 
i
n
i
t
i
a
l
 
v
a
l
u
e
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
 
[
[
i
n
i
t
i
a
l
_
v
a
l
u
e
 
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
c
o
l
u
m
n
s
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
r
o
w
s
)
]






d
e
f
 
p
r
i
n
t
_
m
a
t
r
i
x
(
m
a
t
r
i
x
:
 
l
i
s
t
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"
P
r
i
n
t
s
 
a
 
m
a
t
r
i
x
 
t
o
 
t
h
e
 
c
o
n
s
o
l
e
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
l
i
s
t
)
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
 
t
o
 
p
r
i
n
t
.


 
 
 
 
"
"
"


 
 
 
 
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
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
r
o
w
)






d
e
f
 
g
e
t
_
m
a
t
r
i
x
_
s
i
z
e
(
m
a
t
r
i
x
:
 
l
i
s
t
)
 
-
>
 
t
u
p
l
e
:


 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
r
o
w
s
 
a
n
d
 
c
o
l
u
m
n
s
 
i
n
 
a
 
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


 
 
 
 
 
 
 
 
m
a
t
r
i
x
 
(
l
i
s
t
)
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
 
t
o
 
g
e
t
 
t
h
e
 
s
i
z
e
 
o
f
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
r
o
w
s
 
a
n
d
 
c
o
l
u
m
n
s
 
i
n
 
t
h
e
 
m
a
t
r
i
x
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
,
 
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
[
0
]
)






d
e
f
 
g
e
t
_
m
a
t
r
i
x
_
r
o
w
(
m
a
t
r
i
x
:
 
l
i
s
t
,
 
r
o
w
_
i
n
d
e
x
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
r
o
w
 
f
r
o
m
 
a
 
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


 
 
 
 
 
 
 
 
m
a
t
r
i
x
 
(
l
i
s
t
)
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
 
t
o
 
g
e
t
 
t
h
e
 
r
o
w
 
f
r
o
m
.


 
 
 
 
 
 
 
 
r
o
w
_
i
n
d
e
x
 
(
i
n
t
)
:
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
r
o
w
 
t
o
 
g
e
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
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
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
r
o
w
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
r
i
x
[
r
o
w
_
i
n
d
e
x
]






d
e
f
 
g
e
t
_
m
a
t
r
i
x
_
c
o
l
u
m
n
(
m
a
t
r
i
x
:
 
l
i
s
t
,
 
c
o
l
u
m
n
_
i
n
d
e
x
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
c
o
l
u
m
n
 
f
r
o
m
 
a
 
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


 
 
 
 
 
 
 
 
m
a
t
r
i
x
 
(
l
i
s
t
)
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
 
t
o
 
g
e
t
 
t
h
e
 
c
o
l
u
m
n
 
f
r
o
m
.


 
 
 
 
 
 
 
 
c
o
l
u
m
n
_
i
n
d
e
x
 
(
i
n
t
)
:
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
o
l
u
m
n
 
t
o
 
g
e
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
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
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
c
o
l
u
m
n
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
 
[
r
o
w
[
c
o
l
u
m
n
_
i
n
d
e
x
]
 
f
o
r
 
r
o
w
import unittest


class TestCreateMatrix(unittest.TestCase):

    def test_create_2x2_matrix_filled_with_zeros(self):
        result = create_matrix(2, 2, 0)
        self.assertEqual(result, [[0, 0], [0, 0]])

    def test_create_3x3_matrix_filled_with_ones(self):
        result = create_matrix(3, 3, 1)
        self.assertEqual(result, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def test_create_4x5_matrix_filled_with_string(self):
        result = create_matrix(4, 5, 'test')
        self.assertEqual(result, [['test'] * 5 for _ in range(4)])

    def test_create_0x0_matrix(self):
        result = create_matrix(0, 0, None)
        self.assertEqual(result, [])

    def test_create_1x1_matrix_with_boolean(self):
        result = create_matrix(1, 1, True)
        self.assertEqual(result, [[True]])

    def test_create_5x5_matrix_filled_with_negative_numbers(self):
        result = create_matrix(5, 5, -1)
        self.assertEqual(result, [[-1] * 5 for _ in range(5)])

if __name__ == '__main__':
    unittest.main()