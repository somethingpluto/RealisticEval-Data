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
 
p
a
r
s
e
_
e
x
p
r
e
s
s
i
o
n
(
e
x
p
r
e
s
s
i
o
n
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
m
a
t
h
e
m
a
t
i
c
a
l
 
e
x
p
r
e
s
s
i
o
n
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s
.


 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
i
d
e
n
t
i
f
i
e
s
 
b
o
t
h
 
o
p
e
r
a
n
d
s
 
(
n
u
m
b
e
r
s
)
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
(
+
,
 
-
,
 
*
,
 
/
,
 
e
t
c
.
)


 
 
 
 
i
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
e
x
p
r
e
s
s
i
o
n
 
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
m
 
i
n
 
a
 
l
i
s
t
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
x
p
r
e
s
s
i
o
n
 
(
s
t
r
)
:
 
T
h
e
 
m
a
t
h
e
m
a
t
i
c
a
l
 
e
x
p
r
e
s
s
i
o
n
 
t
o
 
b
e
 
p
a
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


 
 
 
 
 
 
 
 
l
i
s
t
[
s
t
r
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
 
t
o
k
e
n
s
 
i
d
e
n
t
i
f
i
e
d
 
i
n
 
t
h
e
 
e
x
p
r
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
w
i
l
l
 
i
n
c
l
u
d
e
 
b
o
t
h
 
o
p
e
r
a
n
d
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
i
n
 
t
h
e
 
o
r
d
e
r
 
t
h
e
y
 
a
p
p
e
a
r
.


 
 
 
 
"
"
"


 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s


 
 
 
 
t
o
k
e
n
s
 
=
 
[
]




 
 
 
 
#
 
I
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
e
x
p
r
e
s
s
i
o
n
 
s
t
r
i
n
g
,
 
a
d
d
i
n
g
 
o
p
e
r
a
n
d
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
t
o
 
t
h
e
 
l
i
s
t


 
 
 
 
c
u
r
r
e
n
t
_
t
o
k
e
n
 
=
 
"
"


 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
e
x
p
r
e
s
s
i
o
n
:


 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
.
i
s
d
i
g
i
t
(
)
 
o
r
 
c
h
a
r
 
=
=
 
"
.
"
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
p
p
e
n
d
 
t
h
e
 
c
u
r
r
e
n
t
 
d
i
g
i
t
 
o
r
 
d
e
c
i
m
a
l
 
p
o
i
n
t
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
t
o
k
e
n


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
t
o
k
e
n
 
+
=
 
c
h
a
r


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
t
h
e
 
c
u
r
r
e
n
t
 
t
o
k
e
n
 
i
s
 
n
o
t
 
e
m
p
t
y
,
 
a
p
p
e
n
d
 
i
t
 
t
o
 
t
h
e
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
e
n
t
_
t
o
k
e
n
 
!
=
 
"
"
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
k
e
n
s
.
a
p
p
e
n
d
(
c
u
r
r
e
n
t
_
t
o
k
e
n
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
t
o
k
e
n
 
=
 
"
"




 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
p
p
e
n
d
 
t
h
e
 
c
u
r
r
e
n
t
 
o
p
e
r
a
t
o
r
 
t
o
 
t
h
e
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s


 
 
 
 
 
 
 
 
 
 
 
 
t
o
k
e
n
s
.
a
p
p
e
n
d
(
c
h
a
r
)




 
 
 
 
#
 
I
f
 
t
h
e
r
e
 
i
s
 
s
t
i
l
l
 
a
 
c
u
r
r
e
n
t
 
t
o
k
e
n
,
 
a
p
p
e
n
d
 
i
t
 
t
o
 
t
h
e
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s


 
 
 
 
i
f
 
c
u
r
r
e
n
t
_
t
o
k
e
n
 
!
=
 
"
"
:


 
 
 
 
 
 
 
 
t
o
k
e
n
s
.
a
p
p
e
n
d
(
c
u
r
r
e
n
t
_
t
o
k
e
n
)




 
 
 
 
r
e
t
u
r
n
 
t
o
k
e
n
s






d
e
f
 
e
v
a
l
u
a
t
e
_
e
x
p
r
e
s
s
i
o
n
(
e
x
p
r
e
s
s
i
o
n
:
 
s
t
r
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


 
 
 
 
E
v
a
l
u
a
t
e
s
 
a
 
m
a
t
h
e
m
a
t
i
c
a
l
 
e
x
p
r
e
s
s
i
o
n
 
s
t
r
i
n
g
 
u
s
i
n
g
 
t
h
e
 
s
t
a
n
d
a
r
d
 
o
r
d
e
r
 
o
f
 
o
p
e
r
a
t
i
o
n
s
.


 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
p
a
r
s
e
s
 
t
h
e
 
e
x
p
r
e
s
s
i
o
n
 
s
t
r
i
n
g
 
u
s
i
n
g
 
t
h
e
 
`
p
a
r
s
e
_
e
x
p
r
e
s
s
i
o
n
`
 
f
u
n
c
t
i
o
n
,


 
 
 
 
a
n
d
 
t
h
e
n
 
a
p
p
l
i
e
s
 
t
h
e
 
o
r
d
e
r
 
o
f
 
o
p
e
r
a
t
i
o
n
s
 
t
o
 
c
a
l
c
u
l
a
t
e
 
t
h
e
 
r
e
s
u
l
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
x
p
r
e
s
s
i
o
n
 
(
s
t
r
)
:
 
T
h
e
 
m
a
t
h
e
m
a
t
i
c
a
l
 
e
x
p
r
e
s
s
i
o
n
 
t
o
 
b
e
 
e
v
a
l
u
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
r
e
s
u
l
t
 
o
f
 
t
h
e
 
e
v
a
l
u
a
t
i
o
n
 
o
f
 
t
h
e
 
e
x
p
r
e
s
s
i
o
n
.


 
 
 
 
"
"
"


 
 
 
 
#
 
P
a
r
s
e
 
t
h
e
 
e
x
p
r
e
s
s
i
o
n
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s


 
 
 
 
t
o
k
e
n
s
 
=
 
p
a
r
s
e
_
e
x
p
r
e
s
s
i
o
n
(
e
x
p
r
e
s
s
i
o
n
)




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
s
t
a
c
k
 
o
f
 
o
p
e
r
a
n
d
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s


 
 
 
 
o
p
e
r
a
n
d
s
 
=
 
[
]


 
 
 
 
o
p
e
r
a
t
o
r
s
 
=
 
[
]




 
 
 
 
#
 
I
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
l
i
s
t
 
o
f
 
t
o
k
e
n
s
,
 
p
u
s
h
i
n
g
 
o
p
e
r
a
n
d
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
o
n
t
o
 
t
h
e
 
s
t
a
c
k


 
 
 
 
f
o
r
 
t
o
k
e
n
 
i
n
 
t
o
k
e
n
s
:


 
 
 
 
 
 
 
 
i
f
 
t
o
k
e
n
.
i
s
d
i
g
i
t
(
)
 
o
r
 
t
o
k
e
n
 
=
=
 
"
import unittest


class Tester(unittest.TestCase):

    def test_simple_addition(self):
        expression = "2 + 2"
        result = parse_expression(expression)
        self.assertEqual(result, ["2", "+", "2"])

    def test_complex_expression(self):
        expression = "3 + 5 * (2 - 8)"
        result = parse_expression(expression)
        self.assertEqual(result, ["3", "+", "5", "*", "(", "2", "-", "8", ")"])

    def test_negative_numbers(self):
        expression = "-1 + 4 - 5"
        result = parse_expression(expression)
        self.assertEqual(result, ["-", "1", "+", "4", "-", "5"])

    def test_decimals(self):
        expression = "3.5 + 2.1"
        result = parse_expression(expression)
        self.assertEqual(result, ["3.5", "+", "2.1"])

    def test_operators_only(self):
        expression = "+ - * /"
        result = parse_expression(expression)
        self.assertEqual(result, ["+", "-", "*", "/"])

    def test_empty_expression(self):
        expression = ""
        result = parse_expression(expression)
        self.assertTrue(len(result) == 0)

    def test_single_number(self):
        expression = "42"
        result = parse_expression(expression)
        self.assertEqual(result, ["42"])
if __name__ == '__main__':
    unittest.main()