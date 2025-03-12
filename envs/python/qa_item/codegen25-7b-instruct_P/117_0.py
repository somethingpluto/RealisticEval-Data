f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
D
i
c
t






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
:
 
i
n
t
,
 
g
:
 
i
n
t
,
 
b
:
 
i
n
t
)
 
-
>
 
D
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
 
v
a
l
u
e
 
t
o
 
H
S
L
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
 
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
m
p
o
n
e
n
t
 
(
0
-
2
5
5
)
.


 
 
 
 
 
 
 
 
g
 
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
m
p
o
n
e
n
t
 
(
0
-
2
5
5
)
.


 
 
 
 
 
 
 
 
b
 
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
m
p
o
n
e
n
t
 
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


 
 
 
 
 
 
 
 
D
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
 
H
S
L
 
v
a
l
u
e
s
.


 
 
 
 
"
"
"


 
 
 
 
r
 
/
=
 
2
5
5


 
 
 
 
g
 
/
=
 
2
5
5


 
 
 
 
b
 
/
=
 
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
 
=
=
 
0
:


 
 
 
 
 
 
 
 
h
 
=
 
0


 
 
 
 
 
 
 
 
s
 
=
 
0


 
 
 
 
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
 
r
:


 
 
 
 
 
 
 
 
h
 
=
 
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


 
 
 
 
 
 
 
 
i
f
 
g
 
<
 
b
:


 
 
 
 
 
 
 
 
 
 
 
 
h
 
+
=
 
6


 
 
 
 
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
 
+
 
2


 
 
 
 
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
 
+
 
4




 
 
 
 
h
 
/
=
 
6




 
 
 
 
i
f
 
d
e
l
t
a
 
=
=
 
0
:


 
 
 
 
 
 
 
 
s
 
=
 
0


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
s
 
=
 
d
e
l
t
a
 
/
 
(
1
 
-
 
a
b
s
(
2
 
*
 
l
 
-
 
1
)
)




 
 
 
 
r
e
t
u
r
n
 
{
"
h
"
:
 
h
,
 
"
s
"
:
 
s
,
 
"
l
"
:
 
l
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
:
 
f
l
o
a
t
,
 
s
:
 
f
l
o
a
t
,
 
l
:
 
f
l
o
a
t
)
 
-
>
 
D
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
 
a
n
 
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
 
t
o
 
R
G
B
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
 
(
f
l
o
a
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
1
)
.


 
 
 
 
 
 
 
 
s
 
(
f
l
o
a
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
)
.


 
 
 
 
 
 
 
 
l
 
(
f
l
o
a
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


 
 
 
 
 
 
 
 
D
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
 
R
G
B
 
v
a
l
u
e
s
.


 
 
 
 
"
"
"


 
 
 
 
r
 
=
 
0


 
 
 
 
g
 
=
 
0


 
 
 
 
b
 
=
 
0




 
 
 
 
i
f
 
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
 
=
 
l
 
*
 
2
5
5


 
 
 
 
 
 
 
 
g
 
=
 
l
 
*
 
2
5
5


 
 
 
 
 
 
 
 
b
 
=
 
l
 
*
 
2
5
5


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
q
 
=
 
l
 
*
 
(
1
import unittest


class TestRgbToHsl(unittest.TestCase):

    def test_converts_pure_red_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 0, 0), {'h': 0, 's': 100, 'l': 50})

    def test_converts_black_to_hsl(self):
        self.assertEqual(rgb_to_hsl(0, 0, 0), {'h': 0, 's': 0, 'l': 0})

    def test_converts_white_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 255, 255), {'h': 0, 's': 0, 'l': 100})

    def test_converts_a_color_on_edge_of_rgb_range(self):
        self.assertEqual(rgb_to_hsl(0, 255, 255), {'h': 180, 's': 100, 'l': 50})

if __name__ == '__main__':
    unittest.main()