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
e
n
t
s
(
s
t
r
i
n
g
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
 
c
o
m
m
e
n
t
s
 
f
r
o
m
 
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
 
s
t
r
i
n
g
.
 
C
o
m
m
e
n
t
s
 
s
t
a
r
t
 
w
i
t
h
 
a
 
'
#
'
 
a
n
d
 
e
n
d
 
a
t
 
t
h
e
 
n
e
w
l
i
n
e
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
 
H
e
l
l
o
,
 
w
o
r
l
d
!
 
#
 
T
h
i
s
 
i
s
 
a
 
c
o
m
m
e
n
t


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
 
H
e
l
l
o
,
 
w
o
r
l
d
!


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
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
 
p
o
t
e
n
t
i
a
l
 
c
o
m
m
e
n
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
 
a
l
l
 
c
o
m
m
e
n
t
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
#
.
*
\
n
'
,
 
'
'
,
 
s
t
r
i
n
g
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
w
h
i
t
e
s
p
a
c
e
(
s
t
r
i
n
g
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
 
a
l
l
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
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
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
H
e
l
l
o
,
w
o
r
l
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
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
 
p
o
t
e
n
t
i
a
l
 
w
h
i
t
e
s
p
a
c
e
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
t
r
i
n
g
 
w
i
t
h
 
a
l
l
 
w
h
i
t
e
s
p
a
c
e
 
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
s
+
'
,
 
'
'
,
 
s
t
r
i
n
g
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
n
e
w
l
i
n
e
s
(
s
t
r
i
n
g
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
 
a
l
l
 
n
e
w
l
i
n
e
s
 
f
r
o
m
 
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
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
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
 
p
o
t
e
n
t
i
a
l
 
n
e
w
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
t
r
i
n
g
 
w
i
t
h
 
a
l
l
 
n
e
w
l
i
n
e
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
n
'
,
 
'
'
,
 
s
t
r
i
n
g
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
t
r
a
i
l
i
n
g
_
w
h
i
t
e
s
p
a
c
e
(
s
t
r
i
n
g
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
 
a
l
l
 
t
r
a
i
l
i
n
g
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
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
 
H
e
l
l
o
,
 
w
o
r
l
d
 
 


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
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
 
p
o
t
e
n
t
i
a
l
 
t
r
a
i
l
i
n
g
 
w
h
i
t
e
s
p
a
c
e
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
t
r
i
n
g
 
w
i
t
h
 
a
l
l
 
t
r
a
i
l
i
n
g
 
w
h
i
t
e
s
p
a
c
e
 
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
s
+
$
'
,
 
'
'
,
 
s
t
r
i
n
g
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
l
e
a
d
i
n
g
_
w
h
i
t
e
s
p
a
c
e
(
s
t
r
i
n
g
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
 
a
l
l
 
l
e
a
d
i
n
g
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
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
 
 
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
H
e
l
l
o
,
 
w
o
r
l
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
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
 
p
o
t
e
n
t
i
a
l
 
l
e
a
d
i
n
g
import unittest


class TestRemoveComments(unittest.TestCase):

    def test_single_line_comment(self):
        """ Test string with a comment on a single line """
        input_string = "Hello, world!# This is a comment"
        expected_output = "Hello, world!"
        self.assertEqual(remove_comments(input_string), expected_output)


    def test_no_comments(self):
        """ Test string with no comments """
        input_string = "Hello, world!\nPython is fun!"
        expected_output = "Hello, world!\nPython is fun!"
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_empty_string(self):
        """ Test an empty string """
        input_string = ""
        expected_output = ""
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_comments_only(self):
        """ Test string where all lines are comments """
        input_string = "# comment only line\n#another comment line"
        expected_output = "\n"
        self.assertEqual(remove_comments(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()