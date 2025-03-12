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


 
 
 
 
V
e
r
i
f
i
e
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
 
s
t
r
i
n
g
 
i
s
 
a
 
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
 
a
d
d
r
e
s
s
.




 
 
 
 
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
 
a
d
d
r
e
s
s
 
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
 
a
d
d
r
e
s
s
 
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


 
 
 
 
i
f
 
n
o
t
 
e
m
a
i
l
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


 
 
 
 
i
f
 
n
o
t
 
r
e
.
m
a
t
c
h
(
r
"
[
^
@
]
+
@
[
^
@
]
+
\
.
[
^
@
]
+
"
,
 
e
m
a
i
l
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


 
 
 
 
V
e
r
i
f
i
e
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
 
s
t
r
i
n
g
 
i
s
 
a
 
v
a
l
i
d
 
U
R
L
.




 
 
 
 
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


 
 
 
 
i
f
 
n
o
t
 
u
r
l
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


 
 
 
 
i
f
 
n
o
t
 
r
e
.
m
a
t
c
h
(
r
"
^
h
t
t
p
s
?
:
\
/
\
/
[
^
\
s
]
+
"
,
 
u
r
l
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
p
h
o
n
e
_
n
u
m
b
e
r
(
p
h
o
n
e
_
n
u
m
b
e
r
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


 
 
 
 
V
e
r
i
f
i
e
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
 
s
t
r
i
n
g
 
i
s
 
a
 
v
a
l
i
d
 
p
h
o
n
e
 
n
u
m
b
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
h
o
n
e
_
n
u
m
b
e
r
 
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
h
o
n
e
 
n
u
m
b
e
r
 
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
h
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


 
 
 
 
i
f
 
n
o
t
 
p
h
o
n
e
_
n
u
m
b
e
r
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


 
 
 
 
i
f
 
n
o
t
 
r
e
.
m
a
t
c
h
(
r
"
^
\
+
?
\
d
{
1
,
3
}
[
-
.
\
s
]
?
\
d
{
9
,
1
4
}
$
"
,
 
p
h
o
n
e
_
n
u
m
b
e
r
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
i
p
v
4
(
i
p
v
4
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


 
 
 
 
V
e
r
i
f
i
e
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
 
s
t
r
i
n
g
 
i
s
 
a
 
v
a
l
i
d
 
I
P
v
4
 
a
d
d
r
e
s
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
p
v
4
 
(
s
t
r
)
:
T
h
e
 
I
P
v
4
 
a
d
d
r
e
s
s
 
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
 
T
r
u
e
 
i
f
 
t
h
e
 
I
P
v
4
 
a
d
d
r
e
s
s
 
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


 
 
 
 
i
f
 
n
o
t
 
i
p
v
4
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


 
 
 
 
i
f
 
n
o
t
 
r
e
.
m
a
t
c
h
(
r
"
^
(
2
5
[
0
-
5
]
|
2
[
0
-
4
]
[
0
-
9
]
|
[
0
1
]
?
[
0
-
9
]
[
0
-
9
]
?
)
\
.
(
2
5
[
0
-
5
]
import unittest


class TestEmailValidation(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_valid_email_with_subdomain(self):
        self.assertTrue(is_valid_email("user@subdomain.example.com"))

    def test_valid_email_with_plus_tag(self):
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"))

    def test_invalid_email_missing_username(self):
        self.assertFalse(is_valid_email("@missingusername.com"))

    def test_invalid_email_missing_at_symbol(self):
        self.assertFalse(is_valid_email("missingatsign.com"))


    def test_invalid_email_tld_too_short(self):
        self.assertFalse(is_valid_email("user@domain.c"))

    def test_invalid_email_with_special_characters(self):
        self.assertFalse(is_valid_email("user@domain.com!"))


if __name__ == '__main__':
    unittest.main()