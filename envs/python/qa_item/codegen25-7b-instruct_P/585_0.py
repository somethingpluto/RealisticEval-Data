d
e
f
 
i
s
_
c
a
m
e
l
_
c
a
s
e
(
i
n
p
u
t
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


 
 
 
 
D
e
t
e
c
t
s
 
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
 
s
t
r
i
n
g
 
i
s
 
i
n
 
C
A
M
E
L
_
C
A
S
E
.




 
 
 
 
I
n
 
C
A
M
E
L
_
C
A
S
E
,
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
o
f
 
t
h
e
 
f
i
r
s
t
 
w
o
r
d
 
i
s
 
l
o
w
e
r
c
a
s
e
,


 
 
 
 
a
n
d
 
e
a
c
h
 
s
u
b
s
e
q
u
e
n
t
 
w
o
r
d
 
s
t
a
r
t
s
 
w
i
t
h
 
a
n
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
,
 
w
i
t
h
 
n
o
 
s
p
a
c
e
s
 
o
r
 
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


 
 
 
 
s
e
p
a
r
a
t
i
n
g
 
t
h
e
 
w
o
r
d
s
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
t
r
i
n
g
 
t
o
 
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
i
s
 
i
n
 
C
A
M
E
L
_
C
A
S
E
,
 
o
t
h
e
r
w
i
s
e
 
F
a
l
s
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
a
-
z
]
[
a
-
z
A
-
Z
0
-
9
]
*
$
"
,
 
i
n
p
u
t
)
)






d
e
f
 
i
s
_
s
n
a
k
e
_
c
a
s
e
(
i
n
p
u
t
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


 
 
 
 
D
e
t
e
c
t
s
 
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
 
s
t
r
i
n
g
 
i
s
 
i
n
 
S
N
A
K
E
_
C
A
S
E
.




 
 
 
 
I
n
 
S
N
A
K
E
_
C
A
S
E
,
 
e
a
c
h
 
w
o
r
d
 
i
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
 
a
n
 
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
,
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
w
o
r
d


 
 
 
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
a
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r
,
 
a
n
d
 
e
a
c
h
 
s
u
b
s
e
q
u
e
n
t
 
w
o
r
d
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
a
n
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
,


 
 
 
 
w
i
t
h
 
n
o
 
s
p
a
c
e
s
 
o
r
 
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
 
s
e
p
a
r
a
t
i
n
g
 
t
h
e
 
w
o
r
d
s
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
t
r
i
n
g
 
t
o
 
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
i
s
 
i
n
 
S
N
A
K
E
_
C
A
S
E
,
 
o
t
h
e
r
w
i
s
e
 
F
a
l
s
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
a
-
z
]
[
a
-
z
A
-
Z
0
-
9
]
*
(
?
:
_
[
a
-
z
A
-
Z
0
-
9
]
+
)
*
$
"
,
 
i
n
p
u
t
)
)






d
e
f
 
i
s
_
k
e
b
a
b
_
c
a
s
e
(
i
n
p
u
t
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


 
 
 
 
D
e
t
e
c
t
s
 
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
 
s
t
r
i
n
g
 
i
s
 
i
n
 
K
E
B
A
B
_
C
A
S
E
.




 
 
 
 
I
n
 
K
E
B
A
B
_
C
A
S
E
,
 
e
a
c
h
 
w
o
r
d
 
i
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
 
a
 
d
a
s
h
,
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
w
o
r
d


 
 
 
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
a
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r
,
 
a
n
d
 
e
a
c
h
 
s
u
b
s
e
q
u
e
n
t
 
w
o
r
d
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
a
n
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
,


 
 
 
 
w
i
t
h
 
n
o
 
s
p
a
c
e
s
 
o
r
 
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
 
s
e
p
a
r
a
t
i
n
g
 
t
h
e
 
w
o
r
d
s
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
t
r
i
n
g
 
t
o
 
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
i
s
 
i
n
 
K
E
B
A
B
_
C
A
S
E
,
 
o
t
h
e
r
w
i
s
e
 
F
a
l
s
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
a
-
z
]
[
a
-
z
A
-
Z
0
-
9
]
*
(
?
:
-
[
a
-
z
A
-
Z
0
-
9
]
+
)
*
$
"
,
 
i
n
p
u
t
import unittest


class TestIsCamelCase(unittest.TestCase):

    def test_valid_camel_case(self):
        """Should return true for a valid camelCase string."""
        self.assertTrue(is_camel_case('camelCase'))

    def test_valid_camel_case_multiple_words(self):
        """Should return true for a valid camelCase string with multiple words."""
        self.assertTrue(is_camel_case('camelCaseExample'))

    def test_uppercase_start(self):
        """Should return false for a string that starts with an uppercase letter."""
        self.assertFalse(is_camel_case('CamelCase'))

    def test_underscores(self):
        """Should return false for a string with underscores."""
        self.assertFalse(is_camel_case('camel_case'))

    def test_empty_string(self):
        """Should return false for an empty string."""
        self.assertFalse(is_camel_case(''))

if __name__ == '__main__':
    unittest.main()