i
m
p
o
r
t
 
j
s
o
n


i
m
p
o
r
t
 
o
s


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
,
 
D
i
c
t
,
 
A
n
y




d
e
f
 
r
e
a
d
_
j
s
o
n
l
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
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
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
 
a
 
J
S
O
N
 
L
i
n
e
s
 
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
s
 
c
o
n
t
e
n
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
 
J
S
O
N
 
L
i
n
e
s
 
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


 
 
 
 
 
 
 
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:
 
A
 
l
i
s
t
 
o
f
 
J
S
O
N
 
o
b
j
e
c
t
s
 
p
a
r
s
e
d
 
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




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
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
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
j
s
o
n
.
J
S
O
N
D
e
c
o
d
e
E
r
r
o
r
:
 
I
f
 
t
h
e
r
e
 
i
s
 
a
n
 
e
r
r
o
r
 
p
a
r
s
i
n
g
 
a
 
l
i
n
e
 
i
n
 
t
h
e
 
J
S
O
N
 
L
i
n
e
s
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
o
s
.
p
a
t
h
.
e
x
i
s
t
s
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
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
(
f
"
F
i
l
e
 
n
o
t
 
f
o
u
n
d
:
 
{
f
i
l
e
_
p
a
t
h
}
"
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
j
s
o
n
.
l
o
a
d
s
(
l
i
n
e
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
]




d
e
f
 
w
r
i
t
e
_
j
s
o
n
l
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
 
d
a
t
a
:
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
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


 
 
 
 
W
r
i
t
e
s
 
a
 
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
i
o
n
a
r
i
e
s
 
t
o
 
a
 
J
S
O
N
 
L
i
n
e
s
 
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
 
J
S
O
N
 
L
i
n
e
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 
d
a
t
a
 
(
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
)
:
 
T
h
e
 
d
a
t
a
 
t
o
 
w
r
i
t
e
 
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




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
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
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
j
s
o
n
.
J
S
O
N
D
e
c
o
d
e
E
r
r
o
r
:
 
I
f
 
t
h
e
r
e
 
i
s
 
a
n
 
e
r
r
o
r
 
p
a
r
s
i
n
g
 
a
 
l
i
n
e
 
i
n
 
t
h
e
 
J
S
O
N
 
L
i
n
e
s
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
o
s
.
p
a
t
h
.
e
x
i
s
t
s
(
o
s
.
p
a
t
h
.
d
i
r
n
a
m
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
)
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
(
f
"
D
i
r
e
c
t
o
r
y
 
n
o
t
 
f
o
u
n
d
:
 
{
o
s
.
p
a
t
h
.
d
i
r
n
a
m
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
)
}
"
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
 
d
a
t
a
:


 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
j
s
o
n
.
d
u
m
p
s
(
l
i
n
e
)
 
+
 
"
\
n
"
)




d
e
f
 
r
e
a
d
_
j
s
o
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
:
 
s
t
r
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
A
n
y
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
 
J
S
O
N
 
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
s
 
c
o
n
t
e
n
t
 
a
s
 
a
 
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
 
J
S
O
N
 
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


 
 
 
 
 
 
 
 
D
i
c
t
import json
import os
import unittest


class TestReadJsonl(unittest.TestCase):

    def setUp(self):
        """Create temporary JSON Lines files for testing."""
        self.valid_jsonl_file = 'test_valid.jsonl'
        self.invalid_jsonl_file = 'test_invalid.jsonl'
        self.non_existent_file = 'non_existent.jsonl'

        # Valid JSON Lines content
        with open(self.valid_jsonl_file, 'w') as file:
            file.write('{"name": "Alice", "age": 30}\n')
            file.write('{"name": "Bob", "age": 25}\n')
            file.write('{"name": "Charlie", "age": 35}\n')

        # Invalid JSON Lines content
        with open(self.invalid_jsonl_file, 'w') as file:
            file.write('{"name": "Alice", "age": 30}\n')
            file.write('{"name": "Bob", "age": "twenty-five}\n')  # Missing closing quote

    def tearDown(self):
        """Remove the temporary JSON Lines files after testing."""
        if os.path.isfile(self.valid_jsonl_file):
            os.remove(self.valid_jsonl_file)
        if os.path.isfile(self.invalid_jsonl_file):
            os.remove(self.invalid_jsonl_file)

    def test_read_valid_jsonl(self):
        """Test reading a valid JSON Lines file."""
        expected_data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
        result = read_jsonl(self.valid_jsonl_file)
        self.assertEqual(result, expected_data)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            read_jsonl(self.non_existent_file)

    def test_empty_jsonl_file(self):
        """Test reading an empty JSON Lines file."""
        empty_jsonl_file = 'test_empty.jsonl'
        with open(empty_jsonl_file, 'w') as file:
            file.write("")  # Create an empty JSON Lines file

        result = read_jsonl(empty_jsonl_file)
        self.assertEqual(result, [])  # Expecting an empty list for empty file

        os.remove(empty_jsonl_file)  # Cleanup after the test
if __name__ == '__main__':
    unittest.main()