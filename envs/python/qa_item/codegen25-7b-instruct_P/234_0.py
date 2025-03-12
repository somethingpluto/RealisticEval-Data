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
o
r
_
s
k
i
p
_
r
o
w
(
f
i
l
e
_
h
a
n
d
l
e
r
,
 
r
e
a
d
e
r
,
 
r
o
w
_
c
a
n
d
i
d
a
t
e
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
 
a
 
n
e
w
 
r
o
w
 
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
 
i
f
 
t
h
e
r
e
 
i
s
n
'
t
 
a
 
r
o
w
 
w
i
t
h
 
m
a
t
c
h
i
n
g
 
v
a
l
u
e
s
 
i
n
 
t
h
e
 
f
i
r
s
t
 
t
h
r
e
e
 
c
o
l
u
m
n
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
h
a
n
d
l
e
r
:
 
F
i
l
e
 
h
a
n
d
l
e
r
 
o
f
 
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
 
o
p
e
n
e
d
 
i
n
 
r
e
a
d
-
p
l
u
s
 
m
o
d
e
 
(
'
r
+
'
)
.


 
 
 
 
 
 
 
 
r
e
a
d
e
r
:
 
C
S
V
 
r
e
a
d
e
r
 
o
b
j
e
c
t
 
f
o
r
 
r
e
a
d
i
n
g
 
e
x
i
s
t
i
n
g
 
r
o
w
s
.


 
 
 
 
 
 
 
 
r
o
w
_
c
a
n
d
i
d
a
t
e
:
 
L
i
s
t
 
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
e
w
 
r
o
w
 
t
o
 
b
e
 
a
p
p
e
n
d
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




 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
e
a
d
e
r
:


 
 
 
 
 
 
 
 
i
f
 
r
o
w
[
0
]
 
=
=
 
r
o
w
_
c
a
n
d
i
d
a
t
e
[
0
]
 
a
n
d
 
r
o
w
[
1
]
 
=
=
 
r
o
w
_
c
a
n
d
i
d
a
t
e
[
1
]
 
a
n
d
 
r
o
w
[
2
]
 
=
=
 
r
o
w
_
c
a
n
d
i
d
a
t
e
[
2
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n


 
 
 
 
f
i
l
e
_
h
a
n
d
l
e
r
.
s
e
e
k
(
0
)


 
 
 
 
f
i
l
e
_
h
a
n
d
l
e
r
.
t
r
u
n
c
a
t
e
(
)


 
 
 
 
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
_
h
a
n
d
l
e
r
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
(
r
o
w
_
c
a
n
d
i
d
a
t
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
 
g
e
t
_
f
i
l
e
_
h
a
n
d
l
e
r
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


 
 
 
 
"
"
"


 
 
 
 
O
p
e
n
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
 
r
e
t
u
r
n
s
 
a
 
f
i
l
e
 
h
a
n
d
l
e
r
 
a
n
d
 
a
 
C
S
V
 
r
e
a
d
e
r
 
o
b
j
e
c
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


 
 
 
 
 
 
 
 
f
i
l
e
_
h
a
n
d
l
e
r
:
 
F
i
l
e
 
h
a
n
d
l
e
r
 
o
f
 
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
 
o
p
e
n
e
d
 
i
n
 
r
e
a
d
-
p
l
u
s
 
m
o
d
e
 
(
'
r
+
'
)
.


 
 
 
 
 
 
 
 
r
e
a
d
e
r
:
 
C
S
V
 
r
e
a
d
e
r
 
o
b
j
e
c
t
 
f
o
r
 
r
e
a
d
i
n
g
 
e
x
i
s
t
i
n
g
 
r
o
w
s
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
e
_
h
a
n
d
l
e
r
 
=
 
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
+
'
)


 
 
 
 
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
_
h
a
n
d
l
e
r
)


 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
_
h
a
n
d
l
e
r
,
 
r
e
a
d
e
r






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
p
a
t
h
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
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
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
:
 
N
a
m
e
 
o
f
 
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


 
 
 
 
 
 
 
 
P
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
_
_
f
i
l
e
_
_
)
,
 
f
i
l
e
_
n
a
m
e
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
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
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


 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
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


 
 
 
 
r
e
t
u
r
n
 
o
s
.
p
a
t
h
.
b
a
s
e
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
e
x
t
e
n
s
i
o
n
(
f
i
l
e
_
import csv
import io
import unittest


class TestAppendOrSkipRow(unittest.TestCase):

    def setUp(self):
        """Set up a mock CSV file using StringIO."""
        self.mock_file = io.StringIO()
        self.mock_file.write("Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n")
        self.mock_file.seek(0)  # Reset pointer to the start of the mock file
        self.reader = csv.reader(self.mock_file)

    def test_append_new_row(self):
        """Test appending a new row when there are no matching values."""
        new_row = ['David', '28', 'Australia']
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_skip_different_values(self):
        """Test appending a new row with different values."""
        new_row = ['Alice', '31', 'USA']  # Same name, different age
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_append_row_with_different_columns(self):
        """Test appending a row with different values in the first three columns."""
        new_row = ['Eve', '40', 'Australia', 'Engineer']
        append_or_skip_row(self.mock_file, self.reader, new_row)

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        self.assertIn(new_row, result)

    def test_multiple_appends(self):
        """Test appending multiple new rows correctly."""
        new_rows = [
            ['Frank', '29', 'Germany'],
            ['Grace', '22', 'France']
        ]

        for row in new_rows:
            append_or_skip_row(self.mock_file, self.reader, row)
            self.mock_file.seek(0)  # Reset pointer for the next read
            self.reader = csv.reader(self.mock_file)  # Recreate the reader after each append

        self.mock_file.seek(0)  # Reset pointer to read from the start
        result = list(csv.reader(self.mock_file))
        for row in new_rows:
            self.assertIn(row, result)
if __name__ == '__main__':
    unittest.main()