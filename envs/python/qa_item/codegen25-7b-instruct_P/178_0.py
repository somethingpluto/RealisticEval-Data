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
i
n
d
_
l
o
n
g
e
s
t
_
n
o
n
_
d
e
c
r
e
a
s
i
n
g
_
s
u
b
s
e
q
u
e
n
c
e
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"
F
i
n
d
 
t
h
e
 
l
o
n
g
e
s
t
 
n
o
n
-
d
e
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
e
n
c
e
 
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
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
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
i
n
t
]
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
 
l
o
n
g
e
s
t
 
n
o
n
-
d
e
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
e
n
c
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
n
u
m
s
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
n
 
=
 
l
e
n
(
n
u
m
s
)


 
 
 
 
d
p
 
=
 
[
1
]
 
*
 
n


 
 
 
 
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
1
,
 
n
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
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
u
m
s
[
i
]
 
>
 
n
u
m
s
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
p
[
i
]
 
=
 
m
a
x
(
d
p
[
i
]
,
 
d
p
[
j
]
 
+
 
1
)




 
 
 
 
m
a
x
_
l
e
n
 
=
 
m
a
x
(
d
p
)


 
 
 
 
r
e
t
u
r
n
 
[
n
u
m
s
[
i
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
n
)
 
i
f
 
d
p
[
i
]
 
=
=
 
m
a
x
_
l
e
n
]






d
e
f
 
f
i
n
d
_
l
o
n
g
e
s
t
_
i
n
c
r
e
a
s
i
n
g
_
s
u
b
s
e
q
u
e
n
c
e
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"
F
i
n
d
 
t
h
e
 
l
o
n
g
e
s
t
 
i
n
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
e
n
c
e
 
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
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
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
i
n
t
]
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
 
l
o
n
g
e
s
t
 
i
n
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
e
n
c
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
n
u
m
s
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
n
 
=
 
l
e
n
(
n
u
m
s
)


 
 
 
 
d
p
 
=
 
[
1
]
 
*
 
n


 
 
 
 
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
1
,
 
n
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
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
u
m
s
[
i
]
 
>
 
n
u
m
s
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
p
[
i
]
 
=
 
m
a
x
(
d
p
[
i
]
,
 
d
p
[
j
]
 
+
 
1
)




 
 
 
 
m
a
x
_
l
e
n
 
=
 
m
a
x
(
d
p
)


 
 
 
 
r
e
t
u
r
n
 
[
n
u
m
s
[
i
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
n
)
 
i
f
 
d
p
[
i
]
 
=
=
 
m
a
x
_
l
e
n
]






d
e
f
 
f
i
n
d
_
l
o
n
g
e
s
t
_
i
n
c
r
e
a
s
i
n
g
_
s
u
b
s
e
q
u
e
n
c
e
_
w
i
t
h
_
d
u
p
l
i
c
a
t
e
s
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"
F
i
n
d
 
t
h
e
 
l
o
n
g
e
s
t
 
i
n
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
e
n
c
e
 
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
 
l
i
s
t
 
w
i
t
h
 
d
u
p
l
i
c
a
t
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
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
i
n
t
]
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
 
l
o
n
g
e
s
t
 
i
n
c
r
e
a
s
i
n
g
 
s
u
b
s
e
q
u
import unittest
from typing import List


class TestAnswer(unittest.TestCase):

    def test_non_decreasing_sequence(self):
        nums = [5, 7, 4, 8, 6, 10, 2, 11]
        expected: List[int] = [5, 7, 8, 10, 11]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_all_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected: List[int] = [1, 2, 3, 4, 5]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_all_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected: List[int] = [5]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_single_element(self):
        nums = [10]
        expected: List[int] = [10]
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))

    def test_empty_array(self):
        nums = []
        expected: List[int] = []
        self.assertEqual(expected, find_longest_non_decreasing_subsequence(nums))
if __name__ == '__main__':
    unittest.main()