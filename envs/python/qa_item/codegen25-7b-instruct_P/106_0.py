d
e
f
 
i
s
_
b
a
s
e
6
4
_
i
m
a
g
e
(
i
m
a
g
e
_
d
a
t
a
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
p
r
o
v
i
d
e
d
 
i
m
a
g
e
 
d
a
t
a
 
i
s
 
a
 
v
a
l
i
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
i
m
a
g
e
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
m
a
g
e
_
d
a
t
a
 
(
s
t
r
)
:
 
T
h
e
 
i
m
a
g
e
 
d
a
t
a
 
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
 
v
a
l
i
d
a
t
e
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
d
e
c
o
d
e
d
_
i
m
a
g
e
 
=
 
b
a
s
e
6
4
.
b
6
4
d
e
c
o
d
e
(
i
m
a
g
e
_
d
a
t
a
)


 
 
 
 
 
 
 
 
I
m
a
g
e
.
o
p
e
n
(
i
o
.
B
y
t
e
s
I
O
(
d
e
c
o
d
e
d
_
i
m
a
g
e
)
)


 
 
 
 
e
x
c
e
p
t
 
(
b
i
n
a
s
c
i
i
.
E
r
r
o
r
,
 
U
n
i
c
o
d
e
D
e
c
o
d
e
E
r
r
o
r
,
 
V
a
l
u
e
E
r
r
o
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
i
d
a
t
i
o
n
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
_
(
"
T
h
e
 
p
r
o
v
i
d
e
d
 
i
m
a
g
e
 
d
a
t
a
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
i
m
a
g
e
 
s
t
r
i
n
g
.
"
)


 
 
 
 
 
 
 
 
)






d
e
f
 
i
s
_
b
a
s
e
6
4
_
f
i
l
e
(
f
i
l
e
_
d
a
t
a
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
p
r
o
v
i
d
e
d
 
f
i
l
e
 
d
a
t
a
 
i
s
 
a
 
v
a
l
i
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
f
i
l
e
 
s
t
r
i
n
g
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
d
a
t
a
 
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
 
d
a
t
a
 
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
 
v
a
l
i
d
a
t
e
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
d
e
c
o
d
e
d
_
f
i
l
e
 
=
 
b
a
s
e
6
4
.
b
6
4
d
e
c
o
d
e
(
f
i
l
e
_
d
a
t
a
)


 
 
 
 
 
 
 
 
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
 
m
a
g
i
c
.
f
r
o
m
_
b
u
f
f
e
r
(
d
e
c
o
d
e
d
_
f
i
l
e
,
 
m
i
m
e
=
T
r
u
e
)


 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
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
i
m
a
g
e
/
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
i
d
a
t
i
o
n
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
_
(
"
T
h
e
 
p
r
o
v
i
d
e
d
 
f
i
l
e
 
d
a
t
a
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
i
m
a
g
e
 
s
t
r
i
n
g
.
"
)


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
e
x
c
e
p
t
 
(
b
i
n
a
s
c
i
i
.
E
r
r
o
r
,
 
U
n
i
c
o
d
e
D
e
c
o
d
e
E
r
r
o
r
,
 
V
a
l
u
e
E
r
r
o
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
i
d
a
t
i
o
n
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
_
(
"
T
h
e
 
p
r
o
v
i
d
e
d
 
f
i
l
e
 
d
a
t
a
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
i
m
a
g
e
 
s
t
r
i
n
g
.
"
)


 
 
 
 
 
 
 
 
)






d
e
f
 
i
s
_
v
a
l
i
d
_
i
m
a
g
e
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
e
x
t
e
n
s
i
o
n
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
p
r
o
v
i
d
e
d
 
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
 
i
s
 
a
 
v
a
l
i
d
 
i
m
a
g
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
 
e
x
t
e
n
s
i
o
n
 
t
o
 
b
e
 
v
a
l
i
d
a
t
e
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
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
i
m
a
g
e
/
"
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
i
d
a
t
i
o
n
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
_
(
"
T
h
e
 
p
r
o
v
i
d
e
d
 
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
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d
 
i
m
a
g
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
)


 
 
 
 
 
 
 
 
)






d
e
f
 
i
s
_
v
a
l
i
d
_
i
m
a
g
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
(
m
i
m
e
_
t
y
p
e
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
p
r
o
v
i
d
e
d
 
M
I
M
E
 
t
y
p
e
 
i
s
 
a
 
v
a
l
i
d
 
i
m
a
g
e
 
M
I
M
E
 
t
y
p
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
s
t
r
import unittest


class TestIsBase64Image(unittest.TestCase):

    def test_valid_png(self):
        valid_png = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA'
        self.assertTrue(is_base64_image(valid_png))

    def test_valid_jpeg(self):
        valid_jpeg = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA'
        self.assertTrue(is_base64_image(valid_jpeg))

    def test_invalid_format(self):
        invalid_format = 'data:text/plain;base64,SGVsbG8gd29ybGQ='
        self.assertFalse(is_base64_image(invalid_format))

    def test_invalid_base64_characters(self):
        invalid_base64 = 'data:image/png;base64,invalidBase64String@#%'
        self.assertFalse(is_base64_image(invalid_base64))

    def test_empty_string(self):
        self.assertFalse(is_base64_image(''))

if __name__ == '__main__':
    unittest.main()