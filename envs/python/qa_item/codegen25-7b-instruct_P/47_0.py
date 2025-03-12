i
m
p
o
r
t
 
d
a
t
e
t
i
m
e






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
n
t
h
_
w
e
e
k
d
a
y
_
i
n
_
m
o
n
t
h
(
y
e
a
r
:
 
i
n
t
,
 
m
o
n
t
h
:
 
i
n
t
,
 
o
c
c
u
r
r
e
n
c
e
:
 
i
n
t
,
 
w
e
e
k
d
a
y
:
 
i
n
t
)
 
-
>
 
d
a
t
e
t
i
m
e
.
d
a
t
e
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
 
d
a
t
e
 
o
f
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
w
e
e
k
d
a
y
 
(
k
)
 
i
n
 
a
 
g
i
v
e
n
 
m
o
n
t
h
 
(
m
)
 
a
n
d
 
y
e
a
r
 
(
y
)
.


 
 
 
 
I
f
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
w
i
t
h
i
n
 
t
h
e
 
m
o
n
t
h
,
 
i
t
 
r
e
t
u
r
n
s
 
t
h
e
 
l
a
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
a
t
 
w
e
e
k
d
a
y
 
i
n
 
t
h
e
 
m
o
n
t
h
.


 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
e
x
t
e
n
d
s
 
t
h
e
 
c
a
p
a
b
i
l
i
t
y
 
t
o
 
h
a
n
d
l
e
 
e
d
g
e
 
c
a
s
e
s
 
w
h
e
r
e
 
t
h
e
 
n
t
h
 
w
e
e
k
d
a
y
 
m
i
g
h
t
 
n
o
t
 
b
e
 
p
r
e
s
e
n
t
,


 
 
 
 
b
y
 
p
r
o
v
i
d
i
n
g
 
t
h
e
 
c
l
o
s
e
s
t
 
p
r
e
v
i
o
u
s
 
w
e
e
k
d
a
y
 
i
n
 
s
u
c
h
 
c
a
s
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
 
(
i
n
t
)
:
 
T
h
e
 
y
e
a
r
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
d
a
t
e
 
i
s
 
t
o
 
b
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
.


 
 
 
 
 
 
 
 
m
 
(
i
n
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
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
d
a
t
e
 
i
s
 
t
o
 
b
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
,
 
w
h
e
r
e
 
J
a
n
u
a
r
y
 
i
s
 
1
 
a
n
d
 
D
e
c
e
m
b
e
r
 
i
s
 
1
2
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
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y
 
w
i
t
h
i
n
 
t
h
e
 
m
o
n
t
h
.
 
F
o
r
 
e
x
a
m
p
l
e
,
 
1
 
f
o
r
 
t
h
e
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
,
 
2
 
f
o
r
 
t
h
e
 
s
e
c
o
n
d
,
 
e
t
c
.


 
 
 
 
 
 
 
 
k
 
(
i
n
t
)
:
 
T
h
e
 
w
e
e
k
d
a
y
,
 
w
h
e
r
e
 
M
o
n
d
a
y
 
i
s
 
0
 
a
n
d
 
S
u
n
d
a
y
 
i
s
 
6
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
d
a
t
e
t
i
m
e
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
 
d
a
t
e
 
o
f
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y
 
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
 
m
o
n
t
h
 
a
n
d
 
y
e
a
r
.


 
 
 
 
 
 
I
f
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
,
 
r
e
t
u
r
n
s
 
t
h
e
 
d
a
t
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
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
a
t
 
w
e
e
k
d
a
y
 
i
n
 
t
h
e
 
m
o
n
t
h
.


 
 
 
 
"
"
"


 
 
 
 
#
 
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
 
n
u
m
b
e
r
 
o
f
 
d
a
y
s
 
i
n
 
t
h
e
 
m
o
n
t
h


 
 
 
 
m
o
n
t
h
_
d
a
y
s
 
=
 
c
a
l
e
n
d
a
r
.
m
o
n
t
h
r
a
n
g
e
(
y
e
a
r
,
 
m
o
n
t
h
)
[
1
]




 
 
 
 
#
 
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
 
n
u
m
b
e
r
 
o
f
 
d
a
y
s
 
b
e
t
w
e
e
n
 
t
h
e
 
f
i
r
s
t
 
d
a
y
 
o
f
 
t
h
e
 
m
o
n
t
h
 
a
n
d
 
t
h
e
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y


 
 
 
 
w
e
e
k
d
a
y
_
d
a
y
s
 
=
 
(
w
e
e
k
d
a
y
 
-
 
d
a
t
e
t
i
m
e
.
d
a
t
e
(
y
e
a
r
,
 
m
o
n
t
h
,
 
1
)
.
w
e
e
k
d
a
y
(
)
)
 
%
 
7




 
 
 
 
#
 
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
 
n
u
m
b
e
r
 
o
f
 
d
a
y
s
 
b
e
t
w
e
e
n
 
t
h
e
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y
 
a
n
d
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e


 
 
 
 
o
c
c
u
r
r
e
n
c
e
_
d
a
y
s
 
=
 
(
o
c
c
u
r
r
e
n
c
e
 
-
 
1
)
 
*
 
7




 
 
 
 
#
 
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
 
d
a
t
e
 
o
f
 
t
h
e
 
n
t
h
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y


 
 
 
 
n
t
h
_
o
c
c
u
r
r
e
n
c
e
_
d
a
t
e
 
=
 
d
a
t
e
t
i
m
e
.
d
a
t
e
(
y
e
a
r
,
 
m
o
n
t
h
,
 
w
e
e
k
d
a
y
_
d
a
y
s
 
+
 
o
c
c
u
r
r
e
n
c
e
_
d
a
y
s
)




 
 
 
 
#
 
I
f
 
t
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
 
d
a
t
e
 
i
s
 
w
i
t
h
i
n
 
t
h
e
 
m
o
n
t
h
,
 
r
e
t
u
r
n
 
i
t


 
 
 
 
i
f
 
n
t
h
_
o
c
c
u
r
r
e
n
c
e
_
d
a
t
e
.
d
a
y
 
<
=
 
m
o
n
t
h
_
d
a
y
s
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
t
h
_
o
c
c
u
r
r
e
n
c
e
_
d
a
t
e




 
 
 
 
#
 
I
f
 
t
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
 
d
a
t
e
 
i
s
 
o
u
t
s
i
d
e
 
t
h
e
 
m
o
n
t
h
,
 
r
e
t
u
r
n
 
t
h
e
 
l
a
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
w
e
e
k
d
a
y
 
i
n
 
t
h
e
 
m
o
n
t
h


 
 
 
 
r
e
t
u
r
n
 
d
a
t
e
t
i
m
e
.
d
a
t
e
(
y
e
a
r
import unittest
import datetime


class TestFindNthWeekdayOfSpecificYear(unittest.TestCase):

    def test_regular_occurrence(self):
        # Test for the 2nd Monday of May 2023
        result = calculate_nth_weekday_in_month(2023, 5, 2, 0)  # Monday is 0
        expected = datetime.date(2023, 5, 8)
        self.assertEqual(result, expected)

    def test_last_occurrence(self):
        # Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        result = calculate_nth_weekday_in_month(2023, 5, 5, 0)  # Monday is 0
        expected = datetime.date(2023, 5, 29)
        self.assertEqual(result, expected)

    def test_first_day_is_weekday(self):
        # Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        result = calculate_nth_weekday_in_month(2023, 8, 1, 1)  # Tuesday is 1
        expected = datetime.date(2023, 8, 1)
        self.assertEqual(result, expected)

    def test_edge_year_transition(self):
        # Test for the 1st Friday of December 2023
        result = calculate_nth_weekday_in_month(2023, 12, 1, 4)  # Friday is 4
        expected = datetime.date(2023, 12, 1)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()