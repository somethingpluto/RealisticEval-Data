i
m
p
o
r
t
 
c
s
v


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
c
s
v
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
 
a
 
C
S
V
 
f
i
l
e
 
a
n
d
 
p
a
r
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
 
i
n
t
o
 
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
 
C
S
V
 
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
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
l
i
s
t
 
r
e
p
r
e
s
e
n
t
s
 
a
 
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
 
C
S
V
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
i
l
e
:


 
 
 
 
 
 
 
 
r
e
a
d
e
r
 
=
 
c
s
v
.
r
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
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
l
i
s
t
(
r
e
a
d
e
r
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
 
l
i
s
t
s
 
t
o
 
a
 
C
S
V
 
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
 
C
S
V
 
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
 
C
S
V
 
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
,
 
n
e
w
l
i
n
e
=
'
'
)
 
a
s
 
f
i
l
e
:


 
 
 
 
 
 
 
 
w
r
i
t
e
r
 
=
 
c
s
v
.
w
r
i
t
e
r
(
f
i
l
e
)


 
 
 
 
 
 
 
 
w
r
i
t
e
r
.
w
r
i
t
e
r
o
w
s
(
d
a
t
a
)






d
e
f
 
r
e
a
d
_
c
s
v
_
a
s
_
d
i
c
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
d
i
c
t
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
 
C
S
V
 
f
i
l
e
 
a
n
d
 
p
a
r
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
 
i
n
t
o
 
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
 
C
S
V
 
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
d
i
c
t
]
:
 
A
 
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
,
 
w
h
e
r
e
 
e
a
c
h
 
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
 
r
e
p
r
e
s
e
n
t
s
 
a
 
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
 
C
S
V
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
i
l
e
:


 
 
 
 
 
 
 
 
r
e
a
d
e
r
 
=
 
c
s
v
.
D
i
c
t
R
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
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
l
i
s
t
(
r
e
a
d
e
r
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
a
s
_
d
i
c
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
d
i
c
t
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
 
C
S
V
 
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
 
C
S
V
 
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
d
i
c
t
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
 
C
S
V
 
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
,
 
n
e
w
l
i
n
e
=
'
'
)
 
a
s
 
f
i
l
e
:


 
 
 
 
 
 
 
 
w
r
i
t
e
r
 
=
 
c
s
v
.
D
i
c
t
W
r
i
t
e
r
(
f
i
l
e
,
 
f
i
e
l
d
n
a
m
e
s
=
d
a
t
a
[
0
]
.
k
e
y
s
(
)
)
import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_file_path = 'test.csv'
        sample_csv_content = "Name,Age,Location\n" + \
                             "Alice,30,New York\n" + \
                             "Bob,25,Los Angeles\n" + \
                             "Charlie,35,Chicago\n"
        with open(self.test_file_path, 'w') as file:
            file.write(sample_csv_content)

    def test_read_valid_csv(self):
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 4)  # 4 lines including the header
        self.assertEqual(result[0], ["Name", "Age", "Location"])  # Check header
        self.assertEqual(result[1], ["Alice", "30", "New York"])
        self.assertEqual(result[2], ["Bob", "25", "Los Angeles"])
        self.assertEqual(result[3], ["Charlie", "35", "Chicago"])

    def test_read_empty_csv(self):
        # Create an empty CSV file
        with open(self.test_file_path, 'w') as file:
            file.write("")
        result = read_csv(self.test_file_path)
        self.assertTrue(len(result) == 0)  # Expecting an empty list

    def test_read_csv_with_quotes(self):
        # Write CSV content with quoted fields
        content_with_quotes = '"Name","Age","Location"\n' + \
                              '"Alice","30","New York"\n' + \
                              '"Bob","25","Los Angeles"\n'
        with open(self.test_file_path, 'w') as file:
            file.write(content_with_quotes)
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 3)  # 3 lines including the header
        self.assertEqual(result[0], ['Name', 'Age', 'Location'])

    def test_read_invalid_csv_file(self):
        with self.assertRaises(FileNotFoundError):
            read_csv('non_existent_file.csv')

    def test_read_csv_with_different_delimiters(self):
        # Write CSV content with semicolons instead of commas
        content_with_semicolons = "Name;Age;Location\n" + \
                                  "Alice;30;New York\n" + \
                                  "Bob;25;Los Angeles\n"
        with open(self.test_file_path, 'w') as file:
            file.write(content_with_semicolons)
        result = read_csv(self.test_file_path)
        self.assertEqual(len(result), 3)  # Expecting 3 lines
        self.assertEqual(result[0], ["Name;Age;Location"])

    def tearDown(self):
        # Clean up: remove test file after tests
        try:
            os.remove(self.test_file_path)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()