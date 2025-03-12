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
_
a
v
e
r
a
g
e
_
d
i
f
f
e
r
e
n
c
e
(
n
u
m
b
e
r
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
 
i
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
b
e
r
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
 
A
 
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
,
 
o
r
 
0
 
i
f
 
t
h
e
r
e
 
a
r
e
 
f
e
w
e
r
 
t
h
a
n
 
2
 
i
n
t
e
g
e
r
s
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
n
u
m
b
e
r
s
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
d
i
f
f
e
r
e
n
c
e
s
 
=
 
[
n
u
m
b
e
r
s
[
i
]
 
-
 
n
u
m
b
e
r
s
[
i
 
-
 
1
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
1
,
 
l
e
n
(
n
u
m
b
e
r
s
)
)
]


 
 
 
 
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
d
i
f
f
e
r
e
n
c
e
s
)
 
/
 
l
e
n
(
d
i
f
f
e
r
e
n
c
e
s
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
a
v
e
r
a
g
e
_
d
i
f
f
e
r
e
n
c
e
_
w
i
t
h
_
m
i
n
_
m
a
x
(
n
u
m
b
e
r
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
 
i
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
,
 
t
a
k
i
n
g
 
i
n
t
o
 
a
c
c
o
u
n
t
 
t
h
e
 
m
i
n
i
m
u
m
 
a
n
d
 
m
a
x
i
m
u
m
 
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


 
 
 
 
 
 
 
 
n
u
m
b
e
r
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
 
A
 
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
,
 
o
r
 
0
 
i
f
 
t
h
e
r
e
 
a
r
e
 
f
e
w
e
r
 
t
h
a
n
 
2
 
i
n
t
e
g
e
r
s
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
n
u
m
b
e
r
s
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
d
i
f
f
e
r
e
n
c
e
s
 
=
 
[
n
u
m
b
e
r
s
[
i
]
 
-
 
n
u
m
b
e
r
s
[
i
 
-
 
1
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
1
,
 
l
e
n
(
n
u
m
b
e
r
s
)
)
]


 
 
 
 
r
e
t
u
r
n
 
(
s
u
m
(
d
i
f
f
e
r
e
n
c
e
s
)
 
-
 
m
a
x
(
d
i
f
f
e
r
e
n
c
e
s
)
 
-
 
m
i
n
(
d
i
f
f
e
r
e
n
c
e
s
)
)
 
/
 
(
l
e
n
(
d
i
f
f
e
r
e
n
c
e
s
)
 
-
 
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
a
v
e
r
a
g
e
_
d
i
f
f
e
r
e
n
c
e
_
w
i
t
h
_
m
i
n
_
m
a
x
_
a
n
d
_
m
i
n
_
m
a
x
_
d
i
f
f
(
n
u
m
b
e
r
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
 
i
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
,
 
t
a
k
i
n
g
 
i
n
t
o
 
a
c
c
o
u
n
t
 
t
h
e
 
m
i
n
i
m
u
m
 
a
n
d
 
m
a
x
i
m
u
m
 
v
a
l
u
e
s
 
a
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
a
n
d
 
m
a
x
i
m
u
m
 
d
i
f
f
e
r
e
n
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
b
e
r
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
 
A
 
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
 
d
i
f
f
e
r
e
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
 
c
o
n
s
e
c
u
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
s
,
 
o
r
 
0
 
i
f
 
t
h
e
r
e
 
a
r
e
 
f
e
w
e
r
 
t
h
a
n
 
2
 
i
n
t
e
g
e
r
s
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
n
u
m
b
e
r
s
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
d
i
f
f
e
r
e
n
c
e
s
 
=
 
[
n
u
m
b
e
r
s
[
i
]
 
-
 
n
u
m
b
e
r
s
[
i
 
-
 
1
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
1
,
 
l
e
n
(
n
u
m
b
e
r
s
)
)
]


 
 
 
 
m
i
n
_
d
i
f
f
 
=
 
m
i
n
(
d
i
f
f
e
r
e
n
c
e
s
)


 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
m
a
x
(
d
i
f
f
e
r
e
n
c
e
s
)


 
 
 
 
r
e
t
u
r
n
 
(
s
u
m
(
d
i
f
f
e
r
e
n
c
e
s
)
 
-
import unittest
from typing import List


class TestCalculateAverageDifference(unittest.TestCase):

    def test_calculate_average_difference_positive_integers(self):
        numbers: List[int] = [10, 20, 30, 40]
        result = calculate_average_difference(numbers)
        expected = 10.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 10.0")

    def test_calculate_average_difference_mixed_positive_and_negative(self):
        numbers: List[int] = [-10, 0, 10, 20]
        result = calculate_average_difference(numbers)
        expected = 10.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 10.0")

    def test_calculate_average_difference_same_values(self):
        numbers: List[int] = [5, 5, 5, 5]
        result = calculate_average_difference(numbers)
        expected = 0.0
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 as all values are the same")

    def test_calculate_average_difference_single_element(self):
        numbers: List[int] = [100]
        result = calculate_average_difference(numbers)
        expected = 0.0  # Not enough data to calculate differences
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 for a single element list")

    def test_calculate_average_difference_empty_list(self):
        numbers: List[int] = []
        result = calculate_average_difference(numbers)
        expected = 0.0  # Not enough data to calculate differences
        self.assertAlmostEqual(expected, result, msg="The average difference should be 0.0 for an empty list")
if __name__ == '__main__':
    unittest.main()