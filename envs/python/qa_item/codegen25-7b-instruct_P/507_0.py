i
m
p
o
r
t
 
r
e






d
e
f
 
i
s
_
s
t
r
o
n
g
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
 
s
t
r
o
n
g
.




 
 
 
 
A
 
s
t
r
o
n
g
 
p
a
s
s
w
o
r
d
 
m
u
s
t
 
s
a
t
i
s
f
y
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
c
r
i
t
e
r
i
a
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
 
t
o
 
c
h
e
c
k
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
 
i
s
 
s
t
r
o
n
g
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
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
e
m
a
i
l
(
e
m
a
i
l
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
 
e
m
a
i
l
 
i
s
 
v
a
l
i
d
.




 
 
 
 
A
 
v
a
l
i
d
 
e
m
a
i
l
 
m
u
s
t
 
s
a
t
i
s
f
y
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
c
r
i
t
e
r
i
a
:


 
 
 
 
-
 
I
t
 
m
u
s
t
 
c
o
n
t
a
i
n
 
t
h
e
 
'
@
'
 
s
y
m
b
o
l


 
 
 
 
-
 
I
t
 
m
u
s
t
 
c
o
n
t
a
i
n
 
a
 
d
o
m
a
i
n
 
n
a
m
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
m
a
i
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
 
e
m
a
i
l
 
t
o
 
c
h
e
c
k
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
 
T
r
u
e
 
i
f
 
t
h
e
 
e
m
a
i
l
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
@
"
 
i
n
 
e
m
a
i
l
 
a
n
d
 
"
.
"
 
i
n
 
e
m
a
i
l
.
s
p
l
i
t
(
"
@
"
)
[
1
]






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
 
U
R
L
 
i
s
 
v
a
l
i
d
.




 
 
 
 
A
 
v
a
l
i
d
 
U
R
L
 
m
u
s
t
 
s
a
t
i
s
f
y
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
c
r
i
t
e
r
i
a
:


 
 
 
 
-
 
I
t
 
m
u
s
t
 
s
t
a
r
t
 
w
i
t
h
 
e
i
t
h
e
r
 
'
h
t
t
p
:
/
/
'
 
o
r
 
'
h
t
t
p
s
:
/
/
'


 
 
 
 
-
 
I
t
 
m
u
s
t
 
c
o
n
t
a
i
n
 
a
 
d
o
m
a
i
n
 
n
a
m
e




 
 
 
 
A
r
g
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
 
c
h
e
c
k
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
 
T
r
u
e
 
i
f
 
t
h
e
 
U
R
L
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
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
 
u
r
l
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
h
t
t
p
:
/
/
"
)
 
o
r
 
u
r
l
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
h
t
t
p
s
:
/
/
"
)
 
a
n
d
 
"
.
"
 
i
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
/
"
)
[
1
]






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
p
v
4
(
import unittest


class TestStrongPassword(unittest.TestCase):
    def test_valid_password(self):
        """ Test a strong password that meets all criteria. """
        self.assertTrue(is_strong_password("StrongPass1"))

    def test_missing_lowercase(self):
        """ Test a password missing a lowercase letter. """
        self.assertFalse(is_strong_password("STRONGPASS1"))

    def test_missing_uppercase(self):
        """ Test a password missing an uppercase letter. """
        self.assertFalse(is_strong_password("strongpass1"))

    def test_missing_number(self):
        """ Test a password missing a number. """
        self.assertFalse(is_strong_password("StrongPassword"))

    def test_too_short(self):
        """ Test a password that is too short. """
        self.assertFalse(is_strong_password("Short1"))

    def test_valid_with_special_characters(self):
        """ Test a password that includes special characters but is still strong. """
        self.assertTrue(is_strong_password("Strong!Password1"))
if __name__ == '__main__':
    unittest.main()