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
 
c
o
n
t
a
i
n
s
_
e
m
a
i
l
(
t
e
x
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
 
g
i
v
e
n
 
t
e
x
t
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
n
 
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
 
a
n
 
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
 
f
o
u
n
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
 
g
i
v
e
n
 
t
e
x
t
 
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


 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
n
 
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
 
a
n
 
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
 
f
o
u
n
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
'
[
\
w
\
.
-
]
+
@
[
\
w
\
.
-
]
+
\
.
\
w
+
'
)


 
 
 
 
r
e
t
u
r
n
 
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
s
e
a
r
c
h
(
t
e
x
t
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
c
o
n
t
a
i
n
s
_
u
r
l
(
t
e
x
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
 
g
i
v
e
n
 
t
e
x
t
 
c
o
n
t
a
i
n
s
 
a
 
U
R
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
 
U
R
L
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
 
a
 
U
R
L
 
i
s
 
f
o
u
n
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
 
g
i
v
e
n
 
t
e
x
t
 
c
o
n
t
a
i
n
s
 
a
 
U
R
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
 
U
R
L
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
 
a
 
U
R
L
 
i
s
 
f
o
u
n
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
'
h
t
t
p
s
?
:
/
/
(
w
w
w
\
.
)
?
(
\
w
+
)
(
\
.
\
w
+
)
'
)


 
 
 
 
r
e
t
u
r
n
 
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
s
e
a
r
c
h
(
t
e
x
t
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
c
o
n
t
a
i
n
s
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
t
e
x
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
 
g
i
v
e
n
 
t
e
x
t
 
c
o
n
t
a
i
n
s
 
a
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
 
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
 
a
 
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
 
f
o
u
n
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
 
g
i
v
e
n
 
t
e
x
t
 
c
o
n
t
a
i
n
s
 
a
 
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


 
 
 
 
t
e
x
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
 
s
t
r
i
n
g
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
a
 
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
 
a
 
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
 
f
o
u
n
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


 
 
 
 
p
h
o
n
e
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
'
(
\
+
\
d
{
1
,
2
}
\
s
)
?
\
(
?
\
d
{
3
}
\
)
?
import unittest


class TestContainsEmail(unittest.TestCase):

    def test_contains_valid_email(self):
        """Test if a valid email is detected in the string."""
        test_string = "You can reach me at example@example.com for more info."
        self.assertTrue(contains_email(test_string))

    def test_contains_email_with_special_characters(self):
        """Test if an email with special characters is detected."""
        test_string = "My email address is john.doe123+test@gmail.com!"
        self.assertTrue(contains_email(test_string))

    def test_does_not_contain_email(self):
        """Test a string that does not contain any email address."""
        test_string = "This string does not have an email."
        self.assertFalse(contains_email(test_string))

    def test_contains_multiple_emails(self):
        """Test a string containing multiple email addresses."""
        test_string = "You can contact me at example1@example.com or example2@example.com."
        self.assertTrue(contains_email(test_string))

    def test_contains_invalid_email_format(self):
        """Test a string with an invalid email format."""
        test_string = "Please contact me at example@.com or test@domain."
        self.assertFalse(contains_email(test_string))
if __name__ == '__main__':
    unittest.main()