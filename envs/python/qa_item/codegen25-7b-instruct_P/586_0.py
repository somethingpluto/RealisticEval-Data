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
 
a
l
l
 
l
e
t
t
e
r
s
 
a
r
e
 
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
 
w
o
r
d
s
 
a
r
e
 
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


 
 
 
 
T
h
e
r
e
 
s
h
o
u
l
d
 
b
e
 
n
o
 
l
e
a
d
i
n
g
 
o
r
 
t
r
a
i
l
i
n
g
 
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
,
 
a
n
d
 
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
 
o
t
h
e
r
 
s
p
e
c
i
a
l
 
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
_
]
[
a
-
z
0
-
9
_
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
 
i
s
 
n
o
t
 
N
o
n
e






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
-
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
-
C
A
S
E
,
 
a
l
l
 
l
e
t
t
e
r
s
 
a
r
e
 
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
 
w
o
r
d
s
 
a
r
e
 
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
 
d
a
s
h
e
s
.


 
 
 
 
T
h
e
r
e
 
s
h
o
u
l
d
 
b
e
 
n
o
 
l
e
a
d
i
n
g
 
o
r
 
t
r
a
i
l
i
n
g
 
d
a
s
h
e
s
,
 
a
n
d
 
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
 
o
t
h
e
r
 
s
p
e
c
i
a
l
 
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
-
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
0
-
9
-
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
 
i
s
 
n
o
t
 
N
o
n
e






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
-
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
-
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
 
c
a
p
i
t
a
l
i
z
e
d
,
 
a
n
d
 
w
o
r
d
s
 
a
r
e
 
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
s
.


 
 
 
 
T
h
e
r
e
 
s
h
o
u
l
d
 
b
e
 
n
o
 
l
e
a
d
i
n
g
 
o
r
 
t
r
a
i
l
i
n
g
 
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
s
,
 
a
n
d
 
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
 
o
t
h
e
r
 
s
p
e
c
i
a
l
 
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
-
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
A
-
Z
]
[
a
-
z
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
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
i
s
_
p
a
s
c
a
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
 
P
A
S
C
A
L
-
C
A
S
E
.




 
 
 
 
I
n
 
P
A
S
C
A
L
-
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
import unittest


class TestIsSnakeCase(unittest.TestCase):

    def test_valid_snake_case(self):
        """should return true for a valid snake_case string"""
        self.assertTrue(is_snake_case('snake_case'))

    def test_valid_snake_case_multiple_words(self):
        """should return true for a valid snake_case string with multiple words"""
        self.assertTrue(is_snake_case('snake_case_example'))

    def test_uppercase_start(self):
        """should return false for a string that starts with an uppercase letter"""
        self.assertFalse(is_snake_case('Snake_Case'))

    def test_mixed_case_letters(self):
        """should return false for a string with mixed case letters"""
        self.assertFalse(is_snake_case('snakeCASE'))

    def test_string_with_numbers(self):
        """should return false for a string with numbers"""
        self.assertFalse(is_snake_case('snake_case_123'))

    def test_empty_string(self):
        """should return false for an empty string"""
        self.assertFalse(is_snake_case(''))

if __name__ == '__main__':
    unittest.main()