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
 
b
i
n
a
r
y
_
s
e
a
r
c
h
_
c
l
o
s
e
s
t
(
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
[
i
n
t
]
,
 
t
a
r
g
e
t
:
 
i
n
t
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


 
 
 
 
P
e
r
f
o
r
m
s
 
a
 
b
i
n
a
r
y
 
s
e
a
r
c
h
 
t
o
 
f
i
n
d
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
i
n
 
a
 
s
o
r
t
e
d
 
a
r
r
a
y
.


 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
i
s
 
n
o
t
 
f
o
u
n
d
,
 
i
t
 
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
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
l
o
s
e
s
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
s
o
r
t
e
d
 
a
r
r
a
y
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
.
T
h
e
 
s
o
r
t
e
d
 
a
r
r
a
y
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
i
n
t
)
:
 
T
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
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
.




 
 
 
 
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
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
o
r
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
l
o
s
e
s
t
 
v
a
l
u
e
 
i
f
 
t
h
e
 
t
a
r
g
e
t
 
i
s
 
n
o
t
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
l
e
f
t
 
=
 
0


 
 
 
 
r
i
g
h
t
 
=
 
l
e
n
(
a
r
r
a
y
)
 
-
 
1


 
 
 
 
c
l
o
s
e
s
t
 
=
 
N
o
n
e




 
 
 
 
w
h
i
l
e
 
l
e
f
t
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
m
i
d
 
=
 
(
l
e
f
t
 
+
 
r
i
g
h
t
)
 
/
/
 
2


 
 
 
 
 
 
 
 
i
f
 
a
r
r
a
y
[
m
i
d
]
 
=
=
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
i
d


 
 
 
 
 
 
 
 
e
l
i
f
 
a
r
r
a
y
[
m
i
d
]
 
<
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
l
e
f
t
 
=
 
m
i
d
 
+
 
1


 
 
 
 
 
 
 
 
 
 
 
 
c
l
o
s
e
s
t
 
=
 
m
i
d


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
i
g
h
t
 
=
 
m
i
d
 
-
 
1


 
 
 
 
 
 
 
 
 
 
 
 
c
l
o
s
e
s
t
 
=
 
m
i
d
 
-
 
1




 
 
 
 
r
e
t
u
r
n
 
c
l
o
s
e
s
t






d
e
f
 
b
i
n
a
r
y
_
s
e
a
r
c
h
_
c
l
o
s
e
s
t
_
2
(
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
[
i
n
t
]
,
 
t
a
r
g
e
t
:
 
i
n
t
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


 
 
 
 
P
e
r
f
o
r
m
s
 
a
 
b
i
n
a
r
y
 
s
e
a
r
c
h
 
t
o
 
f
i
n
d
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
i
n
 
a
 
s
o
r
t
e
d
 
a
r
r
a
y
.


 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
i
s
 
n
o
t
 
f
o
u
n
d
,
 
i
t
 
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
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
l
o
s
e
s
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
s
o
r
t
e
d
 
a
r
r
a
y
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
.
T
h
e
 
s
o
r
t
e
d
 
a
r
r
a
y
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
i
n
t
)
:
 
T
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
 
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
.




 
 
 
 
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
 
T
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
o
r
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
c
l
o
s
e
s
t
 
v
a
l
u
e
 
i
f
 
t
h
e
 
t
a
r
g
e
t
 
i
s
 
n
o
t
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
l
e
f
t
 
=
 
0


 
 
 
 
r
i
g
h
t
 
=
 
l
e
n
(
a
r
r
a
y
)
 
-
 
1


 
 
 
 
c
l
o
s
e
s
t
 
=
 
N
o
n
e




 
 
 
 
w
h
i
l
e
 
l
e
f
t
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
m
i
d
 
=
 
(
l
e
f
t
 
+
 
r
i
g
h
t
)
 
/
/
 
2


 
 
 
 
 
 
 
 
i
f
 
a
r
r
a
y
[
m
i
d
]
 
=
=
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
i
d


 
 
 
 
 
 
 
 
e
l
i
f
 
a
r
r
a
y
[
m
i
d
]
 
<
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
l
e
f
t
 
=
 
m
i
d
 
+
 
1


 
 
 
 
 
 
 
 
 
 
 
 
c
l
o
s
e
s
t
 
=
 
m
i
d


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
i
g
h
t
 
=
 
m
i
d
 
-
 
1


 
 
 
 
 
 
 
 
 
 
 
 
c
l
o
s
e
s
t
 
=
 
m
i
d
 
-
 
1




 
 
 
 
r
e
t
u
r
n
 
c
l
o
s
e
s
t






d
e
f
 
b
i
n
a
r
y
_
s
e
a
r
c
h
_
c
l
o
s
e
s
t
_
3
(
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
[
i
n
t
]
,
 
t
a
r
g
e
t
:
 
i
n
t
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


 
 
 
 
P
e
r
f
o
r
m
s
 
a
import unittest


class TestBinarySearchClosest(unittest.TestCase):

    def test_target_present(self):
        """Test when the target is present in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 7
        result = binary_search_closest(array, target)
        self.assertEqual(result, 3, "Target should be found at index 3.")

    def test_closest_element_smaller(self):
        """Test when the target is not present and the closest element is smaller."""
        array = [1, 3, 5, 7, 9, 11]
        target = 6
        result = binary_search_closest(array, target)
        self.assertEqual(result, 2, "Closest element should be 5 at index 2.")

    def test_closest_element_larger(self):
        """Test when the target is not present and the closest element is larger."""
        array = [1, 3, 5, 7, 9, 11]
        target = 8
        result = binary_search_closest(array, target)
        self.assertEqual(result, 3, "Closest element should be 7 at index 3.")

    def test_target_smaller_than_all(self):
        """Test when the target is smaller than all elements in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 0
        result = binary_search_closest(array, target)
        self.assertEqual(result, 0, "Closest element should be 1 at index 0.")

    def test_target_larger_than_all(self):
        """Test when the target is larger than all elements in the array."""
        array = [1, 3, 5, 7, 9, 11]
        target = 12
        result = binary_search_closest(array, target)
        self.assertEqual(result, 5, "Closest element should be 11 at index 5.")

if __name__ == '__main__':
    unittest.main()