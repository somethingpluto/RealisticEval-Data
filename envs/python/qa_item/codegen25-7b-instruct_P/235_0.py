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
e
a
r
i
n
g
(
l
a
t
1
:
 
f
l
o
a
t
,
 
l
o
n
1
:
 
f
l
o
a
t
,
 
l
a
t
2
:
 
f
l
o
a
t
,
 
l
o
n
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
 
a
z
i
m
u
t
h
 
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
 
o
n
 
t
h
e
 
e
a
r
t
h
.
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
a
c
c
e
p
t
s
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
o
f
 
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
 
a
s
 
a
 
p
a
r
a
m
e
t
e
r
 
a
n
d
 
r
e
t
u
r
n
s
 
t
h
e
 
a
z
i
m
u
t
h
 
f
r
o
m
 
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
 
t
o
 
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
 
i
n
 
d
e
g
r
e
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
a
t
1
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
s
t
a
r
t
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
1
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
s
t
a
r
t
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
a
t
2
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
2
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
B
e
a
r
i
n
g
 
i
n
 
d
e
g
r
e
e
s
 
f
r
o
m
 
t
h
e
 
s
t
a
r
t
i
n
g
 
p
o
i
n
t
 
t
o
 
t
h
e
 
e
n
d
i
n
g
 
p
o
i
n
t
,
 
r
a
n
g
i
n
g
 
f
r
o
m
 
0
 
t
o
 
3
6
0
.


 
 
 
 
"
"
"


 
 
 
 
l
a
t
1
 
=
 
m
a
t
h
.
r
a
d
i
a
n
s
(
l
a
t
1
)


 
 
 
 
l
o
n
1
 
=
 
m
a
t
h
.
r
a
d
i
a
n
s
(
l
o
n
1
)


 
 
 
 
l
a
t
2
 
=
 
m
a
t
h
.
r
a
d
i
a
n
s
(
l
a
t
2
)


 
 
 
 
l
o
n
2
 
=
 
m
a
t
h
.
r
a
d
i
a
n
s
(
l
o
n
2
)




 
 
 
 
d
l
o
n
 
=
 
l
o
n
2
 
-
 
l
o
n
1


 
 
 
 
y
 
=
 
m
a
t
h
.
s
i
n
(
d
l
o
n
)
 
*
 
m
a
t
h
.
c
o
s
(
l
a
t
2
)


 
 
 
 
x
 
=
 
m
a
t
h
.
c
o
s
(
l
a
t
1
)
 
*
 
m
a
t
h
.
s
i
n
(
l
a
t
2
)
 
-
 
m
a
t
h
.
s
i
n
(
l
a
t
1
)
 
*
 
m
a
t
h
.
c
o
s
(
l
a
t
2
)
 
*
 
m
a
t
h
.
c
o
s
(
d
l
o
n
)


 
 
 
 
b
e
a
r
i
n
g
 
=
 
m
a
t
h
.
a
t
a
n
2
(
y
,
 
x
)


 
 
 
 
b
e
a
r
i
n
g
 
=
 
m
a
t
h
.
d
e
g
r
e
e
s
(
b
e
a
r
i
n
g
)


 
 
 
 
b
e
a
r
i
n
g
 
=
 
(
b
e
a
r
i
n
g
 
+
 
3
6
0
)
 
%
 
3
6
0


 
 
 
 
r
e
t
u
r
n
 
b
e
a
r
i
n
g






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
d
i
s
t
a
n
c
e
(
l
a
t
1
:
 
f
l
o
a
t
,
 
l
o
n
1
:
 
f
l
o
a
t
,
 
l
a
t
2
:
 
f
l
o
a
t
,
 
l
o
n
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
 
o
n
 
t
h
e
 
e
a
r
t
h
.
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
a
c
c
e
p
t
s
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
o
f
 
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
 
a
s
 
a
 
p
a
r
a
m
e
t
e
r
 
a
n
d
 
r
e
t
u
r
n
s
 
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
 
i
n
 
m
e
t
e
r
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
a
t
1
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
s
t
a
r
t
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
1
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
s
t
a
r
t
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
a
t
2
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
2
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
e
n
d
i
n
g
 
p
o
i
n
t
 
i
n
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
D
i
s
t
a
n
c
e
 
i
n
 
m
e
t
e
r
s
 
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
import unittest

class TestCalculateBearing(unittest.TestCase):
    def test_north_bearing(self):
        # From equator directly north
        self.assertAlmostEqual(calculate_bearing(0, 0, 10, 0), 0)

    def test_east_bearing(self):
        # From prime meridian directly east
        self.assertAlmostEqual(calculate_bearing(0, 0, 0, 10), 90)

    def test_south_bearing(self):
        # From a point directly south
        self.assertAlmostEqual(calculate_bearing(10, 0, 0, 0), 180)

    def test_west_bearing(self):
        # From a point directly west
        self.assertAlmostEqual(calculate_bearing(0, 10, 0, 0), 270)

    def test_across_prime_meridian(self):
        # From a point west of the prime meridian to a point east
        self.assertAlmostEqual(calculate_bearing(0, -1, 0, 1), 90)
if __name__ == '__main__':
    unittest.main()