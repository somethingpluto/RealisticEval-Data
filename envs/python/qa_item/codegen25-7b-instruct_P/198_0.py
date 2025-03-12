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
m
a
x
_
d
i
f
f
e
r
e
n
c
e
(
l
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
s
 
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
 
d
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
n
 
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
 
a
r
r
a
y
 
s
u
c
h
 
t
h
a
t
 
t
h
e
 
s
m
a
l
l
e
r
 
e
l
e
m
e
n
t
 
a
p
p
e
a
r
s
 
b
e
f
o
r
e
 
t
h
e
 
l
a
r
g
e
r
 
o
n
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
 
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
 
d
i
f
f
e
r
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
 
l
e
n
(
l
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
l
[
1
]
 
-
 
l
[
0
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
2
,
 
l
e
n
(
l
)
)
:


 
 
 
 
 
 
 
 
d
i
f
f
 
=
 
l
[
i
]
 
-
 
l
[
i
 
-
 
1
]


 
 
 
 
 
 
 
 
i
f
 
d
i
f
f
 
>
 
m
a
x
_
d
i
f
f
:


 
 
 
 
 
 
 
 
 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
d
i
f
f


 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
d
i
f
f






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
d
i
f
f
e
r
e
n
c
e
_
2
(
l
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
s
 
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
 
d
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
n
 
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
 
a
r
r
a
y
 
s
u
c
h
 
t
h
a
t
 
t
h
e
 
s
m
a
l
l
e
r
 
e
l
e
m
e
n
t
 
a
p
p
e
a
r
s
 
b
e
f
o
r
e
 
t
h
e
 
l
a
r
g
e
r
 
o
n
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
 
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
 
d
i
f
f
e
r
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
 
l
e
n
(
l
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
m
i
n
_
v
a
l
 
=
 
l
[
0
]


 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
l
[
1
]
 
-
 
l
[
0
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
2
,
 
l
e
n
(
l
)
)
:


 
 
 
 
 
 
 
 
d
i
f
f
 
=
 
l
[
i
]
 
-
 
l
[
i
 
-
 
1
]


 
 
 
 
 
 
 
 
i
f
 
d
i
f
f
 
>
 
m
a
x
_
d
i
f
f
:


 
 
 
 
 
 
 
 
 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
d
i
f
f


 
 
 
 
 
 
 
 
i
f
 
l
[
i
]
 
<
 
m
i
n
_
v
a
l
:


 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
v
a
l
 
=
 
l
[
i
]


 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
d
i
f
f






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
d
i
f
f
e
r
e
n
c
e
_
3
(
l
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
s
 
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
 
d
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
n
 
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
 
a
r
r
a
y
 
s
u
c
h
 
t
h
a
t
 
t
h
e
 
s
m
a
l
l
e
r
 
e
l
e
m
e
n
t
 
a
p
p
e
a
r
s
 
b
e
f
o
r
e
 
t
h
e
 
l
a
r
g
e
r
 
o
n
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
 
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
 
d
i
f
f
e
r
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
 
l
e
n
(
l
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
m
a
x
_
d
i
f
f
 
=
 
l
[
1
]
 
-
 
l
[
0
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
2
,
 
l
e
n
(
l
)
)
:


 
 
 
 
 
 
 
 
d
i
f
f
 
=
 
l
[
i
]
 
-
 
l
[
i
 
-
 
1
]


 
 
 
 
 
 
 
 
i
f
 
d
i
f
f
 
>
 
m
a
x
_
d
i
f
f
import unittest


class Tester(unittest.TestCase):

    def test_general_case(self):
        l = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(find_max_difference(l), 8)  # Maximum difference is 10 - 2 = 8

    def test_decreasing_sequence(self):
        l = [10, 9, 8, 7, 6, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference should be 0

    def test_all_elements_same(self):
        l = [5, 5, 5, 5, 5]
        self.assertEqual(find_max_difference(l), 0)  # Maximum difference is 5 - 5 = 0

    def test_only_two_elements(self):
        l = [3, 8]
        self.assertEqual(find_max_difference(l), 5)  # Maximum difference is 8 - 3 = 5

    def test_single_element(self):
        l = [4]
        self.assertEqual(find_max_difference(l), 0)  # Only one element, no difference to calculate

if __name__ == '__main__':
    unittest.main()