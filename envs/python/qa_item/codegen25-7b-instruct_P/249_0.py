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
t
e
x
t
_
f
r
o
m
_
p
d
f
(
f
i
l
e
_
p
a
t
h
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
e
x
t
 
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
 
P
D
F
 
f
i
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
P
D
F
 
f
i
l
e
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
e
x
t
r
a
c
t
 
t
e
x
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
 
e
x
t
r
a
c
t
e
d
 
t
e
x
t
 
f
r
o
m
 
t
h
e
 
P
D
F
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
r
b
"
)
 
a
s
 
p
d
f
_
f
i
l
e
:


 
 
 
 
 
 
 
 
p
d
f
_
r
e
a
d
e
r
 
=
 
P
y
P
D
F
2
.
P
d
f
F
i
l
e
R
e
a
d
e
r
(
p
d
f
_
f
i
l
e
)


 
 
 
 
 
 
 
 
t
e
x
t
 
=
 
"
"


 
 
 
 
 
 
 
 
f
o
r
 
p
a
g
e
_
n
u
m
 
i
n
 
r
a
n
g
e
(
p
d
f
_
r
e
a
d
e
r
.
n
u
m
P
a
g
e
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
g
e
 
=
 
p
d
f
_
r
e
a
d
e
r
.
g
e
t
P
a
g
e
(
p
a
g
e
_
n
u
m
)


 
 
 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
+
=
 
p
a
g
e
.
e
x
t
r
a
c
t
T
e
x
t
(
)


 
 
 
 
r
e
t
u
r
n
 
t
e
x
t


`
`
`




T
h
e
 
`
e
x
t
r
a
c
t
_
t
e
x
t
_
f
r
o
m
_
p
d
f
`
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
f
i
l
e
 
p
a
t
h
 
t
o
 
a
 
P
D
F
 
f
i
l
e
 
a
s
 
i
n
p
u
t
,
 
o
p
e
n
s
 
t
h
e
 
f
i
l
e
 
i
n
 
r
e
a
d
-
b
i
n
a
r
y
 
m
o
d
e
,
 
c
r
e
a
t
e
s
 
a
 
`
P
y
P
D
F
2
`
 
r
e
a
d
e
r
 
o
b
j
e
c
t
 
f
o
r
 
t
h
e
 
f
i
l
e
,
 
a
n
d
 
e
x
t
r
a
c
t
s
 
t
e
x
t
 
f
r
o
m
 
e
a
c
h
 
p
a
g
e
 
o
f
 
t
h
e
 
P
D
F
 
u
s
i
n
g
 
t
h
e
 
`
g
e
t
P
a
g
e
`
 
m
e
t
h
o
d
.
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
t
e
x
t
 
i
s
 
t
h
e
n
 
c
o
n
c
a
t
e
n
a
t
e
d
 
f
o
r
 
e
a
c
h
 
p
a
g
e
 
a
n
d
 
r
e
t
u
r
n
e
d
.




N
o
w
 
t
h
a
t
 
w
e
 
h
a
v
e
 
o
u
r
 
f
u
n
c
t
i
o
n
 
r
e
a
d
y
 
t
o
 
e
x
t
r
a
c
t
 
t
e
x
t
 
f
r
o
m
 
a
 
P
D
F
 
f
i
l
e
,
 
l
e
t
'
s
 
u
s
e
 
i
t
 
t
o
 
a
n
a
l
y
z
e
 
t
h
e
 
s
e
n
t
i
m
e
n
t
 
o
f
 
a
 
g
i
v
e
n
 
t
e
x
t
.
 
W
e
 
w
i
l
l
 
u
s
e
 
t
h
e
 
`
n
l
t
k
`
 
l
i
b
r
a
r
y
 
t
o
 
t
o
k
e
n
i
z
e
 
a
n
d
 
c
l
e
a
n
 
t
h
e
 
t
e
x
t
,
 
a
n
d
 
t
h
e
n
 
u
s
e
 
t
h
e
 
`
T
e
x
t
B
l
o
b
`
 
l
i
b
r
a
r
y
 
t
o
 
c
a
l
c
u
l
a
t
e
 
t
h
e
 
s
e
n
t
i
m
e
n
t
 
p
o
l
a
r
i
t
y
 
a
n
d
 
s
u
b
j
e
c
t
i
v
i
t
y
 
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




`
`
`
p
y
t
h
o
n


d
e
f
 
a
n
a
l
y
z
e
_
s
e
n
t
i
m
e
n
t
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
 
t
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
A
n
a
l
y
z
e
s
 
t
h
e
 
s
e
n
t
i
m
e
n
t
 
o
f
 
a
 
g
i
v
e
n
 
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
 
t
e
x
t
 
t
o
 
a
n
a
l
y
z
e
 
s
e
n
t
i
m
e
n
t
 
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


 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
h
e
 
s
e
n
t
i
m
e
n
t
 
p
o
l
a
r
i
t
y
 
a
n
d
 
s
u
b
j
e
c
t
i
v
i
t
y
 
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


 
 
 
 
"
"
"


 
 
 
 
t
e
x
t
 
=
 
t
e
x
t
.
l
o
w
e
r
(
)


 
 
 
 
t
e
x
t
 
=
 
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
[
.
*
?
\
]
'
,
 
'
'
,
 
t
e
x
t
)


 
 
 
 
t
e
x
t
 
=
 
r
e
.
s
u
b
(
r
'
h
t
t
p
s
?
:
\
/
\
/
.
*
[
\
r
\
n
]
*
'
,
 
'
'
,
 
t
e
x
t
)


 
 
 
 
t
e
x
t
 
=
 
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
<
a
 
h
r
e
f
'
,
 
'
 
'
,
 
t
e
x
t
)


 
 
 
 
t
e
x
t
 
=
 
r
e
.
s
u
b
(
r
'
&
a
m
p
;
'
,
 
'
'
,
 
t
e
x
t
)


 
 
 
 
t
e
x
t
 
=
 
r
e
.
s
u
b
(
r
'
[
_
"
\
-
;
%
(
)
|
+
&
=
*
%
.
,
!
?
:
#
$
@
\
[
\
import unittest


class TestExtractTextFromPDF(unittest.TestCase):
    def test_empty_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase01.pdf"
        expected = " \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

    def test_normal_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase02.pdf"
        expected = "11111  \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

    def test_more_text_file(self):
        pdf_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase03.pdf"
        expected = "11111  \n22222  \n33333  \n44444  \n"
        output = extract_text_from_pdf(pdf_path)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()