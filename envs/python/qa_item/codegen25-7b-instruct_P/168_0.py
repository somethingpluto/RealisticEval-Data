d
e
f
 
f
o
r
m
a
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
_
s
t
r
i
n
g
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
d
a
t
e
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
r
e
l
a
t
i
v
e
 
t
i
m
e
 
d
e
s
c
r
i
p
t
i
o
n
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
 
n
o
w
 
t
i
m
e
 
2
0
2
4
-
0
8
-
2
5
T
1
2
:
0
0
:
0
0


 
 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4
-
0
8
-
2
4
T
1
2
:
0
0
:
0
0
 
o
u
t
p
u
t
:
 
1
 
d
a
y
 
a
g
o


 
 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4
-
0
8
-
2
5
T
0
7
:
0
0
:
0
0
 
o
u
t
p
u
t
:
 
5
 
h
o
u
r
s
 
a
g
o




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
e
_
s
t
r
i
n
g
 
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
 
s
t
r
i
n
g
 
t
o
 
c
o
n
v
e
r
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
 
u
s
e
r
-
f
r
i
e
n
d
l
y
 
s
t
r
i
n
g
 
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
 
t
h
e
 
r
e
l
a
t
i
v
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
 
f
r
o
m
 
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


 
 
 
 
d
a
t
e
_
s
t
r
i
n
g
 
=
 
d
a
t
e
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
T
"
,
 
"
 
"
)


 
 
 
 
d
a
t
e
_
s
t
r
i
n
g
 
=
 
d
a
t
e
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
Z
"
,
 
"
"
)


 
 
 
 
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
d
a
t
e
_
s
t
r
i
n
g
,
 
"
%
Y
-
%
m
-
%
d
 
%
H
:
%
M
:
%
S
"
)


 
 
 
 
d
i
f
f
 
=
 
n
o
w
 
-
 
d
a
t
e


 
 
 
 
i
f
 
d
i
f
f
.
d
a
y
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
i
f
 
d
i
f
f
.
s
e
c
o
n
d
s
 
<
 
6
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
d
i
f
f
.
s
e
c
o
n
d
s
}
 
s
e
c
o
n
d
s
 
a
g
o
"


 
 
 
 
 
 
 
 
e
l
i
f
 
d
i
f
f
.
s
e
c
o
n
d
s
 
<
 
3
6
0
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
d
i
f
f
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
}
 
m
i
n
u
t
e
s
 
a
g
o
"


 
 
 
 
 
 
 
 
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
"
{
d
i
f
f
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
 
3
6
0
0
}
 
h
o
u
r
s
 
a
g
o
"


 
 
 
 
e
l
i
f
 
d
i
f
f
.
d
a
y
s
 
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
1
 
d
a
y
 
a
g
o
"


 
 
 
 
e
l
i
f
 
d
i
f
f
.
d
a
y
s
 
<
 
7
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
d
i
f
f
.
d
a
y
s
}
 
d
a
y
s
 
a
g
o
"


 
 
 
 
e
l
i
f
 
d
i
f
f
.
d
a
y
s
 
<
 
3
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
d
i
f
f
.
d
a
y
s
 
/
/
 
7
}
 
w
e
e
k
s
 
a
g
o
"


 
 
 
 
e
l
i
f
 
d
i
f
f
.
d
a
y
s
 
<
 
3
6
5
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
d
i
f
f
.
d
a
y
s
 
/
/
 
3
0
}
 
m
o
n
t
h
s
 
a
g
o
"


 
 
 
 
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
"
{
d
i
f
f
.
d
a
y
s
 
/
/
 
3
6
5
}
 
y
e
a
r
s
 
a
g
o
"






d
e
f
 
f
o
r
m
a
t
_
t
i
m
e
(
t
i
m
e
_
s
t
r
i
n
g
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
t
i
m
e
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
r
e
l
a
t
i
v
e
 
t
i
m
e
 
d
e
s
c
r
i
p
t
i
o
n
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
 
n
o
w
 
t
i
m
e
 
2
0
2
4
-
0
8
-
2
5
T
1
2
:
0
0
:
0
0


 
 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4
-
0
8
-
2
4
T
1
2
:
0
0
:
0
0
 
o
u
t
p
u
t
:
 
1
 
d
a
y
 
a
g
o


 
 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4
-
0
8
-
2
5
T
0
7
:
0
0
:
0
0
 
o
u
t
p
u
t
:
 
5
 
h
o
u
r
s
 
a
g
o




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
T
h
e
 
t
i
m
e
 
s
t
r
i
n
g
 
t
o
 
c
o
n
v
e
r
t
.




 
 
 
import unittest
from datetime import datetime
from unittest.mock import patch


class TestFormatDate(unittest.TestCase):

    @patch('your_module.datetime')
    def setUp(self, mock_datetime):
        # Set the system time to a fixed date for consistent testing
        mock_datetime.now.return_value = datetime(2024, 8, 25, 12, 0, 0)

    def test_one_day_ago(self):
        date_string = '2024-08-24T12:00:00'
        result = format_date(date_string)
        self.assertIn(result, ['1 day ago', '24 hours ago'])

    def test_five_hours_ago(self):
        date_string = '2024-08-25T07:00:00'
        result = format_date(date_string)
        self.assertEqual(result, '5 hours ago')

    def test_two_minutes_ago(self):
        date_string = '2024-08-25T11:58:00'
        result = format_date(date_string)
        self.assertEqual(result, '2 minutes ago')

    def test_just_now(self):
        date_string = '2024-08-25T11:59:59'
        result = format_date(date_string)
        self.assertIn(result, ['1 second ago', '1 seconds ago'])

if __name__ == '__main__':
    unittest.main()