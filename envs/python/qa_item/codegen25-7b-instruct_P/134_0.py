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
 
u
s
e
r
n
a
m
e
 
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
 
u
s
e
r
n
a
m
e
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
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
:


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
5
 
a
n
d
 
1
6
 
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
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
-
 
C
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
 
a
l
p
h
a
n
u
m
e
r
i
c
 
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
 
(
l
e
t
t
e
r
s
 
a
n
d
 
d
i
g
i
t
s
)
 
a
n
d
 
s
p
a
c
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
 
u
s
e
r
n
a
m
e
 
i
s
 
v
a
l
i
d
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


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
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
,
 
s
t
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




 
 
 
 
i
f
 
l
e
n
(
u
s
e
r
n
a
m
e
)
 
<
 
5
 
o
r
 
l
e
n
(
u
s
e
r
n
a
m
e
)
 
>
 
1
6
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
\
s
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
 
d
e
f
i
n
e
d
 
a
s
 
a
 
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
:


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
8
 
a
n
d
 
3
2
 
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
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
-
 
C
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
 
d
i
g
i
t
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
 
(
!
@
#
$
%
^
&
*
(
)
_
+
-
=
[
]
{
}
|
;
'
:
\
"
,
.
/
<
>
?
)




 
 
 
 
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
 
i
s
 
v
a
l
i
d
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


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
p
a
s
s
w
o
r
d
,
 
s
t
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
 
o
r
 
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
 
>
 
3
2
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
 
i
s
 
d
e
f
i
n
e
d
 
a
s
 
a
 
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
:


 
 
 
 
-
 
H
a
s
 
t
h
e
 
f
o
r
m
a
t
 
'
n
a
m
e
@
d
o
m
a
i
n
.
t
l
d
'
.


 
 
 
 
-
 
H
a
s
 
a
 
l
e
n
g
t
h
 
b
e
t
w
e
e
n
 
5
 
a
n
d
import unittest


class TestIsValidUsername(unittest.TestCase):

    def test_valid_username_with_alphanumeric_characters(self):
        self.assertTrue(is_valid_username('User123'))

    def test_valid_username_with_spaces(self):
        self.assertTrue(is_valid_username('User 123'))

    def test_invalid_username_that_is_too_short(self):
        self.assertFalse(is_valid_username('User'))

    def test_invalid_username_that_is_too_long(self):
        self.assertFalse(is_valid_username('ThisIsAVeryLongUsername'))

    def test_invalid_username_with_special_characters(self):
        self.assertFalse(is_valid_username('User!'))

    def test_invalid_username_with_only_spaces(self):
        self.assertFalse(is_valid_username('     '))

    def test_invalid_input_type_number(self):
        self.assertFalse(is_valid_username(12345))
if __name__ == '__main__':
    unittest.main()