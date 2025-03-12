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
 
c
a
l
c
u
l
a
t
e
(
v
a
l
u
e
s
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
 
p
e
r
i
o
d
:
 
i
n
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
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
l
a
s
t
 
'
p
e
r
i
o
d
'
 
i
n
t
e
g
e
r
s
 
i
n
 
t
h
e
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
v
a
l
u
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
s
 
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
 
T
h
e
 
l
i
s
t
 
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
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
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
 
a
v
e
r
a
g
e
.


 
 
 
 
 
 
 
 
p
e
r
i
o
d
 
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
 
l
a
s
t
 
e
l
e
m
e
n
t
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
h
e
 
a
v
e
r
a
g
e
 
c
a
l
c
u
l
a
t
i
o
n
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
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
l
a
s
t
 
'
p
e
r
i
o
d
'
 
i
n
t
e
g
e
r
s
,
 
o
r
 
m
a
t
h
.
n
a
n
 
i
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
o
e
s
 
n
o
t
 
c
o
n
t
a
i
n
 
e
n
o
u
g
h
 
e
l
e
m
e
n
t
s
 
o
r
 
i
f
 
t
h
e
 
p
e
r
i
o
d
 
i
s
 
i
n
v
a
l
i
d
 
(
<
=
 
0
)
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
v
a
l
u
e
s
)
 
<
 
p
e
r
i
o
d
 
o
r
 
p
e
r
i
o
d
 
<
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
a
t
h
.
n
a
n


 
 
 
 
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
v
a
l
u
e
s
[
-
p
e
r
i
o
d
:
]
)
 
/
 
p
e
r
i
o
d






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
o
v
i
n
g
_
a
v
e
r
a
g
e
(
v
a
l
u
e
s
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
 
p
e
r
i
o
d
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
f
l
o
a
t
]
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
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
v
a
l
u
e
s
 
o
v
e
r
 
t
h
e
 
g
i
v
e
n
 
p
e
r
i
o
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
s
 
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
 
T
h
e
 
l
i
s
t
 
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
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
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
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
.


 
 
 
 
 
 
 
 
p
e
r
i
o
d
 
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
 
e
l
e
m
e
n
t
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
h
e
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
c
a
l
c
u
l
a
t
i
o
n
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
f
l
o
a
t
]
:
 
T
h
e
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
v
a
l
u
e
s
 
o
v
e
r
 
t
h
e
 
g
i
v
e
n
 
p
e
r
i
o
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
v
a
l
u
e
s
)
 
<
 
p
e
r
i
o
d
 
o
r
 
p
e
r
i
o
d
 
<
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
m
a
t
h
.
n
a
n
]
 
*
 
l
e
n
(
v
a
l
u
e
s
)


 
 
 
 
r
e
s
u
l
t
 
=
 
[
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
l
e
n
(
v
a
l
u
e
s
)
)
:


 
 
 
 
 
 
 
 
i
f
 
i
 
<
 
p
e
r
i
o
d
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
s
u
m
(
v
a
l
u
e
s
[
:
i
 
+
 
1
]
)
 
/
 
(
i
 
+
 
1
)
)


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
r
e
s
u
l
t
[
-
1
]
 
*
 
(
p
e
r
i
o
d
 
-
 
1
)
 
+
 
v
a
l
u
e
s
[
i
]
)
 
/
 
p
e
r
i
o
d
)


 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t






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
x
p
o
n
e
n
t
i
a
l
_
m
o
v
i
n
g
_
a
v
e
r
a
g
e
(
v
a
l
u
e
s
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
 
p
e
r
i
o
d
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
f
l
o
a
t
]
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
l
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
v
a
l
u
e
s
 
o
v
e
r
 
t
h
e
 
g
i
v
e
n
 
p
e
r
i
o
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
s
 
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
 
T
h
e
 
l
i
s
t
 
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
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
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
l
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
.


 
 
 
 
 
 
 
 
p
e
r
i
o
d
 
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
 
e
l
e
m
e
n
t
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
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
i
a
l
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
c
a
l
c
u
l
a
t
i
o
n
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
f
l
o
a
t
]
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
i
a
l
 
m
o
v
i
n
g
 
a
v
e
r
a
g
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
v
a
l
u
e
s
 
o
v
e
r
 
t
h
e
 
g
i
v
e
n
 
p
e
r
i
o
d
.


 
 
 
 
"
"
"


import math
import unittest


class TestAnswer(unittest.TestCase):

    def test_calculate_with_valid_input(self):
        values = [1, 2, 3, 4, 5]
        period = 3
        expected = 4.0  # (3 + 4 + 5) / 3
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_all_same_values(self):
        values = [5, 5, 5, 5, 5]
        period = 5
        expected = 5.0  # (5 + 5 + 5 + 5 + 5) / 5
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_single_value(self):
        values = [10]
        period = 1
        expected = 10.0  # (10) / 1
        self.assertEqual(expected, calculate(values, period))

    def test_calculate_with_insufficient_values(self):
        values = [1, 2]
        period = 3
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN

    def test_calculate_with_empty_list(self):
        values = []
        period = 1
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN

    def test_calculate_with_negative_period(self):
        values = [1, 2, 3, 4, 5]
        period = -1
        self.assertTrue(math.isnan(calculate(values, period)))  # Expecting NaN
if __name__ == '__main__':
    unittest.main()