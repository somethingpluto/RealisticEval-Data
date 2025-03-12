f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
T
u
p
l
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
s
l
d
_
t
l
d
(
f
q
d
n
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
e
x
t
r
a
c
t
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
a
n
d
 
t
o
p
-
l
e
v
e
l
 
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
s
 
f
r
o
m
 
t
h
e
 
f
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
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
 
F
Q
D
N
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
q
d
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
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
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
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
t
u
p
l
e
 
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
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
d
o
m
a
i
n
 
a
n
d
 
t
o
p
-
l
e
v
e
l
 
d
o
m
a
i
n
.


 
 
 
 
"
"
"


 
 
 
 
#
 
s
p
l
i
t
 
t
h
e
 
f
q
d
n
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
d
o
m
a
i
n
 
c
o
m
p
o
n
e
n
t
s


 
 
 
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
 
=
 
f
q
d
n
.
s
p
l
i
t
(
'
.
'
)


 
 
 
 
#
 
g
e
t
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
l
i
s
t


 
 
 
 
d
o
m
a
i
n
_
l
e
n
g
t
h
 
=
 
l
e
n
(
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
)


 
 
 
 
#
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
l
e
s
s
 
t
h
a
n
 
2
,
 
r
e
t
u
r
n
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g


 
 
 
 
i
f
 
d
o
m
a
i
n
_
l
e
n
g
t
h
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
'
,
 
'
'


 
 
 
 
#
 
g
e
t
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
d
o
m
a
i
n


 
 
 
 
s
l
d
 
=
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
[
d
o
m
a
i
n
_
l
e
n
g
t
h
 
-
 
2
]


 
 
 
 
#
 
g
e
t
 
t
h
e
 
t
o
p
-
l
e
v
e
l
 
d
o
m
a
i
n


 
 
 
 
t
l
d
 
=
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
[
d
o
m
a
i
n
_
l
e
n
g
t
h
 
-
 
1
]


 
 
 
 
#
 
r
e
t
u
r
n
 
t
h
e
 
s
l
d
 
a
n
d
 
t
l
d


 
 
 
 
r
e
t
u
r
n
 
s
l
d
,
 
t
l
d






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
s
l
d
_
t
l
d
_
f
r
o
m
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
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
e
x
t
r
a
c
t
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
a
n
d
 
t
o
p
-
l
e
v
e
l
 
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
s
 
f
r
o
m
 
t
h
e
 
u
r
l
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
m


 
 
 
 
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
 
u
r
l
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
t
u
p
l
e
 
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
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
d
o
m
a
i
n
 
a
n
d
 
t
o
p
-
l
e
v
e
l
 
d
o
m
a
i
n
.


 
 
 
 
"
"
"


 
 
 
 
#
 
s
p
l
i
t
 
t
h
e
 
u
r
l
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
d
o
m
a
i
n
 
c
o
m
p
o
n
e
n
t
s


 
 
 
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
 
=
 
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
'
/
'
)
[
2
]
.
s
p
l
i
t
(
'
.
'
)


 
 
 
 
#
 
g
e
t
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
l
i
s
t


 
 
 
 
d
o
m
a
i
n
_
l
e
n
g
t
h
 
=
 
l
e
n
(
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
)


 
 
 
 
#
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
l
e
s
s
 
t
h
a
n
 
2
,
 
r
e
t
u
r
n
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g


 
 
 
 
i
f
 
d
o
m
a
i
n
_
l
e
n
g
t
h
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
'
,
 
'
'


 
 
 
 
#
 
g
e
t
 
t
h
e
 
s
e
c
o
n
d
-
l
e
v
e
l
 
d
o
m
a
i
n


 
 
 
 
s
l
d
 
=
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
[
d
o
m
a
i
n
_
l
e
n
g
t
h
 
-
 
2
]


 
 
 
 
#
 
g
e
t
 
t
h
e
 
t
o
p
-
l
e
v
e
l
 
d
o
m
a
i
n


 
 
 
 
t
l
d
 
=
 
d
o
m
a
i
n
_
c
o
m
p
o
n
e
n
t
s
[
d
o
m
a
i
n
_
l
e
n
g
t
h
 
-
 
1
]


 
 
 
 
#
 
r
e
t
u
r
n
 
t
h
e
 
s
l
d
 
a
n
d
 
t
l
d


 
 
 
 
r
e
t
u
r
n
 
s
l
d
,
 
t
l
d






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
s
l
d
_
t
l
d
_
f
r
o
m
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
 
T
u
p
l
e
[
s
t
r
,
import unittest


class TestExtractSldTld(unittest.TestCase):
    def test_standard_fqdn(self):
        # Test a typical FQDN
        self.assertEqual(extract_sld_tld("www.example.com"), ("example", "com"))

    def test_standard_fqdn2(self):
        # Test a typical FQDN
        self.assertEqual(extract_sld_tld("www.example.xyz"), ("example", "xyz"))

    def test_fqdn_with_subdomains(self):
        # Test an FQDN with multiple subdomains
        self.assertEqual(extract_sld_tld("blog.subdomain.example.com"), ("example", "com"))

    def test_numeric_tld(self):
        # Test a numeric TLD, which can occur in private networks
        self.assertEqual(extract_sld_tld("server.example.123"), ("example", "123"))

if __name__ == '__main__':
    unittest.main()