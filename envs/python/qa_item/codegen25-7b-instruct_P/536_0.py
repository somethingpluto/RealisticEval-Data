d
e
f
 
g
e
t
_
d
a
t
e
(
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


 
 
 
 
G
e
t
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
 
d
a
t
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
M
o
n
t
h
 
D
a
y
,
 
Y
e
a
r
'
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
 
f
o
r
m
a
t
t
e
d
 
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
n
o
w
(
)
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
"
%
B
 
%
d
,
 
%
Y
"
)






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
(
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


 
 
 
 
G
e
t
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
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
H
o
u
r
:
M
i
n
u
t
e
:
S
e
c
o
n
d
'
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
 
f
o
r
m
a
t
t
e
d
 
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
n
o
w
(
)
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
"
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
e
l
a
p
s
e
d
(
s
t
a
r
t
_
t
i
m
e
:
 
f
l
o
a
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


 
 
 
 
G
e
t
s
 
t
h
e
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
i
n
c
e
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
t
i
m
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
H
o
u
r
:
M
i
n
u
t
e
:
S
e
c
o
n
d
'
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
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
 
s
t
a
r
t
 
t
i
m
e
 
i
n
 
s
e
c
o
n
d
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
o
r
m
a
t
t
e
d
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
t
r
i
n
g
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
 
s
t
r
(
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
s
e
c
o
n
d
s
=
t
i
m
e
(
)
 
-
 
s
t
a
r
t
_
t
i
m
e
)
)






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
e
l
a
p
s
e
d
_
s
i
n
c
e
(
s
t
a
r
t
_
t
i
m
e
:
 
f
l
o
a
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


 
 
 
 
G
e
t
s
 
t
h
e
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
i
n
c
e
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
t
i
m
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
M
i
n
u
t
e
s
:
S
e
c
o
n
d
s
'
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
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
 
s
t
a
r
t
 
t
i
m
e
 
i
n
 
s
e
c
o
n
d
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
o
r
m
a
t
t
e
d
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
t
r
i
n
g
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
 
s
t
r
(
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
s
e
c
o
n
d
s
=
t
i
m
e
(
)
 
-
 
s
t
a
r
t
_
t
i
m
e
)
)
.
s
p
l
i
t
(
"
:
"
)
[
1
]






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
(
s
t
a
r
t
_
t
i
m
e
:
 
f
l
o
a
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


 
 
 
 
G
e
t
s
 
t
h
e
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
i
n
c
e
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
t
i
m
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
M
i
n
u
t
e
s
:
S
e
c
o
n
d
s
'
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
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
 
s
t
a
r
t
 
t
i
m
e
 
i
n
 
s
e
c
o
n
d
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
o
r
m
a
t
t
e
d
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
t
r
i
n
g
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
 
s
t
r
(
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
s
e
c
o
n
d
s
=
t
i
m
e
(
)
 
-
 
s
t
a
r
t
_
t
i
m
e
)
)
.
s
p
l
i
t
(
"
:
"
)
[
1
]






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
d
a
t
e
(
s
t
a
r
t
_
t
i
m
e
:
 
f
l
o
a
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


 
 
 
 
G
e
t
s
 
t
h
e
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
i
n
c
e
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
t
i
m
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
'
M
o
n
t
h
 
D
a
y
,
 
Y
e
a
r
 
H
o
u
r
:
M
i
n
u
t
e
:
S
e
c
o
n
d
'
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
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
 
s
t
a
r
t
 
t
i
m
e
 
i
n
 
s
e
c
o
n
d
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
o
r
m
a
t
t
e
d
 
t
i
m
e
 
e
l
a
p
s
e
d
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


import unittest
from datetime import datetime
from unittest.mock import patch


class TestGetDate(unittest.TestCase):

    @patch('datetime.datetime')
    def setUp(self, mock_datetime):
        # Mock the datetime to return a specific date
        mock_datetime.now.return_value = datetime(2024, 10, 1)

    def test_returns_date_in_format(self):
        result = get_date()
        self.assertEqual(result, 'October 1, 2024')

    def test_returns_correct_year(self):
        result = get_date()
        self.assertIn('2024', result)

    def test_returns_correct_month(self):
        result = get_date()
        self.assertIn('October', result)

    def test_returns_correct_day(self):
        result = get_date()
        self.assertIn('1', result)

    def test_returns_date_as_string(self):
        result = get_date()
        self.assertIsInstance(result, str)

    def test_does_not_return_none(self):
        result = get_date()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()