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
 
C
a
l
l
a
b
l
e






i
m
p
o
r
t
 
i
n
s
p
e
c
t






d
e
f
 
m
e
t
h
o
d
_
a
r
g
_
t
y
p
e
_
c
h
e
c
k
(
m
e
t
h
o
d
_
o
b
j
,
 
*
a
r
g
s
,
 
*
*
k
w
a
r
g
s
)
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
t
h
a
t
 
t
h
e
 
a
r
g
u
m
e
n
t
s
 
p
a
s
s
e
d
 
t
o
 
a
 
g
i
v
e
n
 
m
e
t
h
o
d
 
o
b
j
e
c
t
 
(
e
.
g
.
,
 
m
e
t
h
o
d
 
o
f
 
a
 
c
l
a
s
s
)
 
c
o
m
p
l
y
 
w
i
t
h
 
t
h
e
i
r


 
 
 
 
e
x
p
e
c
t
e
d
 
q
u
e
s
t
i
o
n
 
t
y
p
e
s
,
 
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
 
m
e
t
h
o
d
'
s
 
s
i
g
n
a
t
u
r
e
.
j
s
.
p
y
.
p
y
.
p
y
.
p
y
.
j
s
.
j
s
.
j
s
.
 
I
f
 
t
h
e
r
e
'
s
 
a
 
d
i
s
c
r
e
p
a
n
c
y
,
 
i
t
 
r
a
i
s
e
s
 
a
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
e
t
h
o
d
_
o
b
j
 
(
C
a
l
l
a
b
l
e
)
:
 
T
h
e
 
m
e
t
h
o
d
 
f
o
r
 
w
h
i
c
h
 
a
r
g
u
m
e
n
t
s
 
a
r
e
 
c
h
e
c
k
e
d
.


 
 
 
 
 
 
 
 
*
a
r
g
s
 
(
)
:
 
P
o
s
i
t
i
o
n
a
l
 
a
r
g
u
m
e
n
t
s
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d
.


 
 
 
 
 
 
 
 
*
*
k
w
a
r
g
s
 
(
)
:
 
K
e
y
w
o
r
d
 
a
r
g
u
m
e
n
t
s
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d
.






 
 
 
 
O
p
t
i
o
n
a
l
 
a
r
g
u
m
e
n
t
:


 
 
 
 
 
 
 
 
e
x
c
l
u
d
e
 
(
l
i
s
t
 
o
f
 
s
t
r
)
:
 
N
a
m
e
s
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
e
x
c
l
u
d
e
 
f
r
o
m
 
t
h
e
 
t
y
p
e
 
c
h
e
c
k
.




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
m
e
t
h
o
d
 
s
i
g
n
a
t
u
r
e


 
 
 
 
s
i
g
n
a
t
u
r
e
 
=
 
i
n
s
p
e
c
t
.
s
i
g
n
a
t
u
r
e
(
m
e
t
h
o
d
_
o
b
j
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
 
=
 
s
i
g
n
a
t
u
r
e
.
p
a
r
a
m
e
t
e
r
s




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
 
=
 
l
i
s
t
(
p
a
r
a
m
s
.
k
e
y
s
(
)
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
a
r
g
s
_
l
i
s
t
 
=
 
l
i
s
t
(
a
r
g
s
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
k
w
a
r
g
s
_
l
i
s
t
 
=
 
l
i
s
t
(
k
w
a
r
g
s
.
k
e
y
s
(
)
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
 
=
 
p
a
r
a
m
s
_
l
i
s
t
 
+
 
a
r
g
s
_
l
i
s
t
 
+
 
k
w
a
r
g
s
_
l
i
s
t




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
 
=
 
s
e
t
(
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
_
n
o
_
v
a
r
_
k
e
y
w
o
r
d
 
=
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
 
-
 
s
e
t
(
[
'
*
*
k
w
a
r
g
s
'
]
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
_
n
o
_
v
a
r
_
k
e
y
w
o
r
d
_
n
o
_
v
a
r
_
p
o
s
i
t
i
o
n
a
l
 
=
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
_
n
o
_
v
a
r
_
k
e
y
w
o
r
d
 
-
 
s
e
t
(
[
'
*
a
r
g
s
'
]
)




 
 
 
 
#
 
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
p
a
s
s
e
d
 
t
o
 
t
h
e
 
m
e
t
h
o
d


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
_
a
l
l
_
s
e
t
_
n
o
_
v
a
r
_
k
e
y
w
o
r
d
_
n
o
_
v
a
r
_
import unittest
from typing import Callable


class MyClass:
    def my_method(self, arg1: int, arg2: str, optional_arg: float = 3.14):
        pass


class TestMethodArgTypeCheck(unittest.TestCase):
    def test_correct_types(self):
        """ Test with correct argument types. """
        try:
            method_arg_type_check(MyClass.my_method, MyClass(), 10, "hello", optional_arg=3.14)
        except ValueError:
            self.fail("method_arg_type_check() raised ValueError unexpectedly!")

    def test_missing_argument(self):
        """ Test with missing required argument. """
        with self.assertRaises(TypeError):
            method_arg_type_check(MyClass.my_method, MyClass(), 10)  # Missing arg2

if __name__ == '__main__':
    unittest.main()