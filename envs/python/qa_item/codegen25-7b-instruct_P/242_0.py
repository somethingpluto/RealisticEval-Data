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
,
 
D
i
c
t






d
e
f
 
c
l
a
s
s
i
f
y
_
f
i
l
e
s
_
b
y
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
n
a
m
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
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
C
l
a
s
s
i
f
y
 
a
n
 
a
r
r
a
y
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
i
r
 
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
n
a
m
e
s
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
 
n
a
m
e
s
 
(
s
t
r
i
n
g
s
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


 
 
 
 
 
 
 
 
D
i
c
t
:
 
D
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
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
s
 
a
s
 
k
e
y
s
 
a
n
d
 
l
i
s
t
s
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
s
 
v
a
l
u
e
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
e
x
t
e
n
s
i
o
n
s
 
=
 
{
}


 
 
 
 
f
o
r
 
f
i
l
e
_
n
a
m
e
 
i
n
 
f
i
l
e
_
n
a
m
e
s
:


 
 
 
 
 
 
 
 
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
 
=
 
f
i
l
e
_
n
a
m
e
.
s
p
l
i
t
(
"
.
"
)
[
-
1
]


 
 
 
 
 
 
 
 
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
 
n
o
t
 
i
n
 
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
s
:


 
 
 
 
 
 
 
 
 
 
 
 
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
s
[
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
]
 
=
 
[
]


 
 
 
 
 
 
 
 
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
s
[
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
]
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
n
a
m
e
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
e
x
t
e
n
s
i
o
n
s






d
e
f
 
c
l
a
s
s
i
f
y
_
f
i
l
e
s
_
b
y
_
m
i
m
e
_
t
y
p
e
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
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
C
l
a
s
s
i
f
y
 
a
n
 
a
r
r
a
y
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
i
r
 
M
I
M
E
 
t
y
p
e
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
n
a
m
e
s
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
 
n
a
m
e
s
 
(
s
t
r
i
n
g
s
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


 
 
 
 
 
 
 
 
D
i
c
t
:
 
D
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
M
I
M
E
 
t
y
p
e
s
 
a
s
 
k
e
y
s
 
a
n
d
 
l
i
s
t
s
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
s
 
v
a
l
u
e
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
m
i
m
e
_
t
y
p
e
s
 
=
 
{
}


 
 
 
 
f
o
r
 
f
i
l
e
_
n
a
m
e
 
i
n
 
f
i
l
e
_
n
a
m
e
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
m
i
m
e
_
t
y
p
e
 
=
 
g
e
t
_
m
i
m
e
_
t
y
p
e
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


 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
_
m
i
m
e
_
t
y
p
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
_
m
i
m
e
_
t
y
p
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
_
m
i
m
e
_
t
y
p
e
s
[
f
i
l
e
_
m
i
m
e
_
t
y
p
e
]
 
=
 
[
]


 
 
 
 
 
 
 
 
f
i
l
e
_
m
i
m
e
_
t
y
p
e
s
[
f
i
l
e
_
m
i
m
e
_
t
y
p
e
]
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
n
a
m
e
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
m
i
m
e
_
t
y
p
e
s






d
e
f
 
c
l
a
s
s
i
f
y
_
f
i
l
e
s
_
b
y
_
s
i
z
e
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
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
C
l
a
s
s
i
f
y
 
a
n
 
a
r
r
a
y
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
i
r
 
s
i
z
e
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
n
a
m
e
s
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
 
n
a
m
e
s
 
(
s
t
r
i
n
g
s
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


 
 
 
 
 
 
 
 
D
i
c
t
:
 
D
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
f
i
l
e
 
s
i
z
e
s
 
a
s
 
k
e
y
s
 
a
n
d
 
l
i
s
t
s
 
o
f
 
f
i
l
e
 
n
a
m
e
s
 
a
s
 
v
a
l
u
e
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
s
i
z
e
s
 
=
 
{
}


 
 
 
 
f
o
r
 
f
i
l
e
_
n
a
m
e
 
i
n
 
f
i
l
e
_
n
a
m
e
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
s
i
z
e
 
=
 
g
e
t
_
f
i
l
e
_
s
i
z
e
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


 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
_
s
i
z
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
_
s
i
z
e
s
import unittest


class TestClassifyFilesByExtension(unittest.TestCase):

    def test_multiple_file_types(self):
        """Test with multiple file types."""
        files = [
            "document.docx",
            "photo.jpeg",
            "report.pdf",
            "image.png",
            "archive.zip"
        ]
        expected_result = {
            'docx': ['document.docx'],
            'jpeg': ['photo.jpeg'],
            'pdf': ['report.pdf'],
            'png': ['image.png'],
            'zip': ['archive.zip']
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_empty_list(self):
        """Test with an empty list of file names."""
        files = []
        expected_result = {}
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_files_with_same_extension(self):
        """Test with multiple files having the same extension."""
        files = [
            "file1.txt",
            "file2.txt",
            "file3.txt",
        ]
        expected_result = {
            'txt': [
                "file1.txt",
                "file2.txt",
                "file3.txt",
            ]
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_files_with_multiple_dots(self):
        """Test files that have multiple dots in their names."""
        files = [
            "my.document.docx",
            "report.final.pdf",
            "photo.album.jpeg",
            "archive.backup.zip"
        ]
        expected_result = {
            'docx': ['my.document.docx'],
            'pdf': ['report.final.pdf'],
            'jpeg': ['photo.album.jpeg'],
            'zip': ['archive.backup.zip']
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)
if __name__ == '__main__':
    unittest.main()