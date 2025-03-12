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
n
a
m
e
s
 
a
 
W
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
 
b
y
 
r
e
p
l
a
c
i
n
g
 
c
o
l
o
n
s
 
i
n
 
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
 
w
i
t
h
 
u
n
d
e
r
s
c
o
r
e
s
.




 
 
 
 
P
a
r
a
m
e
t
e
r
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
 
T
h
e
 
o
r
i
g
i
n
a
l
 
f
i
l
e
 
p
a
t
h
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
 
m
o
d
i
f
i
e
d
 
f
i
l
e
 
p
a
t
h
 
w
i
t
h
 
c
o
l
o
n
s
 
i
n
 
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
 
r
e
p
l
a
c
e
d
 
b
y
 
u
n
d
e
r
s
c
o
r
e
s
.


 
 
 
 
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
"
:
"
,
 
"
_
"
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
_
f
r
o
m
_
u
r
l
(
u
r
l
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
 
f
i
l
e
 
p
a
t
h
 
f
r
o
m
 
a
 
U
R
L
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
t
o
 
e
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
p
a
t
h
 
f
r
o
m
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
 
f
i
l
e
 
p
a
t
h
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
U
R
L
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
u
r
l
.
s
p
l
i
t
(
"
/
"
)
[
-
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
p
a
t
h
_
f
r
o
m
_
u
r
l
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
u
r
l
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
 
f
i
l
e
 
p
a
t
h
 
f
r
o
m
 
a
 
U
R
L
 
w
i
t
h
 
a
n
 
e
x
t
e
n
s
i
o
n
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
t
o
 
e
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
p
a
t
h
 
f
r
o
m
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
 
f
i
l
e
 
p
a
t
h
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
U
R
L
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
u
r
l
.
s
p
l
i
t
(
"
/
"
)
[
-
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
?
"
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
u
r
l
(
u
r
l
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
 
a
 
U
R
L
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
t
o
 
e
x
t
r
a
c
t
 
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
 
f
r
o
m
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
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
U
R
L
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
u
r
l
.
s
p
l
i
t
(
"
?
"
)
[
0
]
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
u
r
l
_
w
i
t
h
_
d
o
t
(
u
r
l
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
 
a
 
U
R
L
 
w
i
t
h
 
a
 
d
o
t
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
t
o
 
e
x
t
r
a
c
t
 
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
 
f
r
o
m
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
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
U
R
L
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
u
r
l
.
s
p
l
i
t
(
"
?
"
)
[
0
]
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
u
r
l
_
w
i
t
h
o
u
t
_
d
o
t
(
u
r
l
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
 
a
 
U
R
L
 
w
i
t
h
o
u
t
 
a
 
d
o
t
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
import unittest


class TestRenameFilePath(unittest.TestCase):
    def test_rename_with_colon_in_filename(self):
        # Test path with colon in the filename
        path = 'C:\\Users\\example\\Documents\\report:2023.txt'
        expected = 'C:\\Users\\example\\Documents\\report_2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_without_colon_in_filename(self):
        # Test path without colon in the filename
        path = 'C:\\Users\\example\\Documents\\report2023.txt'
        expected = 'C:\\Users\\example\\Documents\\report2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_multiple_colons_in_filename(self):
        # Test path with multiple colons in the filename
        path = 'C:\\Users\\example\\Documents\\project:report:2023.txt'
        expected = 'C:\\Users\\example\\Documents\\project_report_2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_colon_at_end_of_filename(self):
        # Test path with a colon at the end of the filename
        path = 'C:\\Users\\example\\Documents\\backup:'
        expected = 'C:\\Users\\example\\Documents\\backup_'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_colon_at_start_of_filename(self):
        # Test path with a colon at the start of the filename
        path = 'C:\\Users\\example\\Documents\\:initial_setup.txt'
        expected = 'C:\\Users\\example\\Documents\\_initial_setup.txt'
        self.assertEqual(rename_file_path(path), expected)

if __name__ == '__main__':
    unittest.main()