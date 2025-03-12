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
 
U
n
i
o
n






d
e
f
 
f
i
n
d
_
c
l
o
s
e
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
(
t
a
r
g
e
t
:
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
,
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
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
s
 
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
 
f
r
o
m
 
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
 
t
h
a
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
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
 
n
u
m
b
e
r
 
t
o
 
w
h
i
c
h
 
w
e
 
w
a
n
t
 
t
o
 
f
i
n
d
 
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
 
e
l
e
m
e
n
t
.


 
 
 
 
 
 
 
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
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
 
n
u
m
e
r
i
c
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
 
f
r
o
m
 
w
h
i
c
h
 
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
 
e
l
e
m
e
n
t
 
i
s
 
t
o
 
b
e
 
f
o
u
n
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
:
 
T
h
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
 
t
h
e
 
l
i
s
t
 
t
h
a
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
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
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
a
b
s
(
x
 
-
 
t
a
r
g
e
t
)
)






d
e
f
 
f
i
n
d
_
c
l
o
s
e
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
_
i
n
d
e
x
(
t
a
r
g
e
t
:
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
,
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
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
 
t
h
a
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
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
 
n
u
m
b
e
r
 
t
o
 
w
h
i
c
h
 
w
e
 
w
a
n
t
 
t
o
 
f
i
n
d
 
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
 
e
l
e
m
e
n
t
.


 
 
 
 
 
 
 
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
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
 
n
u
m
e
r
i
c
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
 
f
r
o
m
 
w
h
i
c
h
 
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
 
e
l
e
m
e
n
t
 
i
s
 
t
o
 
b
e
 
f
o
u
n
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
 
t
h
e
 
l
i
s
t
 
t
h
a
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
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
.
i
n
d
e
x
(
f
i
n
d
_
c
l
o
s
e
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
(
t
a
r
g
e
t
,
 
e
l
e
m
e
n
t
s
)
)






d
e
f
 
f
i
n
d
_
c
l
o
s
e
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
_
w
i
t
h
_
c
o
n
d
i
t
i
o
n
s
(


 
 
 
 
t
a
r
g
e
t
:
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
,
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
]
,
 
c
o
n
d
i
t
i
o
n
s
:
 
L
i
s
t
[
b
o
o
l
]


)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
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
s
 
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
 
f
r
o
m
 
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
 
t
h
a
t
 
i
s
 
c
l
o
s
e
s
t
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
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
,


 
 
 
 
w
h
i
l
e
 
s
a
t
i
s
f
y
i
n
g
 
t
h
e
 
g
i
v
e
n
 
c
o
n
d
i
t
i
o
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
]
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
 
n
u
m
b
e
r
 
t
o
 
w
h
i
c
h
 
w
e
 
w
a
n
t
 
t
o
 
f
i
n
d
 
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
 
e
l
e
m
e
n
t
.


 
 
 
 
 
 
 
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
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
 
n
u
m
e
r
i
c
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
 
f
r
o
m
 
w
h
i
c
h
 
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
 
e
l
e
m
e
n
t
 
i
s
 
t
o
 
b
e
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 
c
o
n
d
i
t
i
o
n
s
 
(
L
i
s
t
[
b
o
o
l
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
 
b
o
o
l
e
a
n
 
v
a
l
u
e
s
 
i
n
d
i
c
a
t
i
n
g
 
w
h
e
t
h
e
r
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
l
e
m
e
n
t
 
s
a
t
i
s
f
i
e
s
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
d
i
t
i
o
n
s
 
o
r
 
n
o
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
U
n
i
o
n
[
import unittest


class TestFindClosestElement(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(find_closest_element(5, [1, 3, 7, 8, 9]), 3,
                         "Should return 3 as it is the first closest element to 5")

    def test_exact_match(self):
        self.assertEqual(find_closest_element(7, [1, 3, 7, 8, 9]), 7,
                         "Should return 7 as it exactly matches the target")

    def test_multiple_closest_values(self):
        self.assertEqual(find_closest_element(5, [4, 6, 8, 9]), 4,
                         "Should return 4 as it is the first closest element to 5")

    def test_float_values(self):
        self.assertEqual(find_closest_element(5.5, [1.1, 3.3, 7.7, 8.8]), 3.3,
                         "Should return 3.3 as it is the first closest element to 5.5")

if __name__ == '__main__':
    unittest.main()