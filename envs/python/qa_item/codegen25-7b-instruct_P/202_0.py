d
e
f
 
g
e
t
_
d
a
y
s
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
)
 
-
>
 
i
n
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
 
y
e
a
r
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
 
a
c
c
o
u
n
t
s
 
f
o
r
 
l
e
a
p
 
y
e
a
r
s
 
w
h
e
n
 
c
a
l
c
u
l
a
t
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
 
d
a
y
s
 
i
n
 
F
e
b
r
u
a
r
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
e
a
r
 
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
o
 
g
e
t
 
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
.
 
T
h
i
s
 
s
h
o
u
l
d
 
b
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
 
v
a
l
i
d
 
i
n
t
e
g
e
r
 
r
e
p
r
e
s
e
n
t
i
n
g
 
a
 
y
e
a
r
 
(
e
.
g
.
,
 
2
0
2
4
)
.


 
 
 
 
 
 
 
 
m
o
n
t
h
 
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
o
 
g
e
t
 
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
.
 
I
t
 
s
h
o
u
l
d
 
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
e
t
w
e
e
n
 
1
 
a
n
d
 
1
2
,
 
w
h
e
r
e
 
1
 
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
 
J
a
n
u
a
r
y
 
a
n
d
 
1
2
 
t
o
 
D
e
c
e
m
b
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


 
 
 
 
 
 
 
 
i
n
t
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
 
d
a
y
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
 
m
o
n
t
h
 
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
 
y
e
a
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
m
o
n
t
h
 
=
=
 
2
:


 
 
 
 
 
 
 
 
i
f
 
y
e
a
r
 
%
 
4
 
=
=
 
0
 
a
n
d
 
(
y
e
a
r
 
%
 
1
0
0
 
!
=
 
0
 
o
r
 
y
e
a
r
 
%
 
4
0
0
 
=
=
 
0
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
2
9


 
 
 
 
 
 
 
 
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
 
2
8


 
 
 
 
e
l
i
f
 
m
o
n
t
h
 
i
n
 
[
1
,
 
3
,
 
5
,
 
7
,
 
8
,
 
1
0
,
 
1
2
]
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
3
1


 
 
 
 
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
 
3
0






d
e
f
 
g
e
t
_
d
a
y
s
_
i
n
_
y
e
a
r
(
y
e
a
r
:
 
i
n
t
)
 
-
>
 
i
n
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
 
a
 
g
i
v
e
n
 
y
e
a
r
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
 
a
c
c
o
u
n
t
s
 
f
o
r
 
l
e
a
p
 
y
e
a
r
s
 
w
h
e
n
 
c
a
l
c
u
l
a
t
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
 
d
a
y
s
 
i
n
 
F
e
b
r
u
a
r
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
e
a
r
 
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
o
 
g
e
t
 
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
.
 
T
h
i
s
 
s
h
o
u
l
d
 
b
e
 
a
 
v
a
l
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
t
e
g
e
r
 
r
e
p
r
e
s
e
n
t
i
n
g
 
a
 
y
e
a
r
 
(
e
.
g
.
,
 
2
0
2
4
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


 
 
 
 
 
 
 
 
i
n
t
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
 
d
a
y
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
 
y
e
a
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
y
e
a
r
 
%
 
4
 
=
=
 
0
 
a
n
d
 
(
y
e
a
r
 
%
 
1
0
0
 
!
=
 
0
 
o
r
 
y
e
a
r
 
%
 
4
0
0
 
=
=
 
0
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
3
6
6


 
 
 
 
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
 
3
6
5






d
e
f
 
g
e
t
_
m
o
n
t
h
_
n
a
m
e
(
m
o
n
t
h
:
 
i
n
t
)
 
-
>
 
s
t
r
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
a
m
e
 
o
f
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
o
n
t
h
 
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
o
 
g
e
t
 
t
h
e
 
n
a
m
e
.
 
I
t
 
s
h
o
u
l
d
 
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
 
b
e
t
w
e
e
n


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
1
 
a
n
d
 
1
2
,
 
w
h
e
r
e
 
1
 
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
 
J
a
n
u
a
r
y
 
a
n
d
 
1
2
 
t
o
 
D
e
c
e
m
b
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
n
a
m
e
 
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
 
m
o
n
t
h
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
m
o
n
t
h
 
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
 
"
J
a
n
u
a
r
y
"


 
 
 
 
e
l
i
f
 
m
o
n
t
h
 
=
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
F
e
b
r
u
a
r
y
"


 
 
 
 
e
l
i
f
 
m
o
n
t
h
 
=
=
 
3
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
M
a
r
c
h
"


 
 
 
import unittest


class Tester(unittest.TestCase):

    def test_leap_year_february(self):
        """Test for leap year February."""
        self.assertEqual(get_days_in_month(2024, 2), 29)  # 2024 is a leap year

    def test_non_leap_year_february(self):
        """Test for non-leap year February."""
        self.assertEqual(get_days_in_month(2023, 2), 28)  # 2023 is not a leap year

    def test_month_with_31_days(self):
        """Test for months with 31 days."""
        self.assertEqual(get_days_in_month(2023, 1), 31)  # January has 31 days
        self.assertEqual(get_days_in_month(2023, 7), 31)  # July has 31 days

    def test_month_with_30_days(self):
        """Test for months with 30 days."""
        self.assertEqual(get_days_in_month(2023, 4), 30)  # April has 30 days
        self.assertEqual(get_days_in_month(2023, 11), 30) # November has 30 days

    def test_invalid_month(self):
        """Test for invalid months."""
        with self.assertRaises(InvalidMonthError):
            get_days_in_month(2023, 0)  # Month less than 1
        with self.assertRaises(InvalidMonthError):
            get_days_in_month(2023, 13)  # Month greater than 12

if __name__ == '__main__':
    unittest.main()