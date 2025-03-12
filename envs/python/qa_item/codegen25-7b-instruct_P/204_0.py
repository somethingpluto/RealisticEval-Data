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
 
L
i
s
t






d
e
f
 
s
p
l
i
t
_
s
t
r
i
n
g
(
s
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
S
p
l
i
t
 
a
 
s
t
r
i
n
g
 
i
n
t
o
 
m
u
l
t
i
p
l
e
 
s
u
b
s
t
r
i
n
g
s
 
b
a
s
e
d
 
o
n
 
s
p
a
c
e
s
 
a
n
d
 
r
e
t
u
r
n
 
a
 
l
i
s
t
 
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
s
e
 
s
u
b
s
t
r
i
n
g
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
 
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
 
s
p
l
i
t
 
i
n
t
o
 
w
o
r
d
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


 
 
 
 
 
 
 
 
L
i
s
t
[
s
t
r
]
:
 
A
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
,
 
e
a
c
h
 
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
 
a
 
w
o
r
d
 
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
 
R
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
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
 
o
r
 
c
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
 
s
p
a
c
e
s
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
s
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]


 
 
 
 
w
o
r
d
s
 
=
 
s
.
s
p
l
i
t
(
)


 
 
 
 
r
e
t
u
r
n
 
w
o
r
d
s






d
e
f
 
r
e
v
e
r
s
e
_
s
t
r
i
n
g
(
s
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


 
 
 
 
R
e
v
e
r
s
e
 
a
 
s
t
r
i
n
g
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
r
e
v
e
r
s
e
d
 
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


 
 
 
 
 
 
 
 
s
 
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
 
r
e
v
e
r
s
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
 
T
h
e
 
r
e
v
e
r
s
e
d
 
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
[
:
:
-
1
]






d
e
f
 
r
e
v
e
r
s
e
_
w
o
r
d
s
_
i
n
_
s
t
r
i
n
g
(
s
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
e
r
 
o
f
 
w
o
r
d
s
 
i
n
 
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
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
n
e
w
 
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


 
 
 
 
 
 
 
 
s
 
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
 
m
u
l
t
i
p
l
e
 
w
o
r
d
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
 
w
i
t
h
 
t
h
e
 
w
o
r
d
s
 
r
e
v
e
r
s
e
d
.


 
 
 
 
"
"
"


 
 
 
 
w
o
r
d
s
 
=
 
s
p
l
i
t
_
s
t
r
i
n
g
(
s
)


 
 
 
 
w
o
r
d
s
.
r
e
v
e
r
s
e
(
)


 
 
 
 
r
e
t
u
r
n
 
"
 
"
.
j
o
i
n
(
w
o
r
d
s
)






d
e
f
 
r
e
v
e
r
s
e
_
w
o
r
d
s
_
i
n
_
s
t
r
i
n
g
_
2
(
s
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
e
r
 
o
f
 
w
o
r
d
s
 
i
n
 
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
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
n
e
w
 
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


 
 
 
 
 
 
 
 
s
 
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
 
m
u
l
t
i
p
l
e
 
w
o
r
d
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
 
w
i
t
h
 
t
h
e
 
w
o
r
d
s
 
r
e
v
e
r
s
e
d
.


 
 
 
 
"
"
"


 
 
 
 
w
o
r
d
s
 
=
 
s
p
l
i
t
_
s
t
r
i
n
g
(
s
)


 
 
 
 
r
e
t
u
r
n
 
"
 
"
.
j
o
i
n
(
w
o
r
d
s
[
:
:
-
1
]
)






d
e
f
 
r
e
v
e
r
s
e
_
w
o
r
d
s
_
i
n
_
s
t
r
i
n
g
_
3
(
s
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
e
r
 
o
f
 
w
o
r
d
s
 
i
n
 
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
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
n
e
w
 
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


 
 
 
 
 
 
 
 
s
 
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
 
m
u
l
t
i
p
l
e
 
w
o
r
d
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
 
w
i
t
h
 
t
h
e
 
w
o
r
d
s
 
r
e
v
e
r
s
e
d
.


 
 
 
 
"
"
"


 
 
 
 
w
o
r
d
s
 
=
 
s
p
l
i
t
_
s
t
r
i
n
g
(
s
)


 
 
 
 
r
e
t
u
r
n
 
"
 
"
.
j
o
i
n
(
w
o
r
d
s
[
:
:
-
1
]
)






d
e
f
 
r
e
v
e
r
s
e
_
w
o
r
d
s
_
i
n
_
s
t
r
i
n
g
import unittest


class Tester(unittest.TestCase):

    def test_split_string_regular_sentence(self):
        """Split a regular sentence."""
        input_str = "Hello world from Catch2"
        expected = ["Hello", "world", "from", "Catch2"]
        self.assertEqual(split_string(input_str), expected)

    def test_handle_multiple_spaces(self):
        """Handle multiple spaces between words."""
        input_str = "Multiple   spaces between words"
        expected = ["Multiple", "spaces", "between", "words"]
        self.assertEqual(split_string(input_str), expected)

    def test_single_word_input(self):
        """Single word input."""
        input_str = "Single"
        expected = ["Single"]
        self.assertEqual(split_string(input_str), expected)

    def test_empty_string_input(self):
        """Empty string input."""
        input_str = ""
        expected = []
        self.assertEqual(split_string(input_str), expected)

    def test_leading_and_trailing_spaces(self):
        """String with leading and trailing spaces."""
        input_str = "   Leading and trailing spaces   "
        expected = ["Leading", "and", "trailing", "spaces"]
        self.assertEqual(split_string(input_str), expected)

if __name__ == '__main__':
    unittest.main()