d
e
f
 
r
e
p
l
a
c
e
_
h
t
m
l
_
e
n
t
i
t
i
e
s
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


 
 
 
 
D
e
c
o
d
e
s
 
H
T
M
L
 
e
n
t
i
t
i
e
s
 
i
n
 
a
 
g
i
v
e
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
 
e
n
t
i
t
i
e
s
 
t
o
 
d
e
c
o
d
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
 
d
e
c
o
d
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
 
H
T
M
L
 
e
n
t
i
t
i
e
s
 
c
o
n
v
e
r
t
e
d
 
b
a
c
k
 
t
o
 
t
h
e
i
r
 
o
r
i
g
i
n
a
l
 
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
u
n
e
s
c
a
p
e
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
h
t
m
l
_
t
a
g
s
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


 
 
 
 
R
e
m
o
v
e
s
 
H
T
M
L
 
t
a
g
s
 
f
r
o
m
 
a
 
g
i
v
e
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
 
t
a
g
s
 
t
o
 
r
e
m
o
v
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
 
H
T
M
L
 
t
a
g
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
"
<
[
^
<
]
+
?
>
"
,
 
"
"
,
 
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
h
t
m
l
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


 
 
 
 
R
e
m
o
v
e
s
 
H
T
M
L
 
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
 
a
 
g
i
v
e
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
 
c
o
m
m
e
n
t
s
 
t
o
 
r
e
m
o
v
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
 
H
T
M
L
 
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
"
<
!
-
-
[
^
<
]
+
?
-
-
>
"
,
 
"
"
,
 
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
h
t
m
l
_
a
t
t
r
i
b
u
t
e
s
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


 
 
 
 
R
e
m
o
v
e
s
 
H
T
M
L
 
a
t
t
r
i
b
u
t
e
s
 
f
r
o
m
 
a
 
g
i
v
e
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
 
a
t
t
r
i
b
u
t
e
s
 
t
o
 
r
e
m
o
v
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
 
H
T
M
L
 
a
t
t
r
i
b
u
t
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
"
<
[
^
<
]
+
?
(
?
:
[
^
>
]
+
?
)
?
>
"
,
 
"
"
,
 
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
h
t
m
l
_
s
c
r
i
p
t
s
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


 
 
 
 
R
e
m
o
v
e
s
 
H
T
M
L
 
s
c
r
i
p
t
s
 
f
r
o
m
 
a
 
g
i
v
e
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
 
s
c
r
i
p
t
s
 
t
o
 
r
e
m
o
v
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
 
H
T
M
L
 
s
c
r
i
p
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
"
<
s
c
r
i
p
t
[
^
<
]
+
?
<
/
s
c
r
i
p
t
>
"
,
 
"
"
,
 
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
h
t
m
l
_
s
t
y
l
e
s
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


 
 
 
 
R
e
m
o
v
e
s
import unittest


class TestReplaceHtmlEntities(unittest.TestCase):

    def test_decodes_standard_html_entities(self):
        input_string = 'The &amp; symbol should become an &quot;and&quot; sign.'
        expected = 'The & symbol should become an "and" sign.'
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_returns_empty_string_for_empty_input(self):
        input_string = ''
        expected = ''
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_decodes_multiple_different_entities_in_one_string(self):
        input_string = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;'
        expected = '<div>Hello & Welcome to the \'World\'!</div>'
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_handles_strings_with_no_entities(self):
        input_string = 'Just a normal string without entities.'
        expected = 'Just a normal string without entities.'
        self.assertEqual(replace_html_entities(input_string), expected)

if __name__ == '__main__':
    unittest.main()