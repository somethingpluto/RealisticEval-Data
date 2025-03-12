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
 
w
r
i
t
e
_
c
s
v
_
t
o
_
f
i
l
e
(
s
t
r
i
n
g
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
,
 
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


 
 
 
 
F
o
r
m
a
t
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
 
i
n
t
o
 
a
 
s
i
n
g
l
e
-
l
i
n
e
 
C
S
V
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
L
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
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
 
i
n
t
o
 
C
S
V
.


 
 
 
 
 
 
 
 
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
 
C
S
V
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
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


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
'
,
'
.
j
o
i
n
(
s
t
r
i
n
g
s
)
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
c
s
v
_
t
o
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
n
e
w
l
i
n
e
(
s
t
r
i
n
g
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
,
 
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


 
 
 
 
F
o
r
m
a
t
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
 
i
n
t
o
 
a
 
s
i
n
g
l
e
-
l
i
n
e
 
C
S
V
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
L
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
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
 
i
n
t
o
 
C
S
V
.


 
 
 
 
 
 
 
 
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
 
C
S
V
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
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


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
'
\
n
'
.
j
o
i
n
(
s
t
r
i
n
g
s
)
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
c
s
v
_
t
o
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
n
e
w
l
i
n
e
_
a
n
d
_
h
e
a
d
e
r
(
s
t
r
i
n
g
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
,
 
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


 
 
 
 
F
o
r
m
a
t
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
 
i
n
t
o
 
a
 
s
i
n
g
l
e
-
l
i
n
e
 
C
S
V
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
L
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
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
 
i
n
t
o
 
C
S
V
.


 
 
 
 
 
 
 
 
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
 
C
S
V
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
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


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
'
\
n
'
.
j
o
i
n
(
s
t
r
i
n
g
s
)
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
c
s
v
_
t
o
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
n
e
w
l
i
n
e
_
a
n
d
_
h
e
a
d
e
r
_
w
i
t
h
_
q
u
o
t
e
s
(
s
t
r
i
n
g
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
,
 
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


 
 
 
 
F
o
r
m
a
t
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
 
i
n
t
o
 
a
 
s
i
n
g
l
e
-
l
i
n
e
 
C
S
V
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
L
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
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
 
i
n
t
o
 
C
S
V
.


 
 
 
 
 
 
 
 
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
 
C
S
V
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
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
import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_output.csv"  # Path for test output file

    def tearDown(self):
        # Delete the test file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def read_file(self, file_path):
        """Helper method to read file content as a string."""
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            self.fail(f"Failed to read file: {e}")

    def test_write_csv_to_file_with_multiple_strings(self):
        data = ["Apple", "Banana", "Cherry"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple,Banana,Cherry", content)

    def test_write_csv_to_file_with_single_string(self):
        data = ["Apple"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple", content)

    def test_write_csv_to_file_with_empty_list(self):
        data = []
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file is empty
        content = self.read_file(self.test_file_path)
        self.assertEqual("", content)

    def test_write_csv_to_file_with_special_characters(self):
        data = ["Apple", "Banana, Cherry", "Date"]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple,Banana, Cherry,Date", content)

    def test_write_csv_to_file_with_spaces(self):
        data = ["Apple ", " Banana", " Cherry "]
        write_csv_to_file(data, self.test_file_path)
        # Assert the content of the file with spaces
        content = self.read_file(self.test_file_path)
        self.assertEqual("Apple , Banana, Cherry ", content)

    def test_write_csv_to_file_with_file_overwrite(self):
        # First write to the file
        first_data = ["Apple", "Banana"]
        write_csv_to_file(first_data, self.test_file_path)

        # Now overwrite with new data
        second_data = ["Cherry", "Date"]
        write_csv_to_file(second_data, self.test_file_path)

        # Assert that the file now contains the new data
        content = self.read_file(self.test_file_path)
        self.assertEqual("Cherry,Date", content)
if __name__ == '__main__':
    unittest.main()