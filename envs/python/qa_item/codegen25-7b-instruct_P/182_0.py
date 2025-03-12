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
w
i
t
h
_
b
u
f
f
e
r
e
d
_
s
t
r
e
a
m
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


 
 
 
 
C
o
p
i
e
s
 
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
s
 
o
f
 
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
i
l
e
 
u
s
i
n
g
 
a
 
b
u
f
f
e
r
e
d
 
s
t
r
e
a
m


 
 
 
 
a
n
d
 
m
e
a
s
u
r
e
s
 
t
h
e
 
t
i
m
e
 
i
t
 
t
a
k
e
s
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
o
p
e
r
a
t
i
o
n
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
.


 
 
 
 
 
 
 
 
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
 
t
i
m
e
 
t
a
k
e
n
 
t
o
 
c
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
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
=
 
t
i
m
e
.
t
i
m
e
(
)


 
 
 
 
w
i
t
h
 
o
p
e
n
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
_
p
a
t
h
,
 
"
r
b
"
)
 
a
s
 
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


 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
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
,
 
"
w
b
"
)
 
a
s
 
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
_
f
i
l
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
f
i
l
e
o
b
j
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
_
f
i
l
e
,
 
l
e
n
g
t
h
=
B
U
F
F
E
R
_
S
I
Z
E
)


 
 
 
 
r
e
t
u
r
n
 
(
t
i
m
e
.
t
i
m
e
(
)
 
-
 
s
t
a
r
t
_
t
i
m
e
)
 
*
 
1
0
0
0






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
w
i
t
h
_
d
i
r
e
c
t
_
i
o
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


 
 
 
 
C
o
p
i
e
s
 
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
s
 
o
f
 
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
i
l
e
 
u
s
i
n
g
 
d
i
r
e
c
t
 
I
O


 
 
 
 
a
n
d
 
m
e
a
s
u
r
e
s
 
t
h
e
 
t
i
m
e
 
i
t
 
t
a
k
e
s
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
o
p
e
r
a
t
i
o
n
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
.


 
 
 
 
 
 
 
 
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
 
t
i
m
e
 
t
a
k
e
n
 
t
o
 
c
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
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
=
 
t
i
m
e
.
t
i
m
e
(
)


 
 
 
 
w
i
t
h
 
o
p
e
n
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
_
p
a
t
h
,
 
"
r
b
"
)
 
a
s
 
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


 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
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
,
 
"
w
b
"
)
 
a
s
 
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
_
f
i
l
e
:


 
 
 
 
 
 
 
 
 
 
 
 
o
s
.
w
r
i
t
e
(
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
_
f
i
l
e
.
f
i
l
e
n
o
(
)
,
 
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
a
d
(
)
)


 
 
 
 
r
e
t
u
r
n
 
(
t
i
m
e
.
t
i
m
e
(
)
 
-
 
s
t
a
r
t
_
t
i
m
e
)
 
*
 
1
0
0
0






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
w
i
t
h
_
o
s
_
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


 
 
 
 
C
o
p
i
e
s
 
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
s
 
o
f
 
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
i
l
e
 
u
s
i
n
g
 
o
s
.
c
o
p
y
f
i
l
e
(
)


 
 
 
 
a
n
d
 
m
e
a
s
u
r
e
s
 
t
h
e
 
t
i
m
e
 
i
t
 
t
a
k
e
s
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
o
p
e
r
a
t
i
o
n
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
import os
import unittest


class Tester(unittest.TestCase):
    def setUp(self):
        self.source_file = "testSourceFile.txt"
        self.destination_file = "testDestinationFile.txt"
        with open(self.source_file, 'wb') as f:
            f.write(b"This is a test file content.")

    def tearDown(self):
        for file in [self.source_file, self.destination_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_copy_file_with_content(self):
        time_taken = copy_file_with_buffered_stream(self.source_file, self.destination_file)
        self.assertTrue(os.path.exists(self.destination_file), "Destination file should exist after copying.")
        self.assertEqual(os.path.getsize(self.source_file), os.path.getsize(self.destination_file), "File sizes should match.")
        self.assertGreaterEqual(time_taken, 0, "Time taken should be non-negative.")

    def test_copy_empty_file(self):
        empty_file = "emptyFile.txt"
        with open(empty_file, 'wb') as f:
            pass  # Create an empty file
        destination_empty_file = "destinationEmptyFile.txt"
        time_taken = copy_file_with_buffered_stream(empty_file, destination_empty_file)
        self.assertTrue(os.path.exists(destination_empty_file), "Destination file should exist after copying.")
        self.assertEqual(os.path.getsize(destination_empty_file), 0, "Empty file should have length 0.")
        self.assertGreaterEqual(time_taken, 0, "Time taken should be non-negative.")
        os.remove(empty_file)
        os.remove(destination_empty_file)

    def test_copy_non_existent_file(self):
        non_existent_file_path = "nonExistentFile.txt"
        with self.assertRaises(Exception):
            copy_file_with_buffered_stream(non_existent_file_path, self.destination_file)

    def test_copy_file_overwrite(self):
        with open(self.destination_file, 'wb') as f:
            f.write(b"Old content")
        time_taken = copy_file_with_buffered_stream(self.source_file, self.destination_file)
        self.assertTrue(os.path.exists(self.destination_file), "Destination file should exist after copying.")
        self.assertEqual(os.path.getsize(self.source_file), os.path.getsize(self.destination_file), "File sizes should match after overwriting.")
        self.assertGreater(time_taken, 0, "Time taken should be greater than 0.")

    def test_copy_large_file(self):
        large_content = bytearray(10 * 1024 * 1024)  # 10 MB
        for i in range(len(large_content)):
            large_content[i] = i % 256
        with open(self.source_file, 'wb') as f:
            f.write(large_content)
        time_taken = copy_file_with_buffered_stream(self.source_file, self.destination_file)
        self.assertTrue(os.path.exists(self.destination_file), "Destination file should exist after copying.")
        self.assertEqual(os.path.getsize(self.source_file), os.path.getsize(self.destination_file), "File sizes should match.")
        self.assertGreater(time_taken, 0, "Time taken should be greater than 0.")
if __name__ == '__main__':
    unittest.main()