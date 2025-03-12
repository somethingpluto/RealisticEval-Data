i
m
p
o
r
t
 
m
a
t
h






d
e
f
 
d
e
g
r
e
e
s
_
t
o
_
r
a
d
i
a
n
s
(
d
e
g
r
e
e
s
:
 
i
n
t
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


 
 
 
 
C
o
n
v
e
r
t
 
a
n
 
a
n
g
l
e
 
f
r
o
m
 
d
e
g
r
e
e
s
 
t
o
 
r
a
d
i
a
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
g
r
e
e
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
 
a
n
g
l
e
 
i
n
 
d
e
g
r
e
e
s
 
t
o
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
a
n
g
l
e
 
i
n
 
r
a
d
i
a
n
s
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
 
d
e
g
r
e
e
s
 
*
 
m
a
t
h
.
p
i
 
/
 
1
8
0






d
e
f
 
r
a
d
i
a
n
s
_
t
o
_
d
e
g
r
e
e
s
(
r
a
d
i
a
n
s
:
 
f
l
o
a
t
)
 
-
>
 
i
n
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
 
a
n
 
a
n
g
l
e
 
f
r
o
m
 
r
a
d
i
a
n
s
 
t
o
 
d
e
g
r
e
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
a
d
i
a
n
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
 
a
n
g
l
e
 
i
n
 
r
a
d
i
a
n
s
 
t
o
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
a
n
g
l
e
 
i
n
 
d
e
g
r
e
e
s
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
a
d
i
a
n
s
 
*
 
1
8
0
 
/
 
m
a
t
h
.
p
i






d
e
f
 
d
i
s
t
a
n
c
e
_
b
e
t
w
e
e
n
_
p
o
i
n
t
s
(
x
1
:
 
f
l
o
a
t
,
 
y
1
:
 
f
l
o
a
t
,
 
x
2
:
 
f
l
o
a
t
,
 
y
2
:
 
f
l
o
a
t
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


 
 
 
 
C
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
p
o
i
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
1
 
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
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
y
1
 
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
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
x
2
 
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
 
x
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
y
2
 
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
 
y
-
c
o
o
r
d
i
n
a
t
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
p
o
i
n
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
t
w
o
 
p
o
i
n
t
s
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
 
m
a
t
h
.
s
q
r
t
(
(
x
2
 
-
 
x
1
)
 
*
*
 
2
 
+
 
(
y
2
 
-
 
y
1
)
 
*
*
 
2
)






d
e
f
 
d
i
s
t
a
n
c
e
_
b
e
t
w
e
e
n
_
p
o
i
n
t
s
_
2
d
(
p
o
i
n
t
1
:
 
t
u
p
l
e
,
 
p
o
i
n
t
2
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


 
 
 
 
C
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
p
o
i
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
1
 
(
t
u
p
l
e
)
:
 
T
h
e
 
f
i
r
s
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
o
i
n
t
2
 
(
t
u
p
l
e
)
:
 
T
h
e
 
s
e
c
o
n
d
 
p
o
i
n
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
t
w
o
 
p
o
i
n
t
s
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
 
d
i
s
t
a
n
c
e
_
b
e
t
w
e
e
n
_
p
o
i
n
t
s
(
p
o
i
n
t
1
[
0
]
,
 
p
o
i
n
t
1
[
1
]
,
 
p
o
i
n
t
2
[
0
]
,
 
p
o
i
n
t
2
[
1
]
)






d
e
f
 
d
i
s
t
a
n
c
e
_
b
e
t
w
e
e
n
_
p
o
i
n
t
s
_
3
d
(
p
o
i
n
t
1
:
 
t
u
p
l
e
,
 
p
o
i
n
t
2
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


 
 
 
 
C
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
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
p
o
i
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
o
i
n
t
1
 
(
t
u
p
l
e
)
:
 
T
h
e
 
f
i
r
s
t
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
o
i
n
t
2
 
(
t
u
p
l
e
)
:
 
T
h
e
 
s
e
c
o
n
d
 
p
o
i
n
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
import math
import unittest


class TestDegreesToRadians(unittest.TestCase):
    def test_zero_degrees(self):
        """Test conversion of 0 degrees"""
        self.assertAlmostEqual(degrees_to_radians(0), 0, places=5)

    def test_ninety_degrees(self):
        """Test conversion of 90 degrees"""
        self.assertAlmostEqual(degrees_to_radians(90), math.pi / 2, places=5)

    def test_one_eighty_degrees(self):
        """Test conversion of 180 degrees"""
        self.assertAlmostEqual(degrees_to_radians(180), math.pi, places=5)

    def test_two_seventy_degrees(self):
        """Test conversion of 270 degrees"""
        self.assertAlmostEqual(degrees_to_radians(270), 3 * math.pi / 2, places=5)

    def test_three_sixty_degrees(self):
        """Test conversion of 360 degrees"""
        self.assertAlmostEqual(degrees_to_radians(360), 2 * math.pi, places=5)

    def test_negative_degrees(self):
        """Test conversion of negative degrees"""
        self.assertAlmostEqual(degrees_to_radians(-90), -math.pi / 2, places=5)

    def test_large_degrees(self):
        """Test conversion of a large angle (720 degrees)"""
        self.assertAlmostEqual(degrees_to_radians(720), 4 * math.pi, places=5)

if __name__ == '__main__':
    unittest.main()