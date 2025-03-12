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
 
a
n
d
 
r
e
t
u
r
n
 
i
t
 
i
f
 
i
t
 
e
x
i
s
t
s
.
 
I
f
 
n
o
t
,
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
s
 
r
e
t
u
r
n
e
d
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
 
(
s
t
r
)
:
 
T
h
e
 
f
u
l
l
 
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
 
d
o
t
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
e
x
t
e
n
s
i
o
n
 
i
s
 
f
o
u
n
d
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
 
P
a
t
h
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
.
s
u
f
f
i
x
.
l
s
t
r
i
p
(
"
.
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
n
a
m
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
 
a
n
d
 
r
e
t
u
r
n
 
i
t
 
i
f
 
i
t
 
e
x
i
s
t
s
.
 
I
f
 
n
o
t
,
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
s
 
r
e
t
u
r
n
e
d
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
 
(
s
t
r
)
:
 
T
h
e
 
f
u
l
l
 
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
 
n
a
m
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
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
f
i
l
e
 
n
a
m
e
 
i
s
 
f
o
u
n
d
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
 
P
a
t
h
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
.
s
t
e
m






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
a
n
d
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
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
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
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m
 
i
f
 
t
h
e
y
 
e
x
i
s
t
.
 
I
f
 
n
o
t
,
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
s
 
r
e
t
u
r
n
e
d
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
 
(
s
t
r
)
:
 
T
h
e
 
f
u
l
l
 
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
 
n
a
m
e
 
a
n
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:
 
T
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
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
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
 
d
o
t
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
f
i
l
e
 
n
a
m
e
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
i
s
 
f
o
u
n
d
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
 
P
a
t
h
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
.
s
t
e
m
,
 
P
a
t
h
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
.
s
u
f
f
i
x
.
l
s
t
r
i
p
(
"
.
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
n
a
m
e
_
a
n
d
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
w
i
t
h
o
u
t
_
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
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
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
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m
 
i
f
 
t
h
e
y
 
e
x
i
s
t
.
 
I
f
 
n
o
t
,
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
s
 
r
e
t
u
r
n
e
d
.


 
 
 
 
T
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
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
a
r
e
 
r
e
t
u
r
n
e
d
 
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
 
(
s
t
r
)
:
 
T
h
e
 
f
u
l
l
 
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
 
n
a
m
e
 
a
n
d
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:
 
T
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
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
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
 
d
o
t
 
a
n
d
 
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
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
f
i
l
e
 
n
a
m
e
 
a
n
d
 
e
x
t
e
n
s
i
o
n
 
i
s
 
f
o
u
n
d
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
import unittest


class TestGetFileExtension(unittest.TestCase):

    def test_standard_file_extension(self):
        """should return the file extension for a standard file"""
        self.assertEqual(get_file_extension('example.txt'), 'txt')

    def test_no_extension(self):
        """should return an empty string for files without an extension"""
        self.assertEqual(get_file_extension('example'), '')

    def test_multiple_dots(self):
        """should handle files with multiple dots"""
        self.assertEqual(get_file_extension('example.with.many.dots.jpg'), 'jpg')

    def test_filenames_ending_with_dot(self):
        """should return an empty string for filenames that end with a dot"""
        self.assertEqual(get_file_extension('example.'), '')

    def test_case_sensitivity(self):
        """should correctly handle case sensitivity"""
        self.assertEqual(get_file_extension('example.JPG'), 'JPG')

if __name__ == '__main__':
    unittest.main()