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
,
 
D
i
c
t
,
 
U
n
i
o
n






d
e
f
 
c
o
n
v
e
r
t
_
s
t
r
i
n
g
s
_
t
o
_
n
u
m
b
e
r
s
(
d
a
t
a
:
 
U
n
i
o
n
[
D
i
c
t
,
 
L
i
s
t
]
)
 
-
>
 
U
n
i
o
n
[
D
i
c
t
,
 
L
i
s
t
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
 
s
t
r
i
n
g
s
 
i
n
 
n
e
s
t
e
d
 
s
t
r
u
c
t
u
r
e
s
 
(
e
.
g
.
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
a
r
r
a
y
s
)
 
t
o
 
n
u
m
b
e
r
s
 
(
i
n
t
e
g
e
r
s
 
o
r
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
s
)
 
a
s
 
m
u
c
h
 
a
s
 
p
o
s
s
i
b
l
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
(
U
n
i
o
n
[
D
i
c
t
,
L
i
s
t
]
)
:
 
b
e
f
o
r
e
 
c
o
n
v
e
r
t
 
d
a
t
a




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
U
n
i
o
n
[
D
i
c
t
,
L
i
s
t
]
:
 
a
f
t
e
r
 
c
o
n
v
e
r
t
 
d
a
t
a


 
 
 
 
"
"
"


 
 
 
 
i
f
 
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
d
a
t
a
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
k
e
y
,
 
v
a
l
u
e
 
i
n
 
d
a
t
a
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
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
v
a
l
u
e
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
k
e
y
]
 
=
 
i
n
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
k
e
y
]
 
=
 
f
l
o
a
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
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
v
a
l
u
e
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
k
e
y
]
 
=
 
c
o
n
v
e
r
t
_
s
t
r
i
n
g
s
_
t
o
_
n
u
m
b
e
r
s
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
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
v
a
l
u
e
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
k
e
y
]
 
=
 
c
o
n
v
e
r
t
_
s
t
r
i
n
g
s
_
t
o
_
n
u
m
b
e
r
s
(
v
a
l
u
e
)


 
 
 
 
e
l
i
f
 
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
d
a
t
a
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
i
,
 
v
a
l
u
e
 
i
n
 
e
n
u
m
e
r
a
t
e
(
d
a
t
a
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
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
v
a
l
u
e
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
i
]
 
=
 
i
n
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
i
]
 
=
 
f
l
o
a
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
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
v
a
l
u
e
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
i
]
 
=
 
c
o
n
v
e
r
t
_
s
t
r
i
n
g
s
_
t
o
_
n
u
m
b
e
r
s
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
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
v
a
l
u
e
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
[
i
]
 
=
 
c
o
n
v
e
r
t
_
s
t
r
i
n
g
s
_
t
o
_
n
u
m
b
e
r
s
(
v
a
l
u
e
)


 
 
 
 
r
e
t
u
r
n
 
d
a
t
a






d
e
f
 
c
o
n
v
e
r
t
_
n
u
m
b
e
r
s
_
t
o
_
s
t
r
i
n
g
s
(
d
a
t
a
:
 
U
n
i
o
n
[
D
i
c
t
,
 
L
i
s
t
]
)
 
-
>
 
U
n
i
o
n
[
D
i
c
t
,
 
L
i
s
t
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
 
n
u
m
b
e
r
s
 
i
n
 
n
e
s
t
e
d
 
s
t
r
u
c
t
u
r
e
s
 
(
e
.
g
.
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
a
r
r
a
y
s
)
 
t
o
 
s
t
r
i
n
g
s
 
a
s
 
m
u
c
h
 
a
s
 
p
o
s
s
i
b
l
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
(
U
n
i
o
n
[
D
i
c
t
,
L
i
s
t
]
)
:
 
b
e
f
o
r
e
 
c
o
n
v
e
r
t
 
d
a
t
a




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
U
n
i
o
n
[
D
i
c
t
,
L
i
s
t
]
:
 
a
f
t
e
r
 
c
o
n
v
e
r
t
 
d
a
t
a


 
 
 
 
"
"
"


 
 
 
 
i
f
 
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
d
a
t
a
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
k
e
y
,
 
v
a
l
u
e
 
i
n
 
d
a
t
a
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
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
v
a
l
u
e
,
 
i
n
t
)
 
o
r
 
i
s
import unittest


class TestConvertStringsToNumbers(unittest.TestCase):

    def test_flat_dict(self):
        data = {'a': '1', 'b': '2.5', 'c': 'not a number'}
        expected = {'a': 1, 'b': 2.5, 'c': 'not a number'}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_nested_dict(self):
        data = {'x': {'y': '10', 'z': '3.14'}, 'w': '20.0'}
        expected = {'x': {'y': 10, 'z': 3.14}, 'w': 20.0}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_list_of_strings(self):
        data = ['1', '2.5', '3', 'invalid']
        expected = [1, 2.5, 3, 'invalid']
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_mixed_structure(self):
        data = {'numbers': ['1', '2.0', 3], 'more_numbers': [{'num': '4'}, '5']}
        expected = {'numbers': [1, 2.0, 3], 'more_numbers': [{'num': 4}, 5]}
        self.assertEqual(convert_strings_to_numbers(data), expected)

    def test_empty_structure(self):
        data = {}
        expected = {}
        self.assertEqual(convert_strings_to_numbers(data), expected)
if __name__ == '__main__':
    unittest.main()