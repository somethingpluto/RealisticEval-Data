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
 
c
o
n
v
e
r
t
_
u
n
i
x
_
t
i
m
e
s
t
a
m
p
_
t
o
_
r
e
a
d
a
b
l
e
_
d
a
t
e
(
u
n
i
x
_
t
i
m
e
s
t
a
m
p
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
o
n
v
e
r
t
 
t
h
e
 
U
N
I
X
 
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
 
t
h
e
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
'
M
M
M
 
D
,
 
H
:
M
M
'
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
7
2
5
3
1
2
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
J
a
n
 
1
,
 
8
:
0
0
'




 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
9
6
5
1
6
8
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
O
c
t
 
5
,
 
2
2
:
4
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
n
i
x
_
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
i
n
t
)
:
 
T
h
e
 
U
N
I
X
 
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
 
i
n
 
t
h
e
 
f
o
r
m
 
'
M
M
M
 
D
,
 
H
:
M
M
'
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
u
n
i
x
_
t
i
m
e
s
t
a
m
p
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
'
%
b
 
%
d
,
 
%
H
:
%
M
'
)






d
e
f
 
c
o
n
v
e
r
t
_
u
n
i
x
_
t
i
m
e
s
t
a
m
p
_
t
o
_
r
e
a
d
a
b
l
e
_
d
a
t
e
_
t
i
m
e
(
u
n
i
x
_
t
i
m
e
s
t
a
m
p
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
o
n
v
e
r
t
 
t
h
e
 
U
N
I
X
 
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
 
t
h
e
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
'
M
M
M
 
D
,
 
H
:
M
M
:
S
S
'
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
7
2
5
3
1
2
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
J
a
n
 
1
,
 
8
:
0
0
:
0
0
'




 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
9
6
5
1
6
8
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
O
c
t
 
5
,
 
2
2
:
4
0
:
0
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
n
i
x
_
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
i
n
t
)
:
 
T
h
e
 
U
N
I
X
 
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
 
i
n
 
t
h
e
 
f
o
r
m
 
'
M
M
M
 
D
,
 
H
:
M
M
:
S
S
'
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
u
n
i
x
_
t
i
m
e
s
t
a
m
p
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
'
%
b
 
%
d
,
 
%
H
:
%
M
:
%
S
'
)






d
e
f
 
c
o
n
v
e
r
t
_
u
n
i
x
_
t
i
m
e
s
t
a
m
p
_
t
o
_
r
e
a
d
a
b
l
e
_
d
a
t
e
_
t
i
m
e
_
w
i
t
h
_
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
(
u
n
i
x
_
t
i
m
e
s
t
a
m
p
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
o
n
v
e
r
t
 
t
h
e
 
U
N
I
X
 
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
 
t
h
e
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
'
M
M
M
 
D
,
 
H
:
M
M
:
S
S
.
m
m
m
'
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
7
2
5
3
1
2
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
J
a
n
 
1
,
 
8
:
0
0
:
0
0
.
0
0
0
'




 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
1
6
9
6
5
1
6
8
0
0


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
'
O
c
t
 
5
,
 
2
2
:
4
0
:
0
0
.
0
0
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
n
i
x
_
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
i
n
t
)
:
 
T
h
e
 
U
N
I
X
 
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
import unittest


class TestTimestampToReadableDate(unittest.TestCase):
    def test_convert_unix_timestamp_to_readable_format(self):
        timestamp = 1696516800
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Oct 5, 22:40')

    def test_handle_timestamp_at_start_of_year(self):
        timestamp = 1672531200
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 8:00')

    def test_handle_timestamp_at_end_of_year(self):
        timestamp = 1672531199
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 7:59')

    def test_handle_timestamps_in_leap_year(self):
        timestamp = 1583020800
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Mar 1, 8:00')

    def test_convert_timestamp_to_readable_format_with_single_digit_day(self):
        timestamp = 1675190400
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Feb 1, 2:40')

    def test_handle_zero_unix_timestamp(self):
        timestamp = 0
        self.assertEqual(convert_unix_timestamp_to_readable_date(timestamp), 'Jan 1, 8:00')

if __name__ == '__main__':
    unittest.main()