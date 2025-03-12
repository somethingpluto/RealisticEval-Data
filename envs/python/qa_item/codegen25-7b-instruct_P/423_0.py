d
e
f
 
w
r
i
t
e
_
u
n
i
q
u
e
_
l
i
n
e
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
n
a
m
e
:
 
s
t
r
,
 
l
i
n
e
_
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
 
l
i
n
e
 
t
o
 
a
 
t
e
x
t
 
f
i
l
e
 
o
n
l
y
 
i
f
 
t
h
e
 
l
i
n
e
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
c
o
n
t
e
n
t
 
d
o
e
s
 
n
o
t
 
a
l
r
e
a
d
y
 
e
x
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
 
w
r
i
t
e
 
t
o
.


 
 
 
 
 
 
 
 
l
i
n
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
s
t
r
)
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
 
l
i
n
e
 
t
o
 
w
r
i
t
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
f
i
l
e
n
a
m
e
,
 
'
a
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
_
c
o
n
t
e
n
t
 
n
o
t
 
i
n
 
f
.
r
e
a
d
(
)
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
_
c
o
n
t
e
n
t
 
+
 
'
\
n
'
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
u
n
i
q
u
e
_
l
i
n
e
s
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
n
a
m
e
:
 
s
t
r
,
 
l
i
n
e
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
 
t
o
 
a
 
t
e
x
t
 
f
i
l
e
 
o
n
l
y
 
i
f
 
t
h
e
 
l
i
n
e
s
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
c
o
n
t
e
n
t
 
d
o
 
n
o
t
 
a
l
r
e
a
d
y
 
e
x
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
 
w
r
i
t
e
 
t
o
.


 
 
 
 
 
 
 
 
l
i
n
e
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
 
T
h
e
 
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
 
t
o
 
w
r
i
t
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
f
i
l
e
n
a
m
e
,
 
'
a
'
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


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
 
n
o
t
 
i
n
 
f
.
r
e
a
d
(
)
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
 
'
\
n
'
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
u
n
i
q
u
e
_
j
s
o
n
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
n
a
m
e
:
 
s
t
r
,
 
j
s
o
n
_
c
o
n
t
e
n
t
:
 
D
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
 
j
s
o
n
 
o
b
j
e
c
t
 
t
o
 
a
 
t
e
x
t
 
f
i
l
e
 
o
n
l
y
 
i
f
 
t
h
e
 
j
s
o
n
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
c
o
n
t
e
n
t
 
d
o
e
s
 
n
o
t
 
a
l
r
e
a
d
y
 
e
x
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
 
w
r
i
t
e
 
t
o
.


 
 
 
 
 
 
 
 
j
s
o
n
_
c
o
n
t
e
n
t
 
(
D
i
c
t
)
:
 
T
h
e
 
j
s
o
n
 
o
b
j
e
c
t
 
t
o
 
w
r
i
t
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
f
i
l
e
n
a
m
e
,
 
'
a
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
i
f
 
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
j
s
o
n
_
c
o
n
t
e
n
t
)
 
n
o
t
 
i
n
 
f
.
r
e
a
d
(
)
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
j
s
o
n
_
c
o
n
t
e
n
t
)
 
+
 
'
\
n
'
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
u
n
i
q
u
e
_
j
s
o
n
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
f
i
l
e
n
a
m
e
:
 
s
t
r
,
 
j
s
o
n
_
c
o
n
t
e
n
t
:
 
D
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
 
j
s
o
n
 
o
b
j
e
c
t
 
t
o
 
a
 
t
e
x
t
 
f
i
l
e
 
o
n
l
y
 
i
f
 
t
h
e
 
j
s
o
n
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
c
o
n
t
e
n
t
 
d
o
e
s
 
n
o
t
 
a
l
r
e
a
d
y
 
e
x
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
 
w
r
i
t
e
 
t
o
.


 
 
 
 
 
 
 
 
j
s
o
n
_
c
o
n
t
e
n
t
 
(
D
i
c
t
)
:
 
T
h
e
 
j
s
o
n
 
o
b
j
e
c
t
 
t
o
 
w
r
i
t
e
.
import unittest
import os


class TestWriteUniqueLineToFile(unittest.TestCase):
    def setUp(self):
        # Setup: create a temporary file for testing.
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as file:
            file.write('')

    def test_write_new_line(self):
        # Test case 1: Writing a new line to an empty file.
        line_content = "First unique line."
        write_unique_line_to_file(self.filename, line_content)
        with open(self.filename, 'r') as file:
            self.assertIn(line_content, file.read())

    def test_write_duplicate_line(self):
        # Test case 2: Attempting to write a duplicate line.
        line_content = "First unique line."
        # Write the line once.
        write_unique_line_to_file(self.filename, line_content)
        # Attempt to write it again.
        write_unique_line_to_file(self.filename, line_content)
        # Check if the line was written only once.
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read().strip().count(line_content), 1)

    def test_write_multiple_unique_lines(self):
        # Test case 3: Writing multiple unique lines.
        lines = ["First unique line.", "Second unique line.", "Third unique line."]
        for line in lines:
            write_unique_line_to_file(self.filename, line)
        with open(self.filename, 'r') as file:
            file_content = file.read()
            for line in lines:
                self.assertIn(line, file_content)

    def test_write_empty_line(self):
        # Test case 5: Writing an empty line, should not write.
        line_content = ""
        write_unique_line_to_file(self.filename, line_content)
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read(), "")

if __name__ == '__main__':
    unittest.main()