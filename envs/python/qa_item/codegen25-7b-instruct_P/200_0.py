d
e
f
 
e
x
t
r
a
c
t
_
s
t
r
i
n
g
_
f
r
o
m
_
b
r
a
c
e
s
(
i
n
p
u
t
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
e
d
 
i
n
 
t
h
e
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
 
`
{
}
`
 
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
 
w
h
i
c
h
 
t
h
e
 
b
r
a
c
e
s
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
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
u
b
s
t
r
i
n
g
 
e
n
c
l
o
s
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
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
,
 
o
r
 
a
n
 
e
r
r
o
r
 
m
e
s
s
a
g
e
 
i
f
 
b
r
a
c
e
s
 
a
r
e
 
m
i
s
s
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
I
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
 
i
s
 
e
m
p
t
y
.
"


 
 
 
 
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
.
s
t
a
r
t
s
w
i
t
h
(
"
{
"
)
 
o
r
 
n
o
t
 
i
n
p
u
t
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
}
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
I
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
 
d
o
e
s
 
n
o
t
 
c
o
n
t
a
i
n
 
a
n
y
 
b
r
a
c
e
s
.
"


 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
[
1
:
-
1
]






d
e
f
 
e
x
t
r
a
c
t
_
s
t
r
i
n
g
_
f
r
o
m
_
b
r
a
c
e
s
_
o
r
_
n
o
n
e
(
i
n
p
u
t
:
 
s
t
r
)
 
-
>
 
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
e
d
 
i
n
 
t
h
e
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
 
`
{
}
`
 
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
,
 
o
r
 
N
o
n
e
 
i
f
 
b
r
a
c
e
s
 
a
r
e
 
m
i
s
s
i
n
g
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
 
w
h
i
c
h
 
t
h
e
 
b
r
a
c
e
s
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
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
.




 
 
 
 
R
e
t
u
r
n
s
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
:
 
A
 
s
u
b
s
t
r
i
n
g
 
e
n
c
l
o
s
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
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
,
 
o
r
 
N
o
n
e
 
i
f
 
b
r
a
c
e
s
 
a
r
e
 
m
i
s
s
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
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
.
s
t
a
r
t
s
w
i
t
h
(
"
{
"
)
 
o
r
 
n
o
t
 
i
n
p
u
t
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
}
"
)
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


 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
[
1
:
-
1
]






d
e
f
 
e
x
t
r
a
c
t
_
s
t
r
i
n
g
_
f
r
o
m
_
b
r
a
c
e
s
_
o
r
_
e
m
p
t
y
(
i
n
p
u
t
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
e
d
 
i
n
 
t
h
e
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
 
`
{
}
`
 
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
,
 
o
r
 
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
 
i
f
 
b
r
a
c
e
s
 
a
r
e
 
m
i
s
s
i
n
g
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
 
w
h
i
c
h
 
t
h
e
 
b
r
a
c
e
s
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
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
u
b
s
t
r
i
n
g
 
e
n
c
l
o
s
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
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
,
 
o
r
 
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
 
i
f
 
b
r
a
c
e
s
 
a
r
e
 
m
i
s
s
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"


 
 
 
 
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
.
s
t
a
r
t
s
w
i
t
h
(
"
{
"
)
 
o
r
 
n
o
t
 
i
n
p
u
t
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
}
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
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
p
u
t
[
1
:
-
1
]






d
e
f
 
e
x
t
r
a
c
t
_
s
t
r
i
n
g
_
f
r
o
m
_
b
r
a
c
e
s
_
o
r
_
d
e
f
a
u
l
t
(
i
n
p
u
t
:
 
s
t
r
,
 
d
e
f
a
u
l
t
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
e
d
 
i
n
 
t
h
e
 
f
i
r
s
t
 
p
a
i
r
 
o
f
 
b
r
a
c
e
s
 
`
{
}
import unittest


class Tester(unittest.TestCase):
    """Test cases for extract_string_from_braces function."""

    def test_basic_extraction(self):
        """Basic extraction."""
        input_data = "This is a sample text with some data {data: \"value\"} and more text."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{data: \"value\"}")

    def test_no_braces(self):
        """No braces."""
        input_data = "This string has no braces."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No opening brace found.")

    def test_only_opening_brace(self):
        """Only opening brace."""
        input_data = "This string has an opening brace { but no closing brace."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No closing brace found.")

    def test_only_closing_brace(self):
        """Only closing brace."""
        input_data = "This string has a closing brace } but no opening brace."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No opening brace found.")

    def test_multiple_braces(self):
        """Multiple braces."""
        input_data = "First {first} and second {second} braces."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{first}")

    def test_empty_braces(self):
        """Empty braces."""
        input_data = "This string has empty braces {} and some text."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{}")


if __name__ == '__main__':
    unittest.main()