d
e
f
 
p
r
e
p
e
n
d
_
t
o
_
e
a
c
h
_
l
i
n
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
,
 
p
r
e
f
i
x
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
e
n
d
s
 
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
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
e
a
c
h
 
l
i
n
e
 
o
f
 
t
h
e
 
f
i
l
e
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
 
w
h
o
s
e
 
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
 
m
o
d
i
f
i
e
d
.


 
 
 
 
p
r
e
f
i
x
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
t
o
 
a
p
p
e
n
d
 
t
o
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
e
a
c
h
 
l
i
n
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


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
.
r
e
a
d
l
i
n
e
s
(
)


 
 
 
 
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
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
p
r
e
f
i
x
 
+
 
l
i
n
e
)






d
e
f
 
a
p
p
e
n
d
_
t
o
_
e
a
c
h
_
l
i
n
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
,
 
s
u
f
f
i
x
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
e
n
d
s
 
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
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
e
a
c
h
 
l
i
n
e
 
o
f
 
t
h
e
 
f
i
l
e
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
 
w
h
o
s
e
 
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
 
m
o
d
i
f
i
e
d
.


 
 
 
 
s
u
f
f
i
x
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
t
o
 
a
p
p
e
n
d
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
e
a
c
h
 
l
i
n
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


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
.
r
e
a
d
l
i
n
e
s
(
)


 
 
 
 
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
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
l
i
n
e
 
+
 
s
u
f
f
i
x
)






d
e
f
 
p
r
e
p
e
n
d
_
t
o
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
,
 
p
r
e
f
i
x
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
e
p
e
n
d
s
 
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
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
t
h
e
 
f
i
l
e
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
 
w
h
o
s
e
 
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
 
m
o
d
i
f
i
e
d
.


 
 
 
 
p
r
e
f
i
x
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
t
o
 
a
p
p
e
n
d
 
t
o
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
e
a
c
h
 
l
i
n
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


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
.
r
e
a
d
l
i
n
e
s
(
)


 
 
 
 
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
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
p
r
e
f
i
x
)


 
 
 
 
 
 
 
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
l
i
n
e
)






d
e
f
 
a
p
p
e
n
d
_
t
o
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
,
 
s
u
f
f
i
x
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
e
n
d
s
 
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
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
f
i
l
e
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
 
w
h
o
s
e
 
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
 
m
o
d
i
f
i
e
d
.


 
 
 
 
s
u
f
f
i
x
 
(
s
t
r
)
:
 
S
t
r
i
n
g
 
t
o
 
a
p
p
e
n
d
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
e
a
c
h
 
l
i
n
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


import unittest
import os

class TestPrependToEachLine(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, 'w') as f:
            f.write("Line 1\nLine 2\nLine 3")

    def tearDown(self):
        """Remove the temporary file after testing."""
        os.remove(self.test_file_path)

    def test_prepend_string(self):
        """Test appending a simple string to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "Test: ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["Test: Line 1\n", "Test: Line 2\n", "Test: Line 3"])

    def test_prepend_empty_string(self):
        """Test appending an empty string."""
        prepend_to_each_line(self.test_file_path, "")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])

    def test_prepend_special_characters(self):
        """Test appending special characters to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "#$%^&* ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["#$%^&* Line 1\n", "#$%^&* Line 2\n", "#$%^&* Line 3"])

    def test_prepend_numeric_string(self):
        """Test appending numeric string to the beginning of each line."""
        prepend_to_each_line(self.test_file_path, "123 ")
        with open(self.test_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines, ["123 Line 1\n", "123 Line 2\n", "123 Line 3"])

    def test_file_not_found(self):
        """Test the response when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            prepend_to_each_line("non_existent_file.txt", "Test: ")
if __name__ == '__main__':
    unittest.main()