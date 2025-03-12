d
e
f
 
c
o
n
v
e
r
t
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
n
v
e
r
t
s
 
a
 
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
 
H
T
M
L
 
t
o
 
a
 
M
a
r
k
d
o
w
n
-
f
o
r
m
a
t
t
e
d
 
s
t
r
i
n
g
.




 
 
 
 
1
.
 
L
i
n
e
 
b
r
e
a
k
s
 
(
<
b
r
>
 
o
r
 
<
b
r
/
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
n
e
w
l
i
n
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
s
.


 
 
 
 
2
.
 
P
a
r
a
g
r
a
p
h
s
 
(
<
p
>
 
a
n
d
 
<
/
p
>
)
:
 
O
p
e
n
i
n
g
 
<
p
>
 
t
a
g
s
 
a
r
e
 
r
e
m
o
v
e
d
,
 
w
h
i
l
e
 
c
l
o
s
i
n
g


 
 
 
 
 
 
 
 
<
/
p
>
 
t
a
g
s
 
a
r
e
 
r
e
p
l
a
c
e
d
 
w
i
t
h
 
t
w
o
 
n
e
w
l
i
n
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
s
 
t
o
 
s
e
p
a
r
a
t
e
 
p
a
r
a
g
r
a
p
h
s
.


 
 
 
 
3
.
 
S
t
r
o
n
g
 
e
m
p
h
a
s
i
s
 
(
<
s
t
r
o
n
g
>
 
a
n
d
 
<
/
s
t
r
o
n
g
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
d
o
u
b
l
e
 
a
s
t
e
r
i
s
k
s
 
(
*
*
)
.


 
 
 
 
4
.
 
I
t
a
l
i
c
s
 
(
<
e
m
>
 
a
n
d
 
<
/
e
m
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
s
i
n
g
l
e
 
a
s
t
e
r
i
s
k
s
 
(
*
)
.


 
 
 
 
5
.
 
U
n
d
e
r
l
i
n
e
d
 
t
e
x
t
 
(
<
u
>
 
a
n
d
 
<
/
u
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
s
i
n
g
l
e
 
a
s
t
e
r
i
s
k
s
 
(
*
)


 
 
 
 
 
 
 
 
a
s
 
u
n
d
e
r
l
i
n
i
n
g
 
i
s
 
n
o
t
 
s
u
p
p
o
r
t
e
d
 
i
n
 
M
a
r
k
d
o
w
n
.


 
 
 
 
6
.
 
C
o
d
e
 
s
n
i
p
p
e
t
s
 
(
<
c
o
d
e
>
 
a
n
d
 
<
/
c
o
d
e
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
b
a
c
k
t
i
c
k
s
 
(
`
)
.


 
 
 
 
7
.
 
U
n
o
r
d
e
r
e
d
 
l
i
s
t
s
 
(
<
u
l
>
 
a
n
d
 
<
/
u
l
>
)
:
 
O
p
e
n
i
n
g
 
a
n
d
 
c
l
o
s
i
n
g
 
t
a
g
s
 
a
r
e
 
r
e
m
o
v
e
d
.


 
 
 
 
8
.
 
O
r
d
e
r
e
d
 
l
i
s
t
s
 
(
<
o
l
>
 
a
n
d
 
<
/
o
l
>
)
:
 
O
p
e
n
i
n
g
 
a
n
d
 
c
l
o
s
i
n
g
 
t
a
g
s
 
a
r
e
 
r
e
m
o
v
e
d
.


 
 
 
 
9
.
 
L
i
s
t
 
i
t
e
m
s
 
(
<
l
i
>
)
:
 
O
p
e
n
i
n
g
 
<
l
i
>
 
t
a
g
s
 
a
r
e
 
r
e
p
l
a
c
e
d
 
w
i
t
h
 
a
n
 
a
s
t
e
r
i
s
k
 
f
o
l
l
o
w
e
d


 
 
 
 
 
 
 
 
b
y
 
a
 
s
p
a
c
e
,
 
w
h
i
l
e
 
c
l
o
s
i
n
g
 
<
/
l
i
>
 
t
a
g
s
 
a
r
e
 
r
e
p
l
a
c
e
d
 
w
i
t
h
 
a
 
n
e
w
l
i
n
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
.


 
 
 
 
1
0
.
 
H
y
p
e
r
l
i
n
k
s
 
(
<
a
 
h
r
e
f
=
"
.
.
.
"
>
.
.
.
<
/
a
>
)
:
 
R
e
p
l
a
c
e
d
 
w
i
t
h
 
t
h
e
 
M
a
r
k
d
o
w
n
 
f
o
r
m
a
t


 
 
 
 
 
 
 
 
[
t
e
x
t
]
(
U
R
L
)
,
 
w
h
e
r
e
 
"
t
e
x
t
"
 
i
s
 
t
h
e
 
a
n
c
h
o
r
 
t
e
x
t
 
a
n
d
 
"
U
R
L
"
 
i
s
 
t
h
e
 
l
i
n
k
 
t
a
r
g
e
t
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
 
H
T
M
L
 
c
o
n
t
e
n
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
 
A
 
s
t
r
i
n
g
 
f
o
r
m
a
t
t
e
d
 
i
n
 
M
a
r
k
d
o
w
n
,
 
r
e
f
l
e
c
t
i
n
g
 
t
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
u
c
t
u
r
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
R
e
p
l
a
c
e
 
l
i
n
e
 
b
r
e
a
k
s
 
w
i
t
h
 
n
e
w
l
i
n
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
s


 
 
 
 
h
t
m
l
 
=
 
r
e
.
s
u
b
(
r
"
<
b
r
/
?
>
"
,
 
"
\
n
"
,
 
h
t
m
l
)




 
 
 
 
#
 
R
e
m
o
v
e
 
p
a
r
a
g
r
a
p
h
 
t
a
g
s
 
a
n
d
 
r
e
p
l
a
c
e
 
w
i
t
h
 
t
w
o
 
n
e
w
l
i
n
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
s


 
 
 
 
h
t
m
l
 
=
 
r
e
.
s
u
b
(
r
"
<
p
>
|
<
/
p
>
"
,
 
"
\
n
\
n
"
,
 
h
t
m
l
)




 
 
 
 
#
 
R
e
p
l
a
c
e
 
s
t
r
o
n
g
 
e
m
p
h
a
s
i
s
 
t
a
g
s
 
w
i
t
h
 
d
o
u
b
l
e
 
a
s
t
e
r
i
s
k
s


 
 
 
 
h
t
m
l
 
=
 
r
e
.
s
u
b
(
r
"
<
s
t
r
o
n
g
>
|
<
/
s
t
r
o
n
g
>
"
,
 
"
*
*
"
,
 
h
t
m
l
)




 
 
 
 
#
 
R
e
p
l
a
c
e
 
i
t
a
l
i
c
s
 
t
a
g
s
 
w
i
t
h
 
s
i
n
g
l
e
 
a
s
t
e
r
i
s
k
s


 
 
 
 
h
t
m
l
 
=
 
r
e
.
s
u
b
(
r
"
<
e
m
>
|
<
/
e
m
>
"
,
 
"
*
"
,
 
h
t
m
l
)




 
 
 
 
#
 
R
e
p
l
a
c
e
import unittest

class TestAnswer(unittest.TestCase):
    
    def test_simple_line_break(self):
        input_html = "Hello<br>World"
        expected_output = "Hello\nWorld"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_strong_tags(self):
        input_html = "This is <strong>important</strong> text."
        expected_output = "This is **important** text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_emphasis_tags(self):
        input_html = "This is <em>emphasized</em> text."
        expected_output = "This is *emphasized* text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_unordered_list(self):
        input_html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        expected_output = "* Item 1\n* Item 2"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_anchor_tags(self):
        input_html = 'Check this link: <a href="http://example.com">Example</a>.'
        expected_output = 'Check this link: [Example](http://example.com).'
        self.assertEqual(expected_output, convert(input_html))
if __name__ == '__main__':
    unittest.main()