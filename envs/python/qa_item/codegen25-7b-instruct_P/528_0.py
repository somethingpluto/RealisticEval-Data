d
e
f
 
f
i
n
d
_
m
a
r
k
d
o
w
n
_
f
i
l
e
s
(
d
i
r
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
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
S
e
a
r
c
h
e
s
 
f
o
r
 
M
a
r
k
d
o
w
n
 
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
 
r
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
s
 
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
 
a
s
 
a
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
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
a
t
h
 
t
o
 
s
e
a
r
c
h
 
i
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
p
a
t
h
s
 
t
o
 
M
a
r
k
d
o
w
n
 
f
i
l
e
s
.


 
 
 
 
"
"
"


 
 
 
 
m
a
r
k
d
o
w
n
_
f
i
l
e
s
 
=
 
[
]


 
 
 
 
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
"
.
m
d
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
n
_
f
i
l
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


 
 
 
 
r
e
t
u
r
n
 
m
a
r
k
d
o
w
n
_
f
i
l
e
s






d
e
f
 
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
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
 
o
f
 
a
 
M
a
r
k
d
o
w
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
 
t
o
 
t
h
e
 
M
a
r
k
d
o
w
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


 
 
 
 
 
 
 
 
s
t
r
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
 
M
a
r
k
d
o
w
n
 
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
.
r
e
a
d
(
)






d
e
f
 
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
e
_
t
i
t
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
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
t
i
t
l
e
 
o
f
 
a
 
M
a
r
k
d
o
w
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
 
t
o
 
t
h
e
 
M
a
r
k
d
o
w
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
t
i
t
l
e
 
o
f
 
t
h
e
 
M
a
r
k
d
o
w
n
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
c
o
n
t
e
n
t
 
=
 
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
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
 
c
o
n
t
e
n
t
.
s
p
l
i
t
(
"
\
n
"
)
[
0
]
.
r
e
p
l
a
c
e
(
"
#
"
,
 
"
"
)






d
e
f
 
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
e
_
t
i
t
l
e
s
(
d
i
r
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
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
t
i
t
l
e
s
 
o
f
 
a
l
l
 
M
a
r
k
d
o
w
n
 
f
i
l
e
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
a
t
h
 
t
o
 
s
e
a
r
c
h
 
i
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
t
i
t
l
e
s
 
o
f
 
a
l
l
 
M
a
r
k
d
o
w
n
 
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
.


 
 
 
 
"
"
"


 
 
 
 
m
a
r
k
d
o
w
n
_
f
i
l
e
s
 
=
 
f
i
n
d
_
m
a
r
k
d
o
w
n
_
f
i
l
e
s
(
d
i
r
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
 
[
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
e
_
t
i
t
l
e
(
f
i
l
e
)
 
f
o
r
 
f
i
l
e
 
i
n
 
m
a
r
k
d
o
w
n
_
f
i
l
e
s
]






d
e
f
 
g
e
t
_
m
a
r
k
d
o
w
n
_
f
i
l
e
_
t
i
t
l
e
s
_
w
i
t
h
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
_
p
a
t
h
:
import unittest
from unittest.mock import patch


class TestFindMarkdownFiles(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_empty_directory(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = []
        mock_isdir.return_value = False

        result = find_markdown_files('emptyDir')
        self.assertEqual(result, [])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_one_markdown_file(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.md']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file1.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_multiple_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.md', 'file2.md']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file1.md', 'dir/file2.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_ignore_non_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.md', 'file3.doc']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, ['dir/file2.md'])

    @patch('os.listdir')
    @patch('os.path.isdir')
    def test_only_non_markdown_files(self, mock_isdir, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.doc']
        mock_isdir.return_value = False

        result = find_markdown_files('dir')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()