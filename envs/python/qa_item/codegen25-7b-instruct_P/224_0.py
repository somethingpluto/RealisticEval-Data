d
e
f
 
e
m
p
t
y
_
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
d
i
r
e
c
t
o
r
y
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


 
 
 
 
e
m
p
t
y
 
a
l
l
 
f
i
l
e
s
 
a
n
d
 
s
u
b
d
i
r
e
c
t
o
r
i
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
 
P
a
t
h
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
w
h
o
s
e
 
c
o
n
t
e
n
t
s
 
a
r
e
 
t
o
 
b
e
 
e
m
p
t
i
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
 
o
r
 
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
 
s
p
e
c
i
f
i
e
d
 
p
a
t
h
 
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
 
o
r
 
i
s
 
n
o
t
 
a
 
d
i
r
e
c
t
o
r
y
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
i
s
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
f
"
{
d
i
r
e
c
t
o
r
y
_
p
a
t
h
}
 
i
s
 
n
o
t
 
a
 
d
i
r
e
c
t
o
r
y
"
)


 
 
 
 
f
o
r
 
f
i
l
e
_
p
a
t
h
 
i
n
 
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
_
p
a
t
h
)
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
 
=
 
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
_
p
a
t
h
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
)


 
 
 
 
 
 
 
 
i
f
 
o
s
.
p
a
t
h
.
i
s
d
i
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


 
 
 
 
 
 
 
 
 
 
 
 
s
h
u
t
i
l
.
r
m
t
r
e
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


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
o
s
.
r
e
m
o
v
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
p
a
t
h
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
:
s
t
r
=
N
o
n
e
,
 
r
e
c
u
r
s
i
v
e
:
b
o
o
l
=
F
a
l
s
e
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


 
 
 
 
G
e
t
 
a
 
l
i
s
t
 
o
f
 
f
i
l
e
 
p
a
t
h
s
 
i
n
 
a
 
d
i
r
e
c
t
o
r
y
.


 
 
 
 
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
 
P
a
t
h
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
.


 
 
 
 
 
 
 
 
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
s
t
r
)
:
 
F
i
l
e
 
e
x
t
e
n
s
i
o
n
 
o
f
 
t
h
e
 
f
i
l
e
s
 
t
o
 
b
e
 
r
e
t
u
r
n
e
d
.


 
 
 
 
 
 
 
 
r
e
c
u
r
s
i
v
e
 
(
b
o
o
l
)
:
 
I
f
 
T
r
u
e
,
 
r
e
c
u
r
s
i
v
e
l
y
 
s
e
a
r
c
h
 
s
u
b
d
i
r
e
c
t
o
r
i
e
s
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
 
L
i
s
t
 
o
f
 
f
i
l
e
 
p
a
t
h
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
p
a
t
h
s
 
=
 
[
]


 
 
 
 
i
f
 
r
e
c
u
r
s
i
v
e
:


 
 
 
 
 
 
 
 
f
o
r
 
r
o
o
t
,
 
d
i
r
s
,
 
f
i
l
e
s
 
i
n
 
o
s
.
w
a
l
k
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
_
p
a
t
h
)
:


 
 
 
 
 
 
 
 
 
 
 
 
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
 
i
s
 
N
o
n
e
 
o
r
 
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
)
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
s
.
a
p
p
e
n
d
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
r
o
o
t
,
 
f
i
l
e
)
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
f
o
r
 
f
i
l
e
 
i
n
 
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
_
p
a
t
h
)
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
 
=
 
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
_
p
a
t
h
,
 
f
i
l
e
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
o
s
.
p
a
t
h
.
i
s
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
)
 
a
n
d
 
(
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
 
i
s
 
N
o
n
e
 
o
r
 
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
)
)
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
s
.
a
p
p
e
n
d
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
p
a
t
h
s




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
s
_
w
i
t
h
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
d
i
r
e
c
t
o
r
y
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
:
s
t
r
,
 
r
e
c
u
r
s
i
v
e
:
b
o
o
l
=
F
a
l
s
e
import os
import shutil
import tempfile
import unittest


class TestEmptyDirectory(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory with some files and directories
        self.test_dir = tempfile.mkdtemp()
        # Create some files and directories
        os.mkdir(os.path.join(self.test_dir, 'subdir'))
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Hello")
        with open(os.path.join(self.test_dir, 'subdir', 'file2.txt'), 'w') as f:
            f.write("World")

    def tearDown(self):
        # Remove the temporary directory after each test.js
        shutil.rmtree(self.test_dir)

    def test_empty_directory_success(self):
        """ Test that the directory is emptied successfully """
        empty_directory(self.test_dir)
        self.assertEqual(os.listdir(self.test_dir), [])  # Directory should be empty



    def test_empty_directory_with_subdirectories(self):
        """ Test emptying a directory that includes subdirectories """
        empty_directory(self.test_dir)
        self.assertFalse(os.listdir(self.test_dir))  # Directory and subdirectory should be empty

    def test_empty_already_empty_directory(self):
        """ Test emptying a directory that is already empty """
        empty_directory(self.test_dir)  # First emptying
        empty_directory(self.test_dir)  # Empty again
        self.assertEqual(os.listdir(self.test_dir), [])  # Still should be empty

if __name__ == '__main__':
    unittest.main()