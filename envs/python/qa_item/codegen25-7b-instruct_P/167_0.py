d
e
f
 
a
s
s
e
r
t
9
9
9
(
b
i
t
_
n
a
m
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


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
 
(
a
s
s
u
m
e
d
 
t
o
 
e
n
d
 
w
i
t
h
 
"
.
b
i
t
"
)
 
i
s
 
a
 
v
a
l
i
d
 
3
-
d
i
g
i
t
 
i
n
t
e
g
e
r
.


 
 
 
 
R
e
m
o
v
e
s
 
t
h
e
 
"
.
b
i
t
"
 
s
u
f
f
i
x
,
 
c
h
e
c
k
s
 
i
f
 
t
h
e
 
r
e
m
a
i
n
i
n
g
 
p
a
r
t
 
i
s
 
a
 
n
u
m
b
e
r
,


 
 
 
 
a
n
d
 
v
e
r
i
f
i
e
s
 
i
f
 
i
t
 
f
a
l
l
s
 
w
i
t
h
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
9
9
9
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
t
_
n
a
m
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
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
e
,
 
w
h
i
c
h
 
s
h
o
u
l
d
 
e
n
d
 
w
i
t
h
 
"
.
b
i
t
"
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
 
r
e
m
a
i
n
i
n
g
 
p
a
r
t
 
a
f
t
e
r
 
r
e
m
o
v
i
n
g
 
"
.
b
i
t
"
 
i
s
 
a
 
v
a
l
i
d
 
3
-
d
i
g
i
t
 
i
n
t
e
g
e
r
 
(
0
-
9
9
9
)
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
t
h
e
r
w
i
s
e
,
 
F
a
l
s
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
b
i
t
_
n
a
m
e
.
e
n
d
s
w
i
t
h
(
"
.
b
i
t
"
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


 
 
 
 
b
i
t
_
n
a
m
e
 
=
 
b
i
t
_
n
a
m
e
[
:
-
4
]


 
 
 
 
i
f
 
n
o
t
 
b
i
t
_
n
a
m
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
t
(
b
i
t
_
n
a
m
e
)
 
<
 
0
 
o
r
 
i
n
t
(
b
i
t
_
n
a
m
e
)
 
>
 
9
9
9
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
 
a
s
s
e
r
t
_
b
i
t
_
n
a
m
e
(
b
i
t
_
n
a
m
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


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
 
(
a
s
s
u
m
e
d
 
t
o
 
e
n
d
 
w
i
t
h
 
"
.
b
i
t
"
)
 
i
s
 
a
 
v
a
l
i
d
 
b
i
t
 
n
a
m
e
.


 
 
 
 
R
e
m
o
v
e
s
 
t
h
e
 
"
.
b
i
t
"
 
s
u
f
f
i
x
,
 
c
h
e
c
k
s
 
i
f
 
t
h
e
 
r
e
m
a
i
n
i
n
g
 
p
a
r
t
 
i
s
 
a
 
n
u
m
b
e
r
,


 
 
 
 
a
n
d
 
v
e
r
i
f
i
e
s
 
i
f
 
i
t
 
f
a
l
l
s
 
w
i
t
h
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
9
9
9
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
t
_
n
a
m
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
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
e
,
 
w
h
i
c
h
 
s
h
o
u
l
d
 
e
n
d
 
w
i
t
h
 
"
.
b
i
t
"
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
 
r
e
m
a
i
n
i
n
g
 
p
a
r
t
 
a
f
t
e
r
 
r
e
m
o
v
i
n
g
 
"
.
b
i
t
"
 
i
s
 
a
 
v
a
l
i
d
 
b
i
t
 
n
a
m
e
;


 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
t
h
e
r
w
i
s
e
,
 
F
a
l
s
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
b
i
t
_
n
a
m
e
.
e
n
d
s
w
i
t
h
(
"
.
b
i
t
"
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


 
 
 
 
b
i
t
_
n
a
m
e
 
=
 
b
i
t
_
n
a
m
e
[
:
-
4
]


 
 
 
 
i
f
 
n
o
t
 
b
i
t
_
n
a
m
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
t
(
b
i
t
_
n
a
m
e
)
 
<
 
0
 
o
r
 
i
n
t
(
b
i
t
_
n
a
m
e
)
 
>
 
9
9
9
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
 
a
s
s
e
r
t
_
b
i
t
_
n
a
m
e
_
o
r
_
i
n
t
(
b
i
t
_
n
a
m
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


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
 
(
a
s
s
u
m
e
d
 
t
o
 
e
n
d
 
w
i
t
h
 
"
.
b
i
t
"
)
 
i
s
 
a
 
v
a
l
i
d
 
b
i
t
 
n
a
m
e
 
o
r
 
i
n
t
e
g
e
r
.


 
 
 
 
R
e
m
o
v
e
s
 
t
h
e
 
"
.
b
i
t
"
 
s
u
f
f
i
x
,
 
c
h
e
c
k
s
 
i
f
 
t
h
e
 
r
e
m
a
i
n
i
n
g
 
p
a
r
t
 
i
s
 
a
 
n
u
m
b
e
r
,


 
 
 
 
a
n
d
 
v
e
r
i
f
i
e
s
 
i
f
 
i
t
import unittest


class TestAssert999(unittest.TestCase):
    def test_valid_three_digit_number_with_suffix(self):
        """Test case for a valid 3-digit number with the ".bit" suffix. Expected to return true."""
        input_value = "123.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_valid_two_digit_number_with_suffix(self):
        """Test case for a valid 2-digit number with the ".bit" suffix. Expected to return true."""
        input_value = "12.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_non_numeric_characters_after_suffix(self):
        """Test case for a string containing non-numeric characters after removing ".bit". Expected to return false."""
        input_value = "12a.bit"
        result = assert999(input_value)
        self.assertFalse(result)

    def test_lower_boundary_value(self):
        """Test case for the lower boundary value "0.bit". Expected to return true."""
        input_value = "0.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_upper_boundary_value(self):
        """Test case for the upper boundary value "999.bit". Expected to return true."""
        input_value = "999.bit"
        result = assert999(input_value)
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()