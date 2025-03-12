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
 
r
o
t
a
t
e
_
l
i
s
t
_
e
l
e
m
e
n
t
s
(
e
l
e
m
e
n
t
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


 
 
 
 
R
o
t
a
t
e
 
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
 
o
f
 
t
h
e
 
l
i
s
t
 
t
o
 
t
h
e
 
l
e
f
t
 
b
y
 
o
n
e
 
p
o
s
i
t
i
o
n
.
 
T
h
e
 
f
i
r
s
t
 
e
l
e
m
e
n
t


 
 
 
 
i
s
 
m
o
v
e
d
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
l
i
s
t
,
 
a
n
d
 
a
l
l
 
o
t
h
e
r
 
e
l
e
m
e
n
t
s
 
a
r
e
 
s
h
i
f
t
e
d
 
o
n
e
 
p
o
s
i
t
i
o
n
 
t
o
 
t
h
e
 
l
e
f
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
 
A
 
l
i
s
t
 
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
 
t
o
 
b
e
 
r
o
t
a
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
 
T
h
e
 
r
o
t
a
t
e
d
 
l
i
s
t
 
w
i
t
h
 
e
l
e
m
e
n
t
s
 
s
h
i
f
t
e
d
 
t
o
 
t
h
e
 
l
e
f
t
 
b
y
 
o
n
e
 
p
o
s
i
t
i
o
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
 
e
l
e
m
e
n
t
s
[
1
:
]
 
+
 
[
e
l
e
m
e
n
t
s
[
0
]
]






d
e
f
 
r
e
v
e
r
s
e
_
l
i
s
t
_
e
l
e
m
e
n
t
s
(
e
l
e
m
e
n
t
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


 
 
 
 
R
e
v
e
r
s
e
 
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
 
o
f
 
t
h
e
 
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


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
 
A
 
l
i
s
t
 
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
 
t
o
 
b
e
 
r
e
v
e
r
s
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
 
T
h
e
 
r
e
v
e
r
s
e
d
 
l
i
s
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
 
e
l
e
m
e
n
t
s
[
:
:
-
1
]






d
e
f
 
s
o
r
t
_
l
i
s
t
_
e
l
e
m
e
n
t
s
(
e
l
e
m
e
n
t
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


 
 
 
 
S
o
r
t
 
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
 
o
f
 
t
h
e
 
l
i
s
t
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
 
A
 
l
i
s
t
 
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
 
T
h
e
 
s
o
r
t
e
d
 
l
i
s
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
 
s
o
r
t
e
d
(
e
l
e
m
e
n
t
s
)






d
e
f
 
f
i
n
d
_
m
a
x
_
v
a
l
u
e
_
i
n
_
l
i
s
t
(
e
l
e
m
e
n
t
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


 
 
 
 
F
i
n
d
 
t
h
e
 
m
a
x
i
m
u
m
 
v
a
l
u
e
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
 
A
 
l
i
s
t
 
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
m
a
x
i
m
u
m
 
v
a
l
u
e
 
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


 
 
 
 
"
"
"


 
 
 
 
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
e
l
e
m
e
n
t
s
)






d
e
f
 
f
i
n
d
_
m
i
n
_
v
a
l
u
e
_
i
n
_
l
i
s
t
(
e
l
e
m
e
n
t
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


 
 
 
 
F
i
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
v
a
l
u
e
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
 
A
 
l
i
s
t
 
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
m
i
n
i
m
u
m
 
v
a
l
u
e
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
i
n
(
e
l
e
m
e
n
t
s
)






d
e
f
 
f
i
n
d
_
s
u
m
_
o
f
_
l
i
s
t
_
e
l
e
m
e
n
t
s
(
e
l
e
m
e
n
t
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


 
 
 
 
F
i
n
d
 
t
h
e
 
s
u
m
 
o
f
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
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
import unittest

class TestRotateListElements(unittest.TestCase):

    def test_basic_rotation(self):
        self.assertEqual(rotate_list_elements([1, 2, 3, 4]), [2, 3, 4, 1], "Should rotate the list elements correctly")

    def test_single_element_list(self):
        self.assertEqual(rotate_list_elements([10]), [10], "Single element list should remain unchanged")

    def test_empty_list(self):
        self.assertEqual(rotate_list_elements([]), [], "Empty list should remain unchanged")

    def test_two_element_list(self):
        self.assertEqual(rotate_list_elements([5, 9]), [9, 5], "Should correctly rotate a two-element list")

    def test_large_list(self):
        large_list = list(range(1, 1001))
        rotated_list = rotate_list_elements(large_list)
        self.assertEqual(rotated_list, list(range(2, 1001)) + [1], "Should correctly rotate a large list")




if __name__ == '__main__':
    unittest.main()