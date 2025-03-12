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
 
s
h
e
l
l
_
s
o
r
t
(
a
r
r
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
 
a
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
p
e
r
f
o
r
m
s
 
S
h
e
l
l
 
s
o
r
t
 
o
n
 
a
n
 
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


 
 
 
 
 
 
 
 
a
r
r
 
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
 
a
r
r
a
y
 
t
o
 
b
e
 
s
o
r
t
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
a
r
r
)


 
 
 
 
g
a
p
 
=
 
n
 
/
/
 
2


 
 
 
 
w
h
i
l
e
 
g
a
p
 
>
 
0
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
g
a
p
,
 
n
)
:


 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
 
=
 
a
r
r
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
j
 
=
 
i


 
 
 
 
 
 
 
 
 
 
 
 
w
h
i
l
e
 
j
 
>
=
 
g
a
p
 
a
n
d
 
a
r
r
[
j
 
-
 
g
a
p
]
 
>
 
t
e
m
p
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
j
]
 
=
 
a
r
r
[
j
 
-
 
g
a
p
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
j
 
-
=
 
g
a
p


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
j
]
 
=
 
t
e
m
p


 
 
 
 
 
 
 
 
g
a
p
 
/
/
=
 
2






d
e
f
 
i
n
s
e
r
t
i
o
n
_
s
o
r
t
(
a
r
r
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
 
a
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
p
e
r
f
o
r
m
s
 
I
n
s
e
r
t
i
o
n
 
s
o
r
t
 
o
n
 
a
n
 
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


 
 
 
 
 
 
 
 
a
r
r
 
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
 
a
r
r
a
y
 
t
o
 
b
e
 
s
o
r
t
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
a
r
r
)


 
 
 
 
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


 
 
 
 
 
 
 
 
k
e
y
 
=
 
a
r
r
[
i
]


 
 
 
 
 
 
 
 
j
 
=
 
i
 
-
 
1


 
 
 
 
 
 
 
 
w
h
i
l
e
 
j
 
>
=
 
0
 
a
n
d
 
a
r
r
[
j
]
 
>
 
k
e
y
:


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
j
 
+
 
1
]
 
=
 
a
r
r
[
j
]


 
 
 
 
 
 
 
 
 
 
 
 
j
 
-
=
 
1


 
 
 
 
 
 
 
 
a
r
r
[
j
 
+
 
1
]
 
=
 
k
e
y






d
e
f
 
s
e
l
e
c
t
i
o
n
_
s
o
r
t
(
a
r
r
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
 
a
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
p
e
r
f
o
r
m
s
 
S
e
l
e
c
t
i
o
n
 
s
o
r
t
 
o
n
 
a
n
 
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


 
 
 
 
 
 
 
 
a
r
r
 
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
 
a
r
r
a
y
 
t
o
 
b
e
 
s
o
r
t
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
a
r
r
)


 
 
 
 
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


 
 
 
 
 
 
 
 
m
i
n
_
i
d
x
 
=
 
i


 
 
 
 
 
 
 
 
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
 
n
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
a
r
r
[
j
]
 
<
 
a
r
r
[
m
i
n
_
i
d
x
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
i
d
x
 
=
 
j


 
 
 
 
 
 
 
 
a
r
r
[
i
]
,
 
a
r
r
[
m
i
n
_
i
d
x
]
 
=
 
a
r
r
[
m
i
n
_
i
d
x
]
,
 
a
r
r
[
i
]






d
e
f
 
m
e
r
g
e
_
s
o
r
t
(
a
r
r
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
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
 
a
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
p
e
r
f
o
r
m
s
 
M
e
r
g
e
 
s
o
r
t
 
o
n
 
a
n
 
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


 
 
 
 
 
 
 
 
a
r
r
 
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
 
a
r
r
a
y
 
t
o
 
b
e
 
s
o
r
t
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
d
e
f
 
m
e
r
g
e
(
a
r
r
,
 
l
,
 
m
,
 
r
)
:


 
 
 
 
 
 
 
 
n
1
 
=
 
m
 
-
 
l
 
+
 
1
import unittest

from more_itertools import is_sorted


class Tester(unittest.TestCase):
    """Unit tests for the Shell sort functionality."""

    def test_already_sorted_array(self):
        """Test Case 1: Already sorted array."""
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_reverse_sorted_array(self):
        """Test Case 2: Reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_array_with_duplicate_elements(self):
        """Test Case 3: Array with duplicate elements."""
        arr = [4, 2, 2, 4, 1]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_array_with_negative_numbers(self):
        """Test Case 4: Array with negative numbers."""
        arr = [-3, -1, -4, -2, 0]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_empty_array(self):
        """Test Case 5: Empty array."""
        arr = []
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

if __name__ == '__main__':
    unittest.main()