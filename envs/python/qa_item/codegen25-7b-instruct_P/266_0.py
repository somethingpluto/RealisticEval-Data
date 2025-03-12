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
 
h
a
n
d
l
e
_
n
e
s
t
e
d
_
d
a
t
a
(
d
a
t
a
:
 
D
i
c
t
)
 
-
>
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
h
a
n
d
l
e
 
n
e
s
t
e
d
 
q
u
e
s
t
i
o
n
 
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
,
 
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
 
l
i
s
t
s
,
 
a
n
d
 
e
n
u
m
e
r
a
t
i
o
n
s
)
,
 
d
e
c
o
d
e
 
b
y
t
e
s
 
t
o
 
U
T
F
8
-
s
t
r
i
n
g
s
,
 
a
n
d
 
c
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
 
t
o
 
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
D
i
c
t
)
:
 
q
u
e
s
t
i
o
n
 
o
b
j
e
c
t




 
 
 
 
R
e
t
u
r
n
s
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
e
d
 
q
u
e
s
t
i
o
n


 
 
 
 
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
 
b
y
t
e
s
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
 
v
a
l
u
e
.
d
e
c
o
d
e
(
"
u
t
f
-
8
"
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
v
a
l
u
e
)
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
[
i
]
,
 
b
y
t
e
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
[
i
]
 
=
 
v
a
l
u
e
[
i
]
.
d
e
c
o
d
e
(
"
u
t
f
-
8
"
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
[
i
]
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
[
i
]
 
=
 
h
a
n
d
l
e
_
n
e
s
t
e
d
_
d
a
t
a
(
v
a
l
u
e
[
i
]
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
[
i
]
,
 
i
n
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
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
[
i
]
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
 
h
a
n
d
l
e
_
n
e
s
t
e
d
_
d
a
t
a
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
 
i
n
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
 
h
a
n
d
l
e
_
q
u
e
s
t
i
o
n
_
d
a
t
a
(
d
a
t
a
:
 
D
i
c
t
)
 
-
>
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
h
a
n
d
l
e
 
q
u
e
s
t
i
o
n
 
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
,
 
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
 
l
i
s
t
s
,
 
a
n
d
 
e
n
u
m
e
r
a
t
i
o
n
s
)
,
 
d
e
c
o
d
e
 
b
y
t
e
s
 
t
o
 
U
T
F
8
-
s
t
r
i
n
g
s
,
 
a
n
d
 
c
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
 
t
o
 
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
D
i
c
t
)
:
 
q
u
e
s
t
i
o
n
 
o
b
j
e
c
t




 
 
 
 
R
e
t
u
r
n
s
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
e
d
 
q
u
e
s
t
i
o
n


 
 
 
 
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
 
b
y
t
e
s
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
 
v
a
l
u
e
.
d
e
c
o
d
e
(
"
u
t
f
-
8
"
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
v
a
l
u
e
)
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
[
i
]
,
 
b
y
t
e
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
[
i
]
 
=
 
v
a
l
u
e
[
i
]
.
d
e
c
o
d
e
(
"
u
t
f
-
8
"
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
[
i
]
,
 
i
n
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
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
[
i
]
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
import unittest
from enum import Enum
from numbers import Number


class TestHandleNestedData(unittest.TestCase):
    def test_simple_dictionary(self):
        data = {"name": b"Alice", "age": "30"}
        expected = {"name": "Alice", "age": 30}
        self.assertEqual(handle_nested_data(data), expected)

    def test_nested_dictionary(self):
        data = {"user": {"name": b"Bob", "details": {"age": "25", "height": "175.5"}}}
        expected = {"user": {"name": "Bob", "details": {"age": 25, "height": 175.5}}}
        self.assertEqual(handle_nested_data(data), expected)

    def test_list_of_mixed_data_types(self):
        data = ["100", b"200", 300.0, "400.5"]
        expected = [100, "200", 300.0, 400.5]
        self.assertEqual(handle_nested_data(data), expected)

    def test_incorrect_byte_decoding(self):
        data = {"invalid_bytes": b"\xff\xfe\xfd\xfc"}
        with self.assertRaises(UnicodeDecodeError):
            handle_nested_data(data)

    def test_complex_nested_structure(self):
        data = {
            "team": [
                {"name": b"Charlie", "scores": ["1000", "2000.2"]},
                {"name": b"Daisy", "skills": [b"Coding", "Design"], "age": "22"}
            ]
        }
        expected = {
            "team": [
                {"name": "Charlie", "scores": [1000, 2000.2]},
                {"name": "Daisy", "skills": ["Coding", "Design"], "age": 22}
            ]
        }
        self.assertEqual(handle_nested_data(data), expected)
if __name__ == '__main__':
    unittest.main()