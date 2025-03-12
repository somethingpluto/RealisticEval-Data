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
c
a
l
e
_
t
o
_
r
a
n
g
e
(
i
n
p
u
t
_
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
,
 
i
n
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,
 
i
n
p
u
t
_
m
a
x
:
 
f
l
o
a
t
,
 
o
u
t
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,
 
o
u
t
p
u
t
_
m
a
x
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


 
 
 
 
S
c
a
l
e
s
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
a
n
 
a
r
r
a
y
 
f
r
o
m
 
o
n
e
 
r
a
n
g
e
 
t
o
 
a
n
o
t
h
e
r
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
 
o
f
 
i
n
p
u
t
 
v
a
l
u
e
s
 
t
o
 
b
e
 
s
c
a
l
e
d
.


 
 
 
 
 
 
 
 
i
n
p
u
t
_
m
i
n
 
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
 
i
n
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
i
n
p
u
t
_
m
a
x
 
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
 
i
n
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
m
i
n
 
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
 
o
u
t
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
m
a
x
 
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
 
o
u
t
p
u
t
 
r
a
n
g
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
 
n
e
w
 
a
r
r
a
y
 
w
i
t
h
 
v
a
l
u
e
s
 
s
c
a
l
e
d
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
r
a
n
g
e


 
 
 
 
"
"
"


 
 
 
 
i
n
p
u
t
_
r
a
n
g
e
 
=
 
i
n
p
u
t
_
m
a
x
 
-
 
i
n
p
u
t
_
m
i
n


 
 
 
 
o
u
t
p
u
t
_
r
a
n
g
e
 
=
 
o
u
t
p
u
t
_
m
a
x
 
-
 
o
u
t
p
u
t
_
m
i
n


 
 
 
 
r
e
t
u
r
n
 
[
(
x
 
-
 
i
n
p
u
t
_
m
i
n
)
 
*
 
(
o
u
t
p
u
t
_
r
a
n
g
e
 
/
 
i
n
p
u
t
_
r
a
n
g
e
)
 
+
 
o
u
t
p
u
t
_
m
i
n
 
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
a
r
r
a
y
]






d
e
f
 
s
c
a
l
e
_
t
o
_
r
a
n
g
e
_
u
n
c
l
i
p
p
e
d
(
i
n
p
u
t
_
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
,
 
i
n
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,
 
i
n
p
u
t
_
m
a
x
:
 
f
l
o
a
t
,
 
o
u
t
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
m
a
x
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


 
 
 
 
S
c
a
l
e
s
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
a
n
 
a
r
r
a
y
 
f
r
o
m
 
o
n
e
 
r
a
n
g
e
 
t
o
 
a
n
o
t
h
e
r
 
w
i
t
h
o
u
t
 
c
l
i
p
p
i
n
g
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
 
o
f
 
i
n
p
u
t
 
v
a
l
u
e
s
 
t
o
 
b
e
 
s
c
a
l
e
d
.


 
 
 
 
 
 
 
 
i
n
p
u
t
_
m
i
n
 
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
 
i
n
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
i
n
p
u
t
_
m
a
x
 
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
 
i
n
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
m
i
n
 
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
 
o
u
t
p
u
t
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
m
a
x
 
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
 
o
u
t
p
u
t
 
r
a
n
g
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
 
n
e
w
 
a
r
r
a
y
 
w
i
t
h
 
v
a
l
u
e
s
 
s
c
a
l
e
d
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
r
a
n
g
e


 
 
 
 
"
"
"


 
 
 
 
i
n
p
u
t
_
r
a
n
g
e
 
=
 
i
n
p
u
t
_
m
a
x
 
-
 
i
n
p
u
t
_
m
i
n


 
 
 
 
o
u
t
p
u
t
_
r
a
n
g
e
 
=
 
o
u
t
p
u
t
_
m
a
x
 
-
 
o
u
t
p
u
t
_
m
i
n


 
 
 
 
r
e
t
u
r
n
 
[
(
x
 
-
 
i
n
p
u
t
_
m
i
n
)
 
*
 
(
o
u
t
p
u
t
_
r
a
n
g
e
 
/
 
i
n
p
u
t
_
r
a
n
g
e
)
 
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
a
r
r
a
y
]






d
e
f
 
s
c
a
l
e
_
t
o
_
r
a
n
g
e
_
u
n
c
l
i
p
p
e
d
_
w
i
t
h
_
o
f
f
s
e
t
(
i
n
p
u
t
_
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
,
 
i
n
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,
 
i
n
p
u
t
_
m
a
x
:
 
f
l
o
a
t
,
 
o
u
t
p
u
t
_
m
i
n
:
 
f
l
o
a
t
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
import unittest


class TestScaleToRange(unittest.TestCase):
    def test_simple_scaling(self):
        result = scale_to_range([1, 2, 3, 4, 5], 1, 5, 10, 50)
        self.assertEqual(result, [10, 20, 30, 40, 50])

    def test_scaling_with_negative_input_range(self):
        result = scale_to_range([-5, 0, 5], -5, 5, 0, 100)
        self.assertEqual(result, [0, 50, 100])

    def test_scaling_with_negative_output_range(self):
        result = scale_to_range([0, 50, 100], 0, 100, -100, 100)
        self.assertEqual(result, [-100, 0, 100])

    def test_input_array_containing_the_same_value(self):
        result = scale_to_range([2, 2, 2], 1, 3, 0, 10)
        self.assertEqual(result, [5, 5, 5])

    def test_input_value_out_of_range_should_throw_an_error(self):
        with self.assertRaises(ValueError):
            scale_to_range([1, 2, 3, 6], 1, 5, 0, 10)

if __name__ == '__main__':
    unittest.main()