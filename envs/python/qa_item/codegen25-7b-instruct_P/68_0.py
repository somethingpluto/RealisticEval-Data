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
p
l
i
t
_
l
i
s
t
_
i
n
t
o
_
p
a
r
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


 
 
 
 
d
i
v
i
d
e
 
a
 
l
i
s
t
 
e
v
e
n
l
y
 
i
n
t
o
 
n
 
p
a
r
t
s
 
a
n
d
 
r
e
t
u
r
n
 
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
 
p
a
r
t
s
.
 
I
f
 
t
h
e
 
l
i
s
t
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
d
i
v
i
s
i
b
l
e
 
b
y
 
n
,
 
a
d
d
i
t
i
o
n
a
l
 
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
 
a
d
d
e
d
 
t
o
 
t
h
e
 
p
r
e
v
i
o
u
s
 
s
e
c
t
i
o
n
s
 
o
n
e
 
b
y
 
o
n
e


 
 
 
 
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
 
T
h
e
 
l
i
s
t
 
t
o
 
b
e
 
d
i
v
i
d
e
d
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
 
n
u
m
b
e
r
 
o
f
 
p
a
r
t
s
 
t
o
 
d
i
v
i
d
e
 
t
h
e
 
l
i
s
t
 
i
n
t
o
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
 
n
 
s
u
b
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
 
s
u
b
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
a
r
t
 
o
f
 
t
h
e
 
o
r
i
g
i
n
a
l
 
l
i
s
t
.


 
 
 
 
"
"
"


 
 
 
 
k
,
 
m
 
=
 
d
i
v
m
o
d
(
l
e
n
(
l
s
t
)
,
 
n
)


 
 
 
 
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
 
*
 
k
 
+
 
m
i
n
(
i
,
 
m
)
:
(
i
 
+
 
1
)
 
*
 
k
 
+
 
m
i
n
(
i
 
+
 
1
,
 
m
)
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
]






d
e
f
 
s
p
l
i
t
_
l
i
s
t
_
i
n
t
o
_
p
a
r
t
s
_
w
i
t
h
_
r
e
m
a
i
n
d
e
r
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


 
 
 
 
d
i
v
i
d
e
 
a
 
l
i
s
t
 
e
v
e
n
l
y
 
i
n
t
o
 
n
 
p
a
r
t
s
 
a
n
d
 
r
e
t
u
r
n
 
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
 
p
a
r
t
s
.
 
I
f
 
t
h
e
 
l
i
s
t
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
d
i
v
i
s
i
b
l
e
 
b
y
 
n
,
 
a
d
d
i
t
i
o
n
a
l
 
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
 
a
d
d
e
d
 
t
o
 
t
h
e
 
p
r
e
v
i
o
u
s
 
s
e
c
t
i
o
n
s
 
o
n
e
 
b
y
 
o
n
e


 
 
 
 
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
 
T
h
e
 
l
i
s
t
 
t
o
 
b
e
 
d
i
v
i
d
e
d
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
 
n
u
m
b
e
r
 
o
f
 
p
a
r
t
s
 
t
o
 
d
i
v
i
d
e
 
t
h
e
 
l
i
s
t
 
i
n
t
o
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
 
n
 
s
u
b
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
 
s
u
b
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
a
r
t
 
o
f
 
t
h
e
 
o
r
i
g
i
n
a
l
 
l
i
s
t
.


 
 
 
 
"
"
"


 
 
 
 
k
,
 
m
 
=
 
d
i
v
m
o
d
(
l
e
n
(
l
s
t
)
,
 
n
)


 
 
 
 
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
 
*
 
k
 
+
 
m
i
n
(
i
,
 
m
)
:
(
i
 
+
 
1
)
 
*
 
k
 
+
 
m
i
n
(
i
 
+
 
1
,
 
m
)
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
]






d
e
f
 
s
p
l
i
t
_
l
i
s
t
_
i
n
t
o
_
p
a
r
t
s
_
w
i
t
h
_
r
e
m
a
i
n
d
e
r
_
a
n
d
_
p
a
d
d
i
n
g
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
,
 
p
a
d
d
i
n
g
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


 
 
 
 
d
i
v
i
d
e
 
a
 
l
i
s
t
 
e
v
e
n
l
y
 
i
n
t
o
 
n
 
p
a
r
t
s
 
a
n
d
 
r
e
t
u
r
n
 
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
 
p
a
r
t
s
.
 
I
f
 
t
h
e
 
l
i
s
t
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
d
i
v
i
s
i
b
l
e
 
b
y
 
n
,
 
a
d
d
i
t
i
o
n
a
l
 
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
 
a
d
d
e
d
 
t
o
 
t
h
e
 
p
r
e
v
i
o
u
s
 
s
e
c
t
i
o
n
s
 
o
n
e
 
b
y
 
o
n
e


 
 
 
 
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
 
T
h
e
 
l
i
s
t
 
t
o
 
b
e
 
d
i
v
i
d
e
d
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
 
n
u
m
b
e
r
 
o
f
 
p
a
r
t
s
 
t
o
 
d
i
v
i
d
e
 
t
h
e
 
l
i
s
t
 
i
n
t
o
.


 
 
 
 
 
 
 
 
p
a
d
d
i
n
g
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
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
o
 
a
d
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
a
s
t
 
s
u
b
l
i
s
t
 
i
f
 
i
t
 
i
s
import unittest


class TestDivideList(unittest.TestCase):
    def test_even_division(self):
        lst = [1, 2, 3, 4, 5, 6]
        n = 3
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_uneven_division(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        expected = [[1, 2, 3], [4, 5], [6, 7]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_more_parts_than_items(self):
        lst = [1, 2, 3]
        n = 5
        expected = [[1], [2], [3], [], []]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_single_element(self):
        lst = [1]
        n = 1
        expected = [[1]]
        self.assertEqual(split_list_into_parts(lst, n), expected)

    def test_empty_list(self):
        lst = []
        n = 3
        expected = [[], [], []]
        self.assertEqual(split_list_into_parts(lst, n), expected)

if __name__ == '__main__':
    unittest.main()