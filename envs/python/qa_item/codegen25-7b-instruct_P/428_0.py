i
m
p
o
r
t
 
a
s
t


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
 
L
i
s
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
t
y
p
e
_
h
i
n
t
(
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
:
s
t
r
)
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
P
y
t
h
o
n
 
t
y
p
e
 
h
i
n
t
 
s
t
r
i
n
g
 
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
 
t
h
e
 
i
n
d
i
v
i
d
u
a
l
 
t
y
p
e
s
 
a
s
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
T
h
e
 
t
y
p
e
 
h
i
n
t
 
s
t
r
i
n
g
 
t
o
 
p
a
r
s
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
i
n
d
i
v
i
d
u
a
l
 
t
y
p
e
s
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
t
y
p
e
 
h
i
n
t
 
s
t
r
i
n
g
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
t
y
p
e
_
h
i
n
t
 
=
 
"
U
n
i
o
n
[
t
y
p
i
n
g
.
L
i
s
t
[
s
t
r
]
,
 
t
y
p
i
n
g
.
D
i
c
t
[
s
t
r
,
 
i
n
t
]
,
 
T
u
p
l
e
[
i
n
t
,
 
s
t
r
]
,
 
O
p
t
i
o
n
a
l
[
i
n
t
]
]
"


 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
t
y
p
e
s
 
=
 
p
a
r
s
e
_
t
y
p
e
_
h
i
n
t
(
t
y
p
e
_
h
i
n
t
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
p
a
r
s
e
d
_
t
y
p
e
s
)


 
 
 
 
 
 
 
 
#
 
O
u
t
p
u
t
:
 
[
'
U
n
i
o
n
'
,
 
'
t
y
p
i
n
g
.
L
i
s
t
'
,
 
'
s
t
r
'
,
 
'
t
y
p
i
n
g
.
D
i
c
t
'
,
 
'
s
t
r
'
,
 
'
i
n
t
'
,
 
'
T
u
p
l
e
'
,
 
'
i
n
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
'
s
t
r
'
,
 
'
O
p
t
i
o
n
a
l
'
,
 
'
i
n
t
'
]


 
 
 
 
"
"
"


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
"
,
 
"
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
U
n
i
o
n
"
,
 
"
U
n
i
o
n
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
L
i
s
t
"
,
 
"
L
i
s
t
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
D
i
c
t
"
,
 
"
D
i
c
t
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
T
u
p
l
e
"
,
 
"
T
u
p
l
e
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
O
p
t
i
o
n
a
l
"
,
 
"
O
p
t
i
o
n
a
l
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
A
n
y
"
,
 
"
A
n
y
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
T
y
p
e
"
,
 
"
T
y
p
e
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
C
a
l
l
a
b
l
e
"
,
 
"
C
a
l
l
a
b
l
e
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
S
e
t
"
,
 
"
S
e
t
"
)


 
 
 
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
 
=
 
t
y
p
e
_
h
i
n
t
_
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
t
y
p
i
n
g
.
F
r
o
z
e
n
S
e
t
"
,
 
"
F
r
o
z
e
n
S
e
t
"
)


 
 
 
 
t
y
p
e
_
h
import unittest


# Assuming the parse_type_hint function is defined above or imported here

class TestParseTypeHint(unittest.TestCase):

    def test_basic_types(self):
        type_hint = 'int'
        expected = ['int']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_list_type(self):
        type_hint = 'List[int]'
        expected = ['List', 'int']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_union_type(self):
        type_hint = 'Union[str, float]'
        expected = ['Union', 'str', 'float']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_tuple_type(self):
        type_hint = 'Tuple[str, int, float]'
        expected = ['Tuple', 'str', 'int', 'float']
        self.assertEqual(parse_type_hint(type_hint), expected)

    def test_complex_type(self):
        type_hint = 'List[Union[int, float], Tuple[str, int]]'
        expected = ['List', 'Union', 'int', 'float', 'Tuple', 'str', 'int']
        self.assertEqual(parse_type_hint(type_hint), expected)

if __name__ == '__main__':
    unittest.main()