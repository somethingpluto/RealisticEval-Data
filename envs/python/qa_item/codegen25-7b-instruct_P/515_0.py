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
_
s
t
r
i
n
g
(
d
a
t
e
_
s
t
r
:
s
t
r
)
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
 
f
r
o
m
 
t
h
e
 
f
o
r
m
a
t
 
'
%
a
,
 
%
d
 
%
b
 
%
Y
 
%
H
:
%
M
:
%
S
 
%
z
 
(
%
Z
)
'


 
 
 
 
t
o
 
t
h
e
 
f
o
r
m
a
t
 
'
%
Y
-
%
m
-
%
d
_
%
H
:
%
M
:
%
S
'
.




 
 
 
 
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
 
(
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
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
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
'
%
Y
-
%
m
-
%
d
_
%
H
:
%
M
:
%
S
'
.


 
 
 
 
 
 
 
 
N
o
n
e
:
 
I
f
 
t
h
e
 
i
n
p
u
t
 
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
s
 
i
n
v
a
l
i
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
d
a
t
e
_
o
b
j
 
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
,
 
'
%
a
,
 
%
d
 
%
b
 
%
Y
 
%
H
:
%
M
:
%
S
 
%
z
 
(
%
Z
)
'
)


 
 
 
 
 
 
 
 
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
_
o
b
j
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
Y
-
%
m
-
%
d
_
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


 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e




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
_
s
t
r
i
n
g
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
d
a
t
e
_
s
t
r
:
s
t
r
)
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
 
f
r
o
m
 
t
h
e
 
f
o
r
m
a
t
 
'
%
a
,
 
%
d
 
%
b
 
%
Y
 
%
H
:
%
M
:
%
S
 
%
z
 
(
%
Z
)
'


 
 
 
 
t
o
 
t
h
e
 
f
o
r
m
a
t
 
'
%
Y
-
%
m
-
%
d
_
%
H
:
%
M
:
%
S
'
.




 
 
 
 
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
 
(
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
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
a
t
 
'
%
Y
-
%
m
-
%
d
_
%
H
:
%
M
:
%
S
'
.


 
 
 
 
 
 
 
 
N
o
n
e
:
 
I
f
 
t
h
e
 
i
n
p
u
t
 
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
s
 
i
n
v
a
l
i
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
d
a
t
e
_
o
b
j
 
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
,
 
'
%
a
,
 
%
d
 
%
b
 
%
Y
 
%
H
:
%
M
:
%
S
 
%
z
 
(
%
Z
)
'
)


 
 
 
 
 
 
 
 
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
_
o
b
j


 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e




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
_
s
t
r
i
n
g
_
t
o
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
d
a
t
e
_
s
t
r
:
s
t
r
)
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
 
f
r
o
m
 
t
h
e
 
f
o
r
m
a
t
 
'
%
a
,
 
%
d
 
%
b
 
%
Y
 
%
H
:
%
M
:
%
S
 
%
z
 
(
%
Z
)
'


 
 
 
 
t
o
 
t
h
e
 
f
o
r
m
a
t
 
'
%
Y
-
%
m
-
%
d
_
%
import unittest


class TestFormatDateString(unittest.TestCase):

    def test_valid_date_conversion(self):
        """Test case for a valid date string."""
        date_str = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)"
        expected_date = "2023-09-28_14:45:00"
        self.assertEqual(format_date_string(date_str), expected_date)

    def test_invalid_date_format(self):
        """Test case for an invalid date string format."""
        date_str = "Invalid date format"
        self.assertIsNone(format_date_string(date_str))

    def test_missing_components(self):
        """Test case for a date string missing components."""
        date_str = "Fri, 28 Sep 2023 14:45:00 +0000"
        self.assertIsNone(format_date_string(date_str))

    def test_edge_case_date(self):
        """Test case for an edge case date string (e.g., leap year)."""
        date_str = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)"
        expected_date = "2024-02-29_14:45:00"
        self.assertEqual(format_date_string(date_str), expected_date)
if __name__ == '__main__':
    unittest.main()