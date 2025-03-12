d
e
f
 
i
s
_
s
i
g
n
i
f
i
c
a
n
t
_
n
u
m
b
e
r
(
i
n
p
u
t
_
v
a
l
u
e
:
 
s
t
r
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
 
i
f
 
t
h
e
 
g
i
v
e
n
 
i
n
p
u
t
 
i
s
 
a
 
s
i
g
n
i
f
i
c
a
n
t
 
n
u
m
b
e
r
.




 
 
 
 
A
 
s
i
g
n
i
f
i
c
a
n
t
 
n
u
m
b
e
r
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
s
t
r
i
n
g
 
t
h
a
t
:


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
5
 
a
n
d
 
1
8
 
c
h
a
r
a
c
t
e
r
s
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
-
 
C
o
n
t
a
i
n
s
 
o
n
l
y
 
d
i
g
i
t
 
c
h
a
r
a
c
t
e
r
s
.


 
 
 
 
-
 
C
a
n
n
o
t
 
s
t
a
r
t
 
w
i
t
h
 
'
0
'
 
i
f
 
i
t
s
 
l
e
n
g
t
h
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
1
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
v
a
l
u
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
 
i
n
p
u
t
 
v
a
l
u
e
 
t
o
 
b
e
 
c
h
e
c
k
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
 
t
h
e
 
i
n
p
u
t
 
i
s
 
a
 
s
i
g
n
i
f
i
c
a
n
t
 
n
u
m
b
e
r
,
 
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


 
 
 
 
i
f
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
<
 
5
 
o
r
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
>
 
1
8
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
i
f
 
n
o
t
 
i
n
p
u
t
_
v
a
l
u
e
.
i
s
d
i
g
i
t
(
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
i
f
 
i
n
p
u
t
_
v
a
l
u
e
[
0
]
 
=
=
 
"
0
"
 
a
n
d
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
>
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
i
s
_
v
a
l
i
d
_
n
u
m
b
e
r
(
i
n
p
u
t
_
v
a
l
u
e
:
 
s
t
r
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
 
i
f
 
t
h
e
 
g
i
v
e
n
 
i
n
p
u
t
 
i
s
 
a
 
v
a
l
i
d
 
n
u
m
b
e
r
.




 
 
 
 
A
 
v
a
l
i
d
 
n
u
m
b
e
r
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
s
t
r
i
n
g
 
t
h
a
t
:


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
1
 
a
n
d
 
1
8
 
c
h
a
r
a
c
t
e
r
s
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
-
 
C
o
n
t
a
i
n
s
 
o
n
l
y
 
d
i
g
i
t
 
c
h
a
r
a
c
t
e
r
s
.


 
 
 
 
-
 
C
a
n
 
s
t
a
r
t
 
w
i
t
h
 
'
0
'
 
i
f
 
i
t
s
 
l
e
n
g
t
h
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
1
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
v
a
l
u
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
 
i
n
p
u
t
 
v
a
l
u
e
 
t
o
 
b
e
 
c
h
e
c
k
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
 
t
h
e
 
i
n
p
u
t
 
i
s
 
a
 
v
a
l
i
d
 
n
u
m
b
e
r
,
 
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


 
 
 
 
i
f
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
<
 
1
 
o
r
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
>
 
1
8
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
i
f
 
n
o
t
 
i
n
p
u
t
_
v
a
l
u
e
.
i
s
d
i
g
i
t
(
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
i
f
 
i
n
p
u
t
_
v
a
l
u
e
[
0
]
 
!
=
 
"
0
"
 
a
n
d
 
l
e
n
(
i
n
p
u
t
_
v
a
l
u
e
)
 
>
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
i
s
_
v
a
l
i
d
_
n
u
m
b
e
r
_
w
i
t
h
_
d
e
c
i
m
a
l
(
i
n
p
u
t
_
v
a
l
u
e
:
 
s
t
r
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
 
i
f
 
t
h
e
 
g
i
v
e
n
 
i
n
p
u
t
 
i
s
 
a
 
v
a
l
i
d
 
n
u
m
b
e
r
 
w
i
t
h
 
d
e
c
i
m
a
l
.




 
 
 
 
A
 
v
a
l
i
d
 
n
u
m
b
e
r
 
w
i
t
h
 
d
e
c
i
m
a
l
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
s
t
r
i
n
g
 
t
h
a
t
:


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
5
 
a
n
d
 
1
8
 
c
h
a
r
a
c
t
e
r
s
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
-
 
C
o
n
t
a
i
n
s
 
o
n
l
y
 
d
i
g
i
t
 
c
h
a
r
a
c
t
e
r
s
.


 
 
 
 
-
 
C
a
n
 
s
t
a
r
t
 
w
i
t
h
 
'
0
'
 
i
f
 
i
t
s
 
l
e
n
g
t
h
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
1
.


 
 
 
 
-
 
C
o
n
t
a
i
n
s
 
a
t
 
l
e
a
s
t
 
o
n
e
 
d
e
c
i
m
a
l
 
p
o
i
n
t
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
v
a
l
u
e
import unittest


class TestIsSignificantNumber(unittest.TestCase):

    def test_valid_significant_number_with_exactly_5_digits(self):
        self.assertTrue(is_significant_number("12345"))

    def test_number_with_leading_zero(self):
        self.assertFalse(is_significant_number("01234"))

    def test_valid_significant_number_with_exactly_18_digits(self):
        self.assertTrue(is_significant_number("123456789012345678"))

    def test_number_with_less_than_5_digits(self):
        self.assertFalse(is_significant_number("123"))

    def test_number_with_more_than_18_digits(self):
        self.assertFalse(is_significant_number("1234567890123456789"))

    def test_number_containing_non_digit_characters(self):
        self.assertFalse(is_significant_number("1234a"))

    def test_single_zero(self):
        self.assertFalse(is_significant_number("0"))

    def test_non_string_input(self):
        self.assertFalse(is_significant_number(12345))

if __name__ == '__main__':
    unittest.main()