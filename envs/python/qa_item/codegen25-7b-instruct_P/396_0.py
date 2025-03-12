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
 
l
e
n
g
t
h
_
o
f
_
L
I
S
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
i
v
e
n
 
a
n
 
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
 
n
u
m
s
,
 
f
i
n
d
 
t
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
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
i
t




 
 
 
 
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
 
i
n
t
 
a
r
r
a
y




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
0




 
 
 
 
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




 
 
 
 
r
e
t
u
r
n
 
m
a
x
(
d
p
)






d
e
f
 
l
e
n
g
t
h
_
o
f
_
L
I
S
_
2
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
i
v
e
n
 
a
n
 
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
 
n
u
m
s
,
 
f
i
n
d
 
t
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
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
i
t




 
 
 
 
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
 
i
n
t
 
a
r
r
a
y




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
0




 
 
 
 
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




 
 
 
 
r
e
t
u
r
n
 
m
a
x
(
d
p
)






d
e
f
 
l
e
n
g
t
h
_
o
f
_
L
I
S
_
3
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
i
v
e
n
 
a
n
 
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
 
n
u
m
s
,
 
f
i
n
d
 
t
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
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
i
t




 
 
 
 
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
 
i
n
t
 
a
r
r
a
y




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
l
o
n
g
e
s
t
 
s
t
r
i
c
t
l
y
 
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
 
0




 
 
 
 
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




 
 
 
 
r
e
t
u
r
n
 
m
a
x
import unittest
from typing import List

class TestLengthOfLIS(unittest.TestCase):

    def test_empty_list(self):
        # Test the function with an empty list
        self.assertEqual(length_of_LIS([]), 0)

    def test_single_element(self):
        # Test with a list containing only one element
        self.assertEqual(length_of_LIS([7]), 1)

    def test_increasing_sequence(self):
        # Test with a list where the elements are strictly increasing
        self.assertEqual(length_of_LIS([1, 2, 3, 4, 5]), 5)

    def test_decreasing_sequence(self):
        # Test with a list where the elements are strictly decreasing
        self.assertEqual(length_of_LIS([5, 4, 3, 2, 1]), 1)

    def test_complex_sequence(self):
        # Test with a complex sequence with mix of increasing and decreasing elements
        self.assertEqual(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_all_equal_elements(self):
        # Test with all elements in the list being equal
        self.assertEqual(length_of_LIS([2, 2, 2, 2]), 1)

    def test_with_negative_numbers(self):
        # Test with a mix of negative and positive numbers
        self.assertEqual(length_of_LIS([-1, -2, -3, 0, 1, 2]), 4)
if __name__ == '__main__':
    unittest.main()