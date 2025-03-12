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
 
L
i
s
t
,
 
T
u
p
l
e






d
e
f
 
c
a
l
c
u
l
a
t
e
_
r
e
d
_
p
r
o
p
o
r
t
i
o
n
(
p
i
x
e
l
s
:
 
L
i
s
t
[
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
]
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


 
 
 
 
A
n
a
l
y
z
e
 
a
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
e
a
c
h
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
r
g
b
,
 
a
n
d
 
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
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
r
e
d
 
i
n
 
t
h
e
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
i
x
e
l
s
 
(
L
i
s
t
[
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
]
)
:
 
A
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
w
h
e
r
e
 
e
a
c
h
 
p
i
x
e
l
 
i
s
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
(
R
,
 
G
,
 
B
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
r
e
d
 
i
n
 
t
h
e
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
a
s
 
a
 
v
a
l
u
e
 
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
d
_
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
p
i
x
e
l
 
i
n
 
p
i
x
e
l
s
:


 
 
 
 
 
 
 
 
i
f
 
p
i
x
e
l
[
0
]
 
>
 
p
i
x
e
l
[
1
]
 
a
n
d
 
p
i
x
e
l
[
0
]
 
>
 
p
i
x
e
l
[
2
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
d
_
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
r
e
d
_
c
o
u
n
t
 
/
 
l
e
n
(
p
i
x
e
l
s
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
g
r
e
e
n
_
p
r
o
p
o
r
t
i
o
n
(
p
i
x
e
l
s
:
 
L
i
s
t
[
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
]
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


 
 
 
 
A
n
a
l
y
z
e
 
a
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
e
a
c
h
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
r
g
b
,
 
a
n
d
 
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
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
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
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
i
x
e
l
s
 
(
L
i
s
t
[
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
]
)
:
 
A
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
w
h
e
r
e
 
e
a
c
h
 
p
i
x
e
l
 
i
s
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
(
R
,
 
G
,
 
B
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
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
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
a
s
 
a
 
v
a
l
u
e
 
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


 
 
 
 
g
r
e
e
n
_
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
p
i
x
e
l
 
i
n
 
p
i
x
e
l
s
:


 
 
 
 
 
 
 
 
i
f
 
p
i
x
e
l
[
1
]
 
>
 
p
i
x
e
l
[
0
]
 
a
n
d
 
p
i
x
e
l
[
1
]
 
>
 
p
i
x
e
l
[
2
]
:


 
 
 
 
 
 
 
 
 
 
 
 
g
r
e
e
n
_
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
g
r
e
e
n
_
c
o
u
n
t
 
/
 
l
e
n
(
p
i
x
e
l
s
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
b
l
u
e
_
p
r
o
p
o
r
t
i
o
n
(
p
i
x
e
l
s
:
 
L
i
s
t
[
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
]
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


 
 
 
 
A
n
a
l
y
z
e
 
a
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
e
a
c
h
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
r
g
b
,
 
a
n
d
 
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
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
b
l
u
e
 
i
n
 
t
h
e
 
l
i
s
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
i
x
e
l
s
 
(
L
i
s
t
[
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
]
)
:
 
A
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
w
h
e
r
e
 
e
a
c
h
 
p
i
x
e
l
 
i
s
 
r
e
p
r
e
s
e
n
t
e
d
 
a
s
 
a
 
t
u
p
l
e
 
o
f
 
(
R
,
 
G
,
 
B
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
p
r
o
p
o
r
t
i
o
n
 
o
f
 
b
l
u
e
 
i
n
 
t
h
e
 
l
i
s
t
 
o
f
 
p
i
x
e
l
s
,
 
a
s
 
a
 
v
a
l
u
e
 
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


 
 
 
 
b
l
u
e
_
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
p
i
x
e
l
 
i
n
 
p
i
x
e
l
s
:


 
 
 
 
 
 
 
 
i
f
import unittest


class TestCalculateRedProportion(unittest.TestCase):

    def test_all_red_pixels(self):
        # All pixels are fully red
        pixels = [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 1.0)

    def test_no_red_pixels(self):
        # No red component in any pixel
        pixels = [(0, 255, 0), (0, 0, 255), (0, 255, 255)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)

    def test_empty_pixel_list(self):
        # Empty list of pixels
        pixels = []
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)

    def test_all_black_pixels(self):
        # All pixels are black
        pixels = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        result = calculate_red_proportion(pixels)
        self.assertAlmostEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()