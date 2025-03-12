i
m
p
o
r
t
 
o
s


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
 
c
o
n
c
a
t
e
n
a
t
e
_
j
s
o
n
_
a
r
r
a
y
s
(
d
i
r
e
c
t
o
r
y
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


 
 
 
 
c
o
n
c
a
t
e
n
a
t
e
 
t
h
e
 
r
o
o
t
-
l
e
v
e
l
 
a
r
r
a
y
 
J
S
O
N
 
f
i
l
e
s
 
i
n
 
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
 
d
i
r
e
c
t
o
r
y


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
 
(
s
t
r
)
:
 
d
i
r
e
c
t
o
r
y
 
d
i
r
 
p
a
t
h




 
 
 
 
R
e
t
u
r
n
s
:
 
m
e
r
g
e
d
 
q
u
e
s
t
i
o
n




 
 
 
 
"
"
"


 
 
 
 
f
i
l
e
s
 
=
 
o
s
.
l
i
s
t
d
i
r
(
d
i
r
e
c
t
o
r
y
)


 
 
 
 
m
e
r
g
e
d
_
j
s
o
n
 
=
 
[
]


 
 
 
 
f
o
r
 
f
i
l
e
 
i
n
 
f
i
l
e
s
:


 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
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
.
j
s
o
n
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
o
s
.
p
a
t
h
.
j
o
i
n
(
d
i
r
e
c
t
o
r
y
,
 
f
i
l
e
)
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
e
r
g
e
d
_
j
s
o
n
.
e
x
t
e
n
d
(
j
s
o
n
.
l
o
a
d
(
f
)
)


 
 
 
 
r
e
t
u
r
n
 
m
e
r
g
e
d
_
j
s
o
n






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
t
y
p
e
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
t
y
p
e




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
_
t
y
p
e
"
]






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
i
d
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
i
d
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
i
d




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
_
i
d
"
]






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
t
e
x
t
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
t
e
x
t




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
_
t
e
x
t
"
]






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
t
y
p
e
_
t
e
x
t
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
t
e
x
t
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
t
e
x
t




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
_
t
y
p
e
_
t
e
x
t
"
]






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
t
y
p
e
_
i
d
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
i
d
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
i
d




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
_
t
y
p
e
_
i
d
"
]






d
e
f
 
g
e
t
_
q
u
e
s
t
i
o
n
_
t
y
p
e
_
c
o
d
e
(
q
u
e
s
t
i
o
n
:
 
d
i
c
t
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


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
c
o
d
e
 
f
r
o
m
 
t
h
e
 
q
u
e
s
t
i
o
n


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
d
i
c
t
)
:
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
c
o
d
e




 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
q
u
e
s
t
i
o
n
[
"
q
u
e
s
t
i
o
n
import json
import os
import unittest


class TestConcatenateJsonArrays(unittest.TestCase):

    def setUp(self):
        # Set up a test.js directory and test.js files
        self.test_dir = 'test_json'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create test.js JSON files
        self.create_test_file('array1.json', [1, 2, 3])
        self.create_test_file('array2.json', ['a', 'b', 'c'])
        self.create_test_file('not_array.json', {'key': 'value'})
        self.create_test_file('empty.json', [])
        self.create_test_file('non_json.txt', "This is not a JSON file.")

    def tearDown(self):
        # Clean up: Remove created files and directory
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def create_test_file(self, filename, content):
        # Helper method to create JSON files
        with open(os.path.join(self.test_dir, filename), 'w') as f:
            json.dump(content, f)

    def test_concatenate_valid_json_arrays(self):
        # Test with valid JSON arrays
        result = concatenate_json_arrays(self.test_dir)
        self.assertCountEqual(result, [1, 2, 3, 'a', 'b', 'c'])

    def test_ignore_non_array_json(self):
        # Test that non-array JSON files are ignored
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn('key', result)

    def test_ignore_non_json_files(self):
        # Test that non-JSON files are ignored
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn("This is not a JSON file.", result)

    def test_handle_empty_arrays(self):
        # Test concatenation includes empty arrays
        result = concatenate_json_arrays(self.test_dir)
        self.assertNotIn([], result)

    def test_empty_directory(self):
        # Test with no JSON files in the directory
        empty_dir = 'empty_test_json'
        os.makedirs(empty_dir, exist_ok=True)
        result = concatenate_json_arrays(empty_dir)
        self.assertEqual(result, [])
        os.rmdir(empty_dir)

if __name__ == '__main__':
    unittest.main()