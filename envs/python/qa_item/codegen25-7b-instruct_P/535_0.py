d
e
f
 
c
o
m
p
r
e
s
s
_
h
t
m
l
(
h
t
m
l
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
m
p
r
e
s
s
e
s
 
a
n
 
H
T
M
L
 
s
t
r
i
n
g
 
b
y
 
r
e
m
o
v
i
n
g
 
u
n
n
e
c
e
s
s
a
r
y
 
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
,


 
 
 
 
i
n
c
l
u
d
i
n
g
 
n
e
w
l
i
n
e
s
,
 
t
a
b
s
,
 
a
n
d
 
e
x
t
r
a
 
s
p
a
c
e
s
,


 
 
 
 
w
h
i
l
e
 
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
 
s
t
r
u
c
t
u
r
e
 
o
f
 
t
h
e
 
H
T
M
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
t
m
l
 
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
 
H
T
M
L
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
e
d
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
m
p
r
e
s
s
e
d
 
H
T
M
L
 
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
 
r
e
d
u
c
e
d
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
i
n
i
f
y
(
h
t
m
l
,
 
r
e
m
o
v
e
_
a
l
l
_
e
m
p
t
y
_
s
p
a
c
e
=
T
r
u
e
)






d
e
f
 
c
o
m
p
r
e
s
s
_
c
s
s
(
c
s
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


 
 
 
 
C
o
m
p
r
e
s
s
e
s
 
a
 
C
S
S
 
s
t
r
i
n
g
 
b
y
 
r
e
m
o
v
i
n
g
 
u
n
n
e
c
e
s
s
a
r
y
 
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
,


 
 
 
 
i
n
c
l
u
d
i
n
g
 
n
e
w
l
i
n
e
s
,
 
t
a
b
s
,
 
a
n
d
 
e
x
t
r
a
 
s
p
a
c
e
s
,


 
 
 
 
w
h
i
l
e
 
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
 
s
t
r
u
c
t
u
r
e
 
o
f
 
t
h
e
 
C
S
S
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
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
 
i
n
p
u
t
 
C
S
S
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
e
d
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
m
p
r
e
s
s
e
d
 
C
S
S
 
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
 
r
e
d
u
c
e
d
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
i
n
i
f
y
(
c
s
s
,
 
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
=
T
r
u
e
,
 
r
e
m
o
v
e
_
a
l
l
_
e
m
p
t
y
_
s
p
a
c
e
=
T
r
u
e
)






d
e
f
 
c
o
m
p
r
e
s
s
_
j
s
(
j
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


 
 
 
 
C
o
m
p
r
e
s
s
e
s
 
a
 
J
a
v
a
S
c
r
i
p
t
 
s
t
r
i
n
g
 
b
y
 
r
e
m
o
v
i
n
g
 
u
n
n
e
c
e
s
s
a
r
y
 
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
,


 
 
 
 
i
n
c
l
u
d
i
n
g
 
n
e
w
l
i
n
e
s
,
 
t
a
b
s
,
 
a
n
d
 
e
x
t
r
a
 
s
p
a
c
e
s
,


 
 
 
 
w
h
i
l
e
 
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
 
s
t
r
u
c
t
u
r
e
 
o
f
 
t
h
e
 
J
a
v
a
S
c
r
i
p
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
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
 
J
a
v
a
S
c
r
i
p
t
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
e
d
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
m
p
r
e
s
s
e
d
 
J
a
v
a
S
c
r
i
p
t
 
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
 
r
e
d
u
c
e
d
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
i
n
i
f
y
(
j
s
,
 
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
=
T
r
u
e
,
 
r
e
m
o
v
e
_
a
l
l
_
e
m
p
t
y
_
s
p
a
c
e
=
T
r
u
e
)






d
e
f
 
c
o
m
p
r
e
s
s
_
j
s
o
n
(
j
s
o
n
_
d
a
t
a
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
m
p
r
e
s
s
e
s
 
a
 
J
S
O
N
 
s
t
r
i
n
g
 
b
y
 
r
e
m
o
v
i
n
g
 
u
n
n
e
c
e
s
s
a
r
y
 
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
,


 
 
 
 
i
n
c
l
u
d
i
n
g
 
n
e
w
l
i
n
e
s
,
 
t
a
b
s
,
 
a
n
d
 
e
x
t
r
a
 
s
p
a
c
e
s
,


 
 
 
 
w
h
i
l
e
 
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
 
s
t
r
u
c
t
u
r
e
 
o
f
 
t
h
e
 
J
S
O
N
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
_
d
a
t
a
 
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
 
J
S
O
N
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
e
d
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
m
p
r
e
s
s
e
d
 
J
S
O
N
 
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
 
r
e
d
u
c
e
d
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
m
i
n
i
f
y
(
j
s
o
n
_
d
a
t
a
,
 
r
e
m
o
v
e
_
a
l
l
_
e
m
p
t
y
_
s
p
a
c
e
=
T
r
u
e
)






d
e
f
 
c
o
m
p
r
e
s
s
_
x
m
l
(
x
m
l
_
d
a
t
a
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
m
p
r
e
s
s
e
s
 
a
n
 
X
M
L
 
s
t
r
i
n
g
 
b
y
 
r
e
m
o
v
i
n
g
 
u
n
n
e
c
e
s
s
a
r
y
 
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
,


 
 
 
 
i
n
c
l
u
d
i
n
g
 
n
e
w
l
i
n
e
s
,
 
t
a
b
s
,
 
a
n
d
 
e
x
t
r
a
 
s
p
a
c
e
s
,


 
 
 
 
w
h
i
l
e
 
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
 
s
t
r
u
c
t
u
r
e
 
o
f
 
t
h
e
 
X
M
L
.




 
 
 
 
A
r
g
s
:
import unittest


class TestCompressHtml(unittest.TestCase):

    def test_remove_newlines_and_tabs(self):
        input_html = """            <div>                <p>Test paragraph.</p>            </div>        """
        expected_output = '<div><p>Test paragraph.</p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_replace_multiple_spaces(self):
        input_html = '<div>    <p>     Test with     multiple spaces.   </p></div>'
        expected_output = '<div><p> Test with multiple spaces. </p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_remove_spaces_between_tags(self):
        input_html = '<div> <p>Test</p> </div>'
        expected_output = '<div><p>Test</p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_handle_empty_input(self):
        input_html = ''
        expected_output = ''
        self.assertEqual(compress_html(input_html), expected_output)

    def test_handle_html_with_only_spaces_and_newlines(self):
        input_html = """            <div>                  </div>        """
        expected_output = '<div></div>'
        self.assertEqual(compress_html(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()