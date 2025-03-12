d
e
f
 
e
x
t
r
a
c
t
_
o
u
t
e
r
m
o
s
t
_
b
r
a
c
k
e
t
s
(
s
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
 
f
r
o
m
 
t
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
 
T
e
x
t
 
[
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s
]
 
a
n
d
 
m
o
r
e
 
t
e
x
t


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
b
r
a
c
k
e
t
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
 
T
h
e
 
c
o
n
t
e
n
t
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
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
b
r
a
c
k
e
t
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
f
i
r
s
t
 
o
p
e
n
i
n
g
 
b
r
a
c
k
e
t


 
 
 
 
s
t
a
r
t
 
=
 
s
.
f
i
n
d
(
"
[
"
)


 
 
 
 
i
f
 
s
t
a
r
t
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"


 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
f
i
r
s
t
 
c
l
o
s
i
n
g
 
b
r
a
c
k
e
t


 
 
 
 
e
n
d
 
=
 
s
.
f
i
n
d
(
"
]
"
)


 
 
 
 
i
f
 
e
n
d
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"


 
 
 
 
#
 
R
e
t
u
r
n
 
t
h
e
 
c
o
n
t
e
n
t
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
 
b
r
a
c
k
e
t
s


 
 
 
 
r
e
t
u
r
n
 
s
[
s
t
a
r
t
 
+
 
1
 
:
 
e
n
d
]






d
e
f
 
e
x
t
r
a
c
t
_
o
u
t
e
r
m
o
s
t
_
b
r
a
c
k
e
t
s
_
r
e
g
e
x
(
s
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
 
f
r
o
m
 
t
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
 
u
s
i
n
g
 
r
e
g
e
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
 
T
e
x
t
 
[
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s
]
 
a
n
d
 
m
o
r
e
 
t
e
x
t


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
b
r
a
c
k
e
t
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
 
T
h
e
 
c
o
n
t
e
n
t
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
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
b
r
a
c
k
e
t
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
f
i
r
s
t
 
o
p
e
n
i
n
g
 
b
r
a
c
k
e
t


 
 
 
 
m
a
t
c
h
 
=
 
r
e
.
s
e
a
r
c
h
(
r
"
\
[
(
.
*
?
)
\
]
"
,
 
s
)


 
 
 
 
i
f
 
m
a
t
c
h
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"


 
 
 
 
#
 
R
e
t
u
r
n
 
t
h
e
 
c
o
n
t
e
n
t
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
 
b
r
a
c
k
e
t
s


 
 
 
 
r
e
t
u
r
n
 
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






d
e
f
 
e
x
t
r
a
c
t
_
o
u
t
e
r
m
o
s
t
_
b
r
a
c
k
e
t
s
_
r
e
g
e
x
_
g
r
o
u
p
(
s
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
 
f
r
o
m
 
t
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
 
u
s
i
n
g
 
r
e
g
e
x
 
a
n
d
 
a
 
c
a
p
t
u
r
i
n
g
 
g
r
o
u
p
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
 
T
e
x
t
 
[
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s
]
 
a
n
d
 
m
o
r
e
 
t
e
x
t


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
w
i
t
h
 
[
n
e
s
t
e
d
]
 
b
r
a
c
k
e
t
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
b
r
a
c
k
e
t
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
 
T
h
e
 
c
o
n
t
e
n
t
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
 
o
u
t
e
r
m
o
s
t
 
b
r
a
c
k
e
t
s
,
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
b
r
a
c
k
e
t
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
f
i
r
s
t
 
o
p
e
n
i
n
g
 
b
r
a
c
k
e
t


 
 
 
 
m
a
t
c
h
 
=
 
r
e
.
s
e
a
r
c
h
(
r
"
\
import unittest


class TestExtractOutermostBrackets(unittest.TestCase):
    
    def test_single_parentheses(self):
        self.assertEqual(extract_outermost_brackets("Text (example) more text"), "example")

    def test_nested_brackets(self):
        self.assertEqual(extract_outermost_brackets("Text {with some {nested} brackets}"), "with some {nested} brackets")

    def test_square_brackets(self):
        self.assertEqual(extract_outermost_brackets("Text [with [nested] brackets] and more text"), "with [nested] brackets")

    def test_mixed_bracket_types(self):
        self.assertEqual(extract_outermost_brackets("Mixed (types {of brackets [in use]})"), "types {of brackets [in use]}")

    def test_no_brackets(self):
        self.assertEqual(extract_outermost_brackets("No brackets here"), "")
if __name__ == '__main__':
    unittest.main()