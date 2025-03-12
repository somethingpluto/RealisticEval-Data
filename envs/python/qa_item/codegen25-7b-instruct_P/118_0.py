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
 
i
n
t
,
 
s
:
 
i
n
t
,
 
l
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
i
n
t
)
:
 
H
u
e
 
(
0
-
3
6
0
 
d
e
g
r
e
e
s
)
.


 
 
 
 
 
 
 
 
s
 
(
i
n
t
)
:
 
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
 
(
0
-
1
0
0
%
)
.


 
 
 
 
 
 
 
 
l
 
(
i
n
t
)
:
 
L
i
g
h
t
n
e
s
s
 
(
0
-
1
0
0
%
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


 
 
 
 
h
 
/
=
 
3
6
0


 
 
 
 
s
 
/
=
 
1
0
0


 
 
 
 
l
 
/
=
 
1
0
0




 
 
 
 
i
f
 
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
 
 
 
 
"
r
"
:
 
i
n
t
(
l
 
*
 
2
5
5
)
,


 
 
 
 
 
 
 
 
 
 
 
 
"
g
"
:
 
i
n
t
(
l
 
*
 
2
5
5
)
,


 
 
 
 
 
 
 
 
 
 
 
 
"
b
"
:
 
i
n
t
(
l
 
*
 
2
5
5
)
,


 
 
 
 
 
 
 
 
}




 
 
 
 
q
 
=
 
l
 
*
 
(
1
 
+
 
s
)
 
i
f
 
l
 
<
 
0
.
5
 
e
l
s
e
 
l
 
+
 
s
 
-
 
l
 
*
 
s


 
 
 
 
p
 
=
 
2
 
*
 
l
 
-
 
q


 
 
 
 
r
,
 
g
,
 
b
 
=
 
0
,
 
0
,
 
0


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
0
,
 
3
)
:


 
 
 
 
 
 
 
 
i
f
 
i
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
 
=
 
i
n
t
(
2
5
5
 
*
 
(
p
 
+
 
(
1
 
-
 
s
)
 
*
 
m
a
x
(
l
,
 
q
)
)
)


 
 
 
 
 
 
 
 
e
l
i
f
 
i
 
=
=
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
g
 
=
 
i
n
t
(
2
5
5
 
*
 
(
p
 
+
 
(
1
 
-
 
s
)
 
*
 
m
a
x
(
l
,
 
q
)
)
)


 
 
 
 
 
 
 
 
e
l
i
f
 
i
 
=
=
 
2
:


 
 
 
 
 
 
 
 
 
 
 
 
b
 
=
 
i
n
t
(
2
5
5
 
*
 
(
p
 
+
 
(
1
 
-
 
s
)
 
*
 
m
a
x
(
l
,
 
q
)
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
r
"
:
 
r
,


 
 
 
 
 
 
 
 
"
g
"
:
 
g
,


 
 
 
 
 
 
 
 
"
b
"
:
 
b
,


 
 
 
 
}






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
 
R
e
d
 
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


 
 
 
 
 
 
 
 
g
 
(
i
n
t
)
:
 
G
r
e
e
n
 
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


 
 
 
 
 
 
 
 
b
 
(
i
n
t
)
:
 
B
l
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
x
 
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
n
 
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


 
 
 
 
h
 
=
 
s
 
=
 
l
 
=
 
(
m
x
 
+
 
m
import unittest


class TestHSLToRGB(unittest.TestCase):

    def test_converts_pure_red_hue_correctly(self):
        self.assertEqual(hsl_to_rgb(0, 100, 50), {'r': 255, 'g': 0, 'b': 0})

    def test_returns_gray_for_zero_saturation(self):
        self.assertEqual(hsl_to_rgb(240, 0, 50), {'r': 128, 'g': 128, 'b': 128})

    def test_returns_white_for_full_lightness(self):
        self.assertEqual(hsl_to_rgb(120, 50, 100), {'r': 255, 'g': 255, 'b': 255})

    def test_converts_full_saturation_and_mid_lightness_blue_correctly(self):
        self.assertEqual(hsl_to_rgb(240, 100, 50), {'r': 0, 'g': 0, 'b': 255})

    def test_handles_edge_hue_at_360_degrees_correctly(self):
        self.assertEqual(hsl_to_rgb(360, 100, 50), {'r': 255, 'g': 0, 'b': 0})  # Should be the same as hue 0

if __name__ == '__main__':
    unittest.main()