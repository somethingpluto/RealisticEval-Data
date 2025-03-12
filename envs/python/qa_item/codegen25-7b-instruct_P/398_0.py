i
m
p
o
r
t
 
o
s


i
m
p
o
r
t
 
c
s
v


i
m
p
o
r
t
 
s
h
u
t
i
l






d
e
f
 
e
x
t
r
a
c
t
_
f
i
l
e
s
_
e
x
c
l
u
d
i
n
g
_
c
s
v
(
f
o
l
d
e
r
A
:
 
s
t
r
,
 
c
s
v
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
 
f
o
l
d
e
r
B
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
p
y
 
f
i
l
e
s
 
f
r
o
m
 
f
o
l
d
e
r
A
 
t
o
 
f
o
l
d
e
r
B
 
e
x
c
l
u
d
i
n
g
 
t
h
o
s
e
 
l
i
s
t
e
d
 
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
o
l
d
e
r
A
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
 
s
o
u
r
c
e
 
f
o
l
d
e
r
 
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
 
a
l
l
 
f
i
l
e
s
 
(
s
t
r
)
.


 
 
 
 
 
 
 
 
c
s
v
_
f
i
l
e
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
 
f
i
l
e
n
a
m
e
s
 
t
o
 
e
x
c
l
u
d
e
 
(
s
t
r
)
.


 
 
 
 
 
 
 
 
f
o
l
d
e
r
B
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
e
s
t
i
n
a
t
i
o
n
 
f
o
l
d
e
r
 
(
s
t
r
)
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


 
 
 
 
#
 
R
e
a
d
 
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


 
 
 
 
w
i
t
h
 
o
p
e
n
(
c
s
v
_
f
i
l
e
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
)


 
 
 
 
 
 
 
 
c
s
v
_
l
i
s
t
 
=
 
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
 
f
i
l
e
s
 
i
n
 
f
o
l
d
e
r
A


 
 
 
 
f
i
l
e
s
_
i
n
_
f
o
l
d
e
r
A
 
=
 
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
f
o
l
d
e
r
A
)




 
 
 
 
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
 
f
i
l
e
s
 
t
o
 
e
x
c
l
u
d
e


 
 
 
 
f
i
l
e
s
_
t
o
_
e
x
c
l
u
d
e
 
=
 
[
]


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
c
s
v
_
l
i
s
t
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
_
i
n
_
f
o
l
d
e
r
A
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
.
s
t
a
r
t
s
w
i
t
h
(
r
o
w
[
0
]
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
s
_
t
o
_
e
x
c
l
u
d
e
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
)




 
 
 
 
#
 
C
o
p
y
 
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
 
f
o
l
d
e
r
B


 
 
 
 
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
_
i
n
_
f
o
l
d
e
r
A
:


 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
 
n
o
t
 
i
n
 
f
i
l
e
s
_
t
o
_
e
x
c
l
u
d
e
:


 
 
 
 
 
 
 
 
 
 
 
 
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
f
o
l
d
e
r
A
,
 
f
i
l
e
)
,
 
f
o
l
d
e
r
B
)






d
e
f
 
e
x
t
r
a
c
t
_
f
i
l
e
s
_
e
x
c
l
u
d
i
n
g
_
l
i
s
t
(
f
o
l
d
e
r
A
:
 
s
t
r
,
 
l
i
s
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
,
 
f
o
l
d
e
r
B
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
p
y
 
f
i
l
e
s
 
f
r
o
m
 
f
o
l
d
e
r
A
 
t
o
 
f
o
l
d
e
r
B
 
e
x
c
l
u
d
i
n
g
 
t
h
o
s
e
 
l
i
s
t
e
d
 
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
 
l
i
s
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


 
 
 
 
 
 
 
 
f
o
l
d
e
r
A
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
 
s
o
u
r
c
e
 
f
o
l
d
e
r
 
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
 
a
l
l
 
f
i
l
e
s
 
(
s
t
r
)
.


 
 
 
 
 
 
 
 
l
i
s
t
_
f
i
l
e
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
 
l
i
s
t
 
f
i
l
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
 
f
i
l
e
n
a
m
e
s
 
t
o
 
e
x
c
l
u
d
e
 
(
s
t
r
)
.


 
 
 
 
 
 
 
 
f
o
l
d
e
r
B
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
e
s
t
i
n
a
t
i
o
n
 
f
o
l
d
e
r
 
(
s
t
r
)
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


 
 
 
 
#
 
R
e
a
d
 
t
h
e
 
l
i
s
t
 
f
i
l
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
l
i
s
t
_
f
i
l
e
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
)


 
 
 
 
 
 
 
 
l
i
s
t
_
l
i
s
t
 
=
 
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
 
f
i
l
e
s
 
i
n
 
f
o
l
d
e
r
A


 
 
 
 
f
i
l
e
s
_
i
n
_
f
o
l
d
e
r
A
 
=
 
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
f
o
l
d
e
r
A
)




 
 
 
 
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
 
f
i
l
e
s
 
t
o
 
e
x
c
l
u
d
e


 
 
 
 
f
i
l
e
s
import os
import shutil
import unittest


class TestExtractFiles(unittest.TestCase):

    def setUp(self):
        """Set up test directories and files before each test case."""
        self.folderA = "test_folderA"
        self.folderB = "test_folderB"
        os.makedirs(self.folderA, exist_ok=True)
        os.makedirs(self.folderB, exist_ok=True)

    def tearDown(self):
        """Clean up the test directories after each test case."""
        shutil.rmtree(self.folderA)
        shutil.rmtree(self.folderB)

    def create_csv(self, filename_list):
        """Helper method to create a CSV file for testing."""
        csv_file = "test_exclude.csv"
        with open(csv_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["filename"])  # Write header
            for name in filename_list:
                writer.writerow([name])
        return csv_file

    def test_basic_functionality(self):
        """Test basic functionality with some files excluded."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")
        with open(os.path.join(self.folderA, "file2.txt"), "w") as f:
            f.write("Content of file 2")
        with open(os.path.join(self.folderA, "file3.txt"), "w") as f:
            f.write("Content of file 3")

        csv_file = self.create_csv(["file2.txt"])  # Exclude file2.txt
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))
        self.assertFalse(os.path.exists(os.path.join(self.folderB, "file2.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file3.txt")))

    def test_empty_folderA(self):
        """Test when folderA is empty."""
        csv_file = self.create_csv(["file1.txt"])  # Exclude file1.txt
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertEqual(len(os.listdir(self.folderB)), 0)

    def test_all_files_excluded(self):
        """Test when all files are excluded."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")
        with open(os.path.join(self.folderA, "file2.txt"), "w") as f:
            f.write("Content of file 2")

        csv_file = self.create_csv(["file1.txt", "file2.txt"])  # Exclude all files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertEqual(len(os.listdir(self.folderB)), 0)

    def test_destination_folder_already_has_files(self):
        """Test when folderB already contains files."""
        with open(os.path.join(self.folderB, "existing_file.txt"), "w") as f:
            f.write("This is an existing file.")

        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")

        csv_file = self.create_csv([])  # Do not exclude any files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        # Check if both existing and new files are present
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "existing_file.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))

    def test_empty_csv_file(self):
        """Test with an empty CSV file."""
        with open(os.path.join(self.folderA, "file1.txt"), "w") as f:
            f.write("Content of file 1")

        csv_file = self.create_csv([])  # Empty CSV, do not exclude any files
        extract_files_excluding_csv(self.folderA, csv_file, self.folderB)

        self.assertTrue(os.path.exists(os.path.join(self.folderB, "file1.txt")))
if __name__ == '__main__':
    unittest.main()