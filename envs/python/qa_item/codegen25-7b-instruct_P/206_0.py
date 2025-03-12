d
e
f
 
c
i
r
c
l
e
_
i
n
t
e
r
s
e
c
t
i
o
n
_
a
r
e
a
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
 
r
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
,
 
r
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
 
i
n
t
e
r
s
e
c
t
i
o
n
 
a
r
e
a
 
o
f
 
t
w
o
 
c
i
r
c
l
e
s
.
 
E
a
c
h
 
c
i
r
c
l
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
i
t
s
 
c
e
n
t
e
r
 
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
s
 
a
n
d
 
r
a
d
i
u
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
.


 
 
 
 
 
 
 
 
r
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
 
r
a
d
i
u
s
 
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
 
c
i
r
c
l
e
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
.


 
 
 
 
 
 
 
 
r
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
 
r
a
d
i
u
s
 
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
 
c
i
r
c
l
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
r
e
a
 
o
f
 
t
h
e
 
i
n
t
e
r
s
e
c
t
i
o
n
 
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
 
c
i
r
c
l
e
s
.


 
 
 
 
"
"
"


 
 
 
 
d
 
=
 
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


 
 
 
 
i
f
 
d
 
>
 
r
1
 
+
 
r
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0
.
0


 
 
 
 
e
l
i
f
 
d
 
<
 
a
b
s
(
r
1
 
-
 
r
2
)
:


 
 
 
 
 
 
 
 
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
p
i
 
*
 
m
i
n
(
r
1
,
 
r
2
)
 
*
*
 
2


 
 
 
 
e
l
i
f
 
d
 
=
=
 
r
1
 
+
 
r
2
 
o
r
 
d
 
=
=
 
a
b
s
(
r
1
 
-
 
r
2
)
:


 
 
 
 
 
 
 
 
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
p
i
 
*
 
r
1
 
*
*
 
2


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
a
 
=
 
(
r
1
 
*
*
 
2
 
-
 
r
2
 
*
*
 
2
 
+
 
d
 
*
*
 
2
)
 
/
 
(
2
 
*
 
d
)


 
 
 
 
 
 
 
 
h
 
=
 
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
r
1
 
*
*
 
2
 
-
 
a
 
*
*
 
2
)


 
 
 
 
 
 
 
 
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
p
i
 
*
 
(
a
 
+
 
h
)






d
e
f
 
c
i
r
c
l
e
_
i
n
t
e
r
s
e
c
t
i
o
n
_
a
r
e
a
_
w
i
t
h
_
b
o
u
n
d
a
r
y
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
 
r
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
,
 
r
2
:
 
f
l
o
a
t
,
 
b
o
u
n
d
a
r
y
_
x
:
 
f
l
o
a
t
,
 
b
o
u
n
d
a
r
y
_
y
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
 
i
n
t
e
r
s
e
c
t
i
o
n
 
a
r
e
a
 
o
f
 
t
w
o
 
c
i
r
c
l
e
s
 
w
i
t
h
 
a
 
b
o
u
n
d
a
r
y
.


 
 
 
 
E
a
c
h
 
c
i
r
c
l
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
i
t
s
 
c
e
n
t
e
r
 
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
s
 
a
n
d
 
r
a
d
i
u
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
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
 
c
e
n
t
e
r
 
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
 
c
i
r
c
l
e
.


 
 
 
 
 
 
 
 
r
1
 
(
f
l
o
a
t
import unittest


class Tester(unittest.TestCase):

    def test_circle_intersection_area(self):
        tolerance = 1e-5

        # No overlap, circles far apart
        self.assertAlmostEqual(circle_intersection_area(0.0, 0.0, 3.0, 10.0, 10.0, 3.0), 0.0, delta=tolerance)

        # No overlap, circles just touching
        self.assertAlmostEqual(circle_intersection_area(0.0, 0.0, 3.0, 6.0, 0.0, 3.0), 0.0, delta=tolerance)

        # One circle inside the other
        area = circle_intersection_area(0.0, 0.0, 5.0, 2.0, 0.0, 3.0)
        self.assertAlmostEqual(area, 28.2743, delta=tolerance)  # Area of smaller circle

        # Identical circles, full overlap
        area = circle_intersection_area(0.0, 0.0, 3.0, 0.0, 0.0, 3.0)
        self.assertAlmostEqual(area, 28.2743, delta=tolerance)  # Area of one circle

if __name__ == '__main__':
    unittest.main()