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
 
d
i
f
f
_
f
i
l
e
s
(
f
i
l
e
1
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
2
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
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
a
r
e
 
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
w
o
 
f
i
l
e
s
 
a
n
d
 
p
r
i
n
t
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
s
 
i
n
 
u
n
i
f
i
e
d
 
d
i
f
f
 
f
o
r
m
a
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
1
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
 
f
i
r
s
t
 
f
i
l
e
.


 
 
 
 
f
i
l
e
2
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
 
s
e
c
o
n
d
 
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
s
t
r
]
:
 
A
 
l
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
 
l
i
n
e
s
 
o
f
 
d
i
f
f
e
r
e
n
c
e
s
,
 
i
f
 
a
n
y
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
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
:
 
I
f
 
e
i
t
h
e
r
 
f
i
l
e
 
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


 
 
 
 
I
O
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
r
e
 
i
s
 
a
n
 
e
r
r
o
r
 
r
e
a
d
i
n
g
 
t
h
e
 
f
i
l
e
s
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
1
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
i
l
e
1
,
 
o
p
e
n
(
f
i
l
e
2
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
i
l
e
2
:


 
 
 
 
 
 
 
 
f
i
l
e
1
_
l
i
n
e
s
 
=
 
f
i
l
e
1
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


 
 
 
 
 
 
 
 
f
i
l
e
2
_
l
i
n
e
s
 
=
 
f
i
l
e
2
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




 
 
 
 
r
e
t
u
r
n
 
d
i
f
f
_
l
i
n
e
s
(
f
i
l
e
1
_
l
i
n
e
s
,
 
f
i
l
e
2
_
l
i
n
e
s
)






d
e
f
 
d
i
f
f
_
l
i
n
e
s
(
f
i
l
e
1
_
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
,
 
f
i
l
e
2
_
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


 
 
 
 
C
o
m
p
a
r
e
 
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
w
o
 
l
i
s
t
s
 
o
f
 
l
i
n
e
s
 
a
n
d
 
p
r
i
n
t
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
s
 
i
n
 
u
n
i
f
i
e
d
 
d
i
f
f
 
f
o
r
m
a
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
1
_
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
 
L
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
 
f
r
o
m
 
t
h
e
 
f
i
r
s
t
 
f
i
l
e
.


 
 
 
 
f
i
l
e
2
_
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
 
L
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
 
f
r
o
m
 
t
h
e
 
s
e
c
o
n
d
 
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
s
t
r
]
:
 
A
 
l
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
 
l
i
n
e
s
 
o
f
 
d
i
f
f
e
r
e
n
c
e
s
,
 
i
f
 
a
n
y
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
I
O
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
r
e
 
i
s
 
a
n
 
e
r
r
o
r
 
r
e
a
d
i
n
g
 
t
h
e
 
f
i
l
e
s
.


 
 
 
 
"
"
"


 
 
 
 
d
i
f
f
_
l
i
n
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
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
,
 
(
l
i
n
e
1
,
 
l
i
n
e
2
)
 
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
z
i
p
(
f
i
l
e
1
_
l
i
n
e
s
,
 
f
i
l
e
2
_
l
i
n
e
s
)
)
:


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
1
 
!
=
 
l
i
n
e
2
:


 
 
 
 
 
 
 
 
 
 
 
 
d
i
f
f
_
l
i
n
e
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
"
{
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
>
4
}
 
|
 
{
l
i
n
e
1
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
d
i
f
f
_
l
i
n
e
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
"
{
'
 
'
 
*
 
4
}
 
|
 
{
l
i
n
e
2
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
d
i
f
f
_
l
i
n
e
s
.
a
p
p
e
n
d
(
"
"
)




 
 
 
 
r
e
t
u
r
n
 
d
i
f
f
_
l
i
n
e
s






d
e
f
 
d
i
f
f
_
s
t
r
i
n
g
s
(
s
t
r
i
n
g
1
:
 
s
t
r
,
 
s
t
r
i
n
g
2
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
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
a
r
e
 
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
w
o
 
s
t
r
i
n
g
s
 
a
n
d
 
p
r
i
n
t
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
s
 
i
n
 
u
n
i
f
i
e
d
 
d
i
f
f
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


import os
import unittest
from unittest.mock import mock_open, patch


class TestCompareFiles(unittest.TestCase):

    def setUp(self):
        # 创建文件用于测试
        self.file1_path = 'file1.txt'
        self.file2_path = 'file2.txt'

    def tearDown(self):
        # 删除创建的文件
        if os.path.exists(self.file1_path):
            os.remove(self.file1_path)
        if os.path.exists(self.file2_path):
            os.remove(self.file2_path)

    def test_identical_files(self):
        # Mock question for two identical files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLine2\nLine3\n"

        with open(self.file1_path, 'w') as f1, open(self.file2_path, 'w') as f2:
            f1.write(file1_content)
            f2.write(file2_content)

        result = diff_files(self.file1_path, self.file2_path)
        self.assertEqual(len(result), 0, "There should be no differences detected")

    def test_files_with_differences(self):
        # Mock question for two different files
        file1_content = "Line1\nLine2\nLine3\n"
        file2_content = "Line1\nLineChanged\nLine3\n"

        with open(self.file1_path, 'w') as f1, open(self.file2_path, 'w') as f2:
            f1.write(file1_content)
            f2.write(file2_content)

        result = diff_files(self.file1_path, self.file2_path)
        self.assertNotEqual(len(result), 0, "There should be differences detected")

    def test_nonexistent_file(self):
        # Test when one of the files does not exist
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(FileNotFoundError):
                diff_files('nonexistent.txt', 'file2.txt')

    def test_file_reading_error(self):
        # Test when there's an error reading the file
        with patch('builtins.open', side_effect=IOError("Error reading file")):
            with self.assertRaises(IOError):
                diff_files('file1.txt', 'file2.txt')

if __name__ == '__main__':
    unittest.main()