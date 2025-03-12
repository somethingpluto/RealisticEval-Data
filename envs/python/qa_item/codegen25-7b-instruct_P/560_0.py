d
e
f
 
g
e
t
_
l
i
n
e
_
n
u
m
b
e
r
(
c
o
n
t
e
n
t
:
 
s
t
r
,
 
i
n
d
e
x
:
 
i
n
t
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
n
u
m
b
e
r
 
i
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
 
a
t
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
i
n
d
e
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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
 
c
o
n
t
e
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
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
 
c
h
a
r
a
c
t
e
r
 
i
n
d
e
x
 
t
o
 
f
i
n
d
 
t
h
e
 
l
i
n
e
 
n
u
m
b
e
r
 
f
o
r
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
l
i
n
e
 
n
u
m
b
e
r
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
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
 
c
o
n
t
e
n
t
.
c
o
u
n
t
(
"
\
n
"
,
 
0
,
 
i
n
d
e
x
)
 
+
 
1






d
e
f
 
g
e
t
_
l
i
n
e
_
r
a
n
g
e
(
c
o
n
t
e
n
t
:
 
s
t
r
,
 
s
t
a
r
t
:
 
i
n
t
,
 
e
n
d
:
 
i
n
t
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
r
a
n
g
e
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
i
n
d
i
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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
 
c
o
n
t
e
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
s
t
a
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
 
s
t
a
r
t
 
i
n
d
e
x
.


 
 
 
 
 
 
 
 
e
n
d
 
(
i
n
t
)
:
 
T
h
e
 
e
n
d
 
i
n
d
e
x
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:
 
T
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
l
i
n
e
 
n
u
m
b
e
r
s
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
l
i
n
e
 
=
 
g
e
t
_
l
i
n
e
_
n
u
m
b
e
r
(
c
o
n
t
e
n
t
,
 
s
t
a
r
t
)


 
 
 
 
e
n
d
_
l
i
n
e
 
=
 
g
e
t
_
l
i
n
e
_
n
u
m
b
e
r
(
c
o
n
t
e
n
t
,
 
e
n
d
)


 
 
 
 
r
e
t
u
r
n
 
s
t
a
r
t
_
l
i
n
e
,
 
e
n
d
_
l
i
n
e






d
e
f
 
g
e
t
_
l
i
n
e
_
c
o
n
t
e
n
t
(
c
o
n
t
e
n
t
:
 
s
t
r
,
 
s
t
a
r
t
:
 
i
n
t
,
 
e
n
d
:
 
i
n
t
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
 
t
h
e
 
l
i
n
e
 
c
o
n
t
e
n
t
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
i
n
d
i
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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
 
c
o
n
t
e
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
s
t
a
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
 
s
t
a
r
t
 
i
n
d
e
x
.


 
 
 
 
 
 
 
 
e
n
d
 
(
i
n
t
)
:
 
T
h
e
 
e
n
d
 
i
n
d
e
x
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
 
l
i
n
e
 
c
o
n
t
e
n
t
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
l
i
n
e
,
 
e
n
d
_
l
i
n
e
 
=
 
g
e
t
_
l
i
n
e
_
r
a
n
g
e
(
c
o
n
t
e
n
t
,
 
s
t
a
r
t
,
 
e
n
d
)


 
 
 
 
r
e
t
u
r
n
 
c
o
n
t
e
n
t
.
s
p
l
i
t
(
"
\
n
"
)
[
s
t
a
r
t
_
l
i
n
e
 
-
 
1
 
:
 
e
n
d
_
l
i
n
e
]






d
e
f
 
g
e
t
_
l
i
n
e
_
i
n
d
i
c
e
s
(
c
o
n
t
e
n
t
:
 
s
t
r
,
 
s
t
a
r
t
:
 
i
n
t
,
 
e
n
d
:
 
i
n
t
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
t
h
e
 
l
i
n
e
 
i
n
d
i
c
e
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
i
n
d
i
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
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
 
c
o
n
t
e
n
t
 
t
o
 
c
h
e
c
k
.


 
 
 
 
 
 
 
 
s
t
a
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
 
s
t
a
r
t
 
i
n
d
e
x
.


 
 
 
 
 
 
 
 
e
n
d
 
(
i
n
t
)
:
 
T
h
e
 
e
n
d
 
i
n
d
e
x
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:
 
T
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
l
i
n
e
 
i
n
d
i
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
l
i
n
e
,
 
e
n
d
_
l
i
n
e
 
=
 
g
e
t
_
l
i
n
e
_
r
a
n
g
e
(
c
o
n
t
e
n
t
import unittest


class TestGetLineNumber(unittest.TestCase):

    def test_returns_1_for_first_character(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 0), 1)

    def test_returns_1_for_last_character_of_first_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 5), 1)

    def test_returns_3_for_last_character_of_third_line(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3", 18), 3)

    def test_returns_1_for_single_line_string(self):
        self.assertEqual(get_line_number("Single line string", 0), 1)

    def test_returns_3_for_index_in_multiline_string_with_trailing_newlines(self):
        self.assertEqual(get_line_number("Line 1\nLine 2\nLine 3\n\n", 15), 3)

if __name__ == '__main__':
    unittest.main()