d
e
f
 
r
e
n
a
m
e
_
p
n
g
_
f
i
l
e
s
_
i
n
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
n
a
m
e
s
 
P
N
G
 
f
i
l
e
s
 
i
n
 
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
 
d
i
r
e
c
t
o
r
y
 
b
y
 
a
p
p
e
n
d
i
n
g
 
a
 
s
e
q
u
e
n
c
e
 
n
u
m
b
e
r
 
t
o
 
e
a
c
h
 
f
i
l
e
.


 
 
 
 
T
h
e
 
f
i
l
e
s
 
a
r
e
 
s
o
r
t
e
d
 
a
l
p
h
a
b
e
t
i
c
a
l
l
y
,
 
a
n
d
 
e
a
c
h
 
b
a
s
e
 
n
a
m
e
 
i
s
 
a
s
s
i
g
n
e
d
 
s
e
q
u
e
n
t
i
a
l
 
n
u
m
b
e
r
s
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
 
h
a
v
e
 
t
h
r
e
e
 
P
N
G
 
f
i
l
e
s
 
s
u
c
h
 
a
s
 
"
i
m
a
g
e
1
.
p
n
g
"
,
 
"
i
m
a
g
e
2
.
p
n
g
"
,
 
"
i
m
a
g
e
3
.
p
n
g
"


 
 
 
 
 
 
 
 
a
f
t
e
r
 
r
e
n
a
m
i
n
g
 
P
N
G
 
f
i
l
e
s
 
a
r
e
 
"
i
m
a
g
e
1
0
0
1
.
p
n
g
"
,
 
"
i
m
a
g
e
2
0
0
1
.
p
n
g
"
,
 
"
i
m
a
g
e
3
0
0
1
.
p
n
g
"




 
 
 
 
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
 
d
i
r
e
c
t
o
r
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
 
P
N
G
 
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
n
a
m
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


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
P
N
G
 
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
 
d
i
r
e
c
t
o
r
y


 
 
 
 
p
n
g
_
f
i
l
e
s
 
=
 
g
e
t
_
p
n
g
_
f
i
l
e
s
_
i
n
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
)




 
 
 
 
#
 
R
e
n
a
m
e
 
t
h
e
 
P
N
G
 
f
i
l
e
s


 
 
 
 
f
o
r
 
i
,
 
f
i
l
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
p
n
g
_
f
i
l
e
s
)
:


 
 
 
 
 
 
 
 
#
 
G
e
t
 
t
h
e
 
b
a
s
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


 
 
 
 
 
 
 
 
b
a
s
e
_
n
a
m
e
 
=
 
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
)




 
 
 
 
 
 
 
 
#
 
G
e
t
 
t
h
e
 
b
a
s
e
 
n
a
m
e
 
w
i
t
h
o
u
t
 
t
h
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


 
 
 
 
 
 
 
 
b
a
s
e
_
n
a
m
e
_
w
i
t
h
o
u
t
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
 
=
 
o
s
.
p
a
t
h
.
s
p
l
i
t
e
x
t
(
b
a
s
e
_
n
a
m
e
)
[
0
]




 
 
 
 
 
 
 
 
#
 
G
e
t
 
t
h
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


 
 
 
 
 
 
 
 
e
x
t
e
n
s
i
o
n
 
=
 
o
s
.
p
a
t
h
.
s
p
l
i
t
e
x
t
(
b
a
s
e
_
n
a
m
e
)
[
1
]




 
 
 
 
 
 
 
 
#
 
R
e
n
a
m
e
 
t
h
e
 
f
i
l
e


 
 
 
 
 
 
 
 
n
e
w
_
n
a
m
e
 
=
 
b
a
s
e
_
n
a
m
e
_
w
i
t
h
o
u
t
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
 
+
 
s
t
r
(
i
 
+
 
1
)
.
z
f
i
l
l
(
4
)
 
+
 
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
s
.
r
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
,
 
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
 
n
e
w
_
n
a
m
e
)
)






d
e
f
 
r
e
n
a
m
e
_
p
n
g
_
f
i
l
e
s
_
i
n
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
_
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
:


 
 
 
 
"
"
"


 
 
 
 
R
e
n
a
m
e
s
 
P
N
G
 
f
i
l
e
s
 
i
n
 
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
 
d
i
r
e
c
t
o
r
y
 
a
n
d
 
i
t
s
 
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
 
b
y
 
a
p
p
e
n
d
i
n
g
 
a
 
s
e
q
u
e
n
c
e
 
n
u
m
b
e
r
 
t
o
 
e
a
c
h
 
f
i
l
e
.


 
 
 
 
T
h
e
 
f
i
l
e
s
 
a
r
e
 
s
o
r
t
e
d
 
a
l
p
h
a
b
e
t
i
c
a
l
l
y
,
 
a
n
d
 
e
a
c
h
 
b
a
s
e
 
n
a
m
e
 
i
s
 
a
s
s
i
g
n
e
d
 
s
e
q
u
e
n
t
i
a
l
 
n
u
m
b
e
r
s
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
 
h
a
v
e
 
t
h
r
e
e
 
P
N
G
 
f
i
l
e
s
 
s
u
c
h
 
a
s
 
"
i
m
a
g
e
1
.
p
n
g
"
,
 
"
i
m
a
g
e
2
.
p
n
g
"
,
 
"
i
m
a
g
e
3
.
p
n
g
"


 
 
 
 
 
 
 
 
a
f
t
e
r
 
r
e
n
a
m
i
n
g
 
P
N
G
 
f
i
l
e
s
 
a
r
e
 
"
i
m
a
g
e
1
0
0
1
.
p
n
g
"
,
 
"
i
m
a
g
e
2
0
0
1
.
p
n
g
"
,
 
"
i
m
a
g
e
3
0
0
1
.
p
n
g
"




 
 
 
 
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
 
d
i
r
e
c
t
o
r
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
 
P
N
G
 
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
n
a
m
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


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
P
N
G
 
f
i
l
e
s
import re
import unittest
import os
import shutil
import tempfile
from pathlib import Path



class TestRenameFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for each test
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after each test
        shutil.rmtree(self.test_dir)

    def create_png_files(self, filenames):
        for filename in filenames:
            file_path = Path(self.test_dir) / filename
            file_path.touch()  # Create an empty file

    def test_basic_renaming(self):
        # Test renaming in a basic scenario with simple filenames
        filenames = ["image1.png", "image2.png", "image3.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'image3001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_reset_counter_for_different_base_names(self):
        # Test that the counter resets for different base names
        filenames = ["image1.png", "picture1.png", "image2.png", "picture2.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['image1001.png', 'image2001.png', 'picture1001.png', 'picture2001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_no_png_files(self):
        # Test handling of directories with no PNG files
        filenames = ["file1.txt", "file2.jpg"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = filenames  # No changes expected
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)

    def test_empty_directory(self):
        # Test handling of an empty directory
        rename_png_files_in_directory(self.test_dir)
        expected_files = []  # No files to rename
        result_files = os.listdir(self.test_dir)
        self.assertEqual(result_files, expected_files)

    def test_files_with_existing_numbers(self):
        # Test renaming files that already have numbers in their names
        filenames = ["file001.png", "file002.png", "file003.png"]
        self.create_png_files(filenames)

        rename_png_files_in_directory(self.test_dir)

        expected_files = ['file001001.png', 'file002001.png', 'file003001.png']
        result_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(result_files, expected_files)
if __name__ == '__main__':
    unittest.main()