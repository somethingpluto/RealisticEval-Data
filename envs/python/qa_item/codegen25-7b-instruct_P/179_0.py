d
e
f
 
c
o
p
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
s
o
u
r
c
e
_
d
i
r
:
 
s
t
r
,
 
t
a
r
g
e
t
_
d
i
r
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


 
 
 
 
C
o
p
i
e
s
 
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
 
f
r
o
m
 
t
h
e
 
s
o
u
r
c
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
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
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


 
 
 
 
 
 
 
 
s
o
u
r
c
e
_
d
i
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
 
s
o
u
r
c
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
 
f
r
o
m
 
w
h
i
c
h
 
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
 
w
i
l
l
 
b
e
 
c
o
p
i
e
d
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
d
i
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
 
t
a
r
g
e
t
 
d
i
r
e
c
t
o
r
y
 
t
o
 
w
h
i
c
h
 
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
 
w
i
l
l
 
b
e
 
c
o
p
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
e
x
i
s
t
s
(
s
o
u
r
c
e
_
d
i
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
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
(
f
"
S
o
u
r
c
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
 
{
s
o
u
r
c
e
_
d
i
r
}
 
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
"
)




 
 
 
 
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
e
x
i
s
t
s
(
t
a
r
g
e
t
_
d
i
r
)
:


 
 
 
 
 
 
 
 
o
s
.
m
a
k
e
d
i
r
s
(
t
a
r
g
e
t
_
d
i
r
)




 
 
 
 
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
s
o
u
r
c
e
_
d
i
r
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


 
 
 
 
 
 
 
 
 
 
 
 
s
o
u
r
c
e
_
f
i
l
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


 
 
 
 
 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
f
i
l
e
 
=
 
s
o
u
r
c
e
_
f
i
l
e
.
r
e
p
l
a
c
e
(
s
o
u
r
c
e
_
d
i
r
,
 
t
a
r
g
e
t
_
d
i
r
)


 
 
 
 
 
 
 
 
 
 
 
 
o
s
.
m
a
k
e
d
i
r
s
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
t
a
r
g
e
t
_
f
i
l
e
)
,
 
e
x
i
s
t
_
o
k
=
T
r
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
s
h
u
t
i
l
.
c
o
p
y
(
s
o
u
r
c
e
_
f
i
l
e
,
 
t
a
r
g
e
t
_
f
i
l
e
)






d
e
f
 
c
o
p
y
_
f
i
l
e
(
s
o
u
r
c
e
_
f
i
l
e
:
 
s
t
r
,
 
t
a
r
g
e
t
_
f
i
l
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


 
 
 
 
C
o
p
i
e
s
 
t
h
e
 
s
o
u
r
c
e
 
f
i
l
e
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
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
o
u
r
c
e
_
f
i
l
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
 
s
o
u
r
c
e
 
f
i
l
e
 
f
r
o
m
 
w
h
i
c
h
 
t
h
e
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
e
 
c
o
p
i
e
d
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
f
i
l
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
 
t
a
r
g
e
t
 
f
i
l
e
 
t
o
 
w
h
i
c
h
 
t
h
e
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
e
 
c
o
p
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
e
x
i
s
t
s
(
s
o
u
r
c
e
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
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
(
f
"
S
o
u
r
c
e
 
f
i
l
e
 
{
s
o
u
r
c
e
_
f
i
l
e
}
 
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
"
)




 
 
 
 
o
s
.
m
a
k
e
d
i
r
s
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
t
a
r
g
e
t
_
f
i
l
e
)
,
 
e
x
i
s
t
_
o
k
=
T
r
u
e
)


 
 
 
 
s
h
u
t
i
l
.
c
o
p
y
(
s
o
u
r
c
e
_
f
i
l
e
,
 
t
a
r
g
e
t
_
f
i
l
e
)






d
e
f
 
c
o
p
y
_
f
i
l
e
_
t
o
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
s
o
u
r
c
e
_
f
i
l
e
:
 
s
t
r
,
 
t
a
r
g
e
t
_
d
i
r
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


 
 
 
 
C
o
p
i
e
s
 
t
h
e
 
s
o
u
r
c
e
 
f
i
l
e
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
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


 
 
 
 
 
 
 
 
s
o
u
r
c
e
_
f
i
l
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
 
s
o
u
r
c
e
 
f
i
l
e
 
f
r
o
m
 
w
h
i
c
h
 
t
h
e
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
e
 
c
o
p
i
e
d
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
d
i
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
 
t
a
r
g
e
t
 
d
i
r
e
c
t
o
r
y
 
t
o
 
w
h
i
c
h
 
t
h
e
 
c
o
n
t
e
n
t
 
w
i
l
l
 
b
e
 
c
o
p
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
import os
import shutil
import unittest


class TestDirectoryOperations(unittest.TestCase):

    def setUp(self):
        self.source_dir = "testSourceDir"
        self.target_dir = "testTargetDir"

        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.target_dir, exist_ok=True)

    def tearDown(self):
        self.delete_directory(self.source_dir)
        self.delete_directory(self.target_dir)

    def delete_directory(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def test_copy_empty_directory(self):
        # Simulating Answer.copyDirectory functionality
        copy_directory(self.source_dir, self.target_dir)

        self.assertTrue(os.path.exists(self.target_dir), "Target directory should exist after copying.")
        self.assertTrue(os.path.isdir(self.target_dir), "Target directory should be a directory.")
        self.assertEqual(len(os.listdir(self.target_dir)), 0, "Target directory should be empty.")

    def test_copy_directory_with_files(self):
        test_file = os.path.join(self.source_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Sample content")

        copy_directory(self.source_dir, self.target_dir)

        copied_file = os.path.join(self.target_dir, "testFile.txt")
        self.assertTrue(os.path.exists(copied_file), "File should be copied to target directory.")
        self.assertEqual(os.path.getsize(test_file), os.path.getsize(copied_file),
                         "File size should be the same after copying.")

    def test_non_existent_source_directory(self):
        non_existent_dir = "nonExistentDir"

        with self.assertRaises(Exception) as context:
            copy_directory(non_existent_dir, self.target_dir)

        self.assertEqual(str(context.exception), "Source directory does not exist.")

    def test_copy_directory_with_subdirectories(self):
        sub_dir = os.path.join(self.source_dir, "subDir")
        os.makedirs(sub_dir, exist_ok=True)
        test_file = os.path.join(sub_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Sample content in subdirectory")

        copy_directory(self.source_dir, self.target_dir)

        copied_sub_dir = os.path.join(self.target_dir, "subDir")
        copied_file = os.path.join(copied_sub_dir, "testFile.txt")

        self.assertTrue(os.path.exists(copied_sub_dir), "Subdirectory should be copied to target directory.")
        self.assertTrue(os.path.exists(copied_file), "File within subdirectory should be copied to target directory.")

    def test_overwrite_file_in_target_directory(self):
        # Create a source file with some content
        test_file = os.path.join(self.source_dir, "testFile.txt")
        with open(test_file, 'w') as f:
            f.write("Source content")

        # Create a target file with different content
        target_file = os.path.join(self.target_dir, "testFile.txt")
        with open(target_file, 'w') as f:
            f.write("Target content")

        # Copy the directory, which should overwrite the target file
        copy_directory(self.source_dir, self.target_dir)

        copied_file = os.path.join(self.target_dir, "testFile.txt")
        self.assertTrue(os.path.exists(copied_file), "File should be copied to target directory.")

        # Check that the content of the file is now the same as the source file
        with open(copied_file, 'r') as f:
            copied_content = f.read()

        self.assertEqual(copied_content, "Source content",
                         "File in target directory should be overwritten with source content.")

if __name__ == '__main__':
    unittest.main()