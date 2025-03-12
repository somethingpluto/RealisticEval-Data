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
r
e
m
a
i
n
i
n
g
_
p
a
y
m
e
n
t
(
p
r
i
n
c
i
p
a
l
:
 
f
l
o
a
t
,
 
i
n
t
e
r
e
s
t
_
r
a
t
e
:
 
f
l
o
a
t
,
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
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
 
t
h
e
 
r
e
m
a
i
n
i
n
g
 
p
a
y
m
e
n
t
 
f
o
r
 
a
 
l
o
a
n
 
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
 
g
i
v
e
n
 
d
e
b
t
,
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
,
 
a
n
d
 
t
o
t
a
l
 
p
a
y
m
e
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
r
i
n
c
i
p
a
l
 
(
f
l
o
a
t
)
:
 
T
h
e
 
i
n
i
t
i
a
l
 
a
m
o
u
n
t
 
o
f
 
t
h
e
 
d
e
b
t
.


 
 
 
 
 
 
 
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
 
a
s
 
a
 
d
e
c
i
m
a
l
.


 
 
 
 
 
 
 
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
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
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
p
a
y
m
e
n
t
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
 
T
h
e
 
c
a
l
c
u
l
a
t
e
d
 
r
e
m
a
i
n
i
n
g
 
p
a
y
m
e
n
t
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
 
p
r
i
n
c
i
p
a
l
 
*
 
(
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
 
(
(
1
 
+
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
*
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
)
 
/
 
(
(
(
1
 
+
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
*
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
)
 
-
 
1
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
t
o
t
a
l
_
i
n
t
e
r
e
s
t
(
p
r
i
n
c
i
p
a
l
:
 
f
l
o
a
t
,
 
i
n
t
e
r
e
s
t
_
r
a
t
e
:
 
f
l
o
a
t
,
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
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
 
t
h
e
 
t
o
t
a
l
 
i
n
t
e
r
e
s
t
 
p
a
i
d
 
f
o
r
 
a
 
l
o
a
n
 
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
 
g
i
v
e
n
 
d
e
b
t
,
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
,
 
a
n
d
 
t
o
t
a
l
 
p
a
y
m
e
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
r
i
n
c
i
p
a
l
 
(
f
l
o
a
t
)
:
 
T
h
e
 
i
n
i
t
i
a
l
 
a
m
o
u
n
t
 
o
f
 
t
h
e
 
d
e
b
t
.


 
 
 
 
 
 
 
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
 
a
s
 
a
 
d
e
c
i
m
a
l
.


 
 
 
 
 
 
 
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
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
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
p
a
y
m
e
n
t
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
 
T
h
e
 
c
a
l
c
u
l
a
t
e
d
 
t
o
t
a
l
 
i
n
t
e
r
e
s
t
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
 
p
r
i
n
c
i
p
a
l
 
*
 
(
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
 
(
(
1
 
+
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
*
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
)
 
/
 
(
(
(
1
 
+
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
/
 
1
2
)
 
*
*
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
)
 
-
 
1
)
 
-
 
p
r
i
n
c
i
p
a
l






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
t
o
t
a
l
_
p
a
y
m
e
n
t
(
p
r
i
n
c
i
p
a
l
:
 
f
l
o
a
t
,
 
i
n
t
e
r
e
s
t
_
r
a
t
e
:
 
f
l
o
a
t
,
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
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
 
t
h
e
 
t
o
t
a
l
 
p
a
y
m
e
n
t
 
f
o
r
 
a
 
l
o
a
n
 
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
 
g
i
v
e
n
 
d
e
b
t
,
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
,
 
a
n
d
 
t
o
t
a
l
 
p
a
y
m
e
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
r
i
n
c
i
p
a
l
 
(
f
l
o
a
t
)
:
 
T
h
e
 
i
n
i
t
i
a
l
 
a
m
o
u
n
t
 
o
f
 
t
h
e
 
d
e
b
t
.


 
 
 
 
 
 
 
 
i
n
t
e
r
e
s
t
_
r
a
t
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
m
o
n
t
h
l
y
 
i
n
t
e
r
e
s
t
 
r
a
t
e
 
a
s
 
a
 
d
e
c
i
m
a
l
.


 
 
 
 
 
 
 
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
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
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
p
a
y
m
e
n
t
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
 
T
h
e
 
c
a
l
c
u
l
a
t
e
d
 
t
o
t
a
l
 
p
a
y
m
e
n
t
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
r
e
m
a
i
n
i
n
g
_
p
a
y
m
e
n
t
(
p
r
i
n
c
i
p
a
l
,
 
i
n
t
e
r
e
s
t
_
r
a
t
e
,
 
n
u
m
b
e
r
_
o
f
_
p
a
y
m
e
n
t
s
)
import unittest


class TestCalculateRemainingPayment(unittest.TestCase):

    def test_typical_loan_conditions(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 24), 0, places=2)

    def test_high_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.1, 12), 0, places=2)

    def test_low_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.001, 60), 0, places=2)

    def test_very_short_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 1), 0, places=2)

    def test_no_payments(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 0), 10000, places=2)

    def test_long_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 360), 0, places=2)

if __name__ == '__main__':
    unittest.main()