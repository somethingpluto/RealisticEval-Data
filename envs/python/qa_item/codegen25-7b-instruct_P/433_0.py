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
p
a
r
a
g
r
a
p
h
s
_
a
n
d
_
l
i
n
e
s
(
t
e
x
t
:
 
s
t
r
)
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
 
p
a
r
a
g
r
a
p
h
s
 
a
n
d
 
l
i
n
e
s
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
t
e
x
t
.
T
h
e
 
p
a
r
a
g
r
a
p
h
s
 
e
n
d
 
w
i
t
h
 
\
n
\
n
 
T
h
e
 
l
i
n
e
 
e
n
d
 
w
i
t
h
 
\
n


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
F
i
r
s
t
 
p
a
r
a
g
r
a
p
h
.
\
n
T
h
i
s
 
i
s
 
t
h
e
 
s
e
c
o
n
d
 
l
i
n
e
.
\
n
\
n
S
e
c
o
n
d
 
p
a
r
a
g
r
a
p
h
.
\
n
A
n
o
t
h
e
r
 
l
i
n
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
t
e
x
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
 
p
a
r
a
g
r
a
p
h
s
 
a
n
d
 
l
i
n
e
s
 
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


 
 
 
 
 
 
 
 
d
i
c
t
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
p
a
r
a
g
r
a
p
h
s
'
:
 
A
 
l
i
s
t
 
o
f
 
p
a
r
a
g
r
a
p
h
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
t
e
x
t
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
l
i
n
e
s
'
:
 
A
 
l
i
s
t
 
o
f
 
l
i
n
e
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
t
e
x
t
.


 
 
 
 
"
"
"


 
 
 
 
p
a
r
a
g
r
a
p
h
s
 
=
 
[
]


 
 
 
 
l
i
n
e
s
 
=
 
[
]


 
 
 
 
p
a
r
a
g
r
a
p
h
 
=
 
"
"


 
 
 
 
f
o
r
 
l
i
n
e
 
i
n
 
t
e
x
t
.
s
p
l
i
t
(
"
\
n
"
)
:


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
 
=
=
 
"
"
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
g
r
a
p
h
s
.
a
p
p
e
n
d
(
p
a
r
a
g
r
a
p
h
)


 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
g
r
a
p
h
 
=
 
"
"


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
g
r
a
p
h
 
+
=
 
l
i
n
e
 
+
 
"
\
n
"


 
 
 
 
 
 
 
 
 
 
 
 
l
i
n
e
s
.
a
p
p
e
n
d
(
l
i
n
e
)


 
 
 
 
i
f
 
p
a
r
a
g
r
a
p
h
 
!
=
 
"
"
:


 
 
 
 
 
 
 
 
p
a
r
a
g
r
a
p
h
s
.
a
p
p
e
n
d
(
p
a
r
a
g
r
a
p
h
)


 
 
 
 
r
e
t
u
r
n
 
{
"
p
a
r
a
g
r
a
p
h
s
"
:
 
p
a
r
a
g
r
a
p
h
s
,
 
"
l
i
n
e
s
"
:
 
l
i
n
e
s
}






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
p
a
r
a
g
r
a
p
h
s
_
a
n
d
_
l
i
n
e
s
_
f
r
o
m
_
f
i
l
e
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
)
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
 
p
a
r
a
g
r
a
p
h
s
 
a
n
d
 
l
i
n
e
s
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
.
 
T
h
e
 
p
a
r
a
g
r
a
p
h
s
 
e
n
d
 
w
i
t
h
 
\
n
\
n
 
T
h
e
 
l
i
n
e
 
e
n
d
 
w
i
t
h
 
\
n


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
F
i
r
s
t
 
p
a
r
a
g
r
a
p
h
.
\
n
T
h
i
s
 
i
s
 
t
h
e
 
s
e
c
o
n
d
 
l
i
n
e
.
\
n
\
n
S
e
c
o
n
d
 
p
a
r
a
g
r
a
p
h
.
\
n
A
n
o
t
h
e
r
 
l
i
n
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
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
 
t
o
 
t
h
e
 
f
i
l
e
 
f
r
o
m
 
w
h
i
c
h
 
p
a
r
a
g
r
a
p
h
s
 
a
n
d
 
l
i
n
e
s
 
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


 
 
 
 
 
 
 
 
d
i
c
t
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
p
a
r
a
g
r
a
p
h
s
'
:
 
A
 
l
i
s
t
 
o
f
 
p
a
r
a
g
r
a
p
h
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
t
e
x
t
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
l
i
n
e
s
'
:
 
A
 
l
i
s
t
 
o
f
 
l
i
n
e
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
t
e
x
t
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
t
e
x
t
 
=
 
f
.
r
e
a
d
(
)


 
 
 
 
r
e
t
u
r
n
 
e
x
t
r
a
c
t
_
p
a
r
a
g
r
a
p
h
s
_
a
n
d
_
l
i
n
e
s
(
t
e
x
t
)






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
p
a
r
a
g
r
a
p
h
s
_
a
n
d
_
l
i
n
e
s
_
f
r
o
m
_
u
r
l
(
u
r
l
:
 
s
t
r
)
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
 
p
a
r
a
g
r
a
p
h
s
 
a
n
d
 
l
i
n
e
s
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
u
r
l
.
 
T
h
e
 
p
a
r
a
g
r
a
p
h
s
 
e
n
d
 
w
i
t
h
 
\
n
\
n
 
T
h
e
 
l
i
n
e
 
e
n
d
 
w
i
t
h
 
\
n


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
F
i
r
s
t
 
p
a
r
a
g
r
a
p
h
.
\
n
T
h
i
s
 
i
s
 
t
h
e
 
s
e
c
o
n
d
 
l
i
n
e
.
import unittest


class TestExtractParagraphsAndLines(unittest.TestCase):

    def test_single_paragraph(self):
        input_text = "This is a single paragraph."
        expected_output = {
            'paragraphs': ["This is a single paragraph."],
            'lines': ["This is a single paragraph."]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_multiple_paragraphs(self):
        input_text = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
        expected_output = {
            'paragraphs': [
                "First paragraph.\nThis is the second line.",
                "Second paragraph.\nAnother line."
            ],
            'lines': [
                "First paragraph.",
                "This is the second line.",
                "Second paragraph.",
                "Another line."
            ]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_leading_and_trailing_whitespace(self):
        input_text = "   This paragraph has leading whitespace.\nAnd a line after.\n\n   This one has trailing whitespace.   "
        expected_output = {
            'paragraphs': [
                "This paragraph has leading whitespace.\nAnd a line after.",
                "This one has trailing whitespace."
            ],
            'lines': [
                "This paragraph has leading whitespace.",
                "And a line after.",
                "This one has trailing whitespace."
            ]
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_empty_string(self):
        input_text = ""
        expected_output = {
            'paragraphs': [],
            'lines': []
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

    def test_multiple_empty_paragraphs(self):
        input_text = "\n\n\n"
        expected_output = {
            'paragraphs': [],
            'lines': []
        }
        self.assertEqual(extract_paragraphs_and_lines(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()