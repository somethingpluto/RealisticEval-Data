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
,
 
L
i
s
t






d
e
f
 
s
a
n
i
t
i
z
e
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
,
 
k
e
y
_
t
o
_
r
e
m
o
v
e
:
 
L
i
s
t
 
=
 
N
o
n
e
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


 
 
 
 
r
e
m
o
v
e
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
s
e
n
s
i
t
i
v
e
 
q
u
e
s
t
i
o
n
 
i
n
 
t
h
e
 
g
i
v
e
n
 
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
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
k
e
y
_
t
o
_
r
e
m
o
v
e
 
l
i
s
t




 
 
 
 
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
 
o
r
i
g
i
n
a
l
 
q
u
e
s
t
i
o
n
 
d
i
c
t


 
 
 
 
 
 
 
 
k
e
y
_
t
o
_
r
e
m
o
v
e
 
(
L
i
s
t
)
:
 
k
e
y
_
t
o
_
r
e
m
o
v
e
 
l
i
s
t




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
D
i
c
t
:
 
r
e
m
o
v
e
d
 
d
i
c
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
k
e
y
_
t
o
_
r
e
m
o
v
e
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
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




 
 
 
 
f
o
r
 
k
e
y
 
i
n
 
k
e
y
_
t
o
_
r
e
m
o
v
e
:


 
 
 
 
 
 
 
 
i
f
 
k
e
y
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
 
 
 
 
d
e
l
 
d
a
t
a
[
k
e
y
]




 
 
 
 
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
 
g
e
t
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
t
y
p
e
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
y
p
e
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
d
a
t
a




 
 
 
 
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
 
o
r
i
g
i
n
a
l
 
q
u
e
s
t
i
o
n
 
d
i
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


 
 
 
 
 
 
 
 
s
t
r
:
 
q
u
e
s
t
i
o
n
 
t
y
p
e


 
 
 
 
"
"
"


 
 
 
 
i
f
 
"
q
u
e
s
t
i
o
n
_
t
y
p
e
"
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
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
[
"
q
u
e
s
t
i
o
n
_
t
y
p
e
"
]




 
 
 
 
i
f
 
"
q
u
e
s
t
i
o
n
_
t
y
p
e
_
d
e
t
a
i
l
"
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
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
[
"
q
u
e
s
t
i
o
n
_
t
y
p
e
_
d
e
t
a
i
l
"
]




 
 
 
 
r
e
t
u
r
n
 
"
"






d
e
f
 
g
e
t
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
i
d
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
i
d
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
d
a
t
a




 
 
 
 
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
 
o
r
i
g
i
n
a
l
 
q
u
e
s
t
i
o
n
 
d
i
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


 
 
 
 
 
 
 
 
s
t
r
:
 
q
u
e
s
t
i
o
n
 
i
d


 
 
 
 
"
"
"


 
 
 
 
i
f
 
"
q
u
e
s
t
i
o
n
_
i
d
"
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
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
[
"
q
u
e
s
t
i
o
n
_
i
d
"
]




 
 
 
 
r
e
t
u
r
n
 
"
"






d
e
f
 
g
e
t
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
t
e
x
t
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
d
a
t
a




 
 
 
 
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
 
o
r
i
g
i
n
a
l
 
q
u
e
s
t
i
o
n
 
d
i
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


 
 
 
 
 
 
 
 
s
t
r
:
 
q
u
e
s
t
i
o
n
 
t
e
x
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
"
q
u
e
s
t
i
o
n
_
t
e
x
t
"
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
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
[
"
q
u
e
s
t
i
o
n
_
t
e
x
t
"
]




 
 
 
 
r
e
t
u
r
n
 
"
"






d
e
f
 
g
e
t
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
t
e
x
t
_
z
h
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
 
t
h
e
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
i
n
 
C
h
i
n
e
s
e
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
d
a
t
a




 
 
 
 
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
 
o
r
i
g
i
n
a
l
 
q
u
e
s
t
i
o
n
 
d
i
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


 
 
 
 
 
 
 
 
s
t
r
:
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
i
n
 
C
h
i
n
e
s
e


 
 
 
 
"
"
"


 
 
 
 
i
f
 
"
q
u
e
s
t
i
o
n
_
t
e
x
t
_
z
h
"
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
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
[
"
q
u
e
s
t
i
o
n
_
t
e
x
t
_
z
h
"
]




 
 
 
 
r
e
t
u
r
n
 
"
"






import unittest


class TestSanitizeData(unittest.TestCase):
    def test_empty_dict(self):
        """ Test with an empty dictionary. """
        data = {}
        key_to_remove = ["email", "metadata"]

        expected = {}
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

    def test_remove_default_keys(self):
        """ Test removing default keys from a nested structure. """
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "metadata": {"submitted_at": "2021-07-10", "status": "pending"},
            "comments": ["Good", "Needs review"]
        }
        key_to_remove = ["email", "metadata"]
        expected = {
            "name": "John Doe",
            "comments": ["Good", "Needs review"]
        }
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

    def test_specified_key_to_remove(self):
        """ Test removing a specified key from the dictionary. """
        data = {
            "name": "John Doe",
            "location": "Earth",
            "email": "johndoe@example.com"
        }
        expected = {
            "name": "John Doe",
            "location": "Earth"
        }
        self.assertEqual(sanitize_data(data, key_to_remove=["email"]), expected)
if __name__ == '__main__':
    unittest.main()