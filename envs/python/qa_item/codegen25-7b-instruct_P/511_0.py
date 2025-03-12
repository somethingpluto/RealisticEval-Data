d
e
f
 
h
e
x
_
t
o
_
a
n
s
i
(
h
e
x
_
c
o
l
o
r
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
 
a
 
h
e
x
a
d
e
c
i
m
a
l
 
c
o
l
o
r
 
c
o
d
e
 
t
o
 
a
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
e
x
_
c
o
l
o
r
 
(
s
t
r
)
:
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
h
e
x
a
d
e
c
i
m
a
l
 
c
o
l
o
r
 
c
o
d
e
,
 
e
.
g
.
,
 
'
#
F
F
5
7
3
3
'
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
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
R
G
B
 
c
o
l
o
r
.


 
 
 
 
"
"
"


 
 
 
 
h
e
x
_
c
o
l
o
r
 
=
 
h
e
x
_
c
o
l
o
r
.
l
s
t
r
i
p
(
"
#
"
)


 
 
 
 
r
e
t
u
r
n
 
"
\
0
3
3
[
3
8
;
2
;
{
}
;
{
}
;
{
}
m
"
.
f
o
r
m
a
t
(
*
t
u
p
l
e
(
i
n
t
(
h
e
x
_
c
o
l
o
r
[
i
 
:
 
i
 
+
 
2
]
,
 
1
6
)
 
f
o
r
 
i
 
i
n
 
(
0
,
 
2
,
 
4
)
)
)






d
e
f
 
a
n
s
i
_
t
o
_
h
e
x
(
a
n
s
i
_
c
o
l
o
r
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
 
a
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
t
o
 
a
 
h
e
x
a
d
e
c
i
m
a
l
 
c
o
l
o
r
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
n
s
i
_
c
o
l
o
r
 
(
s
t
r
)
:
 
A
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
f
o
r
 
a
 
c
o
l
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
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
h
e
x
a
d
e
c
i
m
a
l
 
c
o
l
o
r
 
c
o
d
e
,
 
e
.
g
.
,
 
'
#
F
F
5
7
3
3
'
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
#
"
 
+
 
a
n
s
i
_
c
o
l
o
r
.
l
s
t
r
i
p
(
"
\
0
3
3
[
3
8
;
2
;
"
)
.
r
s
t
r
i
p
(
"
m
"
)






d
e
f
 
a
n
s
i
_
t
o
_
r
g
b
(
a
n
s
i
_
c
o
l
o
r
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
,
 
i
n
t
]
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
 
a
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
n
s
i
_
c
o
l
o
r
 
(
s
t
r
)
:
 
A
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
f
o
r
 
a
 
c
o
l
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
,
 
i
n
t
]
:
 
A
 
t
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
R
G
B
 
c
o
l
o
r
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
 
t
u
p
l
e
(
i
n
t
(
x
)
 
f
o
r
 
x
 
i
n
 
a
n
s
i
_
c
o
l
o
r
.
l
s
t
r
i
p
(
"
\
0
3
3
[
3
8
;
2
;
"
)
.
r
s
t
r
i
p
(
"
m
"
)
.
s
p
l
i
t
(
"
;
"
)
)






d
e
f
 
r
g
b
_
t
o
_
a
n
s
i
(
r
g
b
_
c
o
l
o
r
:
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
,
 
i
n
t
]
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
 
a
n
 
R
G
B
 
c
o
l
o
r
 
t
o
 
a
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
g
b
_
c
o
l
o
r
 
(
T
u
p
l
e
[
i
n
t
,
 
i
n
t
,
 
i
n
t
]
)
:
 
A
 
t
u
p
l
e
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
R
G
B
 
c
o
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
n
 
A
N
S
I
 
e
s
c
a
p
e
 
c
o
d
e
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
R
G
B
 
c
o
l
o
r
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
0
3
3
[
3
8
;
2
;
{
}
;
{
import unittest


class TestHexToAnsi(unittest.TestCase):

    def test_valid_colors(self):
        """Test valid hex color inputs."""
        self.assertEqual(hex_to_ansi("#FF5733"), "\x1b[38;2;255;87;51m")
        self.assertEqual(hex_to_ansi("#00FF00"), "\x1b[38;2;0;255;0m")
        self.assertEqual(hex_to_ansi("#0000FF"), "\x1b[38;2;0;0;255m")

    def test_black_and_white(self):
        """Test edge cases with black and white colors."""
        self.assertEqual(hex_to_ansi("#000000"), "\x1b[38;2;0;0;0m")  # Black
        self.assertEqual(hex_to_ansi("#FFFFFF"), "\x1b[38;2;255;255;255m")  # White

if __name__ == '__main__':
    unittest.main()