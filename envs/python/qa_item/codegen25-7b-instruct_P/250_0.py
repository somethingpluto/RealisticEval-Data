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
 
i
n
v
e
r
t
_
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
(
o
r
i
g
i
n
a
l
_
d
i
c
t
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


 
 
 
 
I
n
v
e
r
t
 
t
h
e
 
k
e
y
s
 
a
n
d
 
v
a
l
u
e
s
 
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
.
 
I
f
 
m
u
l
t
i
p
l
e
 
k
e
y
s
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
v
a
l
u
e
,


 
 
 
 
t
h
e
 
n
e
w
 
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
'
s
 
v
a
l
u
e
s
 
w
i
l
l
 
b
e
 
a
 
l
i
s
t
 
o
f
 
t
h
e
s
e
 
k
e
y
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
d
i
c
t
 
(
d
i
c
t
)
:
 
T
h
e
 
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
 
t
o
 
i
n
v
e
r
t
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
 
n
e
w
 
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
 
w
i
t
h
 
v
a
l
u
e
s
 
a
n
d
 
k
e
y
s
 
i
n
v
e
r
t
e
d
.


 
 
 
 
"
"
"


 
 
 
 
i
n
v
e
r
t
e
d
_
d
i
c
t
 
=
 
{
}


 
 
 
 
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
 
o
r
i
g
i
n
a
l
_
d
i
c
t
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
 
v
a
l
u
e
 
n
o
t
 
i
n
 
i
n
v
e
r
t
e
d
_
d
i
c
t
:


 
 
 
 
 
 
 
 
 
 
 
 
i
n
v
e
r
t
e
d
_
d
i
c
t
[
v
a
l
u
e
]
 
=
 
[
k
e
y
]


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
i
n
v
e
r
t
e
d
_
d
i
c
t
[
v
a
l
u
e
]
.
a
p
p
e
n
d
(
k
e
y
)


 
 
 
 
r
e
t
u
r
n
 
i
n
v
e
r
t
e
d
_
d
i
c
t






d
e
f
 
g
e
t
_
a
l
l
_
s
u
b
c
l
a
s
s
e
s
(
c
l
s
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
a
 
c
l
a
s
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
l
s
 
(
c
l
a
s
s
)
:
 
T
h
e
 
c
l
a
s
s
 
t
o
 
g
e
t
 
s
u
b
c
l
a
s
s
e
s
 
o
f
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
 
l
i
s
t
 
o
f
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
c
l
a
s
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
c
l
s
.
_
_
s
u
b
c
l
a
s
s
e
s
_
_
(
)
 
+
 
[


 
 
 
 
 
 
 
 
g
 
f
o
r
 
s
 
i
n
 
c
l
s
.
_
_
s
u
b
c
l
a
s
s
e
s
_
_
(
)
 
f
o
r
 
g
 
i
n
 
g
e
t
_
a
l
l
_
s
u
b
c
l
a
s
s
e
s
(
s
)


 
 
 
 
]






d
e
f
 
g
e
t
_
a
l
l
_
s
u
b
c
l
a
s
s
e
s
_
o
f
_
t
y
p
e
(
c
l
s
,
 
t
y
p
e
_
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
a
 
c
l
a
s
s
 
t
h
a
t
 
a
r
e
 
o
f
 
a
 
c
e
r
t
a
i
n
 
t
y
p
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
l
s
 
(
c
l
a
s
s
)
:
 
T
h
e
 
c
l
a
s
s
 
t
o
 
g
e
t
 
s
u
b
c
l
a
s
s
e
s
 
o
f
.


 
 
 
 
 
 
 
 
t
y
p
e
_
 
(
t
y
p
e
)
:
 
T
h
e
 
t
y
p
e
 
t
o
 
f
i
l
t
e
r
 
s
u
b
c
l
a
s
s
e
s
 
b
y
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
 
l
i
s
t
 
o
f
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
c
l
a
s
s
 
t
h
a
t
 
a
r
e
 
o
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
y
p
e
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
[
s
u
b
c
l
a
s
s
 
f
o
r
 
s
u
b
c
l
a
s
s
 
i
n
 
g
e
t
_
a
l
l
_
s
u
b
c
l
a
s
s
e
s
(
c
l
s
)
 
i
f
 
i
s
s
u
b
c
l
a
s
s
(
s
u
b
c
l
a
s
s
,
 
t
y
p
e
_
)
]






d
e
f
 
g
e
t
_
a
l
l
_
s
u
b
c
l
a
s
s
e
s
_
o
f
_
t
y
p
e
_
r
e
c
u
r
s
i
v
e
l
y
(
c
l
s
,
 
t
y
p
e
_
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
a
 
c
l
a
s
s
 
t
h
a
t
 
a
r
e
 
o
f
 
a
 
c
e
r
t
a
i
n
 
t
y
p
e
,
 
i
n
c
l
u
d
i
n
g
 
t
h
o
s
e
 
o
f
 
s
u
b
c
l
a
s
s
e
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
l
s
 
(
c
l
a
s
s
)
:
 
T
h
e
 
c
l
a
s
s
 
t
o
 
g
e
t
 
s
u
b
c
l
a
s
s
e
s
 
o
f
.


 
 
 
 
 
 
 
 
t
y
p
e
_
 
(
t
y
p
e
)
:
 
T
h
e
 
t
y
p
e
 
t
o
 
f
i
l
t
e
r
 
s
u
b
c
l
a
s
s
e
s
 
b
y
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
 
l
i
s
t
 
o
f
 
a
l
l
 
s
u
b
c
l
a
s
s
e
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
c
l
a
s
s
 
t
h
a
t
 
a
r
e
 
o
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
y
p
e
,
 
i
n
c
l
u
d
i
n
g
 
t
h
o
s
e
 
o
f
import unittest


class TestInvertDictionary(unittest.TestCase):

    def test_normal_dictionary(self):
        """Test inversion of a dictionary without duplicate values."""
        original_dict = {'a': 1, 'b': 2, 'c': 3}
        expected = {1: 'a', 2: 'b', 3: 'c'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_dictionary_with_duplicates(self):
        """Test inversion of a dictionary with duplicate values."""
        original_dict = {'a': 1, 'b': 1, 'c': 2}
        expected = {1: ['a', 'b'], 2: 'c'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_empty_dictionary(self):
        """Test inversion of an empty dictionary."""
        original_dict = {}
        expected = {}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_non_string_keys(self):
        """Test inversion of a dictionary with non-string keys."""
        original_dict = {1: 'apple', 2: 'banana', 3: 'apple'}
        expected = {'apple': [1, 3], 'banana': 2}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

    def test_mixed_types(self):
        """Test inversion of a dictionary with mixed key and value types."""
        original_dict = {'a': 1, 2: 'two', 'three': 3}
        expected = {1: 'a', 'two': 2, 3: 'three'}
        result = invert_dictionary(original_dict)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()