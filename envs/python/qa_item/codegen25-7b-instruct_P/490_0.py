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
s
t
r
_
2
_
m
a
r
k
d
o
w
n
(
x
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


 
 
 
 
F
o
r
m
a
t
s
 
a
 
s
t
r
i
n
g
 
b
y
 
p
r
e
p
e
n
d
i
n
g
 
'
>
 
'
 
t
o
 
e
a
c
h
 
l
i
n
e
 
a
n
d
 
e
n
s
u
r
i
n
g
 
p
r
o
p
e
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
 
o
f
 
c
o
d
e
 
b
l
o
c
k
s
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
 
t
o
 
b
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
.
 
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
 
i
s
 
n
o
t
 
a


 
 
 
 
 
 
 
 
s
t
r
i
n
g
,
 
i
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
 
o
n
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
 
e
a
c
h
 
l
i
n
e
 
p
r
e
f
i
x
e
d
 
b
y
 
'
>
 
'
 
a
n
d


 
 
 
 
 
 
 
 
w
i
t
h
 
b
a
l
a
n
c
e
d
 
c
o
d
e
 
b
l
o
c
k
 
d
e
l
i
m
i
t
e
r
s
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


 
 
 
 
l
i
n
e
s
 
=
 
x
.
s
p
l
i
t
l
i
n
e
s
(
)


 
 
 
 
l
i
n
e
s
 
=
 
[
"
>
 
"
 
+
 
l
i
n
e
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
]


 
 
 
 
l
i
n
e
s
 
=
 
"
\
n
"
.
j
o
i
n
(
l
i
n
e
s
)


 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
.
r
e
p
l
a
c
e
(
"
`
`
`
"
,
 
"
`
`
`
\
n
"
)


 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
.
r
e
p
l
a
c
e
(
"
`
`
`
\
n
\
n
"
,
 
"
`
`
`
\
n
"
)


 
 
 
 
r
e
t
u
r
n
 
l
i
n
e
s






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
s
t
r
_
2
_
r
s
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
 
a
 
s
t
r
i
n
g
 
b
y
 
p
r
e
p
e
n
d
i
n
g
 
'
>
 
'
 
t
o
 
e
a
c
h
 
l
i
n
e
 
a
n
d
 
e
n
s
u
r
i
n
g
 
p
r
o
p
e
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
 
o
f
 
c
o
d
e
 
b
l
o
c
k
s
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
 
t
o
 
b
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
.
 
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
 
i
s
 
n
o
t
 
a


 
 
 
 
 
 
 
 
s
t
r
i
n
g
,
 
i
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
 
o
n
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
 
e
a
c
h
 
l
i
n
e
 
p
r
e
f
i
x
e
d
 
b
y
 
'
>
 
'
 
a
n
d


 
 
 
 
 
 
 
 
w
i
t
h
 
b
a
l
a
n
c
e
d
 
c
o
d
e
 
b
l
o
c
k
 
d
e
l
i
m
i
t
e
r
s
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


 
 
 
 
l
i
n
e
s
 
=
 
x
.
s
p
l
i
t
l
i
n
e
s
(
)


 
 
 
 
l
i
n
e
s
 
=
 
[
"
>
 
"
 
+
 
l
i
n
e
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
]


 
 
 
 
l
i
n
e
s
 
=
 
"
\
n
"
.
j
o
i
n
(
l
i
n
e
s
)


 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
.
r
e
p
l
a
c
e
(
"
`
`
`
"
,
 
"
`
`
`
\
n
"
)


 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
.
r
e
p
l
a
c
e
(
"
`
`
`
\
n
\
n
"
,
 
"
`
`
`
\
n
"
)


 
 
 
 
r
e
t
u
r
n
 
l
i
n
e
s






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
s
t
r
_
2
_
h
t
m
l
(
x
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


 
 
 
 
F
o
r
m
a
t
s
 
a
 
s
t
r
i
n
g
 
b
y
 
p
r
e
p
e
n
d
i
n
g
 
'
>
 
'
 
t
o
 
e
a
c
h
 
l
i
n
e
 
a
n
d
 
e
n
s
u
r
i
n
g
 
p
r
o
p
e
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
 
o
f
 
c
o
d
e
 
b
l
o
c
k
s
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
 
t
o
 
b
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
.
 
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
 
i
s
 
n
o
t
 
a


 
 
 
 
 
 
 
 
s
t
r
i
n
g
,
 
i
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
 
o
n
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
import unittest


class TestFormatStr(unittest.TestCase):

    def test_simple_string(self):
        """Test a simple string input."""
        input_str = "Hello, World!"
        expected_output = "> Hello, World!"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_multiline_string(self):
        """Test a multiline string input."""
        input_str = "Line 1\nLine 2\nLine 3"
        expected_output = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_code_block_delimiters_even(self):
        """Test a string with an even number of code block delimiters."""
        input_str = "Some code:\n```\nprint('Hello')\n```"
        expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_code_block_delimiters_odd(self):
        """Test a string with an odd number of code block delimiters."""
        input_str = "Some code:\n```\nprint('Hello')"
        expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```"
        self.assertEqual(format_str_2_markdown(input_str), expected_output)

    def test_non_string_input(self):
        """Test non-string input (e.g., integer) to ensure it's converted."""
        input_value = 123
        expected_output = "> 123"
        self.assertEqual(format_str_2_markdown(input_value), expected_output)
if __name__ == '__main__':
    unittest.main()