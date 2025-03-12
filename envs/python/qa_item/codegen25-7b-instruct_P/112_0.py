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
_
h
t
m
l
_
h
e
a
d
i
n
g
s
_
t
o
_
m
a
r
k
d
o
w
n
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
 
H
T
M
L
 
h
e
a
d
i
n
g
 
t
a
g
s
 
(
h
1
-
h
6
)
 
t
o
 
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
 
M
a
r
k
d
o
w
n
 
h
e
a
d
i
n
g
s
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
 
h
e
a
d
i
n
g
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
v
e
r
t
e
d
 
M
a
r
k
d
o
w
n
 
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
 
h
t
m
l
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
<
h
1
>
"
,
 
"
#
 
"
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
<
/
h
1
>
"
,
 
"
\
n
"
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
<
h
2
>
"
,
 
"
#
#
 
"
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
<
/
h
2
>
"
,
 
"
\
n
"
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
<
h
3
>
"
,
 
"
#
#
#
 
"
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
<
/
h
3
>
"
,
 
"
\
n
"
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
<
h
4
>
"
,
 
"
#
#
#
#
 
"
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
<
/
h
4
>
"
,
 
"
\
n
"
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
<
h
5
>
"
,
 
"
#
#
#
#
#
 
"
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
<
/
h
5
>
"
,
 
"
\
n
"
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
<
h
6
>
"
,
 
"
#
#
#
#
#
#
 
"
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
<
/
h
6
>
"
,
 
"
\
n
"
)




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
_
h
t
m
l
_
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
_
t
o
_
m
a
r
k
d
o
w
n
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
 
H
T
M
L
 
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
 
(
p
)
 
t
o
 
M
a
r
k
d
o
w
n
 
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
 
M
a
r
k
d
o
w
n
 
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
 
h
t
m
l
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
<
p
>
"
,
 
"
"
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
<
/
p
>
"
,
 
"
\
n
"
)




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
_
h
t
m
l
_
l
i
s
t
s
_
t
o
_
m
a
r
k
d
o
w
n
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
 
H
T
M
L
 
o
r
d
e
r
e
d
 
a
n
d
 
u
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
o
l
 
a
n
d
 
u
l
)
 
t
o
 
M
a
r
k
d
o
w
n
 
l
i
s
t
s
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
 
l
i
s
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
v
e
r
t
e
d
 
M
a
r
k
d
o
w
n
 
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
 
h
t
m
l
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
<
o
l
>
"
,
 
"
"
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
<
/
o
l
>
"
,
 
"
"
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
<
u
l
>
"
,
 
"
"
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
<
/
u
l
>
"
,
 
"
"
)




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
_
h
t
m
l
_
l
i
n
k
s
_
t
o
_
m
a
r
k
d
o
w
n
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
 
H
T
M
L
 
l
i
n
k
s
 
t
o
 
M
a
r
k
d
o
w
n
 
l
i
n
k
s
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
 
l
i
n
k
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
v
e
r
t
e
d
 
M
a
r
k
d
o
w
n
 
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
 
h
t
m
l
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
<
a
 
h
r
e
f
=
"
,
 
"
[
"
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
>
"
,
 
"
]
"
)
import unittest


class TestConvertHtmlHeadingsToMarkdown(unittest.TestCase):

    def test_convert_h1_to_markdown(self):
        input_html = '<h1>This is a Heading 1</h1>'
        expected_output = '# This is a Heading 1'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h2_to_markdown(self):
        input_html = '<h2>This is a Heading 2</h2>'
        expected_output = '## This is a Heading 2'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h3_to_markdown(self):
        input_html = '<h3>This is a Heading 3</h3>'
        expected_output = '### This is a Heading 3'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h4_to_markdown(self):
        input_html = '<h4>This is a Heading 4</h4>'
        expected_output = '#### This is a Heading 4'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h5_to_markdown(self):
        input_html = '<h5>This is a Heading 5</h5>'
        expected_output = '##### This is a Heading 5'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h6_to_markdown(self):
        input_html = '<h6>This is a Heading 6</h6>'
        expected_output = '###### This is a Heading 6'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()