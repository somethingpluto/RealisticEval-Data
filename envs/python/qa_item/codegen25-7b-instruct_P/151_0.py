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
h
s
l
(
r
g
b
:
 
d
i
c
t
)
 
-
>
 
d
i
c
t
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
 
R
G
B
 
c
o
l
o
r
 
v
a
l
u
e
s
 
t
o
 
H
S
L
 
(
H
u
e
,
 
S
a
t
u
r
a
t
i
o
n
,
 
L
i
g
h
t
n
e
s
s
)
 
c
o
l
o
r
 
v
a
l
u
e
s
.




 
 
 
 
T
h
e
 
i
n
p
u
t
 
R
G
B
 
v
a
l
u
e
s
 
s
h
o
u
l
d
 
b
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
2
5
5
,
 
a
n
d
 
t
h
e
 
o
u
t
p
u
t
 
H
S
L
 
v
a
l
u
e
s
 
w
i
l
l
 
h
a
v
e
:


 
 
 
 
-
 
`
h
`
 
(
H
u
e
)
 
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
3
6
0
,


 
 
 
 
-
 
`
s
`
 
(
S
a
t
u
r
a
t
i
o
n
)
 
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
1
0
0
 
(
p
e
r
c
e
n
t
a
g
e
)
,


 
 
 
 
-
 
`
l
`
 
(
L
i
g
h
t
n
e
s
s
)
 
i
n
 
t
h
e
 
r
a
n
g
e
 
o
f
 
0
 
t
o
 
1
0
0
 
(
p
e
r
c
e
n
t
a
g
e
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
g
b
 
(
d
i
c
t
)
:
 
T
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
 
v
a
l
u
e
s
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
g
b
[
'
r
'
]
 
(
i
n
t
)
:
 
T
h
e
 
r
e
d
 
c
o
l
o
r
 
v
a
l
u
e
 
(
0
-
2
5
5
)
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
g
b
[
'
g
'
]
 
(
i
n
t
)
:
 
T
h
e
 
g
r
e
e
n
 
c
o
l
o
r
 
v
a
l
u
e
 
(
0
-
2
5
5
)
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
g
b
[
'
b
'
]
 
(
i
n
t
)
:
 
T
h
e
 
b
l
u
e
 
c
o
l
o
r
 
v
a
l
u
e
 
(
0
-
2
5
5
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
d
i
c
t
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
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
 
H
S
L
 
c
o
l
o
r
 
v
a
l
u
e
s
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
h
 
(
i
n
t
)
:
 
T
h
e
 
h
u
e
 
v
a
l
u
e
 
(
0
-
3
6
0
)
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
s
 
(
i
n
t
)
:
 
T
h
e
 
s
a
t
u
r
a
t
i
o
n
 
v
a
l
u
e
 
(
0
-
1
0
0
)
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
l
 
(
i
n
t
)
:
 
T
h
e
 
l
i
g
h
t
n
e
s
s
 
v
a
l
u
e
 
(
0
-
1
0
0
)
.


 
 
 
 
"
"
"


 
 
 
 
r
 
=
 
r
g
b
[
'
r
'
]
 
/
 
2
5
5


 
 
 
 
g
 
=
 
r
g
b
[
'
g
'
]
 
/
 
2
5
5


 
 
 
 
b
 
=
 
r
g
b
[
'
b
'
]
 
/
 
2
5
5




 
 
 
 
m
a
x
_
c
 
=
 
m
a
x
(
r
,
 
g
,
 
b
)


 
 
 
 
m
i
n
_
c
 
=
 
m
i
n
(
r
,
 
g
,
 
b
)


 
 
 
 
d
e
l
t
a
 
=
 
m
a
x
_
c
 
-
 
m
i
n
_
c




 
 
 
 
h
 
=
 
0


 
 
 
 
s
 
=
 
0


 
 
 
 
l
 
=
 
(
m
a
x
_
c
 
+
 
m
i
n
_
c
)
 
/
 
2




 
 
 
 
i
f
 
d
e
l
t
a
 
!
=
 
0
:


 
 
 
 
 
 
 
 
i
f
 
m
a
x
_
c
 
=
=
 
r
:


 
 
 
 
 
 
 
 
 
 
 
 
h
 
=
 
6
0
 
*
 
(
(
(
g
 
-
 
b
)
 
/
 
d
e
l
t
a
)
 
%
 
6
)


 
 
 
 
 
 
 
 
e
l
i
f
 
m
a
x
_
c
 
=
=
 
g
:


 
 
 
 
 
 
 
 
 
 
 
 
h
 
=
 
6
0
 
*
 
(
(
(
b
 
-
 
r
)
 
/
 
d
e
l
t
a
)
 
+
 
2
)


 
 
 
 
 
 
 
 
e
l
i
f
 
m
a
x
_
c
 
=
=
 
b
:


 
 
 
 
 
 
 
 
 
 
 
 
h
 
=
 
6
0
 
*
 
(
(
(
r
 
-
 
g
)
 
/
 
d
e
l
t
a
)
 
+
 
4
)




 
 
 
 
 
 
 
 
i
f
 
m
a
x
_
c
 
!
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
s
 
=
 
d
e
l
t
a
 
/
 
m
a
x
_
c




 
 
 
 
r
e
t
u
r
n
 
{
'
h
'
:
 
r
o
u
n
d
(
h
)
,
 
'
s
'
:
 
r
o
u
n
d
(
s
 
*
 
1
0
0
)
,
 
'
l
'
:
 
r
o
u
n
d
(
l
 
*
 
1
0
0
)
}






d
e
f
 
h
s
l
_
t
o
_
r
g
b
(
h
s
l
:
 
d
i
c
t
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_basic_rgb_red(self):
        rgb = {'r': 255, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 100, 'l': 50})

    def test_grayscale_middle_gray(self):
        rgb = {'r': 128, 'g': 128, 'b': 128}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 50})

    def test_edge_case_white(self):
        rgb = {'r': 255, 'g': 255, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 100})

    def test_edge_case_black(self):
        rgb = {'r': 0, 'g': 0, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 0, 's': 0, 'l': 0})

    def test_vibrant_green(self):
        rgb = {'r': 0, 'g': 255, 'b': 0}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 120, 's': 100, 'l': 50})

    def test_deep_blue(self):
        rgb = {'r': 0, 'g': 0, 'b': 255}
        result = rgb_to_hsl(rgb)
        self.assertEqual(result, {'h': 240, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()