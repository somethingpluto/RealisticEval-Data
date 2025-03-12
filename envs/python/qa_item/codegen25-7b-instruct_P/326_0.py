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
i
m
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
g
i
v
e
n
_
d
a
t
e
:
 
s
t
r
)
 
-
>
 
d
i
c
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
 
t
i
m
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
 
a
 
g
i
v
e
n
 
d
a
t
e
 
a
n
d
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
g
i
v
e
n
_
d
a
t
e
 
(
s
t
r
)
:
 
T
h
e
 
d
a
t
e
 
t
o
 
c
o
m
p
a
r
e
 
a
g
a
i
n
s
t
 
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
i
c
t
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
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
 
e
l
a
p
s
e
d
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
d
a
y
s
'
:
 
d
a
y
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
h
o
u
r
s
'
:
 
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
h
o
u
r
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
m
i
n
u
t
e
s
'
:
 
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
m
i
n
u
t
e
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
}


 
 
 
 
"
"
"


 
 
 
 
c
u
r
r
e
n
t
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
n
o
w
(
)


 
 
 
 
g
i
v
e
n
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
s
t
r
p
t
i
m
e
(
g
i
v
e
n
_
d
a
t
e
,
 
'
%
Y
-
%
m
-
%
d
'
)


 
 
 
 
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
 
=
 
c
u
r
r
e
n
t
_
d
a
t
e
 
-
 
g
i
v
e
n
_
d
a
t
e


 
 
 
 
d
a
y
s
 
=
 
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
.
d
a
y
s


 
 
 
 
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
m
i
n
u
t
e
s
 
=
 
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
.
s
e
c
o
n
d
s
 
/
/
 
6
0


 
 
 
 
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
h
o
u
r
s
 
=
 
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
m
i
n
u
t
e
s
 
/
/
 
6
0


 
 
 
 
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
m
i
n
u
t
e
s
 
=
 
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
m
i
n
u
t
e
s
 
%
 
6
0


 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
'
d
a
y
s
'
:
 
d
a
y
s
,


 
 
 
 
 
 
 
 
'
h
o
u
r
s
'
:
 
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
h
o
u
r
s
,


 
 
 
 
 
 
 
 
'
m
i
n
u
t
e
s
'
:
 
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
m
i
n
u
t
e
s
,


 
 
 
 
}






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
s
t
r
i
n
g
(
g
i
v
e
n
_
d
a
t
e
:
 
s
t
r
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
 
a
 
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
 
t
i
m
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
 
a
 
g
i
v
e
n
 
d
a
t
e
 
a
n
d
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
g
i
v
e
n
_
d
a
t
e
 
(
s
t
r
)
:
 
T
h
e
 
d
a
t
e
 
t
o
 
c
o
m
p
a
r
e
 
a
g
a
i
n
s
t
 
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
 
t
i
m
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
 
a
 
g
i
v
e
n
 
d
a
t
e
 
a
n
d
 
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
.


 
 
 
 
"
"
"


 
 
 
 
t
i
m
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
 
=
 
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
i
m
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
g
i
v
e
n
_
d
a
t
e
)


 
 
 
 
d
a
y
s
 
=
 
t
i
m
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
[
'
d
a
y
s
'
]


 
 
 
 
h
o
u
r
s
 
=
 
t
i
m
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
[
'
h
o
u
r
s
'
]


 
 
 
 
m
i
n
u
t
e
s
 
=
 
t
i
m
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
[
'
m
i
n
u
t
e
s
'
]


 
 
 
 
i
f
 
d
a
y
s
 
>
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
'
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
'


 
 
 
 
e
l
i
f
 
h
o
u
r
s
 
>
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
'
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
'


 
 
 
 
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
 
f
'
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
'






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
s
t
r
i
n
g
_
f
r
o
m
_
n
o
w
(
g
i
v
e
n
_
d
a
t
e
:
 
s
t
r
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
 
a
 
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
 
t
i
m
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
 
a
 
g
i
v
e
n
 
d
a
t
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
g
i
v
e
n
_
d
a
t
e
 
(
s
t
r
)
:
 
T
h
e
 
d
a
t
e
 
t
o
 
c
o
m
p
a
r
e
import unittest
from datetime import timedelta, datetime


class TestCalculateTimeDifference(unittest.TestCase):

    def test_should_return_correct_time_difference_for_a_date_in_the_past(self):
        past_date = datetime.now() - timedelta(days=3, minutes=5)  # 3 days and 5 minutes ago
        result = calculate_time_difference(past_date)
        self.assertEqual(result, {'days': 3, 'hours': 0, 'minutes': 5})

    def test_should_return_correct_time_difference_for_a_date_that_is_exactly_now(self):
        now = datetime.now()
        result = calculate_time_difference(now)
        self.assertEqual(result, {'days': 0, 'hours': 0, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_just_seconds_ago(self):
        just_now = datetime.now() - timedelta(seconds=45)  # 45 seconds ago
        result = calculate_time_difference(just_now)
        self.assertEqual(result, {'days': 0, 'hours': 0, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_with_only_hours_difference(self):
        hours_ago = datetime.now() - timedelta(hours=7)  # 7 hours ago
        result = calculate_time_difference(hours_ago)
        self.assertEqual(result, {'days': 0, 'hours': 7, 'minutes': 0})

    def test_should_return_correct_time_difference_for_a_date_with_hours_and_minutes_difference(self):
        hours_and_minutes_ago = datetime.now() - timedelta(days=1, minutes=3)  # 1 day and 3 minutes ago
        result = calculate_time_difference(hours_and_minutes_ago)
        self.assertEqual(result, {'days': 1, 'hours': 0, 'minutes': 3})

if __name__ == '__main__':
    unittest.main()