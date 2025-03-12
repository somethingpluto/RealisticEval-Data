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
c
o
m
m
o
n
_
i
n
d
e
n
t
a
t
i
o
n
(
m
u
l
t
i
l
i
n
e
_
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


 
 
 
 
R
e
m
o
v
e
s
 
t
h
e
 
c
o
m
m
o
n
 
l
e
a
d
i
n
g
 
i
n
d
e
n
t
a
t
i
o
n
 
f
r
o
m
 
e
a
c
h
 
l
i
n
e
 
i
n
 
a
 
g
i
v
e
n
 
m
u
l
t
i
-
l
i
n
e
 
s
t
r
i
n
g
,


 
 
 
 
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
 
r
e
l
a
t
i
v
e
 
i
n
d
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
t
e
x
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
u
l
t
i
l
i
n
e
_
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
 
m
u
l
t
i
p
l
e
 
l
i
n
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
 
T
h
e
 
s
a
n
i
t
i
z
e
d
 
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
 
c
o
m
m
o
n
 
l
e
a
d
i
n
g
 
i
n
d
e
n
t
a
t
i
o
n
 
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


 
 
 
 
l
i
n
e
s
 
=
 
m
u
l
t
i
l
i
n
e
_
t
e
x
t
.
s
p
l
i
t
l
i
n
e
s
(
)


 
 
 
 
i
f
 
l
e
n
(
l
i
n
e
s
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
u
l
t
i
l
i
n
e
_
t
e
x
t


 
 
 
 
m
i
n
_
i
n
d
e
n
t
 
=
 
m
i
n
(
l
e
n
(
l
i
n
e
)
 
-
 
l
e
n
(
l
i
n
e
.
l
s
t
r
i
p
(
)
)
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
)


 
 
 
 
r
e
t
u
r
n
 
"
\
n
"
.
j
o
i
n
(
l
i
n
e
[
m
i
n
_
i
n
d
e
n
t
:
]
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
)






d
e
f
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
s
p
a
c
e
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
.




 
 
 
 
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
 
s
t
r
i
n
g
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
 
n
u
m
b
e
r
 
o
f
 
s
p
a
c
e
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
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
 
l
e
n
(
t
e
x
t
)
 
-
 
l
e
n
(
t
e
x
t
.
l
s
t
r
i
p
(
)
)






d
e
f
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
_
s
p
a
c
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


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
s
p
a
c
e
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
.




 
 
 
 
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
 
s
t
r
i
n
g
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
 
n
u
m
b
e
r
 
o
f
 
s
p
a
c
e
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
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
 
*
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
(
t
e
x
t
)






d
e
f
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
_
t
a
b
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


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
t
a
b
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
f
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
.




 
 
 
 
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
 
s
t
r
i
n
g
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
 
n
u
m
b
e
r
 
o
f
 
t
a
b
s
 
i
n
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
o
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
\
t
"
 
*
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
(
t
e
x
t
)






d
e
f
 
g
e
t
_
i
n
d
e
n
t
a
t
i
o
n
_
l
e
v
e
l
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
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
i
n
d
e
n
t
a
t
i
o
n
 
l
e
v
e
l
s
 
i
n
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
.




 
 
 
 
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
 
s
t
r
i
n
g
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
 
n
u
m
b
e
r
 
o
f
 
i
n
d
e
n
t
a
t
i
o
n
 
l
e
v
e
l
s
 
i
n
 
t
h
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
import unittest

class TestRemoveCommonIndentation(unittest.TestCase):

    def test_empty_string(self):
        # Testing edge case with an empty string
        self.assertEqual(remove_common_indentation(""), "", "Should return an empty string")

    def test_single_line_string(self):
        # Testing a single line with no indentation
        self.assertEqual(remove_common_indentation("No indentation here"), "No indentation here", "Should return the same string as input")

    def test_multiple_lines_with_uniform_indentation(self):
        # Testing basic logic with uniform indentation across multiple lines
        input_text = "    Line one\n    Line two\n    Line three"
        expected_output = "Line one\nLine two\nLine three"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should remove common leading indentation")

    def test_multiple_lines_with_mixed_indentation(self):
        # Testing lines with mixed indentation levels
        input_text = "  Line one\n  Line two\n  Line three"
        expected_output = "Line one\nLine two\nLine three"
        self.assertEqual(remove_common_indentation(input_text), expected_output, "Should remove the minimum common indentation")


if __name__ == '__main__':
    unittest.main()