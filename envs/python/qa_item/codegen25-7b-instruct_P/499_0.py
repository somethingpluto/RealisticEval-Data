i
m
p
o
r
t
 
r
e


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
 
U
n
i
o
n






d
e
f
 
c
l
e
a
n
_
p
a
t
t
e
r
n
(
x
:
 
s
t
r
,
 
p
a
t
t
e
r
n
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
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
 
a
 
n
u
m
e
r
i
c
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
r
e
g
e
x
 
p
a
t
t
e
r
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
s
t
r
 
o
r
 
a
n
y
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
 
v
a
l
u
e
.
 
I
t
 
w
i
l
l
 
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
 
a
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
p
a
t
t
e
r
n
 
(
s
t
r
)
:
 
T
h
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
 
p
a
t
t
e
r
n
 
t
o
 
u
s
e
 
f
o
r
 
m
a
t
c
h
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
w
e
i
g
h
t
 
v
a
l
u
e
 
i
f
 
a
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
a
n
 
e
m
p
t
y
 
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


 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
x
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
x
 
=
 
s
t
r
(
x
)


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
l
o
a
t
(
r
e
.
f
i
n
d
a
l
l
(
p
a
t
t
e
r
n
,
 
x
)
[
0
]
)


 
 
 
 
e
x
c
e
p
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
'






d
e
f
 
c
l
e
a
n
_
w
e
i
g
h
t
(
x
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
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
 
a
 
n
u
m
e
r
i
c
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
r
e
g
e
x
 
p
a
t
t
e
r
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
s
t
r
 
o
r
 
a
n
y
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
 
v
a
l
u
e
.
 
I
t
 
w
i
l
l
 
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
 
a
 
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
w
e
i
g
h
t
 
v
a
l
u
e
 
i
f
 
a
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
a
n
 
e
m
p
t
y
 
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
 
c
l
e
a
n
_
p
a
t
t
e
r
n
(
x
,
 
r
'
\
d
+
\
.
?
\
d
*
'
)






d
e
f
 
c
l
e
a
n
_
v
o
l
u
m
e
(
x
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
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
 
a
 
n
u
m
e
r
i
c
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
r
e
g
e
x
 
p
a
t
t
e
r
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
s
t
r
 
o
r
 
a
n
y
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
 
v
a
l
u
e
.
 
I
t
 
w
i
l
l
 
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
 
a
 
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
v
o
l
u
m
e
 
v
a
l
u
e
 
i
f
 
a
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
a
n
 
e
m
p
t
y
 
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
 
c
l
e
a
n
_
p
a
t
t
e
r
n
(
x
,
 
r
'
\
d
+
\
.
?
\
d
*
'
)






d
e
f
 
c
l
e
a
n
_
u
n
i
t
(
x
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
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
 
a
 
n
u
m
e
r
i
c
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
r
e
g
e
x
 
p
a
t
t
e
r
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
 
(
s
t
r
 
o
r
 
a
n
y
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
 
v
a
l
u
e
.
 
I
t
 
w
i
l
l
 
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
 
a
 
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
u
n
i
t
 
v
a
l
u
e
 
i
f
 
a
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
a
n
 
e
m
p
t
y
 
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
 
c
l
e
a
n
import unittest


class TestCleanPattern(unittest.TestCase):

    def setUp(self):
        """Sets up a common regex pattern for testing."""
        self.pattern = r'(\d+\.?\d*) kg'  # Regex pattern to match weight in kg

    def test_valid_integer_weight(self):
        """Test case for valid integer weight."""
        input_string = "The weight is 25 kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 25.0)

    def test_valid_float_weight(self):
        """Test case for valid float weight."""
        input_string = "Weight measured at 15.75 kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 15.75)

    def test_no_weight_found(self):
        """Test case where no weight is present."""
        input_string = "No weight provided."
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, '')

    def test_invalid_float_conversion(self):
        """Test case for non-numeric weight."""
        input_string = "The weight is thirty kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, '')

    def test_weight_with_extra_text(self):
        """Test case for weight with additional text."""
        input_string = "The total weight is 45.3 kg as per the last measurement."
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 45.3)

if __name__ == '__main__':
    unittest.main()