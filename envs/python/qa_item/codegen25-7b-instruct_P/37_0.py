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






c
l
a
s
s
 
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
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
 
w
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


 
 
 
 
 
 
 
 
s
e
l
f
.
x
 
=
 
x


 
 
 
 
 
 
 
 
s
e
l
f
.
w
 
=
 
w






d
e
f
 
l
a
n
c
z
o
s
(
n
:
 
i
n
t
,
 
q
u
a
d
r
a
t
u
r
e
_
r
u
l
e
:
 
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
)
 
-
>
 
T
u
p
l
e
[
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
 
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
]
:


 
 
 
 
"
"
"


 
 
 
 
i
m
p
l
e
m
e
n
t
s
 
t
h
e
 
L
a
n
c
z
o
s
 
f
u
n
c
t
i
o
n
 
f
o
r
 
t
h
e
 
r
e
c
u
r
s
i
v
e
 
r
e
l
a
t
i
o
n
 
c
o
e
f
f
i
c
i
e
n
t
 
a
l
g
o
r
i
t
h
m
 
f
o
r
 
c
o
m
p
u
t
i
n
g
 
o
r
t
h
o
g
o
n
a
l
 
p
o
l
y
n
o
m
i
a
l
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
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
 
o
r
t
h
o
g
o
n
a
l
 
p
o
l
y
n
o
m
i
a
l
s
 
t
o
 
g
e
n
e
r
a
t
e


 
 
 
 
 
 
 
 
q
u
a
d
r
a
t
u
r
e
_
r
u
l
e
 
(
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
)
:
 
A
n
 
o
b
j
e
c
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
 
x
 
(
n
o
d
e
s
)
 
a
n
d
 
w
 
(
w
e
i
g
h
t
s
)
 
f
o
r
 
t
h
e
 
q
u
a
d
r
a
t
u
r
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
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
 
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
]
:


 
 
 
 
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
 
t
h
e
 
o
u
t
p
u
t
 
a
r
r
a
y
s


 
 
 
 
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
n
)


 
 
 
 
w
 
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
n
)


 
 
 
 
c
 
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
n
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
 
t
h
e
 
f
i
r
s
t
 
f
e
w
 
t
e
r
m
s


 
 
 
 
x
[
0
]
 
=
 
0


 
 
 
 
w
[
0
]
 
=
 
2


 
 
 
 
c
[
0
]
 
=
 
1


 
 
 
 
c
[
1
]
 
=
 
1


 
 
 
 
#
 
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
 
r
e
s
t
 
o
f
 
t
h
e
 
t
e
r
m
s


 
 
 
 
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
2
,
 
n
)
:


 
 
 
 
 
 
 
 
x
[
i
]
 
=
 
n
p
.
c
o
s
(
(
i
 
-
 
1
)
 
*
 
n
p
.
p
i
 
/
 
(
2
 
*
 
n
)
)


 
 
 
 
 
 
 
 
w
[
i
]
 
=
 
n
p
.
p
i
 
/
 
(
2
 
*
 
n
)


 
 
 
 
 
 
 
 
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
0
,
 
i
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
[
i
]
 
+
=
 
c
[
j
]
 
*
 
n
p
.
c
o
s
(
(
i
 
-
 
1
)
 
*
 
x
[
i
]
 
-
 
j
)


 
 
 
 
 
 
 
 
c
[
i
]
 
*
=
 
w
[
i
]


 
 
 
 
#
 
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
 
w
e
i
g
h
t
s


 
 
 
 
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
0
,
 
n
)
:


 
 
 
 
 
 
 
 
w
[
i
]
 
*
=
 
c
[
i
]


 
 
 
 
#
 
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
 
n
o
d
e
s


 
 
 
 
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
0
,
 
n
)
:


 
 
 
 
 
 
 
 
x
[
i
]
 
=
 
q
u
a
d
r
a
t
u
r
e
_
r
u
l
e
.
x
[
i
]
 
+
 
x
[
i
]


 
 
 
 
#
 
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
 
q
u
a
d
r
a
t
u
r
e
 
r
u
l
e
 
f
o
r
 
t
h
e
 
n
e
w
 
n
o
d
e
s


 
 
 
 
n
e
w
_
q
u
a
d
r
a
t
u
r
e
_
r
u
l
e
 
=
 
Q
u
a
d
r
a
t
u
r
e
R
u
l
e
(
x
,
 
w
)


 
 
 
 
r
e
t
u
r
n
 
x
,
import unittest

import numpy as np


class QuadratureRule:
    def __init__(self, x, w):
        self.x = np.array(x)
        self.w = np.array(w)


class TestOrthogonalPolynomial(unittest.TestCase):
    def test_lanczos_basic(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 2
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)

    def test_lanczos_n_greater_than_length(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 4

        with self.assertRaises(ValueError):
            lanczos(n, quadrature_rule)

    def test_lanczos_n_zero(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 0

        with self.assertRaises(ValueError):
            lanczos(n, quadrature_rule)

    def test_lanczos_weights_nonuniform(self):
        x = [0.0, 0.5, 1.0]
        w = [0.1, 0.4, 0.5]
        quadrature_rule = QuadratureRule(x, w)
        n = 3
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)
        self.assertTrue(np.all(gamma > 0))

    def test_lanczos_single_node(self):
        x = [0.5]
        w = [1.0]
        quadrature_rule = QuadratureRule(x, w)
        n = 1
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)
        self.assertTrue(np.all(gamma > 0))
if __name__ == '__main__':
    unittest.main()