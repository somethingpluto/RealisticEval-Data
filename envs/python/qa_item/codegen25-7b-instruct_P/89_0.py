d
e
f
 
t
i
m
e
_
p
a
s
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
_
i
n
_
m
i
l
l
i
s
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
 
e
l
a
p
s
e
d
 
t
i
m
e
 
f
r
o
m
 
a
 
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
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
a
n
d
 
r
e
t
u
r
n
s


 
 
 
 
i
t
 
a
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
 
s
t
r
i
n
g
 
i
n
 
"
m
i
n
u
t
e
s
:
s
e
c
o
n
d
s
"
 
f
o
r
m
a
t
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
_
i
n
_
m
i
l
l
i
s
 
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
 
m
i
l
l
i
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
 
A
 
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
 
e
l
a
p
s
e
d
 
t
i
m
e
 
i
n
 
m
i
n
u
t
e
s
 
a
n
d
 
s
e
c
o
n
d
s
.


 
 
 
 
"
"
"


 
 
 
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
m
i
l
l
i
s
 
=
 
i
n
t
(
t
i
m
e
.
t
i
m
e
(
)
 
*
 
1
0
0
0
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
_
i
n
_
m
i
l
l
i
s


 
 
 
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
s
e
c
o
n
d
s
 
=
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
m
i
l
l
i
s
 
/
 
1
0
0
0


 
 
 
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
m
i
n
u
t
e
s
 
=
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
s
e
c
o
n
d
s
 
/
 
6
0


 
 
 
 
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
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
o
u
n
d
(
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
m
i
n
u
t
e
s
,
 
2
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
e
l
a
p
s
e
d
_
t
i
m
e
_
i
n
_
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
f
i
l
e
_
n
a
m
e
_
f
r
o
m
_
u
r
l
(
u
r
l
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
f
i
l
e
 
n
a
m
e
 
f
r
o
m
 
a
 
g
i
v
e
n
 
U
R
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
e
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
n
a
m
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
 
T
h
e
 
f
i
l
e
 
n
a
m
e
 
f
r
o
m
 
t
h
e
 
U
R
L
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
 
u
r
l
.
s
p
l
i
t
(
"
/
"
)
[
-
1
]






d
e
f
 
g
e
t
_
f
i
l
e
_
s
i
z
e
_
f
r
o
m
_
u
r
l
(
u
r
l
:
 
s
t
r
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
f
r
o
m
 
a
 
g
i
v
e
n
 
U
R
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
e
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
s
i
z
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
f
r
o
m
 
t
h
e
 
U
R
L
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
 
i
n
t
(
r
e
q
u
e
s
t
s
.
h
e
a
d
(
u
r
l
)
.
h
e
a
d
e
r
s
.
g
e
t
(
"
C
o
n
t
e
n
t
-
L
e
n
g
t
h
"
,
 
0
)
)






d
e
f
 
g
e
t
_
f
i
l
e
_
s
i
z
e
_
f
r
o
m
_
p
a
t
h
(
p
a
t
h
:
 
s
t
r
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
f
r
o
m
 
a
 
g
i
v
e
n
 
p
a
t
h
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
e
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
s
i
z
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
f
r
o
m
 
t
h
e
 
p
a
t
h
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
 
o
s
.
p
a
t
h
.
g
e
t
s
i
z
e
(
p
a
t
h
)






d
e
f
 
g
e
t
_
f
i
l
e
_
s
i
z
e
(
f
i
l
e
_
p
a
t
h
_
o
r
_
u
r
l
:
 
s
t
r
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
import unittest
from unittest.mock import patch


class TestTimePassed(unittest.TestCase):

    @patch('time.time', return_value=1609459200)  # Mocking time to freeze at Jan 1, 2021, 00:00:00
    def test_time_passed_one_minute_ago(self, mock_time):
        start_time = 1609459140000  # 1 minute earlier
        self.assertEqual(time_passed(start_time), "1:00")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_boundary_59_seconds(self, mock_time):
        start_time = 1609459194100  # 59 seconds and 900 milliseconds earlier
        self.assertEqual(time_passed(start_time), "0:05")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_same_as_current_time(self, mock_time):
        self.assertEqual(time_passed(1609459200000), "0:00")

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_future_start_time(self, mock_time):
        start_time = 1609459260000  # 1 minute into the future
        result = time_passed(start_time)
        self.assertRegex(result, '-')  # Expecting negative output or some error handling

    @patch('time.time', return_value=1609459200)  # Mocking time
    def test_time_passed_large_time_difference(self, mock_time):
        start_time = 1483228800000  # January 1, 2017, 00:00:00 (4 years difference)
        self.assertEqual(time_passed(start_time), "2103840:00")  # Calculated minutes for 4 years

if __name__ == '__main__':
    unittest.main()