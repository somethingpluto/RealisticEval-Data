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
s
e
r
n
a
m
e
(
u
s
e
r
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
 
u
s
e
r
n
a
m
e
 
a
n
d
 
c
h
e
c
k
 
t
h
a
t
 
t
h
e
 
u
s
e
r
n
a
m
e
 
c
o
n
t
a
i
n
s
 
o
n
l
y
 
l
e
t
t
e
r
s
,
 
n
u
m
b
e
r
s
,
 
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
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
s
e
r
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
 
u
s
e
r
n
a
m
e
 
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
 
u
s
e
r
n
a
m
e
 
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
;
F
a
l
s
e
 
i
f
 
t
h
e
 
u
s
e
r
n
a
m
e
 
c
o
n
t
a
i
n
s
 
a
n
y
 
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
 
o
u
t
s
i
d
e
 
o
f
 
l
e
t
t
e
r
s
,
 
n
u
m
b
e
r
s
,
 
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
 
b
o
o
l
(
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
[
a
-
z
A
-
Z
0
-
9
_
]
+
$
"
,
 
u
s
e
r
n
a
m
e
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
 
p
a
s
s
w
o
r
d
 
a
n
d
 
c
h
e
c
k
 
t
h
a
t
 
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
,
 
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
,
 
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
,
 
o
n
e
 
n
u
m
b
e
r
,
 
a
n
d
 
o
n
e
 
s
p
e
c
i
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
.




 
 
 
 
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
 
p
a
s
s
w
o
r
d
 
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
;
F
a
l
s
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
 
d
o
e
s
 
n
o
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
 
b
o
o
l
(
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
?
=
.
*
[
A
-
Z
]
)
(
?
=
.
*
[
a
-
z
]
)
(
?
=
.
*
\
d
)
(
?
=
.
*
[
@
$
!
%
*
?
&
]
)
[
A
-
Z
a
-
z
\
d
@
$
!
%
*
?
&
]
{
8
,
}
$
"
,
 
p
a
s
s
w
o
r
d
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
 
a
d
d
r
e
s
s
 
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
;
F
a
l
s
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
 
d
o
e
s
 
n
o
t
 
m
a
t
c
h
 
t
h
e
 
p
a
t
t
e
r
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
 
b
o
o
l
(
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
$
"
,
 
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
;
F
a
l
s
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
import unittest


class TestUsernameValidation(unittest.TestCase):

    def test_valid_username_with_letters_numbers_and_underscores(self):
        result = is_valid_username('user_123')
        self.assertEqual(result, True)  # 'user_123' is a valid username

    def test_valid_username_with_only_letters(self):
        result = is_valid_username('username')
        self.assertEqual(result, True)  # 'username' is a valid username

    def test_invalid_username_with_special_characters(self):
        result = is_valid_username('user-name')
        self.assertEqual(result, False)  # 'user-name' contains a hyphen

    def test_invalid_username_with_spaces(self):
        result = is_valid_username('user name')
        self.assertEqual(result, False)  # 'user name' contains spaces

    def test_valid_username_with_only_numbers(self):
        result = is_valid_username('12345')
        self.assertEqual(result, True)  # '12345' is a valid username

if __name__ == '__main__':
    unittest.main()