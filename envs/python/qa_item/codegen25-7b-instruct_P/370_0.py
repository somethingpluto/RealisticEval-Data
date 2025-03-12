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
 
T
u
p
l
e






d
e
f
 
d
e
c
o
m
p
o
s
e
(
n
:
 
i
n
t
,
 
s
h
a
p
e
:
 
T
u
p
l
e
)
 
-
>
 
T
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
D
e
c
o
m
p
o
s
e
 
a
 
f
l
a
t
 
i
n
d
e
x
 
`
n
`
 
i
n
t
o
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
s
h
a
p
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
:
 
F
l
a
t
 
i
n
d
e
x
 
(
n
o
n
-
n
e
g
a
t
i
v
e
 
i
n
t
e
g
e
r
)
.


 
 
 
 
 
 
 
 
s
h
a
p
e
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
d
i
m
e
n
s
i
o
n
s
 
o
f
 
t
h
e
 
m
u
l
t
i
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
 
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
 
t
o
 
`
n
`
.


 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
`
n
`
 
i
s
 
o
u
t
 
o
f
 
b
o
u
n
d
s
 
f
o
r
 
t
h
e
 
a
r
r
a
y
 
d
e
f
i
n
e
d
 
b
y
 
`
s
h
a
p
e
`
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
>
=
 
n
p
.
p
r
o
d
(
s
h
a
p
e
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
f
"
I
n
d
e
x
 
{
n
}
 
i
s
 
o
u
t
 
o
f
 
b
o
u
n
d
s
 
f
o
r
 
s
h
a
p
e
 
{
s
h
a
p
e
}
.
"
)


 
 
 
 
r
e
t
u
r
n
 
t
u
p
l
e
(
n
p
.
u
n
r
a
v
e
l
_
i
n
d
e
x
(
n
,
 
s
h
a
p
e
)
)






d
e
f
 
g
e
t
_
f
l
a
t
_
i
n
d
e
x
(
s
h
a
p
e
:
 
T
u
p
l
e
)
 
-
>
 
n
p
.
n
d
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
 
a
 
1
D
 
a
r
r
a
y
 
o
f
 
i
n
d
i
c
e
s
 
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
 
t
o
 
t
h
e
 
f
l
a
t
t
e
n
e
d
 
v
e
r
s
i
o
n
 
o
f
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
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


 
 
 
 
 
 
 
 
s
h
a
p
e
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
d
i
m
e
n
s
i
o
n
s
 
o
f
 
t
h
e
 
m
u
l
t
i
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
n
p
.
n
d
a
r
r
a
y
:
 
1
D
 
a
r
r
a
y
 
o
f
 
i
n
d
i
c
e
s
 
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
 
t
o
 
t
h
e
 
f
l
a
t
t
e
n
e
d
 
v
e
r
s
i
o
n
 
o
f
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
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
 
n
p
.
a
r
a
n
g
e
(
n
p
.
p
r
o
d
(
s
h
a
p
e
)
)






d
e
f
 
g
e
t
_
f
l
a
t
_
i
n
d
e
x
_
f
r
o
m
_
i
n
d
i
c
e
s
(
i
n
d
i
c
e
s
:
 
T
u
p
l
e
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


 
 
 
 
R
e
t
u
r
n
 
t
h
e
 
f
l
a
t
 
i
n
d
e
x
 
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
 
t
o
 
a
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
d
i
c
e
s
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
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
 
F
l
a
t
 
i
n
d
e
x
 
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
 
t
o
 
t
h
e
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
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
 
n
p
.
r
a
v
e
l
_
m
u
l
t
i
_
i
n
d
e
x
(
i
n
d
i
c
e
s
,
 
s
h
a
p
e
=
i
n
d
i
c
e
s
.
s
h
a
p
e
)






d
e
f
 
g
e
t
_
i
n
d
i
c
e
s
_
f
r
o
m
_
f
l
a
t
_
i
n
d
e
x
(
f
l
a
t
_
i
n
d
e
x
:
 
i
n
t
,
 
s
h
a
p
e
:
 
T
u
p
l
e
)
 
-
>
 
T
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
 
t
h
e
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
 
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
 
t
o
 
a
 
f
l
a
t
 
i
n
d
e
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
l
a
t
_
i
n
d
e
x
:
 
F
l
a
t
 
i
n
d
e
x
 
(
n
o
n
-
n
e
g
a
t
i
v
e
 
i
n
t
e
g
e
r
)
.


 
 
 
 
 
 
 
 
s
h
a
p
e
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
d
i
m
e
n
s
i
o
n
s
 
o
f
 
t
h
e
 
m
u
l
t
i
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
:
 
T
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
u
l
t
i
d
i
m
e
n
s
i
o
n
a
l
 
i
n
d
e
x
 
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
 
t
o
 
`
f
l
a
t
_
i
n
d
e
x
`
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
 
d
e
c
o
m
p
o
s
e
(
f
l
a
t
_
i
n
d
e
x
import unittest


class TestDecomposeFunction(unittest.TestCase):

    def test_edge_case_with_larger_shap(self):
        self.assertEqual(decompose(60, (4, 4, 4)), (3, 3, 0))

    def test_last_valid_index(self):
        self.assertEqual(decompose(63, (4, 4, 4)), (3, 3, 3))

    def test_single_dimension_case(self):
        self.assertEqual(decompose(2, (5,)), (2,))

    def test_invalid_cases(self):
        # Test case 5: Out of bounds case (negative index)
        with self.assertRaises(ValueError):
            decompose(-1, (3, 4, 5))

        # Test case 6: Out of bounds case (index too large)
        with self.assertRaises(ValueError):
            decompose(100, (3, 4, 5))

if __name__ == '__main__':
    unittest.main()