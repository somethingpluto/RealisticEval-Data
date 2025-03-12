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
 
p
a
r
s
e
_
g
i
t
_
d
i
f
f
(
d
i
f
f
_
t
e
x
t
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
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
s
t
r
i
n
g
 
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
 
a
 
G
i
t
 
d
i
f
f
 
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
 
a
 
l
i
s
t
 
o
f
 
o
b
j
e
c
t
s


 
 
 
 
d
e
t
a
i
l
i
n
g
 
t
h
e
 
c
h
a
n
g
e
s
 
f
o
r
 
e
a
c
h
 
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


 
 
 
 
 
 
 
 
d
i
f
f
_
t
e
x
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
 
G
i
t
 
d
i
f
f
 
t
e
x
t
 
t
o
 
p
a
r
s
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
 
o
b
j
e
c
t
s
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
d
i
f
f
 
f
o
r
 
e
a
c
h
 
f
i
l
e
,
 
w
h
e
r
e
 
e
a
c
h
 
o
b
j
e
c
t
 
c
o
n
t
a
i
n
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
t
h
e
 
c
h
a
n
g
e
s
,
 
s
u
c
h
 
a
s
 
f
i
l
e
 
n
a
m
e
,
 
a
d
d
e
d
 
l
i
n
e
s
,
 
a
n
d
 
r
e
m
o
v
e
d
 
l
i
n
e
s
.


 
 
 
 
"
"
"


 
 
 
 
l
i
n
e
s
 
=
 
d
i
f
f
_
t
e
x
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
i
l
e
_
n
a
m
e
 
=
 
"
"


 
 
 
 
a
d
d
e
d
_
l
i
n
e
s
 
=
 
[
]


 
 
 
 
r
e
m
o
v
e
d
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
"
d
i
f
f
 
-
-
g
i
t
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
f
i
l
e
_
n
a
m
e
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
f
i
l
e
_
n
a
m
e
"
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
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
a
d
d
e
d
_
l
i
n
e
s
"
:
 
a
d
d
e
d
_
l
i
n
e
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
r
e
m
o
v
e
d
_
l
i
n
e
s
"
:
 
r
e
m
o
v
e
d
_
l
i
n
e
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
_
n
a
m
e
 
=
 
l
i
n
e
.
s
p
l
i
t
(
"
a
/
"
)
[
1
]
.
s
p
l
i
t
(
"
 
b
/
"
)
[
0
]


 
 
 
 
 
 
 
 
 
 
 
 
a
d
d
e
d
_
l
i
n
e
s
 
=
 
[
]


 
 
 
 
 
 
 
 
 
 
 
 
r
e
m
o
v
e
d
_
l
i
n
e
s
 
=
 
[
]


 
 
 
 
 
 
 
 
e
l
i
f
 
l
i
n
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
"
@
@
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 
 
 
 
 
e
l
i
f
 
l
i
n
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
"
-
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
m
o
v
e
d
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
l
i
n
e
[
1
:
]
)


 
 
 
 
 
 
 
 
e
l
i
f
 
l
i
n
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
"
+
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
a
d
d
e
d
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
l
i
n
e
[
1
:
]
)


 
 
 
 
i
f
 
f
i
l
e
_
n
a
m
e
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


 
 
 
 
 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
f
i
l
e
_
n
a
m
e
"
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
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
a
d
d
e
d
_
l
i
n
e
s
"
:
 
a
d
d
e
d
_
l
i
n
e
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
r
e
m
o
v
e
d
_
l
i
n
e
s
"
:
 
r
e
m
o
v
e
d
_
l
i
n
e
s
,


 
 
 
 
 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 
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
 
p
a
r
s
e
_
d
i
f
f
_
l
i
n
e
(
l
i
n
e
:
 
s
t
r
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
s
i
n
g
l
e
 
l
i
n
e
 
o
f
 
a
 
d
i
f
f
 
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
 
a
 
d
i
c
t
i
o
n
a
r
y
 
d
e
t
a
i
l
i
n
g
 
t
h
e
 
c
h
a
n
g
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
n
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
 
l
i
n
e
 
o
f
 
t
h
e
 
d
i
f
f
 
t
o
 
p
a
r
s
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


 
 
 
 
 
 
 
 
d
i
c
t
:
 
A
 
d
i
c
t
i
o
n
a
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
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
t
h
e
 
c
h
a
n
g
e
s
,
 
s
u
c
h
 
a
s
 
t
h
e
 
f
i
l
e
 
n
a
m
e
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
d
d
e
d
 
l
i
n
e
s
,
 
a
n
d
 
r
e
m
o
v
e
d
 
l
i
n
e
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
i
n
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
"
d
i
f
f
 
-
-
g
i
t
"
)
:


import unittest

class TestParseGitDiff(unittest.TestCase):

    def test_parse_simple_file_addition(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "new file mode 100644\n"
            "index 0000000..e69de29\n"
            "--- /dev/null\n"
            "+++ b/file.txt"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].newFileMode, '100644')

    def test_parse_simple_file_deletion(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "deleted file mode 100644\n"
            "index e69de29..0000000\n"
            "--- a/file.txt\n"
            "+++ /dev/null"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].deletedFileMode, '100644')

    def test_parse_file_modification_with_changes(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "index e69de29..d95f3ad 100644\n"
            "--- a/file.txt\n"
            "+++ b/file.txt\n"
            "@@ -0,0 +1 @@\n"
            "+Hello World"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].index, 'e69de29..d95f3ad')
        self.assertEqual(result[0].changes, [
            {"code": "--- a/file.txt"},
            {"code": "+++ b/file.txt"},
            {"diff": '@@ -0,0 +1 @@'},
            {"code": '+Hello World'}
        ])

    def test_handle_multiple_file_diffs(self):
        diff_text = (
            "diff --git a/file1.txt b/file1.txt\n"
            "index e69de29..d95f3ad 100644\n"
            "--- a/file1.txt\n"
            "+++ b/file1.txt\n"
            "@@ -0,0 +1 @@\n"
            "+Hello World\n"
            "diff --git a/file2.txt b/file2.txt\n"
            "index 0a1b2c3..d4e5f6a 100644\n"
            "--- a/file2.txt\n"
            "+++ b/file2.txt\n"
            "@@ -1 +1 @@\n"
            "-Hello\n"
            "+Hi"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].oldPath, 'file1.txt')
        self.assertEqual(result[1].oldPath, 'file2.txt')

    def test_return_empty_array_for_empty_diff_text(self):
        result = parse_git_diff('')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()