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
 
c
a
l
c
u
l
a
t
e
_
t
o
r
o
i
d
a
l
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
p
o
i
n
t
_
a
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
 
f
l
o
a
t
]
,
 
p
o
i
n
t
_
b
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
 
f
l
o
a
t
]
,
 
w
i
d
t
h
:
 
f
l
o
a
t
,
 
h
e
i
g
h
t
:
 
f
l
o
a
t
)
 
-
>
 
L
i
s
t
[
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


 
 
 
 
C
a
l
c
u
l
a
t
e
s
 
t
h
e
 
t
o
r
o
i
d
a
l
 
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
 
t
w
o
 
p
o
i
n
t
s
 
i
n
 
a
 
w
r
a
p
-
a
r
o
u
n
d
 
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
_
a
 
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
 
f
i
r
s
t
 
p
o
i
n
t
 
w
i
t
h
 
k
e
y
s
 
'
x
'
 
a
n
d
 
'
y
'
.


 
 
 
 
 
 
 
 
p
o
i
n
t
_
b
 
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
 
s
e
c
o
n
d
 
p
o
i
n
t
 
w
i
t
h
 
k
e
y
s
 
'
x
'
 
a
n
d
 
'
y
'
.


 
 
 
 
 
 
 
 
w
i
d
t
h
 
(
f
l
o
a
t
)
:
 
T
h
e
 
w
i
d
t
h
 
o
f
 
t
h
e
 
t
o
r
o
i
d
a
l
 
s
p
a
c
e
.


 
 
 
 
 
 
 
 
h
e
i
g
h
t
 
(
f
l
o
a
t
)
:
 
T
h
e
 
h
e
i
g
h
t
 
o
f
 
t
h
e
 
t
o
r
o
i
d
a
l
 
s
p
a
c
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
f
l
o
a
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
 
x
 
a
n
d
 
y
 
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
s
,
 
a
c
c
o
u
n
t
i
n
g
 
f
o
r
 
w
r
a
p
-
a
r
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
x
_
d
i
f
f
 
=
 
p
o
i
n
t
_
b
[
"
x
"
]
 
-
 
p
o
i
n
t
_
a
[
"
x
"
]


 
 
 
 
y
_
d
i
f
f
 
=
 
p
o
i
n
t
_
b
[
"
y
"
]
 
-
 
p
o
i
n
t
_
a
[
"
y
"
]




 
 
 
 
i
f
 
x
_
d
i
f
f
 
>
 
w
i
d
t
h
 
/
 
2
:


 
 
 
 
 
 
 
 
x
_
d
i
f
f
 
-
=
 
w
i
d
t
h


 
 
 
 
e
l
i
f
 
x
_
d
i
f
f
 
<
 
-
w
i
d
t
h
 
/
 
2
:


 
 
 
 
 
 
 
 
x
_
d
i
f
f
 
+
=
 
w
i
d
t
h




 
 
 
 
i
f
 
y
_
d
i
f
f
 
>
 
h
e
i
g
h
t
 
/
 
2
:


 
 
 
 
 
 
 
 
y
_
d
i
f
f
 
-
=
 
h
e
i
g
h
t


 
 
 
 
e
l
i
f
 
y
_
d
i
f
f
 
<
 
-
h
e
i
g
h
t
 
/
 
2
:


 
 
 
 
 
 
 
 
y
_
d
i
f
f
 
+
=
 
h
e
i
g
h
t




 
 
 
 
r
e
t
u
r
n
 
[
x
_
d
i
f
f
,
 
y
_
d
i
f
f
]






d
e
f
 
c
a
l
c
u
l
a
t
e
_
t
o
r
o
i
d
a
l
_
d
i
s
t
a
n
c
e
(
p
o
i
n
t
_
a
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
 
f
l
o
a
t
]
,
 
p
o
i
n
t
_
b
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
 
f
l
o
a
t
]
,
 
w
i
d
t
h
:
 
f
l
o
a
t
,
 
h
e
i
g
h
t
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
"
"
"


 
 
 
 
C
a
l
c
u
l
a
t
e
s
 
t
h
e
 
t
o
r
o
i
d
a
l
 
d
i
s
t
a
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
 
t
w
o
 
p
o
i
n
t
s
 
i
n
 
a
 
w
r
a
p
-
a
r
o
u
n
d
 
s
p
a
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
_
a
 
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
 
f
i
r
s
t
 
p
o
i
n
t
 
w
i
t
h
 
k
e
y
s
 
'
x
'
 
a
n
d
 
'
y
'
.


 
 
 
 
 
 
 
 
p
o
i
n
t
_
b
 
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
 
s
e
c
o
n
d
 
p
o
i
n
t
 
w
i
t
h
 
k
e
y
s
 
'
x
'
 
a
n
d
 
'
y
'
.


 
 
 
 
 
 
 
 
w
i
d
t
h
 
(
f
l
o
a
t
)
:
 
T
h
e
 
w
i
d
t
h
 
o
f
 
t
h
e
 
t
o
r
o
i
d
a
l
 
s
p
a
c
e
.


 
 
 
 
 
 
 
 
h
e
i
g
h
t
 
(
f
l
o
a
t
)
:
 
T
h
e
 
h
e
i
g
h
t
 
o
f
 
t
h
e
 
t
o
r
o
i
d
a
l
 
s
p
a
c
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
t
o
r
o
i
d
a
l
 
d
i
s
t
a
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
 
t
h
e
 
t
w
o
 
p
o
i
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
x
_
d
i
f
f
,
 
y
_
d
i
f
f
 
=
 
c
a
l
c
u
l
a
t
e
_
t
o
r
o
i
d
a
l
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
p
o
i
n
t
_
a
,
 
p
o
i
n
t
_
b
,
 
w
i
d
t
h
,
 
h
e
i
g
h
t
)
import unittest


class TestToroidalDiff(unittest.TestCase):

    def test_no_wrapping(self):
        this_point = {'x': 2, 'y': 3}
        other_point = {'x': 5, 'y': 6}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-3, -3])

    def test_wrapping_x_dimension(self):
        this_point = {'x': 9, 'y': 5}
        other_point = {'x': 1, 'y': 5}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-2, 0])  # dx wraps around the toroidal boundary

    def test_wrapping_y_dimension(self):
        this_point = {'x': 4, 'y': 9}
        other_point = {'x': 4, 'y': 1}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [0, -2])  # dy wraps around the toroidal boundary

    def test_wrapping_both_dimensions(self):
        this_point = {'x': 9, 'y': 9}
        other_point = {'x': 1, 'y': 1}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [-2, -2])  # Both dx and dy wrap around

    def test_same_position(self):
        this_point = {'x': 5, 'y': 5}
        other_point = {'x': 5, 'y': 5}
        width = 10
        height = 10
        result = calculate_toroidal_difference(this_point, other_point, width, height)
        self.assertEqual(result, [0, 0])  # No difference

if __name__ == '__main__':
    unittest.main()