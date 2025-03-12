d
e
f
 
c
o
n
v
e
r
t
_
t
o
_
s
h
o
r
t
_
f
o
r
m
a
t
(
i
n
p
u
t
_
s
t
r
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
s
t
r
i
n
g
 
c
o
n
c
a
t
e
n
a
t
e
d
 
w
i
t
h
 
u
n
d
e
r
s
c
o
r
e
s
 
t
o
 
a
 
s
h
o
r
t
 
f
o
r
m
a
t
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
f
1
_
p
1
_
g
1
_
b
1
_
c
1


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
f
p
g
b
c


 
 
 
 
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
s
t
r
 
(
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
w
i
t
h
 
s
e
g
m
e
n
t
s
 
s
e
p
a
r
a
t
e
d
 
b
y
 
u
n
d
e
r
s
c
o
r
e
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
 
d
e
r
i
v
e
d
 
f
r
o
m
 
t
h
e
 
f
i
r
s
t
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
e
a
c
h
 
s
e
g
m
e
n
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
 
'
'
.
j
o
i
n
(
[
s
e
g
m
e
n
t
[
0
]
 
f
o
r
 
s
e
g
m
e
n
t
 
i
n
 
i
n
p
u
t
_
s
t
r
.
s
p
l
i
t
(
'
_
'
)
]
)






d
e
f
 
g
e
t
_
s
e
g
m
e
n
t
_
f
r
o
m
_
s
h
o
r
t
_
f
o
r
m
a
t
(
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
,
 
s
e
g
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
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
s
e
g
m
e
n
t
 
f
r
o
m
 
a
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
f
p
g
b
c


 
 
 
 
 
 
 
 
s
e
g
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
:
 
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
f


 
 
 
 
 
 
 
 
s
e
g
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
:
 
1


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
p


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
 
(
s
t
r
)
:
 
T
h
e
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
s
e
g
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
i
n
t
)
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
 
s
e
g
m
e
n
t
 
t
o
 
g
e
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
s
e
g
m
e
n
t
 
a
t
 
t
h
e
 
g
i
v
e
n
 
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
 
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
[
s
e
g
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
]






d
e
f
 
g
e
t
_
s
e
g
m
e
n
t
_
f
r
o
m
_
s
h
o
r
t
_
f
o
r
m
a
t
_
w
i
t
h
_
p
r
e
f
i
x
(
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
,
 
s
e
g
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
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
s
e
g
m
e
n
t
 
f
r
o
m
 
a
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
 
w
i
t
h
 
a
 
p
r
e
f
i
x
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
f
p
g
b
c


 
 
 
 
 
 
 
 
s
e
g
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
:
 
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
f


 
 
 
 
 
 
 
 
s
e
g
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
:
 
1


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
p


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
 
(
s
t
r
)
:
 
T
h
e
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
s
e
g
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
i
n
t
)
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
 
s
e
g
m
e
n
t
 
t
o
 
g
e
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
s
e
g
m
e
n
t
 
a
t
 
t
h
e
 
g
i
v
e
n
 
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
 
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
[
s
e
g
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
]






d
e
f
 
g
e
t
_
s
e
g
m
e
n
t
_
f
r
o
m
_
s
h
o
r
t
_
f
o
r
m
a
t
_
w
i
t
h
_
s
u
f
f
i
x
(
s
h
o
r
t
_
f
o
r
m
a
t
_
s
t
r
,
 
s
e
g
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
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
a
 
s
e
g
m
e
n
t
 
f
r
o
m
 
a
 
s
h
o
r
t
 
f
o
r
m
a
t
 
s
t
r
i
n
g
 
w
i
t
h
 
a
 
s
u
f
f
i
x
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
f
p
g
b
c


 
 
 
 
 
 
 
 
s
e
g
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
:
 
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
f


 
 
 
 
 
 
 
 
s
e
g
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
:
 
1
import unittest


class TestConvertToShortFormat(unittest.TestCase):

    def test_basic_case(self):
        """ Test a standard input with mixed characters. """
        self.assertEqual(convert_to_short_format("f1_p1_g1_b1_c1"), "fpgbc")

    def test_multiple_segments(self):
        """ Test input with multiple segments. """
        self.assertEqual(convert_to_short_format("a2_b3_c4"), "abc")

    def test_non_alpha_numeric(self):
        """ Test input with non-alphanumeric characters. """
        self.assertEqual(convert_to_short_format("hello_world_test"), "hwt")

    def test_single_segment(self):
        """ Test a single segment input. """
        self.assertEqual(convert_to_short_format("single"), "s")

if __name__ == '__main__':
    unittest.main()