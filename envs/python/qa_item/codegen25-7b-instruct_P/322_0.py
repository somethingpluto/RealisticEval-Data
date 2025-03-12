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
y
 
t
h
a
t
 
a
 
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
 
m
a
t
c
h
e
s
 
t
h
e
 
r
e
g
e
x
 
p
a
t
t
e
r
n
,
 
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
 
i
t
 
i
s
 
v
a
l
i
d
,
o
r
 
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


 
 
 
 
e
m
a
i
l
_
r
e
g
e
x
 
=
 
r
e
.
c
o
m
p
i
l
e
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
)


 
 
 
 
r
e
t
u
r
n
 
b
o
o
l
(
e
m
a
i
l
_
r
e
g
e
x
.
m
a
t
c
h
(
e
m
a
i
l
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
y
 
t
h
a
t
 
a
 
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
 
m
a
t
c
h
e
s
 
t
h
e
 
r
e
g
e
x
 
p
a
t
t
e
r
n
,
 
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
 
i
t
 
i
s
 
v
a
l
i
d
,
o
r
 
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


 
 
 
 
u
r
l
_
r
e
g
e
x
 
=
 
r
e
.
c
o
m
p
i
l
e
(


 
 
 
 
 
 
 
 
r
"
^
(
?
:
h
t
t
p
|
f
t
p
)
s
?
:
/
/
"
 
 
#
 
h
t
t
p
:
/
/
 
o
r
 
h
t
t
p
s
:
/
/


 
 
 
 
 
 
 
 
r
"
(
?
:
(
?
:
[
A
-
Z
0
-
9
]
(
?
:
[
A
-
Z
0
-
9
-
]
{
0
,
6
1
}
[
A
-
Z
0
-
9
]
)
?
\
.
)
+
(
?
:
[
A
-
Z
]
{
2
,
6
}
\
.
?
|
[
A
-
Z
0
-
9
-
]
{
2
,
}
\
.
?
)
|
"
 
 
#
 
d
o
m
a
i
n
.
.
.


 
 
 
 
 
 
 
 
r
"
l
o
c
a
l
h
o
s
t
|
"
 
 
#
 
l
o
c
a
l
h
o
s
t
.
.
.


 
 
 
 
 
 
 
 
r
"
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
)
"
 
 
#
 
.
.
.
o
r
 
i
p


 
 
 
 
 
 
 
 
r
"
(
?
:
:
\
d
+
)
?
"
 
 
#
 
o
p
t
i
o
n
a
l
 
p
o
r
t


 
 
 
 
 
 
 
 
r
"
(
?
:
/
?
|
[
/
?
]
\
S
+
)
$
"
,


 
 
 
 
 
 
 
 
r
e
.
I
G
N
O
R
E
C
A
S
E
,


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
b
o
o
l
(
u
r
l
_
r
e
g
e
x
.
m
a
t
c
h
(
u
r
l
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
u
u
i
d
(
u
u
i
d
_
t
o
_
t
e
s
t
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
y
 
t
h
a
t
 
a
 
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
U
I
D
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
u
i
d
_
t
o
_
t
e
s
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
 
U
U
I
D
 
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
U
I
D
 
m
a
t
c
h
e
s
 
t
h
e
 
r
e
g
e
x
 
p
a
t
t
e
r
n
,
 
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
 
i
t
 
i
s
 
v
a
l
i
d
,
o
r
 
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


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
u
u
i
d
import unittest


class TestIsValidEmail(unittest.TestCase):

    def test_valid_simple_email(self):
        result = is_valid_email('test@example.com')
        self.assertTrue(result)  # 'test@example.com' is a valid email

    def test_valid_email_with_subdomain(self):
        result = is_valid_email('user@mail.example.com')
        self.assertTrue(result)  # 'user@mail.example.com' is a valid email

    def test_invalid_email_missing_at_symbol(self):
        result = is_valid_email('invalid-email.com')
        self.assertFalse(result)  # 'invalid-email.com' is missing the @ symbol

    def test_invalid_email_missing_domain_part(self):
        result = is_valid_email('user@.com')
        self.assertFalse(result)  # 'user@.com' is missing a valid domain name

    def test_invalid_email_with_spaces(self):
        result = is_valid_email('user name@example.com')
        self.assertFalse(result)  # 'user name@example.com' contains spaces

if __name__ == '__main__':
    unittest.main()