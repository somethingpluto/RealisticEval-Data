i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p






d
e
f
 
c
h
e
c
k
_
x
o
r
_
s
u
m
(
c
o
m
b
i
n
a
t
i
o
n
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
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
t
h
e
 
X
O
R
 
s
u
m
s
 
o
f
 
s
p
e
c
i
f
i
c
 
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
 
g
i
v
e
n
 
c
o
m
b
i
n
a
t
i
o
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


 
 
 
 
 
 
 
 
c
o
m
b
i
n
a
t
i
o
n
 
(
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
)
:
 
A
 
2
D
 
n
u
m
p
y
 
a
r
r
a
y
 
w
h
e
r
e
 
e
a
c
h
 
c
o
l
u
m
n
 
c
o
r
r
e
s
p
o
n
d
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
 
a
 
s
p
e
c
i
f
i
c
 
v
a
l
u
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
X
O
R
 
s
u
m
s
 
o
f
 
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
s
 
m
a
t
c
h
 
t
h
e
 
r
e
q
u
i
r
e
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
s
;
 
o
t
h
e
r
w
i
s
e
,
 
F
a
l
s
e
.


 
 
 
 
"
"
"


 
 
 
 
x
o
r
_
s
u
m
_
1
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
0
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
1
]
)


 
 
 
 
x
o
r
_
s
u
m
_
2
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
0
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
2
]
)


 
 
 
 
x
o
r
_
s
u
m
_
3
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
1
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
2
]
)


 
 
 
 
x
o
r
_
s
u
m
_
4
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
0
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
3
]
)


 
 
 
 
x
o
r
_
s
u
m
_
5
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
1
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
3
]
)


 
 
 
 
x
o
r
_
s
u
m
_
6
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
2
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
3
]
)


 
 
 
 
x
o
r
_
s
u
m
_
7
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
0
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
4
]
)


 
 
 
 
x
o
r
_
s
u
m
_
8
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
1
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
4
]
)


 
 
 
 
x
o
r
_
s
u
m
_
9
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
2
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
4
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
0
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
3
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
4
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
1
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
0
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
5
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
2
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
1
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
5
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
3
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
2
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
5
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
4
 
=
 
n
p
.
b
i
t
w
i
s
e
_
x
o
r
(
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
3
]
,
 
c
o
m
b
i
n
a
t
i
o
n
[
:
,
 
5
]
)


 
 
 
 
x
o
r
_
s
u
m
_
1
5
 
=
 
n
p
.
b
i
t
w
i
s
e
_
import unittest

import numpy as np


class TestCheckXorSum(unittest.TestCase):

    def test_correct_xor_sums(self):
        """ Test with combination values that produce the expected XOR sums. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_incorrect_xor_sums(self):
        """ Test with combination values that do not meet the expected XOR sums. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_edge_case_with_zero(self):
        """ Test with a combination where all values are zero. """
        combination = np.zeros((1, 8), dtype=int)  # 1 row of zeros
        self.assertFalse(check_xor_sum(combination))

    def test_large_numbers(self):
        """ Test with large numbers in the combination. """
        combination = np.array([
            [0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000],
            [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000]
        ])
        self.assertFalse(check_xor_sum(combination))

    def test_multiple_rows(self):
        """ Test with a combination that contains multiple rows. """
        combination = np.array([
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00],
            [0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00]
        ])
        self.assertTrue(check_xor_sum(combination))
if __name__ == '__main__':
    unittest.main()