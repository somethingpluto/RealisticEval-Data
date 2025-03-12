i
m
p
o
r
t
 
o
s






d
e
f
 
r
e
a
d
_
y
a
m
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
 
Y
A
M
L
 
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
 
P
y
t
h
o
n
 
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
 
o
r
 
l
i
s
t
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
 
Y
A
M
L
 
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


 
 
 
 
 
 
 
 
d
i
c
t
 
o
r
 
l
i
s
t
:
 
P
a
r
s
e
d
 
Y
A
M
L
 
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
 
P
y
t
h
o
n
 
d
a
t
a
 
s
t
r
u
c
t
u
r
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


 
 
 
 
 
 
 
 
y
a
m
l
.
Y
A
M
L
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
 
t
h
e
 
Y
A
M
L
 
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
 
'
r
'
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
 
y
a
m
l
.
s
a
f
e
_
l
o
a
d
(
f
)






d
e
f
 
w
r
i
t
e
_
y
a
m
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
 
d
i
c
t
)
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
 
P
y
t
h
o
n
 
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
 
t
o
 
a
 
Y
A
M
L
 
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
 
Y
A
M
L
 
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
d
i
c
t
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
 
Y
A
M
L
 
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


 
 
 
 
 
 
 
 
y
a
m
l
.
Y
A
M
L
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
 
w
r
i
t
i
n
g
 
t
o
 
t
h
e
 
Y
A
M
L
 
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
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
y
a
m
l
.
s
a
f
e
_
d
u
m
p
(
d
a
t
a
,
 
f
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
 
P
y
t
h
o
n
 
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


 
 
 
 
 
 
 
 
d
i
c
t
:
 
P
a
r
s
e
d
 
J
S
O
N
 
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
 
P
y
t
h
o
n
 
d
a
t
a
 
s
t
r
u
c
t
u
r
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
 
'
r
'
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
 
d
i
c
t
)
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
 
P
y
t
h
o
n
 
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
 
t
o
 
a
 
J
S
O
N
 
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
d
i
c
t
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
a
i
s
e
s
import os
import unittest

import yaml


class TestReadYaml(unittest.TestCase):

    def setUp(self):
        """Create a temporary YAML file for testing."""
        self.valid_yaml_file = 'test_valid.yaml'
        self.invalid_yaml_file = 'test_invalid.yaml'
        self.non_existent_file = 'non_existent.yaml'

        # Valid YAML content
        with open(self.valid_yaml_file, 'w') as file:
            file.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\n")

        # Invalid YAML content
        with open(self.invalid_yaml_file, 'w') as file:
            file.write("name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\ninvalid_yaml: \n - ")

    def tearDown(self):
        """Remove the temporary YAML files after testing."""
        if os.path.isfile(self.valid_yaml_file):
            os.remove(self.valid_yaml_file)
        if os.path.isfile(self.invalid_yaml_file):
            os.remove(self.invalid_yaml_file)

    def test_read_valid_yaml(self):
        """Test reading a valid YAML file."""
        expected_data = {
            'name': 'Example',
            'version': 1.0,
            'dependencies': ['package1', 'package2']
        }
        result = read_yaml(self.valid_yaml_file)
        self.assertEqual(result, expected_data)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            read_yaml(self.non_existent_file)


    def test_empty_yaml_file(self):
        """Test reading an empty YAML file."""
        empty_yaml_file = 'test_empty.yaml'
        with open(empty_yaml_file, 'w') as file:
            file.write("")  # Create an empty YAML file

        result = read_yaml(empty_yaml_file)
        self.assertIsNone(result)  # Expecting None for empty file

        os.remove(empty_yaml_file)  # Cleanup after the test
if __name__ == '__main__':
    unittest.main()