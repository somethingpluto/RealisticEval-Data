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
 
D
i
c
t






d
e
f
 
p
a
r
s
e
_
x
a
m
l
_
t
o
_
d
i
c
t
(
x
a
m
l
_
f
i
l
e
:
 
s
t
r
)
 
-
>
 
D
i
c
t
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


 
 
 
 
p
a
r
s
e
 
t
h
e
 
X
A
M
L
 
f
i
l
e
,
 
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
w
i
t
h
i
n
 
t
h
e
 
S
t
r
i
n
g
 
e
l
e
m
e
n
t
,
 
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
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
i
n
 
a
 
d
i
c
t
i
o
n
a
r
y


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
a
m
l
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
X
A
M
L
 
f
i
l
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
 
d
i
c
t
i
o
n
a
r
y
 
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
'
S
t
r
i
n
g
'
 
e
l
e
m
e
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
x
m
l
.
e
t
r
e
e
.
E
l
e
m
e
n
t
T
r
e
e
 
a
s
 
E
T


 
 
 
 
i
m
p
o
r
t
 
r
e


 
 
 
 
i
m
p
o
r
t
 
o
s


 
 
 
 
i
m
p
o
r
t
 
s
y
s




 
 
 
 
#
 
c
h
e
c
k
 
i
f
 
t
h
e
 
x
a
m
l
_
f
i
l
e
 
i
s
 
a
 
v
a
l
i
d
 
f
i
l
e


 
 
 
 
i
f
 
n
o
t
 
o
s
.
p
a
t
h
.
i
s
f
i
l
e
(
x
a
m
l
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
{
x
a
m
l
_
f
i
l
e
}
 
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
 
f
i
l
e
.
"
)


 
 
 
 
 
 
 
 
s
y
s
.
e
x
i
t
(
1
)




 
 
 
 
#
 
p
a
r
s
e
 
t
h
e
 
x
a
m
l
 
f
i
l
e


 
 
 
 
t
r
e
e
 
=
 
E
T
.
p
a
r
s
e
(
x
a
m
l
_
f
i
l
e
)


 
 
 
 
r
o
o
t
 
=
 
t
r
e
e
.
g
e
t
r
o
o
t
(
)




 
 
 
 
#
 
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
f
r
o
m
 
t
h
e
 
S
t
r
i
n
g
 
e
l
e
m
e
n
t
s


 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
=
 
{
}


 
 
 
 
f
o
r
 
s
t
r
i
n
g
 
i
n
 
r
o
o
t
.
f
i
n
d
a
l
l
(
"
.
/
/
S
t
r
i
n
g
"
)
:


 
 
 
 
 
 
 
 
k
e
y
 
=
 
s
t
r
i
n
g
.
g
e
t
(
"
K
e
y
"
)


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
t
r
i
n
g
.
t
e
x
t


 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
[
k
e
y
]
 
=
 
v
a
l
u
e




 
 
 
 
r
e
t
u
r
n
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t






d
e
f
 
p
a
r
s
e
_
x
a
m
l
_
t
o
_
d
i
c
t
_
w
i
t
h
_
r
e
g
e
x
(
x
a
m
l
_
f
i
l
e
:
 
s
t
r
)
 
-
>
 
D
i
c
t
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


 
 
 
 
p
a
r
s
e
 
t
h
e
 
X
A
M
L
 
f
i
l
e
,
 
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
w
i
t
h
i
n
 
t
h
e
 
S
t
r
i
n
g
 
e
l
e
m
e
n
t
,
 
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
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
i
n
 
a
 
d
i
c
t
i
o
n
a
r
y


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
a
m
l
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
X
A
M
L
 
f
i
l
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
 
d
i
c
t
i
o
n
a
r
y
 
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
'
S
t
r
i
n
g
'
 
e
l
e
m
e
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
x
m
l
.
e
t
r
e
e
.
E
l
e
m
e
n
t
T
r
e
e
 
a
s
 
E
T


 
 
 
 
i
m
p
o
r
t
 
r
e


 
 
 
 
i
m
p
o
r
t
 
o
s


 
 
 
 
i
m
p
o
r
t
 
s
y
s




 
 
 
 
#
 
c
h
e
c
k
 
i
f
 
t
h
e
 
x
a
m
l
_
f
i
l
e
 
i
s
 
a
 
v
a
l
i
d
 
f
i
l
e


 
 
 
 
i
f
 
n
o
t
 
o
s
.
p
a
t
h
.
i
s
f
i
l
e
(
x
a
m
l
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
{
x
a
m
l
_
f
i
l
e
}
 
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
 
f
i
l
e
.
"
)


 
 
 
 
 
 
 
 
s
y
s
.
e
x
i
t
(
1
)




 
 
 
 
#
 
p
a
r
s
e
 
t
h
e
 
x
a
m
l
 
f
i
l
e


 
 
 
 
t
r
e
e
 
=
 
E
T
.
p
a
r
s
e
(
x
a
m
l
_
f
i
l
e
)


 
 
 
 
r
o
o
t
import unittest
import xml.etree.ElementTree as ET
from io import StringIO


class TestParseXamlToDict(unittest.TestCase):
    def test_valid_strings(self):
        xaml_data = """<root>
                         <String Key="Username">Alice</String>
                         <String Key="Password">secret</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {'Username': 'Alice', 'Password': 'secret'}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

    def test_missing_key_attribute(self):
        xaml_data = """<root>
                         <String>Alice</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)


    def test_no_string_tags(self):
        xaml_data = """<root>
                         <Data>Some question</Data>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

    def test_nested_string_tags(self):
        xaml_data = """<root>
                         <Container>
                           <String Key="Username">Bob</String>
                         </Container>
                         <String Key="Location">Earth</String>
                       </root>"""
        xaml_input = StringIO(xaml_data)
        expected = {'Username': 'Bob', 'Location': 'Earth'}
        result = parse_xaml_to_dict(xaml_input)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()