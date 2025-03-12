d
e
f
 
i
s
_
s
a
m
e
_
d
a
y
(
t
i
m
e
s
t
a
m
p
1
:
 
i
n
t
,
 
t
i
m
e
s
t
a
m
p
2
:
 
i
n
t
)
 
-
>
 
b
o
o
l
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
 
i
f
 
t
w
o
 
t
i
m
e
s
t
a
m
p
s
 
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
 
t
o
 
t
h
e
 
s
a
m
e
 
d
a
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
1
 
(
i
n
t
)
:
 
T
h
e
 
f
i
r
s
t
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
r
e
.


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
2
 
(
i
n
t
)
:
 
T
h
e
 
s
e
c
o
n
d
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
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
 
b
o
t
h
 
t
i
m
e
s
t
a
m
p
s
 
a
r
e
 
o
n
 
t
h
e
 
s
a
m
e
 
d
a
y
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
1
)
.
d
a
t
e
(
)
 
=
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
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
2
)
.
d
a
t
e
(
)






d
e
f
 
i
s
_
s
a
m
e
_
h
o
u
r
(
t
i
m
e
s
t
a
m
p
1
:
 
i
n
t
,
 
t
i
m
e
s
t
a
m
p
2
:
 
i
n
t
)
 
-
>
 
b
o
o
l
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
 
i
f
 
t
w
o
 
t
i
m
e
s
t
a
m
p
s
 
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
 
t
o
 
t
h
e
 
s
a
m
e
 
h
o
u
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
1
 
(
i
n
t
)
:
 
T
h
e
 
f
i
r
s
t
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
r
e
.


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
2
 
(
i
n
t
)
:
 
T
h
e
 
s
e
c
o
n
d
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
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
 
b
o
t
h
 
t
i
m
e
s
t
a
m
p
s
 
a
r
e
 
o
n
 
t
h
e
 
s
a
m
e
 
h
o
u
r
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
1
)
.
h
o
u
r
 
=
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
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
2
)
.
h
o
u
r






d
e
f
 
i
s
_
s
a
m
e
_
m
i
n
u
t
e
(
t
i
m
e
s
t
a
m
p
1
:
 
i
n
t
,
 
t
i
m
e
s
t
a
m
p
2
:
 
i
n
t
)
 
-
>
 
b
o
o
l
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
 
i
f
 
t
w
o
 
t
i
m
e
s
t
a
m
p
s
 
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
 
t
o
 
t
h
e
 
s
a
m
e
 
m
i
n
u
t
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
1
 
(
i
n
t
)
:
 
T
h
e
 
f
i
r
s
t
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
r
e
.


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
2
 
(
i
n
t
)
:
 
T
h
e
 
s
e
c
o
n
d
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
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
 
b
o
t
h
 
t
i
m
e
s
t
a
m
p
s
 
a
r
e
 
o
n
 
t
h
e
 
s
a
m
e
 
m
i
n
u
t
e
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
1
)
.
m
i
n
u
t
e
 
=
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
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
2
)
.
m
i
n
u
t
e






d
e
f
 
i
s
_
s
a
m
e
_
s
e
c
o
n
d
(
t
i
m
e
s
t
a
m
p
1
:
 
i
n
t
,
 
t
i
m
e
s
t
a
m
p
2
:
 
i
n
t
)
 
-
>
 
b
o
o
l
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
 
i
f
 
t
w
o
 
t
i
m
e
s
t
a
m
p
s
 
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
 
t
o
 
t
h
e
 
s
a
m
e
 
s
e
c
o
n
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
1
 
(
i
n
t
)
:
 
T
h
e
 
f
i
r
s
t
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
r
e
.


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
2
 
(
i
n
t
)
:
 
T
h
e
 
s
e
c
o
n
d
 
t
i
m
e
s
t
a
m
p
 
t
o
 
c
o
m
p
a
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
 
b
o
t
h
 
t
i
m
e
s
t
a
m
p
s
 
a
r
e
 
o
n
 
t
h
e
 
s
a
m
e
 
s
e
c
o
n
d
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
1
)
.
s
e
c
o
n
d
 
=
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
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
2
)
.
s
e
c
o
n
d






d
e
f
 
i
s
import unittest
from datetime import datetime


class TestIsSameDay(unittest.TestCase):

    def test_different_days(self):
        timestamp1 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # October 1, 2024, 10:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 2, 10, 0, 0).timestamp())  # October 2, 2024, 10:00 AM UTC
        self.assertFalse(is_same_day(timestamp1, timestamp2))

    def test_same_day_different_times(self):
        timestamp1 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # October 1, 2024, 12:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 12, 30, 0).timestamp())  # October 1, 2024, 12:30 PM UTC
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_same_day_different_time_zones(self):
        timestamp1 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # UTC
        timestamp2 = int(datetime.fromisoformat('2024-10-01T12:00:00+02:00').timestamp())  # October 1, 2024, 12:00 PM UTC+2
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_midnight_same_day(self):
        timestamp1 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # October 1, 2024, 12:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 0, 0, 0).timestamp())  # Same timestamp
        self.assertTrue(is_same_day(timestamp1, timestamp2))

    def test_different_years(self):
        timestamp1 = int(datetime(2023, 10, 1, 10, 0, 0).timestamp())  # October 1, 2023, 10:00 AM UTC
        timestamp2 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # October 1, 2024, 10:00 AM UTC
        self.assertFalse(is_same_day(timestamp1, timestamp2))

    def test_invalid_timestamps(self):
        timestamp1 = int(datetime.fromisoformat('invalid').timestamp())  # This will raise an error, so handle it
        timestamp2 = int(datetime(2024, 10, 1, 10, 0, 0).timestamp())  # Valid timestamp
        with self.assertRaises(ValueError):
            is_same_day(timestamp1, timestamp2)

if __name__ == '__main__':
    unittest.main()