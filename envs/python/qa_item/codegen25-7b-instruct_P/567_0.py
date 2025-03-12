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






d
e
f
 
g
e
t
_
r
e
l
a
t
i
v
e
_
t
i
m
e
(
m
e
s
s
a
g
e
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
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
.




 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
t
o
d
a
y
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
 
"
T
o
d
a
y
"
.


 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
y
e
s
t
e
r
d
a
y
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
 
"
Y
e
s
t
e
r
d
a
y
"
.


 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
w
i
t
h
i
n
 
t
h
e
 
p
a
s
t
 
w
e
e
k
 
(
b
u
t
 
n
o
t
 
t
o
d
a
y
 
o
r
 
y
e
s
t
e
r
d
a
y
)
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
i
n
g
 
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
 
(
e
.
g
.
,
 
"
M
o
n
d
a
y
"
)
.


 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
e
a
r
l
i
e
r
 
t
h
a
n
 
o
n
e
 
w
e
e
k
 
a
g
o
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
 
a
 
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


 
 
 
 
 
 
(
e
.
g
.
,
 
"
Y
Y
Y
Y
/
M
M
/
D
D
"
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
e
s
s
a
g
e
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
 
d
a
t
e
 
w
h
e
n
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
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
 
i
n
d
i
c
a
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
 
t
o
 
t
h
e
 
m
e
s
s
a
g
e
 
c
r
e
a
t
i
o
n
 
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
i
f
f
 
=
 
n
o
w
 
-
 
m
e
s
s
a
g
e
_
d
a
t
e


 
 
 
 
d
i
f
f
_
d
a
y
s
 
=
 
d
i
f
f
.
d
a
y
s


 
 
 
 
d
i
f
f
_
s
e
c
o
n
d
s
 
=
 
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




 
 
 
 
i
f
 
d
i
f
f
_
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
_
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
 
"
T
o
d
a
y
"


 
 
 
 
 
 
 
 
e
l
i
f
 
d
i
f
f
_
s
e
c
o
n
d
s
 
<
 
8
6
4
0
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
Y
e
s
t
e
r
d
a
y
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
 
"
T
o
d
a
y
"


 
 
 
 
e
l
i
f
 
d
i
f
f
_
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
Y
e
s
t
e
r
d
a
y
"


 
 
 
 
e
l
i
f
 
d
i
f
f
_
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
 
m
e
s
s
a
g
e
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
"
%
A
"
)


 
 
 
 
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
 
m
e
s
s
a
g
e
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
"
%
Y
/
%
m
/
%
d
"
)






d
e
f
 
g
e
t
_
m
e
s
s
a
g
e
_
t
i
m
e
(
m
e
s
s
a
g
e
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
 
t
i
m
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
m
e
s
s
a
g
e
.




 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
i
n
 
t
h
e
 
p
a
s
t
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
 
a
 
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
 
(
e
.
g
.
,
 
"
Y
Y
Y
Y
/
M
M
/
D
D
 
H
H
:
M
M
:
S
S
"
)
.


 
 
 
 
-
 
I
f
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
 
i
n
 
t
h
e
 
f
u
t
u
r
e
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
 
a
 
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
 
(
e
.
g
.
,
 
"
Y
Y
Y
Y
/
M
M
/
D
D
 
H
H
:
M
M
:
S
S
 
(
i
n
 
t
h
e
 
f
u
t
u
r
e
)
"
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
e
s
s
a
g
e
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
 
d
a
t
e
 
w
h
e
n
 
t
h
e
 
m
e
s
s
a
g
e
 
w
a
s
 
c
r
e
a
t
e
d
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
 
i
n
d
i
c
a
t
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
 
o
f
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch


class TestGetRelativeTime(unittest.TestCase):

    @patch('datetime.datetime')
    def setUp(self, mock_datetime):
        # Mock the current date to ensure consistent test results
        self.mock_now = datetime(2024, 10, 1)
        mock_datetime.now.return_value = self.mock_now

    def test_should_return_today_for_a_message_created_today(self):
        message_date = datetime.now()  # Current date
        self.assertEqual(get_relative_time(message_date), "Today")

    def test_should_return_yesterday_for_a_message_created_yesterday(self):
        message_date = datetime.now() - timedelta(days=1)  # Yesterday
        self.assertEqual(get_relative_time(message_date), "Yesterday")

    def test_should_return_formatted_date_string_for_a_message_created_10_days_ago(self):
        message_date = datetime.now() - timedelta(days=10)  # 10 days ago
        self.assertEqual(get_relative_time(message_date), "2024/09/21")  # Adjust based on the mock date

    def test_should_return_formatted_date_string_for_a_message_created_15_days_ago(self):
        message_date = datetime.now() - timedelta(days=15)  # 15 days ago
        self.assertEqual(get_relative_time(message_date), "2024/09/16")  # Adjust based on the mock date

if __name__ == '__main__':
    unittest.main()