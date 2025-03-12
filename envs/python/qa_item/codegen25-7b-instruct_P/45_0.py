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
 
g
e
t
_
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
_
i
n
f
o
(
t
e
s
t
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
.
d
a
t
e
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
 
c
u
r
r
e
n
t
 
t
i
m
e
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
c
l
u
d
i
n
g
 
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
,
 
a
n
d
 
d
a
y
 
o
f
.
e
g
 
{


 
 
 
 
 
 
 
 
 
 
 
 
'
y
e
a
r
'
:
 
2
0
2
4
,


 
 
 
 
 
 
 
 
 
 
 
 
'
m
o
n
t
h
'
:
 
'
F
e
b
r
u
a
r
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
'
w
e
e
k
_
o
f
_
t
h
e
_
m
o
n
t
h
'
:
 
5
,


 
 
 
 
 
 
 
 
 
 
 
 
'
d
a
y
_
o
f
_
t
h
e
_
w
e
e
k
'
:
 
'
T
h
u
r
s
d
a
y
'


 
 
 
 
 
 
 
 
}




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
s
t
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
.
d
a
t
e
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
u
t
e
 
i
n
f
o
r
m
a
t
i
o
n
 
f
o
r
,
 
d
e
f
a
u
l
t
s
 
t
o
 
t
o
d
a
y
'
s
 
d
a
t
e
 
i
f
 
n
o
t
 
p
r
o
v
i
d
e
d
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
 
t
h
e
 
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
,
 
a
n
d
 
d
a
y
 
o
f
 
t
h
e
 
w
e
e
k
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
t
e
s
t
_
d
a
t
e
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
t
e
s
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
d
a
t
e
.
t
o
d
a
y
(
)




 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
'
y
e
a
r
'
:
 
t
e
s
t
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
,


 
 
 
 
 
 
 
 
'
m
o
n
t
h
'
:
 
t
e
s
t
_
d
a
t
e
.
s
t
r
f
t
i
m
e
(
'
%
B
'
)
,


 
 
 
 
 
 
 
 
'
w
e
e
k
_
o
f
_
t
h
e
_
m
o
n
t
h
'
:
 
t
e
s
t
_
d
a
t
e
.
i
s
o
c
a
l
e
n
d
a
r
(
)
[
1
]
,


 
 
 
 
 
 
 
 
'
d
a
y
_
o
f
_
t
h
e
_
w
e
e
k
'
:
 
t
e
s
t
_
d
a
t
e
.
s
t
r
f
t
i
m
e
(
'
%
A
'
)


 
 
 
 
}






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
i
n
f
o
(
t
e
s
t
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
.
d
a
t
e
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
 
m
o
n
t
h
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
c
l
u
d
i
n
g
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
d
a
t
e
s
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
s
t
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
.
d
a
t
e
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
u
t
e
 
i
n
f
o
r
m
a
t
i
o
n
 
f
o
r
,
 
d
e
f
a
u
l
t
s
 
t
o
 
t
o
d
a
y
'
s
 
d
a
t
e
 
i
f
 
n
o
t
 
p
r
o
v
i
d
e
d
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
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
d
a
t
e
s
 
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
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
t
e
s
t
_
d
a
t
e
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
t
e
s
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
d
a
t
e
.
t
o
d
a
y
(
)




 
 
 
 
m
o
n
t
h
_
s
t
a
r
t
 
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
t
e
s
t
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
,
 
t
e
s
t
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
,
 
1
)


 
 
 
 
m
o
n
t
h
_
e
n
d
 
=
 
m
o
n
t
h
_
s
t
a
r
t
 
+
 
d
a
t
e
t
i
m
e
.
t
i
m
e
d
e
l
t
a
(
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
t
e
s
t
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
,
 
t
e
s
t
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
)
[
1
]
 
-
 
1
)




 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
'
s
t
a
r
t
_
d
a
t
e
'
:
 
m
o
n
t
h
_
s
t
a
r
t
,


 
 
 
 
 
 
 
 
'
e
n
d
_
d
a
t
e
'
:
 
m
o
n
t
h
_
e
n
d


 
 
 
 
}






d
e
f
 
g
e
t
_
w
e
e
k
_
i
n
f
o
(
t
e
s
t
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
.
d
a
t
e
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
 
w
e
e
k
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
c
l
u
d
i
n
g
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
d
a
t
e
s
 
o
f
 
t
h
e
 
w
e
e
k
.




 
 
 
 
A
r
import unittest
import datetime


class TestGetCurrentDateInfo(unittest.TestCase):

    def test_beginning_of_month(self):
        result = get_current_date_info(datetime.date(2023, 1, 1))
        expected = {
            'year': 2023,
            'month': 'January',
            'week_of_the_month': 1,
            'day_of_the_week': 'Sunday'
        }
        self.assertEqual(result, expected)

    def test_middle_of_month(self):
        result = get_current_date_info(datetime.date(2023, 1, 15))
        expected = {
            'year': 2023,
            'month': 'January',
            'week_of_the_month': 3,
            'day_of_the_week': 'Sunday'
        }
        self.assertEqual(result, expected)

    def test_leap_year(self):
        result = get_current_date_info(datetime.date(2024, 2, 29))
        expected = {
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }
        self.assertEqual(result, expected)

    def test_change_of_year(self):
        result = get_current_date_info(datetime.date(2022, 12, 31))
        expected = {
            'year': 2022,
            'month': 'December',
            'week_of_the_month': 5,
            'day_of_the_week': 'Saturday'
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()