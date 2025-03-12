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
 
r
e
a
d
_
m
a
p
p
i
n
g
_
f
i
l
e
(
m
a
p
p
i
n
g
_
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
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
q
u
e
s
t
i
o
n
 
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
 
m
a
p
p
i
n
g
 
f
i
l
e
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
e
l
e
m
e
n
t
 
i
s
 
a
 
t
u
p
l
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
 
t
h
e
 
c
o
m
p
i
l
e
d
 
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
 
a
n
d
 
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
 
s
t
r
i
n
g
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
p
p
i
n
g
_
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
 
P
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
 
r
e
g
e
x
 
m
a
p
p
i
n
g
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


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
:
 
E
a
c
h
 
t
u
p
l
e
 
c
o
n
t
a
i
n
s
 
a
 
c
o
m
p
i
l
e
d
 
r
e
g
e
x
 
o
b
j
e
c
t
 
a
n
d
 
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


 
 
 
 
m
a
p
p
i
n
g
_
f
i
l
e
 
=
 
o
p
e
n
(
m
a
p
p
i
n
g
_
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


 
 
 
 
m
a
p
p
i
n
g
_
l
i
s
t
 
=
 
[
]


 
 
 
 
f
o
r
 
l
i
n
e
 
i
n
 
m
a
p
p
i
n
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
.
s
t
r
i
p
(
)
 
!
=
 
"
"
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
g
e
x
,
 
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
 
=
 
l
i
n
e
.
s
t
r
i
p
(
)
.
s
p
l
i
t
(
"
\
t
"
)


 
 
 
 
 
 
 
 
 
 
 
 
m
a
p
p
i
n
g
_
l
i
s
t
.
a
p
p
e
n
d
(
(
r
e
.
c
o
m
p
i
l
e
(
r
e
g
e
x
)
,
 
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
)
)


 
 
 
 
m
a
p
p
i
n
g
_
f
i
l
e
.
c
l
o
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
 
m
a
p
p
i
n
g
_
l
i
s
t






d
e
f
 
r
e
p
l
a
c
e
_
m
a
p
p
i
n
g
(
m
a
p
p
i
n
g
_
l
i
s
t
:
 
L
i
s
t
,
 
t
e
x
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


 
 
 
 
A
p
p
l
i
e
s
 
t
h
e
 
r
e
g
e
x
 
m
a
p
p
i
n
g
s
 
t
o
 
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
 
a
n
d
 
r
e
t
u
r
n
s
 
t
h
e
 
m
o
d
i
f
i
e
d
 
t
e
x
t
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
p
p
i
n
g
_
l
i
s
t
 
(
l
i
s
t
 
o
f
 
t
u
p
l
e
s
)
:
 
L
i
s
t
 
o
f
 
t
u
p
l
e
s
 
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
 
c
o
m
p
i
l
e
d
 
r
e
g
e
x
 
o
b
j
e
c
t
s
 
a
n
d
 
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
 
s
t
r
i
n
g
s
.


 
 
 
 
 
 
 
 
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
e
x
t
 
t
o
 
b
e
 
m
o
d
i
f
i
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
 
M
o
d
i
f
i
e
d
 
t
e
x
t
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
r
e
g
e
x
,
 
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
 
i
n
 
m
a
p
p
i
n
g
_
l
i
s
t
:


 
 
 
 
 
 
 
 
t
e
x
t
 
=
 
r
e
g
e
x
.
s
u
b
(
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
,
 
t
e
x
t
)


 
 
 
 
r
e
t
u
r
n
 
t
e
x
t






d
e
f
 
m
a
i
n
(
)
:


 
 
 
 
p
a
r
s
e
r
 
=
 
a
r
g
p
a
r
s
e
.
A
r
g
u
m
e
n
t
P
a
r
s
e
r
(


 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
=
"
A
p
p
l
i
e
s
 
r
e
g
e
x
 
m
a
p
p
i
n
g
s
 
t
o
 
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
"


 
 
 
 
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(


 
 
 
 
 
 
 
 
"
-
-
m
a
p
p
i
n
g
_
f
i
l
e
"
,


 
 
 
 
 
 
 
 
t
y
p
e
=
s
t
r
,


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
d
=
T
r
u
e
,


 
 
 
 
 
 
 
 
h
e
l
p
=
"
P
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
 
r
e
g
e
x
 
m
a
p
p
i
n
g
s
.
"
,


 
 
 
 
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(


 
 
 
 
 
 
 
 
"
-
-
i
n
p
u
t
_
f
i
l
e
"
,


 
 
 
 
 
 
 
 
t
y
p
e
=
s
t
r
,


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
d
=
T
r
u
e
,


 
 
 
 
 
 
 
 
h
e
l
p
=
"
P
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
f
i
l
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
 
t
e
x
t
 
t
o
 
b
e
 
m
o
d
i
f
i
e
d
.
"
,


 
 
 
 
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(


 
 
 
 
 
 
 
 
"
-
-
o
u
t
p
u
t
_
f
i
l
e
"
,


 
 
 
 
 
 
 
 
t
y
p
e
=
s
t
r
,


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
d
=
T
r
u
e
,


 
 
 
 
 
 
 
 
h
e
l
p
=
"
P
a
t
h
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
f
i
l
e
 
w
h
e
r
e
 
t
h
e
 
m
o
d
i
f
i
e
d
 
t
e
x
t
 
w
i
l
l
 
b
e
 
w
r
i
t
t
e
n
.
"
,


 
 
 
 
)


 
 
 
 
a
r
g
s
 
=
 
p
a
r
s
e
r
.
p
a
r
s
e
_
a
r
g
s
(
)




 
 
 
 
m
a
p
p
i
n
g
_
l
i
s
t
 
=
 
r
e
a
d
import re
import unittest
from unittest.mock import patch, mock_open


class TestReadMappingFile(unittest.TestCase):

    def test_valid_mapping_file(self):
        # Test with a valid mapping file content
        mock_file_content = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = read_mapping_file("dummy_path.txt")
            expected = [
                (re.compile("old_pattern1"), "new_word1"),
                (re.compile("old_pattern2"), "new_word2"),
            ]
            self.assertEqual(result, expected)

    def test_missing_file(self):
        # Test with a missing file
        with self.assertRaises(FileNotFoundError):
            read_mapping_file("non_existent_file.txt")

    def test_malformed_line_no_comma(self):
        # Test with a line that does not contain a comma
        mock_file_content = "'old_pattern1' 'new_word1'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            with self.assertRaises(ValueError) as context:
                read_mapping_file("dummy_path.txt")
            self.assertEqual(str(context.exception), "Each line must contain exactly one comma separating the pattern and the replacement.")

    def test_valid_patterns_with_special_characters(self):
        # Test with valid patterns that contain special regex characters
        mock_file_content = "'\\d+', 'number'\n'\\w+', 'word'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = read_mapping_file("dummy_path.txt")
            expected = [
                (re.compile(r"\d+"), "number"),
                (re.compile(r"\w+"), "word"),
            ]
            self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()