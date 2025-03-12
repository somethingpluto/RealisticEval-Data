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
 
T
u
p
l
e






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
v
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


 
 
 
 
c
o
n
v
e
r
t
 
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
 
H
S
V
 
c
o
l
o
r
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
 
0
,
 
0
,
 
2
5
5


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
2
4
0
,
 
1
0
0
,
 
1
0
0


 
 
 
 
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
 
r
g
b
 
r
e
a
d
 
v
a
l
u
e


 
 
 
 
 
 
 
 
g
 
(
i
n
t
)
:
 
r
g
b
 
g
r
e
e
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 
b
 
(
i
n
t
)
:
 
r
g
b
 
b
l
u
e
 
v
a
l
u
e




 
 
 
 
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
 
H
S
V
 
v
a
l
u
e


 
 
 
 
"
"
"


 
 
 
 
r
,
 
g
,
 
b
 
=
 
r
 
/
 
2
5
5
.
0
,
 
g
 
/
 
2
5
5
.
0
,
 
b
 
/
 
2
5
5
.
0


 
 
 
 
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


 
 
 
 
d
f
 
=
 
m
x
 
-
 
m
n


 
 
 
 
i
f
 
m
x
 
=
=
 
m
n
:


 
 
 
 
 
 
 
 
h
 
=
 
0


 
 
 
 
e
l
i
f
 
m
x
 
=
=
 
r
:


 
 
 
 
 
 
 
 
h
 
=
 
(
6
0
 
*
 
(
(
g
 
-
 
b
)
 
/
 
d
f
)
 
+
 
3
6
0
)
 
%
 
3
6
0


 
 
 
 
e
l
i
f
 
m
x
 
=
=
 
g
:


 
 
 
 
 
 
 
 
h
 
=
 
(
6
0
 
*
 
(
(
b
 
-
 
r
)
 
/
 
d
f
)
 
+
 
1
2
0
)
 
%
 
3
6
0


 
 
 
 
e
l
i
f
 
m
x
 
=
=
 
b
:


 
 
 
 
 
 
 
 
h
 
=
 
(
6
0
 
*
 
(
(
r
 
-
 
g
)
 
/
 
d
f
)
 
+
 
2
4
0
)
 
%
 
3
6
0


 
 
 
 
i
f
 
m
x
 
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
 
(
d
f
 
/
 
m
x
)
 
*
 
1
0
0


 
 
 
 
v
 
=
 
m
x
 
*
 
1
0
0


 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
h
)
,
 
i
n
t
(
s
)
,
 
i
n
t
(
v
)






d
e
f
 
h
s
v
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
 
v
:
 
i
n
t
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


 
 
 
 
c
o
n
v
e
r
t
 
H
S
V
 
c
o
l
o
r
 
t
o
 
R
G
B
 
c
o
l
o
r
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
 
2
4
0
,
 
1
0
0
,
 
1
0
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
0
,
 
0
,
 
2
5
5


 
 
 
 
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
 
h
s
v
 
h
u
e
 
v
a
l
u
e


 
 
 
 
 
 
 
 
s
 
(
i
n
t
)
:
 
h
s
v
 
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


 
 
 
 
 
 
 
 
v
 
(
i
n
t
)
:
 
h
s
v
 
v
a
l
u
e
 
v
a
l
u
e




 
 
 
 
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
 
R
G
B
 
v
a
l
u
e


 
 
 
 
"
"
"


 
 
 
 
h
 
=
 
h
 
/
 
3
6
0


 
 
 
 
s
 
=
 
s
 
/
 
1
0
0


 
 
 
 
v
 
=
 
v
 
/
 
1
0
0


 
 
 
 
i
 
=
 
i
n
t
(
h
 
*
 
6
)


 
 
 
 
f
 
=
 
h
 
*
 
6
 
-
 
i


 
 
 
 
p
 
=
 
v
 
*
 
(
1
 
-
import unittest


class TestRGBtoHSV(unittest.TestCase):

    def test_rgb_to_hsv_red(self):
        # Test conversion of pure red color
        r, g, b = 255, 0, 0
        expected_result = (0, 100, 100)  # Hue should be 0, Saturation 1, Value 1 for red
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_green(self):
        # Test conversion of pure green color
        r, g, b = 0, 255, 0
        expected_result = (120, 100, 100)  # Hue should be 120, Saturation 1, Value 1 for green
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_blue(self):
        # Test conversion of pure blue color
        r, g, b = 0, 0, 255
        expected_result = (240, 100, 100)  # Hue should be 240, Saturation 1, Value 1 for blue
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_white(self):
        # Test conversion of white color
        r, g, b = 255, 255, 255
        expected_result = (0, 0, 100)  # Hue is undefined, typically 0; Saturation 0, Value 1 for white
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)

    def test_rgb_to_hsv_black(self):
        # Test conversion of black color
        r, g, b = 0, 0, 0
        expected_result = (0, 0, 0)  # Hue is undefined, typically 0; Saturation 0, Value 0 for black
        result = rgb_to_hsv(r, g, b)
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()