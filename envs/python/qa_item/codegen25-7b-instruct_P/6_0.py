d
e
f
 
s
i
m
p
l
i
f
y
_
w
i
n
d
o
w
s
_
p
a
t
h
(
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


 
 
 
 
s
i
m
p
l
i
f
y
 
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
 
w
i
n
d
o
w
s
 
s
y
s
t
e
m
s
 
i
n
t
o
 
n
a
m
e
 
s
t
r
i
n
g
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
C
:
\
\
U
s
e
r
s
\
\
U
s
e
r
\
\
f
i
l
e
.
t
x
t


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
C
_
U
s
e
r
s
_
U
s
e
r
_
f
i
l
e
.
t
x
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
w
i
n
d
o
w
s
 
f
i
l
e
 
p
a
t
h
 
s
t
r




 
 
 
 
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
 
s
i
m
p
l
i
f
y
 
p
a
t
h
 
s
t
r


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
p
a
t
h
.
r
e
p
l
a
c
e
(
'
\
\
'
,
 
'
_
'
)
.
r
e
p
l
a
c
e
(
'
:
'
,
 
'
_
'
)
.
r
e
p
l
a
c
e
(
'
/
'
,
 
'
_
'
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
n
a
m
e
_
f
r
o
m
_
p
a
t
h
(
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


 
 
 
 
g
e
t
 
f
i
l
e
 
n
a
m
e
 
f
r
o
m
 
f
i
l
e
 
p
a
t
h


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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
 
f
i
l
e
 
n
a
m
e


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
n
a
m
e
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
_
f
r
o
m
_
p
a
t
h
(
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


 
 
 
 
g
e
t
 
f
i
l
e
 
n
a
m
e
 
w
i
t
h
 
e
x
t
e
n
s
i
o
n
 
f
r
o
m
 
f
i
l
e
 
p
a
t
h


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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
 
f
i
l
e
 
n
a
m
e
 
w
i
t
h
 
e
x
t
e
n
s
i
o
n


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
e
x
t
e
n
s
i
o
n
_
f
r
o
m
_
p
a
t
h
(
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


 
 
 
 
g
e
t
 
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
 
f
r
o
m
 
f
i
l
e
 
p
a
t
h


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
p
a
t
h
)
[
1
]






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
e
x
t
e
n
s
i
o
n
_
f
r
o
m
_
n
a
m
e
(
n
a
m
e
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


 
 
 
 
g
e
t
 
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
 
f
r
o
m
 
f
i
l
e
 
n
a
m
e


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
a
m
e
 
(
s
t
r
)
:
 
f
i
l
e
 
n
a
m
e




 
 
 
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
n
a
m
e
)
[
1
]






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
_
f
r
o
m
_
p
a
t
h
(
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


 
 
 
 
g
e
t
 
f
i
l
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
 
e
x
t
e
n
s
i
o
n
 
f
r
o
m
 
f
i
l
e
 
p
a
t
h


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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
 
f
i
l
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
 
e
x
t
e
n
s
i
o
n


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
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
p
a
t
h
)
)
[
0
]






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
_
import unittest


class TestSimplifyWindowsPath(unittest.TestCase):
    def test_simple_path(self):
        self.assertEqual(simplify_windows_path(r"C:\Users\User\file.txt"), "C_Users_User_file.txt")

    def test_simple_path2(self):
        self.assertEqual(simplify_windows_path(r"D:\User\file.txt"), "D_User_file.txt")

    def test_path_with_spaces(self):
        self.assertEqual(simplify_windows_path(r"E:\New Folder\my file.docx"), "E_New Folder_my file.docx")

    def test_nested_directories(self):
        self.assertEqual(simplify_windows_path(r"G:\folder1\folder2\folder3\file.jpeg"),
                         "G_folder1_folder2_folder3_file.jpeg")

if __name__ == '__main__':
    unittest.main()