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


 
 
 
 
c
o
m
p
o
n
e
n
t
s
 
=
 
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


 
 
 
 
r
e
t
u
r
n
 
c
o
m
p
o
n
e
n
t
s
[
0
]
 
+
 
"
"
.
j
o
i
n
(
x
.
t
i
t
l
e
(
)
 
f
o
r
 
x
 
i
n
 
c
o
m
p
o
n
e
n
t
s
[
1
:
]
)






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
"
(
.
)
(
[
A
-
Z
]
[
a
-
z
]
+
)
"
,
 
r
"
\
1
_
\
2
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
t
i
t
l
e
(
)






d
e
f
 
p
a
s
c
a
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
p
a
s
c
a
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


 
 
 
 
 
 
 
 
p
a
s
c
a
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
p
a
s
c
a
l
_
s
t
r
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
 
r
e
.
s
u
b
(
"
_
(
[
a
-
z
]
)
"
,
 
l
a
m
b
d
a
 
m
a
t
c
h
:
 
m
a
t
c
h
.
g
r
o
u
p
(
1
)
.
u
p
p
e
r
(
)
,
 
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
)




import unittest


class TestSnakeToCamel(unittest.TestCase):
    def test_basic_conversion(self):
        """ Test basic snake_case to CamelCase conversion. """
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_multiple_words(self):
        """ Test conversion of a snake_case string with multiple words. """
        self.assertEqual(snake_to_camel("this_is_a_test"), "ThisIsATest")

    def test_with_numbers(self):
        """ Test conversion with numbers in the string. """
        self.assertEqual(snake_to_camel("convert_this_123_string"), "ConvertThis123String")

    def test_leading_trailing_underscores(self):
        """ Test conversion with leading and trailing underscores. """
        self.assertEqual(snake_to_camel("_leading_and_trailing_"), "LeadingAndTrailing")
        self.assertEqual(snake_to_camel("___multiple___underscores___"), "MultipleUnderscores")

    def test_empty_string(self):
        """ Test conversion of an empty string. """
        self.assertEqual(snake_to_camel(""), "")
if __name__ == '__main__':
    unittest.main()