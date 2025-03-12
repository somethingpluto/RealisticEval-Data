d
e
f
 
s
a
v
e
_
c
o
n
t
e
n
t
_
t
o
_
f
i
l
e
(
c
o
n
t
e
n
t
:
 
s
t
r
,
 
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
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
S
a
v
e
s
 
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
 
c
o
n
t
e
n
t
 
t
o
 
a
 
s
p
e
c
i
f
i
e
d
 
f
i
l
e
 
a
f
t
e
r
 
c
l
e
a
n
i
n
g
 
u
p


 
 
 
 
r
e
d
u
n
d
a
n
t
 
w
h
i
t
e
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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
 
t
e
x
t
 
c
o
n
t
e
n
t
 
t
o
 
b
e
 
s
a
v
e
d
 
t
o
 
t
h
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
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
 
s
a
v
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


 
 
 
 
 
 
 
 
N
o
n
e


 
 
 
 
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
c
o
n
t
e
n
t
.
s
t
r
i
p
(
)
)






d
e
f
 
g
e
t
_
f
i
l
e
_
c
o
n
t
e
n
t
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
a
 
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
 
f
i
l
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
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
 
r
e
a
d
 
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
 
c
o
n
t
e
n
t
 
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
.
r
e
a
d
(
)






d
e
f
 
g
e
t
_
f
i
l
e
_
c
o
n
t
e
n
t
_
a
s
_
l
i
s
t
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
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
a
 
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
 
i
t
 
a
s
 
a
 
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
 
f
i
l
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
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
 
r
e
a
d
 
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
 
T
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
f
i
l
e
 
a
s
 
a
 
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
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






d
e
f
 
g
e
t
_
f
i
l
e
_
c
o
n
t
e
n
t
_
a
s
_
l
i
s
t
_
o
f
_
s
t
r
i
n
g
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
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
a
 
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
 
i
t
 
a
s
 
a
 
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
 
f
i
l
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
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
 
r
e
a
d
 
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
 
T
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
f
i
l
e
 
a
s
 
a
 
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
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
]






d
e
f
 
g
e
t
_
f
i
l
e
_
c
o
n
t
e
n
t
_
a
s
_
l
i
s
t
_
o
f
_
l
i
s
t
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
L
i
s
t
[
s
t
r
]
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
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
a
 
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
 
i
t
 
a
s
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s
 
o
f
 
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
 
f
i
l
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
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
 
r
e
a
d
 
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
import os
import unittest


class TestSaveContentToFile(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file path for testing."""
        self.test_file_path = 'test_output.txt'

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_basic_content(self):
        """Test with basic content and check if it saves correctly."""
        content = "Hello,  World!  "
        expected = "Hello, World!"
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_multiple_spaces_and_empty_lines(self):
        """Test handling of multiple spaces and empty lines."""
        content = """

        This is a    test.

        Another line.      
        """
        expected = "This is a test. Another line."
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_only_whitespace(self):
        """Test if only whitespace is handled correctly."""
        content = "    \n  \n   "
        expected = ""
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

    def test_empty_content(self):
        """Test if empty content is saved correctly."""
        content = ""
        expected = ""
        save_content_to_file(content, self.test_file_path)
        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            result = file.read().strip()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()