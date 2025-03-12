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
o
f
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
n
:
 
i
n
t
,
 
x
:
 
i
n
t
,
 
y
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
 
n
 
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
 
d
r
a
w
n
 
w
h
e
n
 
1
5
 
b
a
l
l
s
 
a
r
e
 
r
a
n
d
o
m
l
y
 
r
e
t
u
r
n
e
d
 
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
 
x
 
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
 
y
 
b
l
u
e
 
b
a
l
l
s
.




 
 
 
 
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
 
t
o
 
b
e
 
d
r
a
w
n
.


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
y
 
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


 
 
 
 
 
 
 
 
f
l
o
a
t
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
 
o
f
 
d
r
a
w
i
n
g
 
e
x
a
c
t
l
y
 
n
 
r
e
d
 
b
a
l
l
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
 
b
i
n
o
m
i
a
l
(
x
 
+
 
y
,
 
n
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
x
 
+
 
y
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
o
f
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
g
i
v
e
n
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
n
:
 
i
n
t
,
 
x
:
 
i
n
t
,
 
y
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
 
n
 
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
 
d
r
a
w
n
 
w
h
e
n
 
1
5
 
b
a
l
l
s
 
a
r
e
 
r
a
n
d
o
m
l
y
 
r
e
t
u
r
n
e
d
 
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
 
x
 
r
e
d
 
b
a
l
l
s
,
 
y
 
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
 
n
 
-
 
y
 
b
l
u
e
 
b
a
l
l
s
.




 
 
 
 
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
 
t
o
 
b
e
 
d
r
a
w
n
.


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
y
 
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


 
 
 
 
 
 
 
 
f
l
o
a
t
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
 
o
f
 
d
r
a
w
i
n
g
 
e
x
a
c
t
l
y
 
n
 
r
e
d
 
b
a
l
l
s
 
g
i
v
e
n
 
t
h
a
t
 
y
 
b
l
u
e
 
b
a
l
l
s
 
h
a
v
e
 
b
e
e
n
 
s
e
l
e
c
t
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
x
 
+
 
y
,
 
n
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
y
,
 
n
 
-
 
y
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
o
f
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
g
i
v
e
n
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
_
a
l
t
e
r
n
a
t
e
(
n
:
 
i
n
t
,
 
x
:
 
i
n
t
,
 
y
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
 
n
 
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
 
d
r
a
w
n
 
w
h
e
n
 
1
5
 
b
a
l
l
s
 
a
r
e
 
r
a
n
d
o
m
l
y
 
r
e
t
u
r
n
e
d
 
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
 
x
 
r
e
d
 
b
a
l
l
s
,
 
y
 
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
 
n
 
-
 
y
 
b
l
u
e
 
b
a
l
l
s
.




 
 
 
 
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
 
t
o
 
b
e
 
d
r
a
w
n
.


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
y
 
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


 
 
 
 
 
 
 
 
f
l
o
a
t
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
 
o
f
 
d
r
a
w
i
n
g
 
e
x
a
c
t
l
y
 
n
 
r
e
d
 
b
a
l
l
s
 
g
i
v
e
n
 
t
h
a
t
 
y
 
b
l
u
e
 
b
a
l
l
s
 
h
a
v
e
 
b
e
e
n
 
s
e
l
e
c
t
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
x
 
+
 
y
,
 
n
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
y
,
 
n
 
-
 
y
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
o
f
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
g
i
v
e
n
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
_
a
l
t
e
r
n
a
t
e
_
o
p
t
i
m
i
z
e
d
import unittest
from math import isclose


class TestProbabilityOfRedBalls(unittest.TestCase):

    def test_half_red_balls(self):
        # Scenario where half of the drawn balls are expected to be red
        result = probability_of_red_balls(7, 10, 10)
        expected_result = probability_of_red_balls(7, 10, 10)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with half red balls failed")

    def test_some_red_balls(self):
        # Scenario with some red balls in the jar, expecting a few red draws
        result = probability_of_red_balls(5, 5, 10)
        expected_result = probability_of_red_balls(5, 5, 10)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with some red balls failed")

    def test_extreme_case(self):
        # Extreme scenario where the probability is low for the chosen n
        result = probability_of_red_balls(15, 1, 99)
        expected_result = probability_of_red_balls(15, 1, 99)  # Calculate manually or from another tool
        self.assertTrue(isclose(result, expected_result), "Test with extreme case failed")
if __name__ == '__main__':
    unittest.main()