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
f
i
l
e
_
a
n
d
_
p
r
o
c
e
s
s
_
l
i
n
e
s
(
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
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
a
 
f
i
l
e
 
f
r
o
m
 
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
 
p
a
t
h
,
 
p
r
o
c
e
s
s
e
s
 
e
a
c
h
 
l
i
n
e
 
t
o
 
r
e
m
o
v
e
 
i
n
l
i
n
e
 
c
o
m
m
e
n
t
s
,


 
 
 
 
r
e
m
o
v
e
s
 
l
i
n
e
 
b
r
e
a
k
s
,
 
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
 
o
f
 
t
h
e
 
p
r
o
c
e
s
s
e
d
 
l
i
n
e
 
c
o
n
t
e
n
t
s
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
 
t
o
 
t
h
e
 
f
i
l
e
 
t
o
 
b
e
 
r
e
a
d
.
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
 
t
o
 
b
e
 
r
e
a
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
 
p
r
o
c
e
s
s
e
d
 
l
i
n
e
 
f
r
o
m
 
t
h
e
 
f
i
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
i
l
e
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
i
l
e
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


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
[
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
 
[
l
i
n
e
.
s
p
l
i
t
(
"
/
/
"
)
[
0
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
 
l
i
n
e
s
]


 
 
 
 
 
 
 
 
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
 
p
r
o
c
e
s
s
_
l
i
n
e
(
l
i
n
e
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


 
 
 
 
P
r
o
c
e
s
s
e
s
 
a
 
l
i
n
e
 
o
f
 
c
o
d
e
 
t
o
 
r
e
m
o
v
e
 
i
n
l
i
n
e
 
c
o
m
m
e
n
t
s
,
 
r
e
m
o
v
e
 
l
i
n
e
 
b
r
e
a
k
s
,
 
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
 
p
r
o
c
e
s
s
e
d
 
l
i
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
n
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
 
l
i
n
e
 
t
o
 
b
e
 
p
r
o
c
e
s
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
 
p
r
o
c
e
s
s
e
d
 
l
i
n
e
.


 
 
 
 
"
"
"


 
 
 
 
l
i
n
e
 
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


 
 
 
 
l
i
n
e
 
=
 
l
i
n
e
.
s
p
l
i
t
(
"
/
/
"
)
[
0
]


 
 
 
 
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






d
e
f
 
g
e
t
_
l
i
n
e
_
n
u
m
b
e
r
(
l
i
n
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


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
n
u
m
b
e
r
 
f
r
o
m
 
a
 
l
i
n
e
 
o
f
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
n
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
 
l
i
n
e
 
o
f
 
c
o
d
e
 
t
o
 
g
e
t
 
t
h
e
 
l
i
n
e
 
n
u
m
b
e
r
 
f
r
o
m
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
 
l
i
n
e
 
n
u
m
b
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
 
i
n
t
(
l
i
n
e
.
s
p
l
i
t
(
"
:
"
)
[
0
]
)






d
e
f
 
g
e
t
_
l
i
n
e
_
t
y
p
e
(
l
i
n
e
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


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
t
y
p
e
 
f
r
o
m
 
a
 
l
i
n
e
 
o
f
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
n
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
 
l
i
n
e
 
o
f
 
c
o
d
e
 
t
o
 
g
e
t
 
t
h
e
 
l
i
n
e
 
t
y
p
e
 
f
r
o
m
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
 
l
i
n
e
 
t
y
p
e
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
 
l
i
n
e
.
s
p
l
i
t
(
"
:
"
)
[
1
]






d
e
f
 
g
e
t
_
l
i
n
e
_
v
a
l
u
e
(
l
i
n
e
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


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
v
a
l
u
e
 
f
r
o
m
 
a
 
l
i
n
e
 
o
f
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
n
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
 
l
i
n
e
 
o
f
 
c
o
d
e
 
t
o
 
g
e
t
 
t
h
e
 
l
i
n
e
 
v
a
l
u
e
 
f
r
o
m
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
 
l
i
n
e
 
v
a
l
u
e
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
 
l
i
n
e
.
s
p
l
i
t
import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file_path = "testFile.txt"
        open(self.test_file_path, 'w').close()  # Create an empty file

    def write_to_file(self, content):
        """Helper method to write to the test file."""
        with open(self.test_file_path, 'w') as writer:
            writer.write(content)

    def test_normal_input(self):
        """Test processing of normal input."""
        self.write_to_file("Line 1\nLine 2 # Comment\nLine 3\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_only_comments(self):
        """Test processing when only comments are present."""
        self.write_to_file("# This is a comment\n# Another comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, [])

    def test_empty_lines(self):
        """Test processing with empty lines."""
        self.write_to_file("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_no_inline_comments(self):
        """Test processing when there are no inline comments."""
        self.write_to_file("Line 1\nLine 2\nLine 3\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_only_new_lines(self):
        """Test processing with only new lines."""
        self.write_to_file("\n\n\n\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, [])

    def test_mixed_content(self):
        """Test processing with mixed content."""
        self.write_to_file("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Valid line", "Line 2", "Line 3"])

    def tearDown(self):
        """Cleanup after tests."""
        try:
            os.remove(self.test_file_path)
        except OSError:
            pass  # Ignore if the file doesn't exist
if __name__ == '__main__':
    unittest.main()