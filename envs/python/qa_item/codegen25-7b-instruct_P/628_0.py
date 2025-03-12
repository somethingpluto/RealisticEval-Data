d
e
f
 
m
o
d
i
f
y
_
l
i
n
e
_
i
n
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
p
a
t
h
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
n
u
m
b
e
r
:
 
i
n
t
,
 
n
e
w
_
v
a
l
u
e
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


 
 
 
 
M
o
d
i
f
i
e
s
 
a
 
s
p
e
c
i
f
i
c
 
l
i
n
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
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
 
b
e
 
m
o
d
i
f
i
e
d
.


 
 
 
 
 
 
 
 
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
 
n
u
m
b
e
r
 
t
o
 
b
e
 
m
o
d
i
f
i
e
d
 
(
1
-
b
a
s
e
d
 
i
n
d
e
x
)
.


 
 
 
 
 
 
 
 
n
e
w
_
v
a
l
u
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
e
w
 
v
a
l
u
e
 
t
o
 
u
p
d
a
t
e
 
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
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
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


 
 
 
 
l
i
n
e
s
[
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
 
-
 
1
]
 
=
 
n
e
w
_
v
a
l
u
e


 
 
 
 
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
l
i
n
e
s
(
l
i
n
e
s
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
n
u
m
b
e
r
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
p
a
t
h
:
 
s
t
r
,
 
s
e
a
r
c
h
_
v
a
l
u
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
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
l
i
n
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
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
 
b
e
 
s
e
a
r
c
h
e
d
.


 
 
 
 
 
 
 
 
s
e
a
r
c
h
_
v
a
l
u
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
 
v
a
l
u
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
i
n
 
t
h
e
 
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
 
o
f
 
t
h
e
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
s
e
a
r
c
h
 
v
a
l
u
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


 
 
 
 
 
 
 
 
f
o
r
 
i
,
 
l
i
n
e
 
i
n
 
e
n
u
m
e
r
a
t
e
(
f
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
s
e
a
r
c
h
_
v
a
l
u
e
 
i
n
 
l
i
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
 
+
 
1


 
 
 
 
r
e
t
u
r
n
 
-
1






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
r
e
g
e
x
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
 
s
e
a
r
c
h
_
r
e
g
e
x
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
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
l
i
n
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
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
 
b
e
 
s
e
a
r
c
h
e
d
.


 
 
 
 
 
 
 
 
s
e
a
r
c
h
_
r
e
g
e
x
 
(
s
t
r
)
:
 
T
h
e
 
r
e
g
e
x
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
i
n
 
t
h
e
 
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
 
o
f
 
t
h
e
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
t
h
e
 
s
e
a
r
c
h
 
v
a
l
u
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


 
 
 
 
 
 
 
 
f
o
r
 
i
,
 
l
i
n
e
 
i
n
 
e
n
u
m
e
r
a
t
e
(
f
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
r
e
.
s
e
a
r
c
h
(
s
e
a
r
c
h
_
r
e
g
e
x
,
 
l
i
n
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
 
+
 
1


 
 
 
 
r
e
t
u
r
n
 
-
1






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
r
e
g
e
x
_
m
u
l
t
i
p
l
e
_
m
a
t
import os
import unittest


class TestAnswer(unittest.TestCase):
    TEST_FILE = "testFile.txt"

    def setUp(self):
        # Create a test file with initial content
        with open(self.TEST_FILE, 'w') as writer:
            writer.write("Line 1\n")
            writer.write("Line 2\n")
            writer.write("Line 3\n")

    def tearDown(self):
        # Clean up the test file after each test
        try:
            os.remove(self.TEST_FILE)
        except FileNotFoundError:
            pass  # File might already be deleted

    def test_modify_line_success(self):
        modify_line_in_file(self.TEST_FILE, 2, "Updated Line 2")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Line 1\n", reader.readline())
            self.assertEqual("Updated Line 2\n", reader.readline())
            self.assertEqual("Line 3\n", reader.readline())

    def test_modify_first_line(self):
        modify_line_in_file(self.TEST_FILE, 1, "Updated Line 1")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Updated Line 1\n", reader.readline())
            self.assertEqual("Line 2\n", reader.readline())
            self.assertEqual("Line 3\n", reader.readline())

    def test_modify_last_line(self):
        modify_line_in_file(self.TEST_FILE, 3, "Updated Line 3")
        with open(self.TEST_FILE, 'r') as reader:
            self.assertEqual("Line 1\n", reader.readline())
            self.assertEqual("Line 2\n", reader.readline())
            self.assertEqual("Updated Line 3\n", reader.readline())

    def test_modify_non_existent_line(self):
        with self.assertRaises(Exception):
            modify_line_in_file(self.TEST_FILE, 4, "Should Fail")

    def test_modify_negative_line_number(self):
        with self.assertRaises(Exception):
            modify_line_in_file(self.TEST_FILE, 0, "Should Fail")

if __name__ == '__main__':
    unittest.main()