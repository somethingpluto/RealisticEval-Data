d
e
f
 
s
a
n
i
t
i
z
e
_
f
i
l
e
n
a
m
e
(
f
i
l
e
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


 
 
 
 
r
e
m
o
v
e
 
i
l
l
e
g
a
l
 
c
h
a
r
a
c
t
e
r
s
 
f
r
o
m
 
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
i
n
g




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
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
 
t
o
 
b
e
 
s
a
n
i
t
i
z
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
s
a
n
i
t
i
z
e
d
 
s
t
r
i
n
g
 
t
h
a
t
 
i
s
 
s
a
f
e
 
t
o
 
u
s
e
 
a
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
n
a
m
e
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
 
"
"
.
j
o
i
n
(
c
 
f
o
r
 
c
 
i
n
 
f
i
l
e
n
a
m
e
 
i
f
 
c
.
i
s
a
l
p
h
a
(
)
 
o
r
 
c
.
i
s
d
i
g
i
t
(
)
 
o
r
 
c
 
i
n
 
[
"
 
"
,
 
"
-
"
,
 
"
.
"
]
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
(
f
i
l
e
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


 
 
 
 
G
e
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
 
a
 
f
i
l
e
n
a
m
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
i
l
e
n
a
m
e
 
t
o
 
g
e
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
f
i
l
e
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
(
f
i
l
e
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


 
 
 
 
G
e
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
 
f
r
o
m
 
a
 
f
i
l
e
n
a
m
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
i
l
e
n
a
m
e
 
t
o
 
g
e
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
 
n
a
m
e
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
f
i
l
e
n
a
m
e
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
p
a
t
h
(
f
i
l
e
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


 
 
 
 
G
e
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
 
a
 
f
i
l
e
n
a
m
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
i
l
e
n
a
m
e
 
t
o
 
g
e
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
f
i
l
e
n
a
m
e
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
s
i
z
e
(
f
i
l
e
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
f
r
o
m
 
a
 
f
i
l
e
n
a
m
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
i
l
e
n
a
m
e
 
t
o
 
g
e
t
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
b
y
t
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
 
o
s
.
p
a
t
h
.
g
e
t
s
i
z
e
(
f
i
l
e
n
a
m
e
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
c
r
e
a
t
i
o
n
_
t
i
m
e
(
f
i
l
e
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
 
d
a
t
e
t
i
m
e
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
t
h
e
 
f
i
l
e
 
c
r
e
a
t
i
o
n
 
t
i
m
e
 
f
r
o
m
 
a
 
f
i
l
e
n
a
m
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
i
l
e
n
a
m
e
 
t
o
 
g
e
t
 
t
h
e
 
f
i
l
e
 
c
r
e
a
t
i
o
n
 
t
i
m
e
 
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


 
 
 
 
 
 
 
 
d
a
t
e
t
i
m
e
:
 
T
h
e
 
f
i
l
e
 
c
r
e
a
t
i
o
n
 
t
i
m
e
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
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
o
s
.
p
a
t
h
.
g
e
t
c
t
i
m
e
(
f
i
l
e
n
a
m
e
)
)
import unittest


class TestSanitizeFilename(unittest.TestCase):

    def test_valid_filename(self):
        self.assertEqual(sanitize_filename("valid_filename.txt"), "valid_filename.txt")

    def test_illegal_characters(self):
        self.assertEqual(sanitize_filename("invalid<filename>.txt"), "invalid_filename_.txt")
        self.assertEqual(sanitize_filename("file/name:with*illegal|chars?.txt"), "file_name_with_illegal_chars_.txt")


    def test_long_filename(self):
        long_filename = "a" * 300 + ".txt"
        sanitized_filename = sanitize_filename(long_filename)
        self.assertEqual(len(sanitized_filename), 255)
        self.assertEqual(sanitized_filename, "a" * 255)

    def test_empty_filename(self):
        self.assertEqual(sanitize_filename(""), "")
if __name__ == '__main__':
    unittest.main()