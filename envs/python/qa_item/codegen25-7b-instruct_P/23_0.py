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
 
U
n
i
o
n






d
e
f
 
c
h
e
c
k
_
s
e
g
m
e
n
t
s
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
(
s
e
g
1
:
 
t
u
p
l
e
,
 
s
e
g
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
 
U
n
i
o
n
[
t
u
p
l
e
,
 
N
o
n
e
]
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
 
p
o
i
n
t
 
o
f
 
t
w
o
 
l
i
n
e
 
s
e
g
m
e
n
t
s
,
 
i
f
 
i
t
 
e
x
i
s
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
g
1
 
(
t
u
p
l
e
)
:
 
C
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
 
l
i
n
e
 
s
e
g
m
e
n
t
,
 
d
e
f
i
n
e
d
 
a
s
 
(
(
x
1
,
 
y
1
)
,
 
(
x
2
,
 
y
2
)
)
.


 
 
 
 
 
 
 
 
s
e
g
2
 
(
t
u
p
l
e
)
:
 
C
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
 
l
i
n
e
 
s
e
g
m
e
n
t
,
 
d
e
f
i
n
e
d
 
a
s
 
(
(
x
3
,
 
y
3
)
,
 
(
x
4
,
 
y
4
)
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
t
u
p
l
e
,
 
N
o
n
e
]
:
 
T
h
e
 
(
x
,
 
y
)
 
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
 
p
o
i
n
t
 
i
f
 
t
h
e
 
l
i
n
e
 
s
e
g
m
e
n
t
s
 
i
n
t
e
r
s
e
c
t
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
x
1
,
 
y
1
 
=
 
s
e
g
1
[
0
]


 
 
 
 
x
2
,
 
y
2
 
=
 
s
e
g
1
[
1
]


 
 
 
 
x
3
,
 
y
3
 
=
 
s
e
g
2
[
0
]


 
 
 
 
x
4
,
 
y
4
 
=
 
s
e
g
2
[
1
]




 
 
 
 
d
e
n
o
m
i
n
a
t
o
r
 
=
 
(
x
1
 
-
 
x
2
)
 
*
 
(
y
3
 
-
 
y
4
)
 
-
 
(
y
1
 
-
 
y
2
)
 
*
 
(
x
3
 
-
 
x
4
)




 
 
 
 
i
f
 
d
e
n
o
m
i
n
a
t
o
r
 
=
=
 
0
:


 
 
 
 
 
 
 
 
#
 
T
h
e
 
l
i
n
e
 
s
e
g
m
e
n
t
s
 
a
r
e
 
p
a
r
a
l
l
e
l
.


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e




 
 
 
 
a
 
=
 
(
x
1
 
*
 
y
2
 
-
 
y
1
 
*
 
x
2
)


 
 
 
 
b
 
=
 
(
x
3
 
*
 
y
4
 
-
 
y
3
 
*
 
x
4
)


 
 
 
 
x
 
=
 
(
a
 
*
 
(
x
3
 
-
 
x
4
)
 
-
 
(
x
1
 
-
 
x
2
)
 
*
 
b
)
 
/
 
d
e
n
o
m
i
n
a
t
o
r


 
 
 
 
y
 
=
 
(
a
 
*
 
(
y
3
 
-
 
y
4
)
 
-
 
(
y
1
 
-
 
y
2
)
 
*
 
b
)
 
/
 
d
e
n
o
m
i
n
a
t
o
r




 
 
 
 
i
f
 
x
1
 
<
=
 
x
 
<
=
 
x
2
 
a
n
d
 
y
1
 
<
=
 
y
 
<
=
 
y
2
 
a
n
d
 
x
3
 
<
=
 
x
 
<
=
 
x
4
 
a
n
d
 
y
3
 
<
=
 
y
 
<
=
 
y
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
x
,
 
y


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e






d
e
f
 
c
h
e
c
k
_
p
o
i
n
t
_
i
n
_
p
o
l
y
g
o
n
(
p
o
i
n
t
:
 
t
u
p
l
e
,
 
p
o
l
y
g
o
n
:
 
l
i
s
t
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
i
f
 
a
 
p
o
i
n
t
 
i
s
 
i
n
s
i
d
e
 
a
 
p
o
l
y
g
o
n
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
 
(
x
,
 
y
)
 
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
 
o
f
 
t
h
e
 
p
o
i
n
t
.


 
 
 
 
 
 
 
 
p
o
l
y
g
o
n
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
(
x
,
 
y
)
 
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
 
o
f
 
t
h
e
 
p
o
l
y
g
o
n
 
v
e
r
t
i
c
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
p
o
i
n
t
import unittest

class TestLineSegmentIntersection(unittest.TestCase):

    def test_intersection(self):
        seg1 = ((1, 1), (4, 4))
        seg2 = ((1, 4), (4, 1))
        expected = (2.5, 2.5)
        result = check_segments_intersection(seg1, seg2)
        self.assertEqual(result, expected, "The intersection should be at (2.5, 2.5)")

    def test_no_intersection(self):
        seg1 = ((1, 1), (2, 2))
        seg2 = ((3, 3), (4, 4))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "There should be no intersection")

    def test_parallel_segments(self):
        seg1 = ((1, 1), (2, 2))
        seg2 = ((1, 2), (2, 3))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "Parallel segments should not intersect")

    def test_no_intersection_due_to_offset(self):
        seg1 = ((1, 1), (3, 3))
        seg2 = ((3, 2), (4, 2))
        result = check_segments_intersection(seg1, seg2)
        self.assertIsNone(result, "There should be no intersection due to offset between segments")

    def test_intersection_with_large_coordinates(self):
        seg1 = ((1000, 1000), (2000, 2000))
        seg2 = ((1000, 2000), (2000, 1000))
        expected = (1500.0, 1500.0)
        result = check_segments_intersection(seg1, seg2)
        self.assertEqual(result, expected, "The intersection should be at (1500.0, 1500.0)")



if __name__ == '__main__':
    unittest.main()