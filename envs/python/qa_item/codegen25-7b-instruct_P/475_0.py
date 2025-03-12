d
e
f
 
s
a
f
e
_
f
o
r
m
a
t
(
t
e
m
p
l
a
t
e
,
 
*
*
k
w
a
r
g
s
)
:


 
 
 
 
"
"
"


 
 
 
 
S
a
f
e
l
y
 
f
o
r
m
a
t
s
 
a
 
t
e
m
p
l
a
t
e
 
s
t
r
i
n
g
 
b
y
 
r
e
p
l
a
c
i
n
g
 
p
l
a
c
e
h
o
l
d
e
r
s
 
w
i
t
h
 
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
 
v
a
l
u
e
s


 
 
 
 
f
r
o
m
 
t
h
e
 
p
r
o
v
i
d
e
d
 
k
e
y
w
o
r
d
 
a
r
g
u
m
e
n
t
s
.
 
I
f
 
a
 
p
l
a
c
e
h
o
l
d
e
r
 
d
o
e
s
 
n
o
t
 
h
a
v
e
 
a
 
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


 
 
 
 
v
a
l
u
e
 
i
n
 
k
w
a
r
g
s
,
 
i
t
 
r
e
m
a
i
n
s
 
u
n
c
h
a
n
g
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
m
p
l
a
t
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
e
m
p
l
a
t
e
 
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
 
p
l
a
c
e
h
o
l
d
e
r
s
 
i
n
 
t
h
e
 
f
o
r
m
 
{
k
e
y
}
.


 
 
 
 
 
 
 
 
*
*
k
w
a
r
g
s
:
 
K
e
y
w
o
r
d
 
a
r
g
u
m
e
n
t
s
 
t
h
a
t
 
m
a
p
 
k
e
y
s
 
t
o
 
t
h
e
i
r
 
r
e
p
l
a
c
e
m
e
n
t
 
v
a
l
u
e
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
 
s
t
r
i
n
g
 
w
i
t
h
 
p
l
a
c
e
h
o
l
d
e
r
s
 
r
e
p
l
a
c
e
d
 
b
y
 
v
a
l
u
e
s
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
 
t
e
m
p
l
a
t
e
.
f
o
r
m
a
t
(
*
*
{
k
:
 
v
 
f
o
r
 
k
,
 
v
 
i
n
 
k
w
a
r
g
s
.
i
t
e
m
s
(
)
 
i
f
 
v
 
i
s
 
n
o
t
 
N
o
n
e
}
)






d
e
f
 
g
e
t
_
l
o
g
g
e
r
(
n
a
m
e
,
 
l
e
v
e
l
=
l
o
g
g
i
n
g
.
I
N
F
O
)
:


 
 
 
 
"
"
"


 
 
 
 
C
r
e
a
t
e
s
 
a
 
l
o
g
g
e
r
 
w
i
t
h
 
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
 
n
a
m
e
 
a
n
d
 
l
e
v
e
l
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
n
a
m
e
 
o
f
 
t
h
e
 
l
o
g
g
e
r
.


 
 
 
 
 
 
 
 
l
e
v
e
l
 
(
i
n
t
)
:
 
T
h
e
 
l
o
g
g
i
n
g
 
l
e
v
e
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


 
 
 
 
 
 
 
 
l
o
g
g
i
n
g
.
L
o
g
g
e
r
:
 
T
h
e
 
l
o
g
g
e
r
.


 
 
 
 
"
"
"


 
 
 
 
l
o
g
g
e
r
 
=
 
l
o
g
g
i
n
g
.
g
e
t
L
o
g
g
e
r
(
n
a
m
e
)


 
 
 
 
l
o
g
g
e
r
.
s
e
t
L
e
v
e
l
(
l
e
v
e
l
)


 
 
 
 
r
e
t
u
r
n
 
l
o
g
g
e
r






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
s
t
a
m
p
(
)
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
s
t
a
m
p
 
i
n
 
I
S
O
 
f
o
r
m
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
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
 
i
n
 
I
S
O
 
f
o
r
m
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
 
d
a
t
e
t
i
m
e
.
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
i
s
o
f
o
r
m
a
t
(
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
s
t
a
m
p
_
f
i
l
e
n
a
m
e
(
f
i
l
e
n
a
m
e
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
f
i
l
e
n
a
m
e
 
w
i
t
h
 
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
s
t
a
m
p
 
a
p
p
e
n
d
e
d
 
t
o
 
i
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
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
 
w
i
t
h
 
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
 
a
p
p
e
n
d
e
d
 
t
o
 
i
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
 
f
"
{
f
i
l
e
n
a
m
e
}
_
{
g
e
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
(
)
}
"






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
s
t
a
m
p
_
d
i
r
e
c
t
o
r
y
(
d
i
r
e
c
t
o
r
y
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
d
i
r
e
c
t
o
r
y
 
w
i
t
h
 
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
s
t
a
m
p
 
a
p
p
e
n
d
e
d
 
t
o
 
i
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
 
(
s
t
r
)
:
 
T
h
e
 
d
i
r
e
c
t
o
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
 
T
h
e
 
d
i
r
e
c
t
o
r
y
 
w
i
t
h
 
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
 
a
p
p
e
n
d
e
d
 
t
o
 
i
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
 
f
"
{
d
i
r
e
c
t
o
r
y
}
_
{
g
e
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
(
)
}
"






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
s
t
a
m
p
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
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
p
a
t
h
 
w
i
t
h
 
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
s
t
a
m
p
 
a
p
p
e
n
d
e
d
 
t
o
 
i
t
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
 
p
a
t
h
import unittest


class TestSafeFormat(unittest.TestCase):

    def test_full_replacement(self):
        """Test with all placeholders having corresponding values."""
        template = "Hello, {name}! Welcome to {place}."
        result = safe_format(template, name="Alice", place="Wonderland")
        expected = "Hello, Alice! Welcome to Wonderland."
        self.assertEqual(result, expected)

    def test_partial_replacement(self):
        """Test with some placeholders missing corresponding values."""
        template = "Hello, {name}! Welcome to {place}."
        result = safe_format(template, name="Alice")
        expected = "Hello, Alice! Welcome to {place}."
        self.assertEqual(result, expected)

    def test_no_replacement(self):
        """Test when no placeholders are provided."""
        template = "Hello, world!"
        result = safe_format(template)
        expected = "Hello, world!"
        self.assertEqual(result, expected)

    def test_missing_placeholder(self):
        """Test with a placeholder that has no corresponding value."""
        template = "My name is {name}, and I live in {city}."
        result = safe_format(template, name="Alice")
        expected = "My name is Alice, and I live in {city}."
        self.assertEqual(result, expected)

    def test_numeric_values(self):
        """Test with numeric values as replacements."""
        template = "Your score is {score} out of {total}."
        result = safe_format(template, score=85, total=100)
        expected = "Your score is 85 out of 100."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()