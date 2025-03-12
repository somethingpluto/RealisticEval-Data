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
 
f
l
a
t
t
e
n
_
a
r
r
a
y
(
m
u
l
t
i
_
d
i
m
_
a
r
r
a
y
:
 
L
i
s
t
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


 
 
 
 
c
o
n
v
e
r
t
 
a
 
m
u
l
t
i
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
i
n
t
o
 
a
 
o
n
e
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
u
l
t
i
_
d
i
m
_
a
r
r
a
y
 
(
L
i
s
t
)
:
 
A
 
m
u
l
t
i
-
d
i
m
e
n
s
i
o
n
a
l
 
l
i
s
t
 
(
n
e
s
t
e
d
 
l
i
s
t
)
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
 
A
 
o
n
e
-
d
i
m
e
n
s
i
o
n
a
l
 
l
i
s
t
 
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
 
a
l
l
 
e
l
e
m
e
n
t
s
 
o
f
 
t
h
e
 
i
n
p
u
t
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
e
l
e
m
e
n
t
 
f
o
r
 
r
o
w
 
i
n
 
m
u
l
t
i
_
d
i
m
_
a
r
r
a
y
 
f
o
r
 
e
l
e
m
e
n
t
 
i
n
 
r
o
w
]






d
e
f
 
g
e
t
_
s
u
b
_
l
i
s
t
s
(
l
s
t
:
 
L
i
s
t
,
 
n
:
 
i
n
t
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


 
 
 
 
g
e
t
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
 
f
r
o
m
 
a
 
l
i
s
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
s
t
 
(
L
i
s
t
)
:
 
A
 
l
i
s
t
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
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
 
s
u
b
 
l
i
s
t
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
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
l
s
t
[
i
:
i
 
+
 
n
]
 
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
l
s
t
)
 
-
 
n
 
+
 
1
)
]






d
e
f
 
g
e
t
_
s
u
b
_
l
i
s
t
s
_
o
f
_
l
e
n
g
t
h
_
n
(
l
s
t
:
 
L
i
s
t
,
 
n
:
 
i
n
t
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


 
 
 
 
g
e
t
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
 
f
r
o
m
 
a
 
l
i
s
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
s
t
 
(
L
i
s
t
)
:
 
A
 
l
i
s
t
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
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
 
s
u
b
 
l
i
s
t
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
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
l
s
t
[
i
:
i
 
+
 
n
]
 
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
l
s
t
)
 
-
 
n
 
+
 
1
)
]






d
e
f
 
g
e
t
_
s
u
b
_
l
i
s
t
s
_
o
f
_
l
e
n
g
t
h
_
n
_
f
r
o
m
_
l
i
s
t
_
o
f
_
l
i
s
t
s
(
l
s
t
:
 
L
i
s
t
,
 
n
:
 
i
n
t
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


 
 
 
 
g
e
t
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
 
f
r
o
m
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
s
t
 
(
L
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
l
i
s
t
s
.


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
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
 
s
u
b
 
l
i
s
t
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
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
l
i
s
t
 
f
o
r
 
s
u
b
l
i
s
t
 
i
n
 
l
s
t
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
n
)
]






d
e
f
 
g
e
t
_
s
u
b
_
l
i
s
t
s
_
o
f
_
l
e
n
g
t
h
_
n
_
f
r
o
m
_
l
i
s
t
_
o
f
_
l
i
s
t
s
_
o
f
_
l
i
s
t
s
(
l
s
t
:
 
L
i
s
t
,
 
n
:
 
i
n
t
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


 
 
 
 
g
e
t
 
s
u
b
 
l
i
s
t
s
 
o
f
 
l
e
n
g
t
h
 
n
 
f
r
o
m
 
a
 
l
i
s
t
 
o
f
 
l
i
s
t
s
 
o
f
 
l
i
s
t
s


import unittest


class TestFlattenArray(unittest.TestCase):
    def test_deeply_nested_array(self):
        """Test a deeply nested array."""
        nested_array = [1, [2, [3, [4, [5]]]]]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_array(nested_array), expected_result)

    def test_mixed_types(self):
        """Test an array with mixed question types."""
        mixed_array = ["a", ["b", 2, [True, [3.14]]], False]
        expected_result = ["a", "b", 2, True, 3.14, False]
        self.assertEqual(flatten_array(mixed_array), expected_result)

    def test_empty_array(self):
        """Test an empty array."""
        empty_array = []
        expected_result = []
        self.assertEqual(flatten_array(empty_array), expected_result)

    def test_array_with_empty_subarrays(self):
        """Test an array that includes empty subarrays."""
        complex_array = [1, [], [2, [], 3], [4, [5, [], 6], 7], []]
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_array(complex_array), expected_result)

    def test_no_nested_array(self):
        """Test an array that has no nested structure."""
        flat_array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_array(flat_array), expected_result)

if __name__ == '__main__':
    unittest.main()