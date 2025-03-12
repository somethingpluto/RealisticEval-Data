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
p
h
o
n
e
_
n
u
m
b
e
r
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
:


 
 
 
 
"
"
"


 
 
 
 
r
e
p
l
a
c
e
 
a
l
l
 
p
h
o
n
e
s
(
p
h
o
n
e
 
f
o
r
m
a
t
s
 
i
n
 
m
a
n
y
)
 
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
 
w
i
t
h
 
t
h
e
 
s
t
r
i
n
g
 
[
P
H
O
N
E
_
N
U
M
]


 
 
 
 
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
 
C
a
l
l
 
m
e
 
a
t
 
1
2
3
-
4
5
6
-
7
8
9
0
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
C
a
l
l
 
m
e
 
a
t
 
[
P
H
O
N
E
_
N
U
M
]
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
 
t
h
a
t
 
m
a
y
 
c
o
n
t
a
i
n
 
p
h
o
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
 
m
o
d
i
f
i
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
 
p
h
o
n
e
 
n
u
m
b
e
r
s
 
r
e
p
l
a
c
e
d
 
b
y
 
'
[
P
H
O
N
E
_
N
U
M
]
'
.


 
 
 
 
"
"
"


 
 
 
 
p
h
o
n
e
_
p
a
t
t
e
r
n
 
=
 
r
"
(
\
+
?
\
d
{
1
,
3
}
\
s
)
?
\
(
?
\
d
{
3
}
\
)
?
[
\
s
.
-
]
\
d
{
3
}
[
\
s
.
-
]
\
d
{
4
}
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
p
h
o
n
e
_
p
a
t
t
e
r
n
,
 
"
[
P
H
O
N
E
_
N
U
M
]
"
,
 
t
e
x
t
)






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
u
r
l
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
:


 
 
 
 
"
"
"


 
 
 
 
r
e
p
l
a
c
e
 
a
l
l
 
u
r
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
 
w
i
t
h
 
t
h
e
 
s
t
r
i
n
g
 
[
U
R
L
]


 
 
 
 
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
 
C
h
e
c
k
 
o
u
t
 
t
h
i
s
 
w
e
b
s
i
t
e
:
 
h
t
t
p
s
:
/
/
w
w
w
.
e
x
a
m
p
l
e
.
c
o
m
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
C
h
e
c
k
 
o
u
t
 
t
h
i
s
 
w
e
b
s
i
t
e
:
 
[
U
R
L
]
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
 
t
h
a
t
 
m
a
y
 
c
o
n
t
a
i
n
 
u
r
l
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
 
m
o
d
i
f
i
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
 
u
r
l
s
 
r
e
p
l
a
c
e
d
 
b
y
 
'
[
U
R
L
]
'
.


 
 
 
 
"
"
"


 
 
 
 
u
r
l
_
p
a
t
t
e
r
n
 
=
 
r
"
h
t
t
p
s
?
:
/
/
(
w
w
w
\
.
)
?
(
\
w
+
)
(
\
.
\
w
+
)
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
u
r
l
_
p
a
t
t
e
r
n
,
 
"
[
U
R
L
]
"
,
 
t
e
x
t
)






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
e
m
a
i
l
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
:


 
 
 
 
"
"
"


 
 
 
 
r
e
p
l
a
c
e
 
a
l
l
 
e
m
a
i
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
 
w
i
t
h
 
t
h
e
 
s
t
r
i
n
g
 
[
E
M
A
I
L
]


 
 
 
 
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
 
Y
o
u
 
c
a
n
 
c
o
n
t
a
c
t
 
m
e
 
a
t
 
<
E
M
A
I
L
>
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
Y
o
u
 
c
a
n
 
c
o
n
t
a
c
t
 
m
e
 
a
t
 
[
E
M
A
I
L
]
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
 
t
h
a
t
 
m
a
y
 
c
o
n
t
a
i
n
 
e
m
a
i
l
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
 
m
o
d
i
f
i
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
 
e
m
a
i
l
s
 
r
e
p
l
a
c
e
d
 
b
y
 
'
[
E
M
A
I
L
]
'
.


 
 
 
 
"
"
"


 
 
 
 
e
m
a
i
l
_
p
a
t
t
e
r
n
 
=
 
r
"
\
b
[
A
-
Z
a
-
z
0
-
9
.
_
%
+
-
]
+
@
[
A
-
Z
a
-
z
0
-
9
.
-
]
+
\
.
[
A
-
Z
|
a
-
z
]
{
2
,
}
\
b
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
e
m
a
i
l
_
p
a
t
t
e
r
n
,
 
"
[
E
M
A
I
L
]
"
,
 
t
e
x
t
)






d
e
f
import unittest


class TestReplacePhoneNumbers(unittest.TestCase):
    def test_basic_number(self):
        msg = "Call me at 123-456-7890."
        expected = "Call me at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)


    def test_number_with_parentheses(self):
        msg = "Our office number is 123 456-7890."
        expected = "Our office number is [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_number_with_dots(self):
        msg = "Fax us at 123.456.7890."
        expected = "Fax us at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_no_phone_number(self):
        msg = "Hello, please reply to this email."
        expected = "Hello, please reply to this email."
        self.assertEqual(replace_phone_numbers(msg), expected)

if __name__ == '__main__':
    unittest.main()