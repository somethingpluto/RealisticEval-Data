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
b
i
b
_
i
n
f
o
(
b
i
b
_
f
i
l
e
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
 
t
h
e
 
t
i
t
l
e
,
 
a
u
t
h
o
r
,
 
a
n
d
 
y
e
a
r
 
f
r
o
m
 
a
 
B
i
b
T
e
X
 
f
i
l
e
.
b
i
b
 
f
i
l
e
 
c
o
n
t
e
n
t
 
s
u
c
h
 
a
s
 
@
a
r
t
i
c
l
e
{
s
a
m
p
l
e
2
0
2
4
,
\
n
 
 
a
u
t
h
o
r
 
=
 
{
J
o
h
n
 
D
o
e
 
a
n
d
 
J
a
n
e
 
S
m
i
t
h
}
,
\
n
 
 
t
i
t
l
e
 
=
 
{
A
 
C
o
m
p
r
e
h
e
n
s
i
v
e
 
S
t
u
d
y
 
o
n
 
A
I
}
,
\
n
 
 
y
e
a
r
 
=
 
{
2
0
2
4
}
\
n
}




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
b
_
f
i
l
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
 
p
a
t
h
 
t
o
 
t
h
e
 
B
i
b
T
e
X
 
f
i
l
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


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
d
i
c
t
:
 
A
 
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
 
d
i
c
t
i
o
n
a
r
i
e
s
 
w
i
t
h
 
t
i
t
l
e
,
 
a
u
t
h
o
r
,
 
a
n
d
 
y
e
a
r
 
f
o
r
 
e
a
c
h
 
a
r
t
i
c
l
e
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
b
i
b
_
f
i
l
e
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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


 
 
 
 
b
i
b
_
e
n
t
r
i
e
s
 
=
 
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
r
"
@
\
w
+
{
.
*
?
}
"
,
 
c
o
n
t
e
n
t
,
 
r
e
.
D
O
T
A
L
L
)


 
 
 
 
b
i
b
_
i
n
f
o
 
=
 
[
]


 
 
 
 
f
o
r
 
e
n
t
r
y
 
i
n
 
b
i
b
_
e
n
t
r
i
e
s
:


 
 
 
 
 
 
 
 
t
i
t
l
e
 
=
 
r
e
.
s
e
a
r
c
h
(
r
"
t
i
t
l
e
\
s
*
=
\
s
*
\
{
(
.
*
?
)
\
}
"
,
 
e
n
t
r
y
)
.
g
r
o
u
p
(
1
)


 
 
 
 
 
 
 
 
a
u
t
h
o
r
 
=
 
r
e
.
s
e
a
r
c
h
(
r
"
a
u
t
h
o
r
\
s
*
=
\
s
*
\
{
(
.
*
?
)
\
}
"
,
 
e
n
t
r
y
)
.
g
r
o
u
p
(
1
)


 
 
 
 
 
 
 
 
y
e
a
r
 
=
 
r
e
.
s
e
a
r
c
h
(
r
"
y
e
a
r
\
s
*
=
\
s
*
(
\
d
+
)
"
,
 
e
n
t
r
y
)
.
g
r
o
u
p
(
1
)


 
 
 
 
 
 
 
 
b
i
b
_
i
n
f
o
.
a
p
p
e
n
d
(
{
"
t
i
t
l
e
"
:
 
t
i
t
l
e
,
 
"
a
u
t
h
o
r
"
:
 
a
u
t
h
o
r
,
 
"
y
e
a
r
"
:
 
y
e
a
r
}
)


 
 
 
 
r
e
t
u
r
n
 
b
i
b
_
i
n
f
o






d
e
f
 
g
e
t
_
b
i
b
_
i
n
f
o
(
b
i
b
_
f
i
l
e
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
 
t
h
e
 
t
i
t
l
e
,
 
a
u
t
h
o
r
,
 
a
n
d
 
y
e
a
r
 
f
r
o
m
 
a
 
B
i
b
T
e
X
 
f
i
l
e
.
b
i
b
 
f
i
l
e
 
c
o
n
t
e
n
t
 
s
u
c
h
 
a
s
 
@
a
r
t
i
c
l
e
{
s
a
m
p
l
e
2
0
2
4
,
\
n
 
 
a
u
t
h
o
r
 
=
 
{
J
o
h
n
 
D
o
e
 
a
n
d
 
J
a
n
e
 
S
m
i
t
h
}
,
\
n
 
 
t
i
t
l
e
 
=
 
{
A
 
C
o
m
p
r
e
h
e
n
s
i
v
e
 
S
t
u
d
y
 
o
n
 
A
I
}
,
\
n
 
 
y
e
a
r
 
=
 
{
2
0
2
4
}
\
n
}




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
b
_
f
i
l
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
 
p
a
t
h
 
t
o
 
t
h
e
 
B
i
b
T
e
X
 
f
i
l
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


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
d
i
c
t
:
 
A
 
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
 
d
i
c
t
i
o
n
a
r
i
e
s
 
w
i
t
h
 
t
i
t
l
e
,
 
a
u
t
h
o
r
,
 
a
n
d
 
y
e
a
r
 
f
o
r
 
e
a
c
h
 
a
r
t
i
c
l
e
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
b
i
b
_
f
i
l
e
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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


 
 
 
 
b
i
b
_
e
n
t
r
i
e
s
 
=
 
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
r
"
@
\
w
+
{
import re
import unittest
from unittest.mock import mock_open, patch


class TestExtractBibInfo(unittest.TestCase):

    def test_valid_entry(self):
        """Test extraction from a valid BibTeX entry."""
        mock_bib = "@article{sample2024,\n  author = {John Doe and Jane Smith},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'A Comprehensive Study on AI', 'author': 'John Doe and Jane Smith', 'year': '2024'}]
            self.assertEqual(result, expected)

    def test_multiple_entries(self):
        """Test extraction from multiple BibTeX entries."""
        mock_bib = (
            "@article{sample2024,\n"
            "  author = {John Doe},\n"
            "  title = {A Comprehensive Study on AI},\n"
            "  year = {2024}\n}\n"
            "@article{sample2023,\n"
            "  author = {Jane Smith},\n"
            "  title = {Deep Learning Techniques},\n"
            "  year = {2023}\n}"
        )
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [
                {'title': 'A Comprehensive Study on AI', 'author': 'John Doe', 'year': '2024'},
                {'title': 'Deep Learning Techniques', 'author': 'Jane Smith', 'year': '2023'}
            ]
            self.assertEqual(result, expected)

    def test_missing_fields(self):
        """Test extraction when some fields are missing."""
        mock_bib = "@article{sample2024,\n  author = {John Doe},\n  title = {Title Missing Year}\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'Title Missing Year', 'author': 'John Doe', 'year': None}]
            self.assertEqual(result, expected)

    def test_empty_file(self):
        """Test extraction from an empty BibTeX file."""
        mock_bib = ""
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = []
            self.assertEqual(result, expected)

    def test_incorrect_format(self):
        """Test extraction from a badly formatted BibTeX entry."""
        mock_bib = "@article{sample2024,\n  author = John Doe,\n  title = {Title Without Braces},\n  year = 2024\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'Title Without Braces', 'author': None, 'year': None}]
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()