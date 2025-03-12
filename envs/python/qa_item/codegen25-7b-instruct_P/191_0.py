d
e
f
 
f
l
o
a
t
_
t
o
_
h
e
x
(
v
a
l
u
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
 
t
o
 
i
t
s
 
h
e
x
a
d
e
c
i
m
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
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
 
f
l
o
a
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
o
n
v
e
r
t
e
d
 
t
o
 
h
e
x
a
d
e
c
i
m
a
l
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
 
h
e
x
a
d
e
c
i
m
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
i
n
p
u
t
 
f
l
o
a
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
 
h
e
x
(
s
t
r
u
c
t
.
u
n
p
a
c
k
(
'
<
I
'
,
 
s
t
r
u
c
t
.
p
a
c
k
(
'
<
f
'
,
 
v
a
l
u
e
)
)
[
0
]
)






d
e
f
 
h
e
x
_
t
o
_
f
l
o
a
t
(
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
 
f
l
o
a
t
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
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
i
t
s
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
 
t
o
 
f
l
o
a
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
i
n
p
u
t
 
h
e
x
a
d
e
c
i
m
a
l
 
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
u
c
t
.
u
n
p
a
c
k
(
'
<
f
'
,
 
s
t
r
u
c
t
.
p
a
c
k
(
'
<
I
'
,
 
i
n
t
(
v
a
l
u
e
,
 
1
6
)
)
)
[
0
]






d
e
f
 
h
e
x
_
t
o
_
i
n
t
(
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
 
i
n
t
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
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
i
t
s
 
i
n
t
e
g
e
r
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
 
t
o
 
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
 
i
n
t
e
g
e
r
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
i
n
p
u
t
 
h
e
x
a
d
e
c
i
m
a
l
 
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
 
i
n
t
(
v
a
l
u
e
,
 
1
6
)






d
e
f
 
i
n
t
_
t
o
_
h
e
x
(
v
a
l
u
e
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
s
 
a
n
 
i
n
t
e
g
e
r
 
t
o
 
i
t
s
 
h
e
x
a
d
e
c
i
m
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
i
n
t
)
:
 
T
h
e
 
i
n
t
e
g
e
r
 
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
o
n
v
e
r
t
e
d
 
t
o
 
h
e
x
a
d
e
c
i
m
a
l
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
 
h
e
x
a
d
e
c
i
m
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
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
n
t
e
g
e
r
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
 
h
e
x
(
v
a
l
u
e
)






d
e
f
 
i
n
t
_
t
o
_
b
i
n
(
v
a
l
u
e
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
s
 
a
n
 
i
n
t
e
g
e
r
 
t
o
 
i
t
s
 
b
i
n
a
r
y
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
i
n
t
)
:
 
T
h
e
 
i
n
t
e
g
e
r
 
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
o
n
v
e
r
t
e
d
 
t
o
 
b
i
n
a
r
y
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
 
b
i
n
a
r
y
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
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
n
t
e
g
e
r
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
 
b
i
n
(
v
a
l
u
e
)
[
2
:
]






d
e
f
 
b
i
n
_
t
o
_
i
n
t
(
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
 
i
n
t
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
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
i
t
s
 
i
n
t
e
g
e
r
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:
import unittest

class Tester(unittest.TestCase):
    """Test case for the float_to_hex function."""

    def test_positive_float(self):
        """Test with positive float 123.456."""
        input_value = 123.456
        expected = "42f6e979"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_negative_float(self):
        """Test with negative float -123.456."""
        input_value = -123.456
        expected = "c2f6e979"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_zero(self):
        """Test with zero."""
        input_value = 0.0
        expected = "00000000"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_small_positive_float(self):
        """Test with small positive float 0.0001."""
        input_value = 0.0001
        expected = "38d1b717"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_large_float(self):
        """Test with large float 1e30."""
        input_value = 1e30
        expected = "7149f2ca"
        self.assertEqual(float_to_hex(input_value), expected)

if __name__ == '__main__':
    unittest.main()