i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p






d
e
f
 
r
e
a
d
_
n
u
m
e
r
i
c
a
l
_
c
o
l
u
m
n
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
n
a
m
e
:
 
s
t
r
)
 
-
>
 
n
p
.
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
n
u
m
e
r
i
c
a
l
 
c
o
l
u
m
n
s
 
f
r
o
m
 
a
 
f
i
l
e
 
s
t
a
r
t
i
n
g
 
f
r
o
m
 
t
h
e
 
l
i
n
e
 
a
f
t
e
r
 
t
h
e
 
l
a
s
t
 
l
i
n
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
 
'
/
'
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
n
a
m
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
 
n
a
m
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
 
t
o
 
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


 
 
 
 
 
 
 
 
n
u
m
p
y
.
n
d
a
r
r
a
y
:
 
A
 
2
D
 
n
u
m
p
y
 
a
r
r
a
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
 
t
h
e
 
n
u
m
e
r
i
c
a
l
 
q
u
e
s
t
i
o
n
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
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
 
c
o
n
t
a
i
n
 
a
n
y
 
'
/
'
 
c
h
a
r
a
c
t
e
r
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
n
a
m
e
,
 
'
r
'
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
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
 
-
1


 
 
 
 
 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
l
i
n
e
s
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
'
/
'
 
i
n
 
l
i
n
e
s
[
i
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
 
i


 
 
 
 
 
 
 
 
i
f
 
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
'
T
h
e
 
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
 
c
o
n
t
a
i
n
 
a
n
y
 
"
/
"
 
c
h
a
r
a
c
t
e
r
.
'
)


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
[
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
+
 
1
:
]


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
p
.
a
r
r
a
y
(
[
[
f
l
o
a
t
(
x
)
 
f
o
r
 
x
 
i
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
)
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
)






d
e
f
 
r
e
a
d
_
n
u
m
e
r
i
c
a
l
_
c
o
l
u
m
n
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
_
w
i
t
h
_
h
e
a
d
e
r
(
f
i
l
e
_
n
a
m
e
:
 
s
t
r
)
 
-
>
 
n
p
.
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
n
u
m
e
r
i
c
a
l
 
c
o
l
u
m
n
s
 
f
r
o
m
 
a
 
f
i
l
e
 
s
t
a
r
t
i
n
g
 
f
r
o
m
 
t
h
e
 
l
i
n
e
 
a
f
t
e
r
 
t
h
e
 
l
a
s
t
 
l
i
n
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
 
'
/
'
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
n
a
m
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
 
n
a
m
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
 
t
o
 
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


 
 
 
 
 
 
 
 
n
u
m
p
y
.
n
d
a
r
r
a
y
:
 
A
 
2
D
 
n
u
m
p
y
 
a
r
r
a
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
 
t
h
e
 
n
u
m
e
r
i
c
a
l
 
q
u
e
s
t
i
o
n
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
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
 
c
o
n
t
a
i
n
 
a
n
y
 
'
/
'
 
c
h
a
r
a
c
t
e
r
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
n
a
m
e
,
 
'
r
'
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
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
 
-
1


 
 
 
 
 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
l
i
n
e
s
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
'
/
'
 
i
n
 
l
i
n
e
s
[
i
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
 
i


 
 
 
 
 
 
 
 
i
f
 
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
'
T
h
e
 
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
 
c
o
n
t
a
i
n
 
a
n
y
 
"
/
"
 
c
h
a
r
a
c
t
e
r
.
'
)


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
l
i
n
e
s
[
l
a
s
t
_
l
i
n
e
_
w
i
t
h
_
s
l
a
s
h
 
+
 
1
:
]


 
 
 
 
 
 
 
import os
import unittest
import numpy as np

class TestReadColumns(unittest.TestCase):

    def setUp(self):
        # Setup a temporary directory to use for each test
        self.test_file = 'test_file.txt'

    def tearDown(self):
        # Clean up the temporary file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_basic_functionality(self):
        # Test reading a file with a valid structure and numerical question
        content = """Line 1
Line 2
/
1.0 2.0 3.0
4.0 5.0 6.0
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        result = read_numerical_columns_from_file(self.test_file)
        expected_result = np.array([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0]])
        np.testing.assert_array_equal(result, expected_result)

    def test_no_slash_character(self):
        # Test that a ValueError is raised if no '/' character is found
        content = """Line 1
Line 2
Line 3
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_numerical_columns_from_file(self.test_file)

    def test_file_with_comments_and_empty_lines(self):
        # Test handling of comments and empty lines
        content = """Line 1
/
! This is a comment
1.0 2.0 3.0

4.0 5.0 6.0
! Another comment
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        result = read_numerical_columns_from_file(self.test_file)
        expected_result = np.array([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0]])
        np.testing.assert_array_equal(result, expected_result)

    def test_different_number_of_columns(self):
        # Test that the function handles different number of columns correctly
        content = """Line 1
/
1.0 2.0
3.0 4.0
5.0 6.0 7.0
"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_numerical_columns_from_file(self.test_file)

    def test_empty_file(self):
        # Test handling of an empty file
        content = """"""
        with open(self.test_file, 'w') as f:
            f.write(content)

        with self.assertRaises(ValueError):
            read_numerical_columns_from_file(self.test_file)

if __name__ == '__main__':
    unittest.main()