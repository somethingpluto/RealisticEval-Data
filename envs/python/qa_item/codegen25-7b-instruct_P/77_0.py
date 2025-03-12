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
 
O
p
t
i
o
n
a
l






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
s
t
a
m
p
_
t
o
_
s
t
r
i
n
g
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
:
 
f
l
o
a
t
,
 
d
a
t
e
_
f
o
r
m
a
t
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
'
%
a
 
%
b
 
%
d
 
%
I
:
%
M
:
%
S
 
%
p
 
%
z
 
%
Y
'
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


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
g
i
v
e
n
 
t
i
m
e
s
t
a
m
p
 
a
s
 
a
 
s
t
r
i
n
g
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
f
o
r
m
a
t
,
 
u
s
i
n
g
 
t
h
e
 
s
y
s
t
e
m
'
s
 
l
o
c
a
l
 
t
i
m
e
 
z
o
n
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
 
t
i
m
e
 
v
a
l
u
e
 
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
 
s
e
c
o
n
d
s
 
s
i
n
c
e
 
t
h
e
 
e
p
o
c
h
.


 
 
 
 
 
 
 
 
d
a
t
e
_
f
o
r
m
a
t
 
(
O
p
t
i
o
n
a
l
[
s
t
r
]
)
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
 
s
t
r
i
n
g
 
t
o
 
u
s
e
 
f
o
r
 
f
o
r
m
a
t
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
s
t
a
m
p
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
D
e
f
a
u
l
t
s
 
t
o
 
'
%
a
 
%
b
 
%
d
 
%
I
:
%
M
:
%
S
 
%
p
 
%
z
 
%
Y
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
 
a
n
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
,
 
t
z
=
t
i
m
e
z
o
n
e
.
u
t
c
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
d
a
t
e
_
f
o
r
m
a
t
)






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
s
t
a
m
p
_
t
o
_
d
a
t
e
t
i
m
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
:
 
f
l
o
a
t
,
 
d
a
t
e
_
f
o
r
m
a
t
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
'
%
a
 
%
b
 
%
d
 
%
I
:
%
M
:
%
S
 
%
p
 
%
z
 
%
Y
'
)
 
-
>
 
d
a
t
e
t
i
m
e
:


 
 
 
 
"
"
"


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
g
i
v
e
n
 
t
i
m
e
s
t
a
m
p
 
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
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
f
o
r
m
a
t
,
 
u
s
i
n
g
 
t
h
e
 
s
y
s
t
e
m
'
s
 
l
o
c
a
l
 
t
i
m
e
 
z
o
n
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
 
t
i
m
e
 
v
a
l
u
e
 
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
 
s
e
c
o
n
d
s
 
s
i
n
c
e
 
t
h
e
 
e
p
o
c
h
.


 
 
 
 
 
 
 
 
d
a
t
e
_
f
o
r
m
a
t
 
(
O
p
t
i
o
n
a
l
[
s
t
r
]
)
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
 
s
t
r
i
n
g
 
t
o
 
u
s
e
 
f
o
r
 
f
o
r
m
a
t
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
s
t
a
m
p
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
D
e
f
a
u
l
t
s
 
t
o
 
'
%
a
 
%
b
 
%
d
 
%
I
:
%
M
:
%
S
 
%
p
 
%
z
 
%
Y
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


 
 
 
 
 
 
 
 
d
a
t
e
t
i
m
e
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
 
a
n
d
 
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
,
 
t
z
=
t
i
m
e
z
o
n
e
.
u
t
c
)






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
t
i
m
e
_
t
o
_
s
t
r
i
n
g
(
d
t
:
 
d
a
t
e
t
i
m
e
,
 
d
a
t
e
_
f
o
r
m
a
t
:
 
O
p
t
i
o
n
a
l
[
s
t
r
]
 
=
 
'
%
a
 
%
b
 
%
d
 
%
I
:
%
M
:
%
S
 
%
p
 
%
z
 
%
Y
'
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


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
g
i
v
e
n
 
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
 
a
s
 
a
 
s
t
r
i
n
g
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
f
o
r
m
a
t
,
 
u
s
i
n
g
 
t
h
e
 
s
y
s
t
e
m
'
s
 
l
o
c
a
l
 
t
i
m
e
 
z
o
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
t
 
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
 
t
o
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
d
a
t
e
_
f
o
r
m
a
t
 
(
O
p
t
i
o
n
a
l
[
s
t
r
]
)
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
 
s
t
r
i
n
g
 
t
o
 
u
s
e
 
f
o
r
 
f
o
r
m
a
t
t
i
n
g
 
t
h
e
 
d
a
t
import unittest
from typing import Optional

class TestFormatTimestampToString(unittest.TestCase):
    def test_basic_functionality(self):
        """Test basic functionality with a known timestamp."""
        timestamp = 1655364000.0  # Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
        # Assuming the local timezone is UTC
        expected_date_str = 'Thu Jun 16 03:20:00 PM +0800 2022'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Should correctly format the timestamp")

    def test_default_format(self):
        """Test using the default format string."""
        timestamp = 1655364000.0
        expected_date_str = 'Thu Jun 16 03:20:00 PM +0800 2022'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Default format should match the expected date string")

    def test_custom_format(self):
        """Test with a custom format string."""
        timestamp = 1655364000.0
        custom_format = '%Y-%m-%d %H:%M:%S'
        expected_date_str = '2022-06-16 15:20:00'
        self.assertEqual(format_timestamp_to_string(timestamp, custom_format), expected_date_str, "Should correctly format the timestamp using the custom format")


    def test_edge_case_boundary_value(self):
        """Test with an edge case timestamp (e.g., Unix epoch start)."""
        timestamp = 0.0  # Unix epoch start
        expected_date_str = 'Thu Jan 01 08:00:00 AM +0800 1970'
        self.assertEqual(format_timestamp_to_string(timestamp), expected_date_str, "Should correctly format the Unix epoch start time")
if __name__ == '__main__':
    unittest.main()