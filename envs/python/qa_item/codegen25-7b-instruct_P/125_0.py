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
_
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
 
w
i
t
h
o
u
t
 
d
i
s
r
u
p
t
i
n
g


 
 
 
 
t
h
e
 
i
n
t
e
g
r
i
t
y
 
o
f
 
c
o
n
t
e
n
t
 
w
i
t
h
i
n
 
<
p
r
e
>
,
 
<
d
i
v
>
,
 
<
s
c
r
i
p
t
>
,
 
a
n
d
 
<
s
t
y
l
e
>
 
t
a
g
s
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
 
'
 
 
 
<
d
i
v
>
 
 
 
C
o
n
t
e
n
t
 
 
<
/
d
i
v
>
 
 
 
'


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
'
<
d
i
v
>
 
C
o
n
t
e
n
t
 
<
/
d
i
v
>
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
t
m
l
_
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
 
t
o
 
c
o
m
p
r
e
s
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


 
 
 
 
r
e
t
u
r
n
 
_
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
_
s
t
r
i
n
g
,
 
F
a
l
s
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
h
t
m
l
_
w
i
t
h
_
p
r
e
t
t
i
e
r
(
h
t
m
l
_
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


 
 
 
 
c
o
n
t
e
n
t
 
w
i
t
h
i
n
 
<
p
r
e
>
,
 
<
d
i
v
>
,
 
<
s
c
r
i
p
t
>
,
 
a
n
d
 
<
s
t
y
l
e
>
 
t
a
g
s
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
 
'
 
 
 
<
d
i
v
>
 
 
 
C
o
n
t
e
n
t
 
 
<
/
d
i
v
>
 
 
 
'


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
'
<
d
i
v
>
\
n
 
 
 
 
C
o
n
t
e
n
t
\
n
<
/
d
i
v
>
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
t
m
l
_
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
 
t
o
 
c
o
m
p
r
e
s
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


 
 
 
 
r
e
t
u
r
n
 
_
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
_
s
t
r
i
n
g
,
 
T
r
u
e
)






d
e
f
 
_
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
_
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
,
 
w
i
t
h
_
p
r
e
t
t
i
e
r
:
 
b
o
o
l
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


 
 
 
 
c
o
n
t
e
n
t
 
w
i
t
h
i
n
 
<
p
r
e
>
,
 
<
d
i
v
>
,
 
<
s
c
r
i
p
t
>
,
 
a
n
d
 
<
s
t
y
l
e
>
 
t
a
g
s
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
 
'
 
 
 
<
d
i
v
>
 
 
 
C
o
n
t
e
n
t
 
 
<
/
d
i
v
>
 
 
 
'


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
'
<
d
i
v
>
\
n
 
 
 
 
C
o
n
t
e
n
t
\
n
<
/
d
i
v
>
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
t
m
l
_
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
 
t
o
 
c
o
m
p
r
e
s
s
.


 
 
 
 
 
 
 
 
w
i
t
h
_
p
r
e
t
t
i
e
r
 
(
b
o
o
l
)
:
 
W
h
e
t
h
e
r
 
t
o
 
u
s
e
 
t
h
e
 
p
r
e
t
t
i
e
r
 
l
i
b
r
a
r
y
 
t
o
 
f
o
r
m
a
t
 
t
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
o
u
p
 
=
 
B
e
a
u
t
i
f
u
l
S
o
u
p
(
h
t
m
l
_
s
t
r
i
n
g
,
 
"
h
t
m
l
.
p
a
r
s
e
r
"
)


 
 
 
 
f
o
r
 
t
a
g
 
i
n
 
s
o
u
p
.
f
i
n
d
_
a
l
l
(
[
"
p
r
e
"
,
 
"
d
i
v
"
,
 
"
s
c
r
i
p
t
"
,
 
"
s
t
y
l
e
"
]
)
:


 
 
 
 
 
 
 
 
t
a
g
.
s
t
r
i
n
g
 
=
 
_
c
o
m
p
r
e
s
s
_
s
t
r
i
n
g
(
t
a
g
.
s
t
r
i
n
g
,
 
w
i
t
h
_
p
r
e
t
t
i
e
r
)
import unittest


class TestCompressHTML(unittest.TestCase):

    def test_remove_leading_and_trailing_spaces_around_tags(self):
        input_html = '  <div>  <p>Test</p>  </div>  '
        expected = '<div><p>Test</p></div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_replace_multiple_newlines_with_single_space(self):
        input_html = '<div>\n\n<p>Test</p>\n\n</div>'
        expected = '<div> <p>Test</p> </div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_remove_unnecessary_spaces_within_text(self):
        input_html = '<p>This    is a test</p>'
        expected = '<p>This is a test</p>'
        self.assertEqual(compress_html(input_html), expected)

    def test_handle_empty_strings(self):
        input_html = ''
        expected = ''
        self.assertEqual(compress_html(input_html), expected)

    def test_process_complex_nested_html_correctly(self):
        input_html = '<div>   <span>    Text <i>    Italic </i> more text </span>   </div>'
        expected = '<div><span>Text <i>Italic</i> more text</span></div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_not_disrupt_content_within_pre_and_textarea_tags(self):
        input_html = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'
        expected = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'
        self.assertEqual(compress_html(input_html), expected)

    def test_handle_html_with_attributes_correctly(self):
        input_html = '<a href="http://example.com"    title="Example" >Link</a>'
        expected = '<a href="http://example.com" title="Example">Link</a>'
        self.assertEqual(compress_html(input_html), expected)

if __name__ == '__main__':
    unittest.main()