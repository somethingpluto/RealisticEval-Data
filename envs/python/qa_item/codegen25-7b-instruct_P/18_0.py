d
e
f
 
f
l
o
a
t
_
t
o
_
r
g
b
(
v
a
l
u
e
:
 
f
l
o
a
t
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


 
 
 
 
c
o
n
v
e
r
t
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
 
t
o
 
a
 
c
o
l
o
r
 
f
r
o
m
 
r
e
d
 
t
o
 
g
r
e
e
n
 
i
n
 
t
h
e
 
c
o
l
o
r
 
f
o
r
m
a
t
 
R
G
B


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
f
l
o
a
t
)
:
 
a
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
a
 
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


 
 
 
 
i
f
 
v
a
l
u
e
 
<
 
0
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
0


 
 
 
 
i
f
 
v
a
l
u
e
 
>
 
1
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
1


 
 
 
 
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
1
 
-
 
v
a
l
u
e
)
)


 
 
 
 
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
 
v
a
l
u
e
)


 
 
 
 
r
e
t
u
r
n
 
r
,
 
g
,
 
0






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
e
x
(
r
g
b
:
 
t
u
p
l
e
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


 
 
 
 
c
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
 
h
e
x
 
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


 
 
 
 
 
 
 
 
r
g
b
 
(
t
u
p
l
e
)
:
 
a
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
a
 
h
e
x
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
'
#
%
0
2
x
%
0
2
x
%
0
2
x
'
 
%
 
r
g
b






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
r
g
b
(
h
e
x
_
c
o
d
e
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


 
 
 
 
c
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


 
 
 
 
 
 
 
 
h
e
x
_
c
o
d
e
 
(
s
t
r
)
:
 
a
 
h
e
x
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
a
 
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
h
e
x
_
c
o
d
e
.
l
s
t
r
i
p
(
'
#
'
)
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
f
l
o
a
t
(
h
e
x
_
c
o
d
e
:
 
s
t
r
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
"
"
"


 
 
 
 
c
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
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
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
d
e
 
(
s
t
r
)
:
 
a
 
h
e
x
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
a
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
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
g
b
_
t
o
_
f
l
o
a
t
(
h
e
x
_
t
o
_
r
g
b
(
h
e
x
_
c
o
d
e
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
f
l
o
a
t
(
r
g
b
:
 
t
u
p
l
e
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
"
"
"


 
 
 
 
c
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
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
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
t
u
p
l
e
)
:
 
a
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
a
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
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
 
s
u
m
(
r
g
b
)
 
/
 
3
 
/
 
2
5
5






d
e
f
 
f
l
o
a
t
_
t
o
_
h
e
x
(
v
a
l
u
e
:
 
f
l
o
a
t
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


 
 
 
 
c
o
n
v
e
r
t
 
a
 
f
l
o
a
t
 
b
e
t
w
e
e
n
 
0
import unittest


class TestFloatToRGB(unittest.TestCase):

    def test_pure_red(self):
        # Value at the lower boundary (0.0) should return pure red
        result = float_to_rgb(0.0)
        self.assertEqual(result, (255, 0, 0))

    def test_pure_green(self):
        # Value at the upper boundary (1.0) should return pure green
        result = float_to_rgb(1.0)
        self.assertEqual(result, (0, 255, 0))

    def test_midpoint(self):
        # Value at 0.5 should return an equal mix of red and green, resulting in yellow
        result = float_to_rgb(0.5)
        self.assertEqual(result, (127, 127, 0))

    def test_quarter_point(self):
        # Value at 0.25 should return more red than green
        result = float_to_rgb(0.25)
        self.assertEqual(result, (191, 63, 0))

    def test_invalid_value(self):
        # Value outside the range [0, 1] should raise a ValueError
        with self.assertRaises(ValueError):
            float_to_rgb(1.5)
if __name__ == '__main__':
    unittest.main()