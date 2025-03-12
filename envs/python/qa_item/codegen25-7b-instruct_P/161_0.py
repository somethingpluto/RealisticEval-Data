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
 
g
e
n
e
r
a
t
e
_
c
o
m
b
i
n
a
t
i
o
n
s
(
m
a
p
:
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
i
n
t
]
]
)
 
-
>
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
l
l
 
c
o
m
b
i
n
a
t
i
o
n
s
 
o
f
 
n
u
m
e
r
i
c
 
a
r
r
a
y
s
 
f
o
r
 
e
a
c
h
 
k
e
y
 
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
 
m
a
p
 
o
b
j
e
c
t
 
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
m
 
a
s
 
a
 
t
w
o
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
p
 
(
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
i
n
t
]
]
)
:
 
A
 
m
a
p
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
i
s
 
a
 
s
t
r
i
n
g
,
 
a
n
d
 
e
a
c
h
 
v
a
l
u
e
 
i
s
 
a
n
 
a
r
r
a
y
 
o
f
 
n
u
m
b
e
r
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


 
 
 
 
 
 
 
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
:
 
A
n
 
a
r
r
a
y
 
o
f
 
a
r
r
a
y
s
,
 
w
h
e
r
e
 
e
a
c
h
 
s
u
b
-
a
r
r
a
y
 
i
s
 
a
 
u
n
i
q
u
e
 
c
o
m
b
i
n
a
t
i
o
n
 
o
f
 
n
u
m
b
e
r
s
 
f
r
o
m
 
t
h
e
 
m
a
p
'
s
 
v
a
l
u
e
s
.


 
 
 
 
"
"
"


 
 
 
 
c
o
m
b
i
n
a
t
i
o
n
s
 
=
 
[
]


 
 
 
 
f
o
r
 
k
e
y
 
i
n
 
m
a
p
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
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
i
 
+
 
1
,
 
l
e
n
(
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
k
 
i
n
 
r
a
n
g
e
(
j
 
+
 
1
,
 
l
e
n
(
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
m
b
i
n
a
t
i
o
n
s
.
a
p
p
e
n
d
(
[
m
a
p
[
k
e
y
]
[
i
]
,
 
m
a
p
[
k
e
y
]
[
j
]
,
 
m
a
p
[
k
e
y
]
[
k
]
]
)


 
 
 
 
r
e
t
u
r
n
 
c
o
m
b
i
n
a
t
i
o
n
s






d
e
f
 
g
e
n
e
r
a
t
e
_
c
o
m
b
i
n
a
t
i
o
n
s
_
w
i
t
h
_
r
e
p
l
a
c
e
m
e
n
t
(
m
a
p
:
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
i
n
t
]
]
)
 
-
>
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
l
l
 
c
o
m
b
i
n
a
t
i
o
n
s
 
o
f
 
n
u
m
e
r
i
c
 
a
r
r
a
y
s
 
f
o
r
 
e
a
c
h
 
k
e
y
 
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
 
m
a
p
 
o
b
j
e
c
t
 
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
m
 
a
s
 
a
 
t
w
o
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
p
 
(
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
i
n
t
]
]
)
:
 
A
 
m
a
p
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
i
s
 
a
 
s
t
r
i
n
g
,
 
a
n
d
 
e
a
c
h
 
v
a
l
u
e
 
i
s
 
a
n
 
a
r
r
a
y
 
o
f
 
n
u
m
b
e
r
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


 
 
 
 
 
 
 
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
:
 
A
n
 
a
r
r
a
y
 
o
f
 
a
r
r
a
y
s
,
 
w
h
e
r
e
 
e
a
c
h
 
s
u
b
-
a
r
r
a
y
 
i
s
 
a
 
u
n
i
q
u
e
 
c
o
m
b
i
n
a
t
i
o
n
 
o
f
 
n
u
m
b
e
r
s
 
f
r
o
m
 
t
h
e
 
m
a
p
'
s
 
v
a
l
u
e
s
.


 
 
 
 
"
"
"


 
 
 
 
c
o
m
b
i
n
a
t
i
o
n
s
 
=
 
[
]


 
 
 
 
f
o
r
 
k
e
y
 
i
n
 
m
a
p
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
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
i
 
+
 
1
,
 
l
e
n
(
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
k
 
i
n
 
r
a
n
g
e
(
j
 
+
 
1
,
 
l
e
n
(
m
a
p
[
k
e
y
]
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
m
b
i
n
a
t
i
o
n
s
.
a
p
p
e
n
d
(
[
m
a
p
[
k
e
y
]
[
i
]
,
 
m
a
p
[
k
e
y
]
[
j
]
,
 
m
a
p
[
k
e
y
]
[
k
]
]
)


 
 
 
 
r
e
t
u
r
n
 
c
o
m
b
i
n
a
t
i
o
n
s






d
e
f
 
g
e
n
e
r
a
t
e
_
p
e
r
m
u
t
a
t
i
o
n
s
(
m
a
p
:
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
i
n
t
]
]
)
 
-
>
 
L
i
s
t
[
L
i
s
t
[
i
n
t
]
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
l
l
 
p
e
r
m
u
t
a
t
i
o
n
s
 
o
f
 
n
u
m
e
r
i
c
 
a
r
r
a
y
s
 
f
o
r
 
e
a
c
h
 
k
e
y
 
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
 
m
a
p
 
o
b
j
e
c
t
 
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
m
import unittest


class TestGenerateCombinations(unittest.TestCase):

    def test_single_key_multiple_values(self):
        # Test: generates combinations for a single key with multiple values
        map_data = {'a': [1, 2, 3]}
        expected = [[1], [2], [3]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_multiple_keys_single_values(self):
        # Test: generates combinations for multiple keys with single values
        map_data = {'a': [1], 'b': [2]}
        expected = [[1, 2]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_multiple_keys_multiple_values(self):
        # Test: generates combinations for multiple keys with multiple values
        map_data = {'a': [1, 2], 'b': [3, 4]}
        expected = [
            [1, 3], [1, 4],
            [2, 3], [2, 4]
        ]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_empty_map(self):
        # Test: handles an empty map
        map_data = {}
        expected = [[]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_empty_array_values(self):
        # Test: handles keys with empty arrays as values
        map_data = {'a': [], 'b': [1, 2]}
        expected = []
        self.assertEqual(generate_combinations(map_data), expected)

if __name__ == '__main__':
    unittest.main()