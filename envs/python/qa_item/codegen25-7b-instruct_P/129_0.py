d
e
f
 
i
s
_
v
a
l
i
d
_
u
r
l
(
u
r
l
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
V
a
l
i
d
a
t
e
s
 
a
 
U
R
L
 
s
t
r
i
n
g
 
u
s
i
n
g
 
a
 
s
i
m
p
l
i
f
i
e
d
 
a
n
d
 
c
o
m
p
r
e
h
e
n
s
i
v
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
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
 
U
R
L
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
U
R
L
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
r
e
g
e
x
 
=
 
r
e
.
c
o
m
p
i
l
e
(


 
 
 
 
 
 
 
 
r
"
^
(
?
:
h
t
t
p
|
f
t
p
)
s
?
:
/
/
"
 
 
#
 
h
t
t
p
:
/
/
 
o
r
 
h
t
t
p
s
:
/
/


 
 
 
 
 
 
 
 
r
"
(
?
:
(
?
:
[
A
-
Z
0
-
9
]
(
?
:
[
A
-
Z
0
-
9
-
]
{
0
,
6
1
}
[
A
-
Z
0
-
9
]
)
?
\
.
)
+
(
?
:
[
A
-
Z
]
{
2
,
6
}
\
.
?
|
[
A
-
Z
0
-
9
-
]
{
2
,
}
\
.
?
)
|
"
 
 
#
 
d
o
m
a
i
n
.
.
.


 
 
 
 
 
 
 
 
r
"
l
o
c
a
l
h
o
s
t
|
"
 
 
#
 
l
o
c
a
l
h
o
s
t
.
.
.


 
 
 
 
 
 
 
 
r
"
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
\
.
\
d
{
1
,
3
}
)
"
 
 
#
 
.
.
.
o
r
 
i
p


 
 
 
 
 
 
 
 
r
"
(
?
:
:
\
d
+
)
?
"
 
 
#
 
o
p
t
i
o
n
a
l
 
p
o
r
t


 
 
 
 
 
 
 
 
r
"
(
?
:
/
?
|
[
/
?
]
\
S
+
)
$
"
,


 
 
 
 
 
 
 
 
r
e
.
I
G
N
O
R
E
C
A
S
E
,


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
r
e
.
m
a
t
c
h
(
r
e
g
e
x
,
 
u
r
l
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
i
s
_
v
a
l
i
d
_
e
m
a
i
l
(
e
m
a
i
l
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
V
a
l
i
d
a
t
e
s
 
a
n
 
e
m
a
i
l
 
s
t
r
i
n
g
 
u
s
i
n
g
 
a
 
s
i
m
p
l
i
f
i
e
d
 
a
n
d
 
c
o
m
p
r
e
h
e
n
s
i
v
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
e
m
a
i
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
 
e
m
a
i
l
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
e
m
a
i
l
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
r
e
g
e
x
 
=
 
r
e
.
c
o
m
p
i
l
e
(


 
 
 
 
 
 
 
 
r
"
(
^
[
a
-
z
A
-
Z
0
-
9
_
.
+
-
]
+
@
[
a
-
z
A
-
Z
0
-
9
-
]
+
\
.
[
a
-
z
A
-
Z
0
-
9
-
.
]
+
$
)
"
,
 
r
e
.
I
G
N
O
R
E
C
A
S
E


 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
r
e
.
m
a
t
c
h
(
r
e
g
e
x
,
 
e
m
a
i
l
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
i
s
_
v
a
l
i
d
_
u
u
i
d
(
u
u
i
d
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
V
a
l
i
d
a
t
e
s
 
a
 
U
U
I
D
 
s
t
r
i
n
g
 
u
s
i
n
g
 
a
 
s
i
m
p
l
i
f
i
e
d
 
a
n
d
 
c
o
m
p
r
e
h
e
n
s
i
v
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
u
i
d
 
(
s
t
r
)
:
 
T
h
e
 
U
U
I
D
 
s
t
r
i
n
g
 
t
o
 
v
a
l
i
d
a
t
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
U
U
I
D
 
i
s
 
v
a
l
i
d
import unittest


class TestValidURL(unittest.TestCase):

    def test_validates_standard_http_url(self):
        url = 'http://www.example.com'
        self.assertTrue(is_valid_url(url))

    def test_validates_secure_https_url(self):
        url = 'https://www.example.com'
        self.assertTrue(is_valid_url(url))

    def test_rejects_malformed_url(self):
        url = 'htp:/www.example.com'
        self.assertFalse(is_valid_url(url))

if __name__ == '__main__':
    unittest.main()