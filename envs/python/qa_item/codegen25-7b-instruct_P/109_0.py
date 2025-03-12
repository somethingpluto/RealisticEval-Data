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
 
U
n
i
o
n
,
 
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
 
O
p
t
i
o
n
a
l






d
e
f
 
g
e
t
_
o
b
j
e
c
t
_
b
y
_
i
d
(
i
d
:
 
U
n
i
o
n
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
 
o
b
j
_
l
i
s
t
:
 
L
i
s
t
[
D
i
c
t
]
)
 
-
>
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
o
b
j
e
c
t
 
f
r
o
m
 
t
h
e
 
l
i
s
t
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
I
D
,
 
o
r
 
N
o
n
e
 
i
f
 
i
t
 
i
s
 
n
o
t
 
p
r
e
s
e
n
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
d
 
(
U
n
i
o
n
[
s
t
r
,
 
i
n
t
]
)
:
 
T
h
e
 
`
i
d
`
 
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
 
i
n
 
t
h
e
 
l
i
s
t
.


 
 
 
 
 
 
 
 
o
b
j
_
l
i
s
t
 
(
L
i
s
t
[
D
i
c
t
]
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
o
b
j
e
c
t
s
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:
 
T
h
e
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
m
a
t
c
h
i
n
g
 
`
i
d
`
,
 
o
r
 
N
o
n
e
 
i
f
 
n
o
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
o
b
j
 
i
n
 
o
b
j
_
l
i
s
t
:


 
 
 
 
 
 
 
 
i
f
 
o
b
j
[
"
i
d
"
]
 
=
=
 
i
d
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
o
b
j


 
 
 
 
r
e
t
u
r
n
 
N
o
n
e






d
e
f
 
g
e
t
_
o
b
j
e
c
t
_
b
y
_
n
a
m
e
(
n
a
m
e
:
 
s
t
r
,
 
o
b
j
_
l
i
s
t
:
 
L
i
s
t
[
D
i
c
t
]
)
 
-
>
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
o
b
j
e
c
t
 
f
r
o
m
 
t
h
e
 
l
i
s
t
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
,
 
o
r
 
N
o
n
e
 
i
f
 
i
t
 
i
s
 
n
o
t
 
p
r
e
s
e
n
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
`
n
a
m
e
`
 
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
 
i
n
 
t
h
e
 
l
i
s
t
.


 
 
 
 
 
 
 
 
o
b
j
_
l
i
s
t
 
(
L
i
s
t
[
D
i
c
t
]
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
o
b
j
e
c
t
s
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:
 
T
h
e
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
m
a
t
c
h
i
n
g
 
`
n
a
m
e
`
,
 
o
r
 
N
o
n
e
 
i
f
 
n
o
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
o
b
j
 
i
n
 
o
b
j
_
l
i
s
t
:


 
 
 
 
 
 
 
 
i
f
 
o
b
j
[
"
n
a
m
e
"
]
 
=
=
 
n
a
m
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
o
b
j


 
 
 
 
r
e
t
u
r
n
 
N
o
n
e






d
e
f
 
g
e
t
_
o
b
j
e
c
t
_
b
y
_
n
a
m
e
_
o
r
_
i
d
(
n
a
m
e
_
o
r
_
i
d
:
 
U
n
i
o
n
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
 
o
b
j
_
l
i
s
t
:
 
L
i
s
t
[
D
i
c
t
]
)
 
-
>
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
o
b
j
e
c
t
 
f
r
o
m
 
t
h
e
 
l
i
s
t
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
 
o
r
 
I
D
,
 
o
r
 
N
o
n
e
 
i
f
 
i
t
 
i
s
 
n
o
t
 
p
r
e
s
e
n
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
a
m
e
_
o
r
_
i
d
 
(
U
n
i
o
n
[
s
t
r
,
 
i
n
t
]
)
:
 
T
h
e
 
`
n
a
m
e
`
 
o
r
 
`
i
d
`
 
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
 
i
n
 
t
h
e
 
l
i
s
t
.


 
 
 
 
 
 
 
 
o
b
j
_
l
i
s
t
 
(
L
i
s
t
[
D
i
c
t
]
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
o
b
j
e
c
t
s
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
D
i
c
t
]
:
 
T
h
e
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
m
a
t
c
h
i
n
g
 
`
n
a
m
e
`
 
o
r
 
`
i
d
`
,
 
o
r
 
N
o
n
e
 
i
f
 
n
o
 
m
a
t
c
h
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
o
b
j
 
i
n
 
o
b
j
_
l
i
s
t
:


 
 
 
 
 
 
 
 
i
f
 
o
b
j
[
"
n
a
m
e
"
]
 
=
=
 
n
a
m
e
_
o
r
_
i
d
 
o
r
 
o
b
j
[
"
i
d
"
]
 
=
=
 
n
a
m
e
import unittest


class TestGetObjectById(unittest.TestCase):

    def test_should_return_object_with_matching_id(self):
        obj_list = [
            {'id': 1, 'name': 'Object 1'},
            {'id': 2, 'name': 'Object 2'},
            {'id': 3, 'name': 'Object 3'}
        ]
        result = get_object_by_id(2, obj_list)
        self.assertEqual(result, {'id': 2, 'name': 'Object 2'})

    def test_should_return_none_if_no_object_with_matching_id(self):
        obj_list = [
            {'id': 1, 'name': 'Object 1'},
            {'id': 2, 'name': 'Object 2'},
            {'id': 3, 'name': 'Object 3'}
        ]
        result = get_object_by_id(4, obj_list)
        self.assertIsNone(result)

    def test_should_return_none_if_list_is_empty(self):
        obj_list = []
        result = get_object_by_id(1, obj_list)
        self.assertIsNone(result)

    def test_should_return_none_if_objects_do_not_have_id_property(self):
        obj_list = [
            {'name': 'Object 1'},
            {'name': 'Object 2'},
            {'name': 'Object 3'}
        ]
        result = get_object_by_id(1, obj_list)
        self.assertIsNone(result)

    def test_should_return_correct_object_when_id_is_string(self):
        obj_list = [
            {'id': 'a', 'name': 'Object A'},
            {'id': 'b', 'name': 'Object B'},
            {'id': 'c', 'name': 'Object C'}
        ]
        result = get_object_by_id('b', obj_list)
        self.assertEqual(result, {'id': 'b', 'name': 'Object B'})

if __name__ == '__main__':
    unittest.main()