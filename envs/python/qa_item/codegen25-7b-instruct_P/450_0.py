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
p
a
s
s
w
o
r
d
(
p
a
s
s
w
o
r
d
:
 
s
t
r
)
 
-
>
 
b
o
o
l
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
 
w
h
e
t
h
e
r
 
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
 
p
a
s
s
w
o
r
d
 
m
e
e
t
s
 
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
 
f
o
r
m
a
t
 
r
e
q
u
i
r
e
m
e
n
t
s
:


 
 
 
 
-
 
A
t
 
l
e
a
s
t
 
o
n
e
 
n
u
m
b
e
r


 
 
 
 
-
 
A
t
 
l
e
a
s
t
 
o
n
e
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r


 
 
 
 
-
 
A
t
 
l
e
a
s
t
 
o
n
e
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r


 
 
 
 
-
 
A
t
 
l
e
a
s
t
 
o
n
e
 
p
u
n
c
t
u
a
t
i
o
n
 
m
a
r
k


 
 
 
 
-
 
M
i
n
i
m
u
m
 
l
e
n
g
t
h
 
o
f
 
8
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
s
s
w
o
r
d
 
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
s
s
w
o
r
d
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
R
e
t
u
r
n
s
 
T
r
u
e
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
m
e
e
t
s
 
a
l
l
 
r
e
q
u
i
r
e
m
e
n
t
s
;
 
o
t
h
e
r
w
i
s
e
,
 
F
a
l
s
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
m
e
e
t
s
 
t
h
e
 
m
i
n
i
m
u
m
 
l
e
n
g
t
h
 
r
e
q
u
i
r
e
m
e
n
t


 
 
 
 
i
f
 
l
e
n
(
p
a
s
s
w
o
r
d
)
 
<
 
8
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
c
o
n
t
a
i
n
s
 
a
t
 
l
e
a
s
t
 
o
n
e
 
n
u
m
b
e
r


 
 
 
 
i
f
 
n
o
t
 
a
n
y
(
c
h
a
r
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
 
f
o
r
 
c
h
a
r
 
i
n
 
p
a
s
s
w
o
r
d
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
c
o
n
t
a
i
n
s
 
a
t
 
l
e
a
s
t
 
o
n
e
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r


 
 
 
 
i
f
 
n
o
t
 
a
n
y
(
c
h
a
r
.
i
s
l
o
w
e
r
(
)
 
f
o
r
 
c
h
a
r
 
i
n
 
p
a
s
s
w
o
r
d
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
c
o
n
t
a
i
n
s
 
a
t
 
l
e
a
s
t
 
o
n
e
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r


 
 
 
 
i
f
 
n
o
t
 
a
n
y
(
c
h
a
r
.
i
s
u
p
p
e
r
(
)
 
f
o
r
 
c
h
a
r
 
i
n
 
p
a
s
s
w
o
r
d
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
p
a
s
s
w
o
r
d
 
c
o
n
t
a
i
n
s
 
a
t
 
l
e
a
s
t
 
o
n
e
 
p
u
n
c
t
u
a
t
i
o
n
 
m
a
r
k


 
 
 
 
i
f
 
n
o
t
 
a
n
y
(
c
h
a
r
 
i
n
 
s
t
r
i
n
g
.
p
u
n
c
t
u
a
t
i
o
n
 
f
o
r
 
c
h
a
r
 
i
n
 
p
a
s
s
w
o
r
d
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


`
`
`




T
h
e
 
`
i
s
_
v
a
l
i
d
_
p
a
s
s
w
o
r
d
(
)
`
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
p
a
s
s
w
o
r
d
 
s
t
r
i
n
g
 
a
s
 
i
n
p
u
t
 
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
 
b
o
o
l
e
a
n
 
v
a
l
u
e
 
i
n
d
i
c
a
t
i
n
g
 
w
h
e
t
h
e
r
 
t
h
e
 
p
a
s
s
w
o
r
d
 
m
e
e
t
s
 
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
 
f
o
r
m
a
t
 
r
e
q
u
i
r
e
m
e
n
t
s
 
o
r
 
n
o
t
.
 
T
h
e
 
f
u
n
c
t
i
o
n
 
f
i
r
s
t
 
c
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
a
s
s
w
o
r
d
 
i
s
 
a
t
 
l
e
a
s
t
 
8
 
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
 
l
o
n
g
,
 
a
n
d
 
t
h
e
n
 
c
h
e
c
k
s
 
f
o
r
 
t
h
e
 
r
e
q
u
i
r
e
d
 
c
h
a
r
a
c
t
e
r
 
t
y
p
e
s
 
u
s
i
n
g
 
t
h
e
 
`
a
n
y
(
)
`
 
f
u
n
c
t
i
o
n
 
a
n
d
 
s
t
r
i
n
g
 
m
e
t
h
o
d
s
 
s
u
c
h
 
a
s
 
`
i
s
d
i
g
i
t
(
)
`
,
 
`
i
s
l
o
w
e
r
(
)
`
,
 
`
i
s
u
p
p
e
r
(
)
`
,
 
a
n
d
 
`
p
u
n
c
t
u
a
t
i
o
n
`
 
(
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
 
a
l
l
 
t
h
e
 
p
u
n
c
t
u
a
t
i
o
n
 
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
)
.




T
o
 
t
e
s
t
 
t
h
e
 
f
u
n
c
t
i
o
n
,
 
y
o
u
 
c
a
n
 
c
a
l
l
 
i
t
 
w
i
t
h
 
d
i
f
f
e
r
e
n
t
 
p
a
s
s
w
o
r
d
 
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
 
r
e
t
u
r
n
e
d
 
b
o
o
l
e
a
n
 
v
a
l
u
e
:




`
`
`
p
y
t
h
o
n


p
r
i
n
t
(
i
s
_
v
a
l
i
d
_
p
a
s
s
w
o
r
d
(
"
S
h
o
r
t
"
)
)


p
r
i
n
t
(
i
s
_
v
a
l
i
d
_
p
a
s
s
w
o
r
d
(
"
P
a
s
s
w
o
r
d
"
)
)


p
r
i
n
t
(
i
s
_
v
a
l
i
d
_
p
a
s
s
w
o
r
d
(
"
<
P
A
S
S
W
O
R
D
>
"
)
)


p
r
i
n
t
(
i
s
_
v
a
l
i
d
_
p
a
s
s
w
o
r
d
(
"
<
P
A
S
S
W
O
R
D
>
!
"
)
)


`
`
`




T
h
i
s
 
s
h
o
u
l
d
 
o
u
t
p
u
t
:




`
`
`


F
a
l
s
e


F
a
l
s
e


F
a
l
s
e


T
r
u
e


`
`
`




A
s
 
y
o
u
 
c
a
n
 
s
e
e
,
 
t
h
e
 
f
u
n
c
t
i
o
n
 
c
o
r
r
e
c
t
l
y
 
i
d
e
n
t
i
f
i
e
s
 
s
o
m
e
 
i
n
v
a
l
i
d
 
p
a
s
s
w
o
r
d
s
 
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
 
F
a
l
s
e
,
 
w
h
i
l
e
 
t
h
e
 
v
a
l
i
d
 
p
a
s
s
w
o
r
d
import unittest


class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password1!"))

    def test_password_without_number(self):
        self.assertFalse(is_valid_password("Password!"))

    def test_password_without_uppercase(self):
        self.assertFalse(is_valid_password("password1!"))

    def test_password_without_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1!"))

    def test_password_without_punctuation(self):
        self.assertFalse(is_valid_password("Password1"))

    def test_password_shorter_than_8_characters(self):
        self.assertFalse(is_valid_password("Pass1!"))

if __name__ == '__main__':
    unittest.main()