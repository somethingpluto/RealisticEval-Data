d
e
f
 
p
r
o
b
a
b
i
l
i
t
y
_
r
e
d
_
b
a
l
l
s
(
x
:
 
i
n
t
,
 
n
:
 
i
n
t
,
 
m
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
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
x
 
b
a
l
l
s
 
w
i
l
l
 
b
e
 
r
a
n
d
o
m
l
y
 
d
r
a
w
n
 
f
r
o
m
 
a
 
j
a
r
 
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
 
n
 
r
e
d
 
b
a
l
l
s
 
a
n
d
 
m
 
b
l
u
e
 
b
a
l
l
s
,
 
a
n
d
 
a
l
l
 
o
f
 
t
h
e
m
 
w
i
l
l
 
b
e
 
r
e
d
 
b
a
l
l
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
a
l
l
s
 
t
o
 
d
r
a
w
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
r
e
d
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
r
.


 
 
 
 
 
 
 
 
m
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
l
u
e
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
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


 
 
 
 
 
 
 
 
T
h
e
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
a
l
l
 
x
 
d
r
a
w
n
 
b
a
l
l
s
 
a
r
e
 
r
e
d
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
 
b
i
n
o
m
i
a
l
(
n
 
+
 
m
,
 
x
)
 
/
 
b
i
n
o
m
i
a
l
(
n
 
+
 
m
,
 
n
)






d
e
f
 
p
r
o
b
a
b
i
l
i
t
y
_
b
l
u
e
_
b
a
l
l
s
(
x
:
 
i
n
t
,
 
n
:
 
i
n
t
,
 
m
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
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
x
 
b
a
l
l
s
 
w
i
l
l
 
b
e
 
r
a
n
d
o
m
l
y
 
d
r
a
w
n
 
f
r
o
m
 
a
 
j
a
r
 
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
 
n
 
r
e
d
 
b
a
l
l
s
 
a
n
d
 
m
 
b
l
u
e
 
b
a
l
l
s
,
 
a
n
d
 
a
l
l
 
o
f
 
t
h
e
m
 
w
i
l
l
 
b
e
 
b
l
u
e
 
b
a
l
l
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
a
l
l
s
 
t
o
 
d
r
a
w
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
r
e
d
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
r
.


 
 
 
 
 
 
 
 
m
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
l
u
e
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
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


 
 
 
 
 
 
 
 
T
h
e
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
a
l
l
 
x
 
d
r
a
w
n
 
b
a
l
l
s
 
a
r
e
 
b
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
 
1
 
-
 
p
r
o
b
a
b
i
l
i
t
y
_
r
e
d
_
b
a
l
l
s
(
x
,
 
n
,
 
m
)






d
e
f
 
p
r
o
b
a
b
i
l
i
t
y
_
r
e
d
_
b
l
u
e
_
b
a
l
l
s
(
x
:
 
i
n
t
,
 
n
:
 
i
n
t
,
 
m
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
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
x
 
b
a
l
l
s
 
w
i
l
l
 
b
e
 
r
a
n
d
o
m
l
y
 
d
r
a
w
n
 
f
r
o
m
 
a
 
j
a
r
 
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
 
n
 
r
e
d
 
b
a
l
l
s
 
a
n
d
 
m
 
b
l
u
e
 
b
a
l
l
s
,
 
a
n
d
 
a
t
 
l
e
a
s
t
 
o
n
e
 
o
f
 
t
h
e
m
 
w
i
l
l
 
b
e
 
r
e
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
a
l
l
s
 
t
o
 
d
r
a
w
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
r
e
d
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
r
.


 
 
 
 
 
 
 
 
m
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
b
l
u
e
 
b
a
l
l
s
 
i
n
 
t
h
e
 
j
a
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


 
 
 
 
 
 
 
 
T
h
e
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
a
t
 
l
e
a
s
t
 
o
n
e
 
o
f
 
x
 
d
r
a
w
n
 
b
a
l
l
s
 
i
s
 
r
e
d
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
 
1
 
-
 
p
r
o
b
a
b
i
l
i
t
y
_
r
e
d
_
b
a
l
l
s
(
x
,
 
n
,
 
m
)
 
*
 
p
r
o
b
a
b
i
l
i
t
y
_
b
l
u
e
_
b
a
l
l
s
(
x
,
 
n
,
 
m
)






d
e
f
 
p
r
o
b
a
b
i
l
i
t
y
_
r
e
d
_
b
a
l
l
s
_
i
n
_
g
r
o
u
p
(
x
:
 
i
n
t
,
 
n
:
 
i
n
t
,
 
m
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
 
p
r
o
b
a
b
i
l
i
t
y
 
t
h
a
t
 
x
 
r
e
d
 
b
a
l
l
s
 
w
i
l
l
 
b
e
 
r
a
n
d
o
m
l
y
 
d
r
a
w
n
 
f
r
o
m
 
a
 
j
a
r
 
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
 
n
 
r
e
d
 
b
a
l
l
s
 
a
n
d
 
m
 
b
l
u
e
 
b
a
l
l
s
,
 
a
n
d
 
a
t
 
l
e
a
s
t
 
o
n
e
 
o
f
 
t
h
e
m
 
w
i
l
l
 
b
e
 
r
e
d


 
 
 
 
A
r
g
s
:
import unittest
from math import comb


class TestProbabilityRedBalls(unittest.TestCase):
    def test_all_red(self):
        # Case where all balls are red
        self.assertEqual(probability_red_balls(5, 5, 0), 1)

    def test_no_red(self):
        # Case where no red balls are available
        self.assertEqual(probability_red_balls(1, 0, 5), 0)

    def test_typical_case(self):
        # Typical scenario
        self.assertAlmostEqual(probability_red_balls(2, 10, 5), comb(10, 2) / comb(15, 2))

    def test_impossible_case(self):
        # More balls requested than available
        self.assertEqual(probability_red_balls(6, 5, 4), 0)

    def test_high_combinations(self):
        # Test with higher number of combinations
        self.assertAlmostEqual(probability_red_balls(3, 20, 30), comb(20, 3) / comb(50, 3))
if __name__ == '__main__':
    unittest.main()