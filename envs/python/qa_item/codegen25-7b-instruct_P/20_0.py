i
m
p
o
r
t
 
r
e






d
e
f
 
r
e
m
o
v
e
_
i
n
n
e
r
_
a
s
t
e
r
i
s
k
s
(
t
e
x
t
:
 
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


 
 
 
 
T
r
a
n
s
f
o
r
m
s
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
 
b
y
 
f
i
n
d
i
n
g
 
a
n
d
 
m
o
d
i
f
y
i
n
g
 
p
a
t
t
e
r
n
s
 
t
h
a
t
 
m
a
t
c
h
 
t
h
e
 
f
o
r
m
a
t
 
'
(
*
.
.
.
*
)
'
.


 
 
 
 
S
p
e
c
i
f
i
c
a
l
l
y
,
 
i
t
 
r
e
m
o
v
e
s
 
a
n
y
 
a
s
t
e
r
i
s
k
s
 
i
n
s
i
d
e
 
t
h
e
 
p
a
r
e
n
t
h
e
s
e
s
 
w
h
i
l
e
 
p
r
e
s
e
r
v
i
n
g
 
t
h
e
 
o
u
t
e
r
 
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
 
*
h
e
*
l
*
l
o
*


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
*
h
e
l
l
o
*




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
t
 
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
 
t
e
x
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
 
p
a
t
t
e
r
n
s
 
t
o
 
b
e
 
t
r
a
n
s
f
o
r
m
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
t
r
a
n
s
f
o
r
m
e
d
 
t
e
x
t
 
w
i
t
h
 
a
s
t
e
r
i
s
k
s
 
i
n
s
i
d
e
 
'
(
*
.
.
.
*
)
'
 
p
a
t
t
e
r
n
s
 
r
e
m
o
v
e
d
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
 
r
e
.
s
u
b
(
r
'
\
*
(
[
^
*
]
*
)
\
*
'
,
 
r
'
\
1
'
,
 
t
e
x
t
)






d
e
f
 
r
e
m
o
v
e
_
i
n
n
e
r
_
a
s
t
e
r
i
s
k
s
_
a
n
d
_
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
(
t
e
x
t
:
 
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


 
 
 
 
T
r
a
n
s
f
o
r
m
s
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
 
b
y
 
f
i
n
d
i
n
g
 
a
n
d
 
m
o
d
i
f
y
i
n
g
 
p
a
t
t
e
r
n
s
 
t
h
a
t
 
m
a
t
c
h
 
t
h
e
 
f
o
r
m
a
t
 
'
(
*
_
.
.
.
_
*
)
'
.


 
 
 
 
S
p
e
c
i
f
i
c
a
l
l
y
,
 
i
t
 
r
e
m
o
v
e
s
 
a
n
y
 
a
s
t
e
r
i
s
k
s
 
a
n
d
 
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
 
i
n
s
i
d
e
 
t
h
e
 
p
a
r
e
n
t
h
e
s
e
s
 
w
h
i
l
e
 
p
r
e
s
e
r
v
i
n
g
 
t
h
e
 
o
u
t
e
r
 
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
 
*
_
h
e
_
*
_
l
_
*
_
l
o
_
*


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
*
_
h
e
l
l
o
_
*




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
t
 
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
 
t
e
x
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
 
p
a
t
t
e
r
n
s
 
t
o
 
b
e
 
t
r
a
n
s
f
o
r
m
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
t
r
a
n
s
f
o
r
m
e
d
 
t
e
x
t
 
w
i
t
h
 
a
s
t
e
r
i
s
k
s
 
a
n
d
 
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
 
i
n
s
i
d
e
 
'
(
*
_
.
.
.
_
*
)
'
 
p
a
t
t
e
r
n
s
 
r
e
m
o
v
e
d
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
 
r
e
.
s
u
b
(
r
'
\
*
_
(
[
^
*
_
]
*
)
\
_
\
*
'
,
 
r
'
\
1
'
,
 
t
e
x
t
)






d
e
f
 
r
e
m
o
v
e
_
i
n
n
e
r
_
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
(
t
e
x
t
:
 
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


 
 
 
 
T
r
a
n
s
f
o
r
m
s
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
 
b
y
 
f
i
n
d
i
n
g
 
a
n
d
 
m
o
d
i
f
y
i
n
g
 
p
a
t
t
e
r
n
s
 
t
h
a
t
 
m
a
t
c
h
 
t
h
e
 
f
o
r
m
a
t
 
'
_
.
.
.
_
'
.


 
 
 
 
S
p
e
c
i
f
i
c
a
l
l
y
,
 
i
t
 
r
e
m
o
v
e
s
 
a
n
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
 
i
n
s
i
d
e
 
t
h
e
 
p
a
r
e
n
t
h
e
s
e
s
 
w
h
i
l
e
 
p
r
e
s
e
r
v
i
n
g
 
t
h
e
 
o
u
t
e
r
 
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
 
_
h
e
_
l
_
l
o
_


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
_
h
e
l
l
o
_




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
t
 
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
 
t
e
x
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
 
p
a
t
t
e
r
n
s
 
t
o
 
b
e
 
t
r
a
n
s
f
o
r
m
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
t
r
a
n
s
f
o
r
m
e
d
 
t
e
x
t
 
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
 
i
n
s
i
d
e
 
'
_
.
.
.
_
'
 
p
a
t
t
e
r
n
s
 
r
e
m
o
v
e
d
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
 
r
e
.
s
u
b
(
r
'
_
(
[
^
_
]
*
)
_
'
,
 
r
'
\
1
'
,
 
t
e
x
t
)






d
e
f
 
r
e
m
o
v
e
_
i
n
n
e
r
_
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
_
a
n
d
_
a
s
t
e
r
i
s
k
s
(
t
e
x
t
:
 
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


 
 
 
import unittest
import re


class TestTransformParentheses(unittest.TestCase):

    def test_basic_case(self):
        text = "Hello (*wo*rld*)!"
        expected = "Hello (*world*)!"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_multiple_asterisks(self):
        text = "(*he*l*lo*)"
        expected = "(*hello*)"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_no_asterisks_inside(self):
        text = "(*hello*)"
        expected = "(*hello*)"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_multiple_patterns(self):
        text = "(*hi*), (*there*), (*world*)!"
        expected = "(*hi*), (*there*), (*world*)!"
        self.assertEqual(remove_inner_asterisks(text), expected)

    def test_no_matching_pattern(self):
        text = "This is a test without matching parentheses."
        expected = "This is a test without matching parentheses."
        self.assertEqual(remove_inner_asterisks(text), expected)

if __name__ == '__main__':
    unittest.main()