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
 
c
a
m
e
l
_
t
o
_
s
n
a
k
e
(
c
a
m
e
l
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
C
a
m
e
l
C
a
s
e
 
s
t
r
i
n
g
 
t
o
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
a
m
e
l
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
 
C
a
m
e
l
C
a
s
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
o
n
v
e
r
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
 
c
o
n
v
e
r
t
e
d
 
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
"
(
?
<
!
^
)
(
?
=
[
A
-
Z
]
)
"
,
 
"
_
"
,
 
c
a
m
e
l
_
s
t
r
)
.
l
o
w
e
r
(
)






d
e
f
 
s
n
a
k
e
_
t
o
_
c
a
m
e
l
(
s
n
a
k
e
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
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
 
s
t
r
i
n
g
 
t
o
 
C
a
m
e
l
C
a
s
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
n
a
k
e
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
n
a
k
e
_
c
a
s
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
o
n
v
e
r
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
 
c
o
n
v
e
r
t
e
d
 
C
a
m
e
l
C
a
s
e
 
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


 
 
 
 
r
e
t
u
r
n
 
"
"
.
j
o
i
n
(
w
o
r
d
.
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
(
)
 
f
o
r
 
w
o
r
d
 
i
n
 
s
n
a
k
e
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
"
_
"
)
)






d
e
f
 
s
n
a
k
e
_
t
o
_
p
a
s
c
a
l
(
s
n
a
k
e
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
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
 
s
t
r
i
n
g
 
t
o
 
P
a
s
c
a
l
C
a
s
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
n
a
k
e
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
n
a
k
e
_
c
a
s
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
o
n
v
e
r
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
 
c
o
n
v
e
r
t
e
d
 
P
a
s
c
a
l
C
a
s
e
 
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


 
 
 
 
r
e
t
u
r
n
 
s
n
a
k
e
_
t
o
_
c
a
m
e
l
(
s
n
a
k
e
_
s
t
r
)
.
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
(
)






d
e
f
 
s
n
a
k
e
_
t
o
_
k
e
b
a
b
(
s
n
a
k
e
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
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
 
s
t
r
i
n
g
 
t
o
 
k
e
b
a
b
-
c
a
s
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
n
a
k
e
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
n
a
k
e
_
c
a
s
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
o
n
v
e
r
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
 
c
o
n
v
e
r
t
e
d
 
k
e
b
a
b
-
c
a
s
e
 
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


 
 
 
 
r
e
t
u
r
n
 
s
n
a
k
e
_
s
t
r
.
r
e
p
l
a
c
e
(
"
_
"
,
 
"
-
"
)






d
e
f
 
s
n
a
k
e
_
t
o
_
c
o
n
s
t
a
n
t
(
s
n
a
k
e
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
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
 
s
t
r
i
n
g
 
t
o
 
C
O
N
S
T
A
N
T
_
C
A
S
E
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
n
a
k
e
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
n
a
k
e
_
c
a
s
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
o
n
v
e
r
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
 
c
o
n
v
e
r
t
e
d
 
C
O
N
S
T
A
N
T
_
C
A
S
E
 
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


 
 
 
 
r
e
t
u
r
n
 
s
n
a
k
e
_
s
t
r
.
u
p
p
e
r
(
)
.
r
e
p
l
a
c
e
(
"
_
"
,
 
"
"
)






d
e
f
 
s
n
a
k
e
_
t
o
_
k
e
b
a
b
_
u
p
p
e
r
(
s
n
a
k
e
_
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
 
a
 
s
n
a
k
e
_
import unittest


class TestCamelToSnake(unittest.TestCase):
    def test_basic_conversion(self):
        """ Test basic CamelCase to snake_case conversion. """
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_multiple_words(self):
        """ Test conversion of a CamelCase string with multiple words. """
        self.assertEqual(camel_to_snake("ThisIsATest"), "this_is_a_test")

    def test_with_numbers(self):
        """ Test conversion with numbers in the string. """
        self.assertEqual(camel_to_snake("ConvertThis123String"), "convert_this123_string")

    def test_leading_uppercase(self):
        """ Test conversion with leading uppercase letters. """
        self.assertEqual(camel_to_snake("PythonFunction"), "python_function")

    def test_empty_string(self):
        """ Test conversion of an empty string. """
        self.assertEqual(camel_to_snake(""), "")

if __name__ == '__main__':
    unittest.main()