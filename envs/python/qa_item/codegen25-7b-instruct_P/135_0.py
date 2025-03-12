d
e
f
 
i
s
_
v
a
l
i
d
_
p
o
r
t
_
n
u
m
b
e
r
(
p
o
r
t
:
 
i
n
t
)
 
-
>
 
b
o
o
l
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
 
i
f
 
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
 
p
o
r
t
 
n
u
m
b
e
r
 
i
s
 
w
i
t
h
i
n
 
t
h
e
 
v
a
l
i
d
 
r
a
n
g
e
 
o
f
 
T
C
P
/
U
D
P
 
p
o
r
t
s
.


 
 
 
 


 
 
 
 
V
a
l
i
d
 
T
C
P
/
U
D
P
 
p
o
r
t
 
n
u
m
b
e
r
s
 
r
a
n
g
e
 
f
r
o
m
 
1
 
t
o
 
6
5
5
3
5
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
r
t
 
(
i
n
t
)
:
 
T
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
t
o
 
v
e
r
i
f
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
R
e
t
u
r
n
s
 
T
r
u
e
 
i
f
 
t
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
T
y
p
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
i
s
 
n
o
t
 
a
n
 
i
n
t
e
g
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
p
o
r
t
,
 
i
n
t
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
T
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
m
u
s
t
 
b
e
 
a
n
 
i
n
t
e
g
e
r
.
"
)


 
 
 
 
r
e
t
u
r
n
 
1
 
<
=
 
p
o
r
t
 
<
=
 
6
5
5
3
5




d
e
f
 
i
s
_
v
a
l
i
d
_
i
p
_
a
d
d
r
e
s
s
(
i
p
_
a
d
d
r
e
s
s
:
 
s
t
r
)
 
-
>
 
b
o
o
l
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
 
i
f
 
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
 
I
P
 
a
d
d
r
e
s
s
 
i
s
 
a
 
v
a
l
i
d
 
I
P
v
4
 
o
r
 
I
P
v
6
 
a
d
d
r
e
s
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
p
_
a
d
d
r
e
s
s
 
(
s
t
r
)
:
 
T
h
e
 
I
P
 
a
d
d
r
e
s
s
 
t
o
 
v
e
r
i
f
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
R
e
t
u
r
n
s
 
T
r
u
e
 
i
f
 
t
h
e
 
I
P
 
a
d
d
r
e
s
s
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
T
y
p
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
I
P
 
a
d
d
r
e
s
s
 
i
s
 
n
o
t
 
a
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
i
p
_
a
d
d
r
e
s
s
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
T
h
e
 
I
P
 
a
d
d
r
e
s
s
 
m
u
s
t
 
b
e
 
a
 
s
t
r
i
n
g
.
"
)


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
i
p
a
d
d
r
e
s
s
.
i
p
_
a
d
d
r
e
s
s
(
i
p
_
a
d
d
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
e
x
c
e
p
t
 
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


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




d
e
f
 
i
s
_
v
a
l
i
d
_
i
p
_
n
e
t
w
o
r
k
(
i
p
_
n
e
t
w
o
r
k
:
 
s
t
r
)
 
-
>
 
b
o
o
l
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
 
i
f
 
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
 
I
P
 
n
e
t
w
o
r
k
 
i
s
 
a
 
v
a
l
i
d
 
I
P
v
4
 
o
r
 
I
P
v
6
 
n
e
t
w
o
r
k
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
p
_
n
e
t
w
o
r
k
 
(
s
t
r
)
:
 
T
h
e
 
I
P
 
n
e
t
w
o
r
k
 
t
o
 
v
e
r
i
f
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
R
e
t
u
r
n
s
 
T
r
u
e
 
i
f
 
t
h
e
 
I
P
 
n
e
t
w
o
r
k
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
T
y
p
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
I
P
 
n
e
t
w
o
r
k
 
i
s
 
n
o
t
 
a
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
i
p
_
n
e
t
w
o
r
k
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
T
h
e
 
I
P
 
n
e
t
w
o
r
k
 
m
u
s
t
 
b
e
 
a
 
s
t
r
i
n
g
.
"
)


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
i
p
a
d
d
r
e
s
s
.
i
p
_
n
e
t
w
o
r
k
(
i
p
_
n
e
t
w
o
r
k
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
e
x
c
e
p
t
 
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


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




d
e
f
 
i
s
_
v
a
l
i
d
_
i
p
_
r
a
n
g
e
(
i
p
_
r
a
n
g
e
:
 
s
t
r
)
 
-
>
 
b
o
o
l
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
 
i
f
 
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
 
I
P
 
r
a
n
g
e
 
i
s
 
a
 
v
a
l
i
d
 
I
P
v
4
 
o
r
 
I
P
v
6
 
r
a
n
g
e
.




 
 
 
 
A
r
g
s
:
import unittest


class TestIsValidPortNumber(unittest.TestCase):

    def test_valid_port_number_middle(self):
        """Returns true for a valid port number in the middle of the range."""
        self.assertTrue(is_valid_port_number(8080))

    def test_lowest_valid_port_number(self):
        """Returns true for the lowest valid port number."""
        self.assertTrue(is_valid_port_number(1))

    def test_highest_valid_port_number(self):
        """Returns true for the highest valid port number."""
        self.assertTrue(is_valid_port_number(65535))

    def test_below_valid_range(self):
        """Returns false for a port number below the valid range."""
        self.assertFalse(is_valid_port_number(0))

    def test_above_valid_range(self):
        """Returns false for a port number above the valid range."""
        self.assertFalse(is_valid_port_number(65536))

if __name__ == '__main__':
    unittest.main()