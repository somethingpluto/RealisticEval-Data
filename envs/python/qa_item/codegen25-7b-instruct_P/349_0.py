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
 
A
n
y






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
i
n
p
u
t
_
l
i
s
t
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
A
n
y
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
A
n
y
]
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
l
l
 
p
o
s
s
i
b
l
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
s
 
o
f
 
e
l
e
m
e
n
t
s
 
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
.


 
 
 
 
E
a
c
h
 
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
 
c
o
n
s
i
s
t
s
 
o
f
 
p
i
c
k
i
n
g
 
e
x
a
c
t
l
y
 
o
n
e
 
e
l
e
m
e
n
t
 
f
r
o
m
 
e
a
c
h
 
l
i
s
t
 
i
n
 
t
h
e
 
i
n
p
u
t
 
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


 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
u
s
e
f
u
l
 
f
o
r
 
g
e
n
e
r
a
t
i
n
g
 
p
r
o
d
u
c
t
 
v
a
r
i
a
t
i
o
n
s
,
 
s
c
e
n
a
r
i
o
s
 
i
n
 
d
e
c
i
s
i
o
n
-
m
a
k
i
n
g
 
t
o
o
l
s
,


 
 
 
 
o
r
 
a
n
y
 
c
o
n
t
e
x
t
 
w
h
e
r
e
 
a
l
l
 
p
o
s
s
i
b
l
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
s
 
o
f
 
a
 
s
e
t
 
o
f
 
o
p
t
i
o
n
s
 
n
e
e
d
 
t
o
 
b
e
 
e
x
p
l
o
r
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
l
i
s
t
s
 
(
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
A
n
y
]
]
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
 
e
l
e
m
e
n
t
s
 
t
o
 
c
o
m
b
i
n
e
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
s
 
m
u
s
t
 
n
o
t
 
b
e
 
e
m
p
t
y
 
b
u
t
 
c
a
n
 
c
o
n
t
a
i
n
 
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
 
a
n
y
 
t
y
p
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
A
n
y
]
]
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
 
i
n
n
e
r
 
l
i
s
t
 
r
e
p
r
e
s
e
n
t
s
 
a
 
p
o
s
s
i
b
l
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
 
e
l
e
m
e
n
t
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
a
k
e
n
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
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
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
i
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
i
s
 
e
m
p
t
y
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
i
n
p
u
t
_
l
i
s
t
s
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]


 
 
 
 
e
l
i
f
 
l
e
n
(
i
n
p
u
t
_
l
i
s
t
s
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
_
l
i
s
t
s
[
0
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
x
 
+
 
y
 
f
o
r
 
x
 
i
n
 
i
n
p
u
t
_
l
i
s
t
s
[
0
]
 
f
o
r
 
y
 
i
n
 
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
i
n
p
u
t
_
l
i
s
t
s
[
1
:
]
)
]






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
i
n
p
u
t
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
A
n
y
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
A
n
y
]
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
l
l
 
p
o
s
s
i
b
l
e
 
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
 
e
l
e
m
e
n
t
s
 
i
n
 
a
 
l
i
s
t
.


 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
u
s
e
f
u
l
 
f
o
r
 
g
e
n
e
r
a
t
i
n
g
 
s
c
e
n
a
r
i
o
s
 
i
n
 
d
e
c
i
s
i
o
n
-
m
a
k
i
n
g
 
t
o
o
l
s
,


 
 
 
 
o
r
 
a
n
y
 
c
o
n
t
e
x
t
 
w
h
e
r
e
 
a
l
l
 
p
o
s
s
i
b
l
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
s
 
o
f
 
a
 
s
e
t
 
o
f
 
o
p
t
i
o
n
s
 
n
e
e
d
 
t
o
 
b
e
 
e
x
p
l
o
r
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
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
A
n
y
]
)
:
 
A
 
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
 
t
h
e
 
e
l
e
m
e
n
t
s
 
t
o
 
p
e
r
m
u
t
e
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
m
u
s
t
 
n
o
t
 
b
e
 
e
m
p
t
y
 
b
u
t
 
c
a
n
 
c
o
n
t
a
i
n
 
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
 
a
n
y
 
t
y
p
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
A
n
y
]
]
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
 
i
n
n
e
r
 
l
i
s
t
 
r
e
p
r
e
s
e
n
t
s
 
a
 
p
o
s
s
i
b
l
e
 
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
 
o
f
 
e
l
e
m
e
n
t
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
a
k
e
n
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
.
 
R
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
i
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
i
s
 
e
m
p
t
y
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
i
n
p
u
t
_
l
i
s
t
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]


 
 
 
 
e
l
i
f
 
l
e
n
(
i
n
p
u
t
_
l
i
s
t
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
i
n
p
u
t
_
l
i
s
t
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
x
 
+
 
[
y
]
 
f
o
r
 
x
 
i
n
 
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
i
n
p
u
t
_
l
i
s
t
[
1
:
]
)
 
f
o
r
 
y
import unittest
from typing import List


class TestGenerateCombinations(unittest.TestCase):

    def test_empty_input(self):
        input_data: List[List[str]] = []
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with empty input")

    def test_single_empty_list(self):
        input_data: List[List[str]] = [[]]  # Equivalent to Arrays.asList(new ArrayList<>())
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with a single empty list")

    def test_single_non_empty_list(self):
        input_data: List[List[str]] = [["a", "b", "c"]]  # Equivalent to Arrays.asList(Arrays.asList("a", "b", "c"))
        expected: List[List[str]] = [["a"], ["b"], ["c"]]
        self.assertEqual(generate_combinations(input_data), expected, "Testing with a single non-empty list")

    def test_multiple_lists(self):
        input_data: List[List[str]] = [["a", "b"], ["1", "2"]]  # Equivalent to Arrays.asList(Arrays.asList("a", "b"), Arrays.asList("1", "2"))
        expected: List[List[str]] = [["a", "1"], ["a", "2"], ["b", "1"], ["b", "2"]]
        self.assertEqual(generate_combinations(input_data), expected, "Testing with multiple lists")

    def test_input_containing_empty_list(self):
        input_data: List[List[str]] = [["a", "b"], [], ["1", "2"]]  # Equivalent to the Java example
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with an input that contains an empty list")

if __name__ == '__main__':
    unittest.main()