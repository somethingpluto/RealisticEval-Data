d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
e
t
a
i
l
s
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
s
 
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
 
a
n
d
 
m
a
i
l
b
o
x
 
s
u
f
f
i
x
 
f
r
o
m
 
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
e
g
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
e
t
a
i
l
s
(
"
x
x
x
@
g
m
a
i
l
.
c
o
m
"
)
 
r
e
t
u
r
n
s
 
(
'
x
x
x
'
,
 
'
g
m
a
i
l
.
c
o
m
'
)


 
 
 
 
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
 
t
o
 
e
x
t
r
a
c
t
 
d
e
t
a
i
l
s
 
f
r
o
m




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
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
 
d
o
m
a
i
n
)


 
 
 
 
"
"
"


 
 
 
 
u
s
e
r
n
a
m
e
,
 
d
o
m
a
i
n
 
=
 
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


 
 
 
 
r
e
t
u
r
n
 
u
s
e
r
n
a
m
e
,
 
d
o
m
a
i
n






d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
s
u
f
f
i
x
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
s
 
t
h
e
 
m
a
i
l
b
o
x
 
s
u
f
f
i
x
 
f
r
o
m
 
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
e
g
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
s
u
f
f
i
x
(
"
x
x
x
@
g
m
a
i
l
.
c
o
m
"
)
 
r
e
t
u
r
n
s
 
'
g
m
a
i
l
.
c
o
m
'


 
 
 
 
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
 
t
o
 
e
x
t
r
a
c
t
 
d
e
t
a
i
l
s
 
f
r
o
m




 
 
 
 
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
 
m
a
i
l
b
o
x
 
s
u
f
f
i
x


 
 
 
 
"
"
"


 
 
 
 
u
s
e
r
n
a
m
e
,
 
d
o
m
a
i
n
 
=
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
e
t
a
i
l
s
(
e
m
a
i
l
)


 
 
 
 
r
e
t
u
r
n
 
d
o
m
a
i
n






d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
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
s
 
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
 
f
r
o
m
 
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
e
g
 
e
x
t
r
a
c
t
_
e
m
a
i
l
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
"
x
x
x
@
g
m
a
i
l
.
c
o
m
"
)
 
r
e
t
u
r
n
s
 
'
x
x
x
'


 
 
 
 
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
 
t
o
 
e
x
t
r
a
c
t
 
d
e
t
a
i
l
s
 
f
r
o
m




 
 
 
 
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
 
u
s
e
r
n
a
m
e


 
 
 
 
"
"
"


 
 
 
 
u
s
e
r
n
a
m
e
,
 
d
o
m
a
i
n
 
=
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
e
t
a
i
l
s
(
e
m
a
i
l
)


 
 
 
 
r
e
t
u
r
n
 
u
s
e
r
n
a
m
e






d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
o
m
a
i
n
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
s
 
t
h
e
 
d
o
m
a
i
n
 
f
r
o
m
 
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
e
g
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
o
m
a
i
n
(
"
x
x
x
@
g
m
a
i
l
.
c
o
m
"
)
 
r
e
t
u
r
n
s
 
'
g
m
a
i
l
.
c
o
m
'


 
 
 
 
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
 
t
o
 
e
x
t
r
a
c
t
 
d
e
t
a
i
l
s
 
f
r
o
m




 
 
 
 
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
 
d
o
m
a
i
n


 
 
 
 
"
"
"


 
 
 
 
u
s
e
r
n
a
m
e
,
 
d
o
m
a
i
n
 
=
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
e
t
a
i
l
s
(
e
m
a
i
l
)


 
 
 
 
r
e
t
u
r
n
 
d
o
m
a
i
n






d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
o
m
a
i
n
_
n
a
m
e
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
s
 
t
h
e
 
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
 
f
r
o
m
 
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
e
g
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
o
m
a
i
n
_
n
a
m
e
(
"
x
x
x
@
g
m
a
i
l
.
c
o
m
"
)
 
r
e
t
u
r
n
s
 
'
g
m
a
i
l
'


 
 
 
 
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
 
t
o
 
e
x
t
r
a
c
t
 
d
e
t
a
i
l
s
 
f
r
o
m




 
 
 
 
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


 
 
 
 
"
"
"


 
 
 
 
d
o
m
a
i
n
 
=
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
s
u
f
f
i
x
(
e
m
a
i
l
)


 
 
 
 
r
e
t
u
r
n
 
d
o
m
a
i
n
.
s
p
l
i
t
(
"
.
"
)
[
0
]






d
e
f
 
e
x
t
r
a
c
t
_
e
m
a
i
l
_
d
o
m
a
i
n
_
s
u
f
f
i
x
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
import unittest

class TestExtractEmailDetails(unittest.TestCase):

    def test_valid_email(self):
        # Test with a typical email address
        email = "user@example.com"
        expected = ("user", "example.com")
        result = extract_email_details(email)
        self.assertEqual(result, expected)

    def test_valid_email_with_subdomain(self):
        # Test with an email that includes a subdomain
        email = "user@mail.office.com"
        expected = ("user", "mail.office.com")
        result = extract_email_details(email)
        self.assertEqual(result, expected)


    def test_email_without_at_symbol(self):
        # Test with an email that lacks an '@' symbol
        email = "userexample.com"
        with self.assertRaises(ValueError):
            extract_email_details(email)

    def test_empty_email(self):
        # Test with an empty string as an email
        email = ""
        with self.assertRaises(ValueError):
            extract_email_details(email)
if __name__ == '__main__':
    unittest.main()