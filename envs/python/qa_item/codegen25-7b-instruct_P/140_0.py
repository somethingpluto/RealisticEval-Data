f
r
o
m
 
d
a
t
e
t
i
m
e
 
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






d
e
f
 
g
e
t
_
t
i
m
e
_
s
i
n
c
e
_
b
o
r
n
_
u
n
t
i
l
_
n
o
w
(
b
i
r
t
h
_
d
a
t
e
:
 
d
a
t
e
t
i
m
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
i
n
t
,
 
i
n
t
,
 
i
n
t
,
 
i
n
t
,
 
i
n
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
 
t
h
e
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
a
n
d
 
m
i
n
u
t
e
s
 
t
h
a
t
 
h
a
v
e
 
p
a
s
s
e
d


 
 
 
 
f
r
o
m
 
t
h
e
 
b
i
r
t
h
 
d
a
t
e
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
d
a
t
e
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m
 
a
s
 
a
 
t
u
p
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
r
t
h
_
d
a
t
e
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
b
i
r
t
h
 
d
a
t
e
 
a
s
 
a
 
d
a
t
e
t
i
m
e
 
o
b
j
e
c
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
,
 
i
n
t
,
 
i
n
t
,
 
i
n
t
]
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
 
v
a
l
u
e
s
 
o
f
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
a
n
d
 
m
i
n
u
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
n
o
w
 
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
n
o
w
(
)


 
 
 
 
y
e
a
r
s
 
=
 
n
o
w
.
y
e
a
r
 
-
 
b
i
r
t
h
_
d
a
t
e
.
y
e
a
r


 
 
 
 
m
o
n
t
h
s
 
=
 
n
o
w
.
m
o
n
t
h
 
-
 
b
i
r
t
h
_
d
a
t
e
.
m
o
n
t
h


 
 
 
 
d
a
y
s
 
=
 
n
o
w
.
d
a
y
 
-
 
b
i
r
t
h
_
d
a
t
e
.
d
a
y


 
 
 
 
h
o
u
r
s
 
=
 
n
o
w
.
h
o
u
r
 
-
 
b
i
r
t
h
_
d
a
t
e
.
h
o
u
r


 
 
 
 
m
i
n
u
t
e
s
 
=
 
n
o
w
.
m
i
n
u
t
e
 
-
 
b
i
r
t
h
_
d
a
t
e
.
m
i
n
u
t
e


 
 
 
 
r
e
t
u
r
n
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s






d
e
f
 
g
e
t
_
t
i
m
e
_
s
i
n
c
e
_
b
o
r
n
_
u
n
t
i
l
_
n
o
w
_
a
s
_
s
t
r
i
n
g
(
b
i
r
t
h
_
d
a
t
e
:
 
d
a
t
e
t
i
m
e
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
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
a
n
d
 
m
i
n
u
t
e
s
 
t
h
a
t
 
h
a
v
e
 
p
a
s
s
e
d


 
 
 
 
f
r
o
m
 
t
h
e
 
b
i
r
t
h
 
d
a
t
e
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
d
a
t
e
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m
 
a
s
 
a
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
r
t
h
_
d
a
t
e
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
b
i
r
t
h
 
d
a
t
e
 
a
s
 
a
 
d
a
t
e
t
i
m
e
 
o
b
j
e
c
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
s
t
r
i
n
g
 
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
 
o
f
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
a
n
d
 
m
i
n
u
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
 
=
 
g
e
t
_
t
i
m
e
_
s
i
n
c
e
_
b
o
r
n
_
u
n
t
i
l
_
n
o
w
(
b
i
r
t
h
_
d
a
t
e
)


 
 
 
 
r
e
t
u
r
n
 
f
"
{
y
e
a
r
s
}
 
y
e
a
r
s
,
 
{
m
o
n
t
h
s
}
 
m
o
n
t
h
s
,
 
{
d
a
y
s
}
 
d
a
y
s
,
 
{
h
o
u
r
s
}
 
h
o
u
r
s
,
 
{
m
i
n
u
t
e
s
}
 
m
i
n
u
t
e
s
"






d
e
f
 
g
e
t
_
t
i
m
e
_
s
i
n
c
e
_
b
o
r
n
_
u
n
t
i
l
_
n
o
w
_
a
s
_
s
t
r
i
n
g
_
w
i
t
h
_
s
u
f
f
i
x
(
b
i
r
t
h
_
d
a
t
e
:
 
d
a
t
e
t
i
m
e
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
 
y
e
a
r
s
,
 
m
o
n
t
h
s
,
 
d
a
y
s
,
 
h
o
u
r
s
,
 
a
n
d
 
m
i
n
u
t
e
s
 
t
h
a
t
 
h
a
v
e
 
p
a
s
s
e
d


 
 
 
 
f
r
o
m
 
t
h
e
 
b
i
r
t
h
 
d
a
t
e
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
d
a
t
e
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m
 
a
s
 
a
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
r
t
h
_
d
a
t
e
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
b
i
r
t
h
 
d
a
t
e
 
a
s
 
a
 
d
a
t
e
t
i
m
e
 
o
b
j
e
c
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


 
 
 
 
 
 
 
import unittest
from datetime import datetime, timedelta

# Assuming the function get_time_since_born_until_now is defined here

class TestGetTimeSinceBornUntilNow(unittest.TestCase):

    def setUp(self):
        # Set the system time to a fixed date
        self.fixed_time = datetime(2024, 8, 23, 15, 45)
        # Mock datetime.now() for the tests
        self.original_datetime_now = datetime.now

        def mock_datetime_now():
            return self.fixed_time
        
        datetime.now = mock_datetime_now

    def tearDown(self):
        # Restore original datetime.now
        datetime.now = self.original_datetime_now

    def test_typical_birth_date(self):
        birth_date = datetime(1990, 5, 15, 10, 30)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (34, 3, 8, 5, 15))  # 34 years, 3 months, 8 days, 5 hours, 15 minutes

    def test_recent_birth_date(self):
        birth_date = datetime(2024, 8, 20, 12, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 3, 3, 45))  # 3 days, 3 hours, 45 minutes

    def test_edge_case_end_of_year(self):
        birth_date = datetime(2023, 12, 31, 23, 59)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 7, 22, 15, 46))  # 7 months, 22 days, 15 hours, 46 minutes

    def test_birthday_earlier_in_month(self):
        birth_date = datetime(2024, 8, 1, 0, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 22, 15, 45))  # 22 days, 15 hours, 45 minutes

    def test_birthday_later_in_year_before_month(self):
        birth_date = datetime(2024, 1, 1, 1, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 7, 22, 14, 45))  # 7 months, 22 days, 14 hours, 45 minutes

    def test_birthday_previous_month(self):
        birth_date = datetime(2024, 7, 30, 10, 0)
        result = get_time_since_born_until_now(birth_date)
        self.assertEqual(result, (0, 0, 24, 5, 45))  # 24 days, 5 hours, 45 minutes
if __name__ == '__main__':
    unittest.main()