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






d
e
f
 
c
o
n
v
e
r
t
_
t
o
_
r
i
n
g
_
f
o
r
m
a
t
(
h
o
l
e
s
:
 
L
i
s
t
)
 
-
>
 
L
i
s
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
 
l
i
s
t
 
o
f
 
h
o
l
e
 
p
o
s
i
t
i
o
n
s
 
t
o
 
t
h
e
 
r
i
n
g
 
f
o
r
m
a
t
 
(
l
i
s
t
 
o
f
 
1
s
 
a
n
d
 
0
s
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
o
l
e
s
 
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
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
p
o
s
i
t
i
o
n
s
 
o
f
 
t
h
e
 
h
o
l
e
s
 
(
0
-
i
n
d
e
x
e
d
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


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
0
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
1
.




 
 
 
 
"
"
"


 
 
 
 
r
i
n
g
_
f
o
r
m
a
t
 
=
 
[
0
]
 
*
 
3
2


 
 
 
 
f
o
r
 
h
o
l
e
 
i
n
 
h
o
l
e
s
:


 
 
 
 
 
 
 
 
r
i
n
g
_
f
o
r
m
a
t
[
h
o
l
e
]
 
=
 
1


 
 
 
 
r
e
t
u
r
n
 
r
i
n
g
_
f
o
r
m
a
t






d
e
f
 
c
o
n
v
e
r
t
_
t
o
_
h
o
l
e
_
f
o
r
m
a
t
(
r
i
n
g
_
f
o
r
m
a
t
:
 
L
i
s
t
)
 
-
>
 
L
i
s
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
 
r
i
n
g
 
f
o
r
m
a
t
 
(
l
i
s
t
 
o
f
 
1
s
 
a
n
d
 
0
s
)
 
t
o
 
a
 
l
i
s
t
 
o
f
 
h
o
l
e
 
p
o
s
i
t
i
o
n
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
i
n
g
_
f
o
r
m
a
t
 
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
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
0
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
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


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
p
o
s
i
t
i
o
n
s
 
o
f
 
t
h
e
 
h
o
l
e
s
 
(
0
-
i
n
d
e
x
e
d
)
.




 
 
 
 
"
"
"


 
 
 
 
h
o
l
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
i
,
 
b
i
t
 
i
n
 
e
n
u
m
e
r
a
t
e
(
r
i
n
g
_
f
o
r
m
a
t
)
:


 
 
 
 
 
 
 
 
i
f
 
b
i
t
 
=
=
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
h
o
l
e
s
.
a
p
p
e
n
d
(
i
)


 
 
 
 
r
e
t
u
r
n
 
h
o
l
e
s






d
e
f
 
c
o
n
v
e
r
t
_
t
o
_
b
i
t
_
f
o
r
m
a
t
(
r
i
n
g
_
f
o
r
m
a
t
:
 
L
i
s
t
)
 
-
>
 
L
i
s
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
 
r
i
n
g
 
f
o
r
m
a
t
 
(
l
i
s
t
 
o
f
 
1
s
 
a
n
d
 
0
s
)
 
t
o
 
a
 
l
i
s
t
 
o
f
 
b
i
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
i
n
g
_
f
o
r
m
a
t
 
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
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
0
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
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


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
1
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
0
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
 
[
1
 
-
 
b
i
t
 
f
o
r
 
b
i
t
 
i
n
 
r
i
n
g
_
f
o
r
m
a
t
]






d
e
f
 
c
o
n
v
e
r
t
_
t
o
_
r
i
n
g
_
f
o
r
m
a
t
_
f
r
o
m
_
b
i
t
_
f
o
r
m
a
t
(
b
i
t
_
f
o
r
m
a
t
:
 
L
i
s
t
)
 
-
>
 
L
i
s
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
 
l
i
s
t
 
o
f
 
b
i
t
s
 
t
o
 
a
 
r
i
n
g
 
f
o
r
m
a
t
 
(
l
i
s
t
 
o
f
 
1
s
 
a
n
d
 
0
s
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
t
_
f
o
r
m
a
t
 
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
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
1
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
0
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
l
e
n
g
t
h
 
3
2
,
 
w
h
e
r
e
 
p
o
s
i
t
i
o
n
s
 
w
i
t
h
 
h
o
l
e
s
 
a
r
e
 
0
 
a
n
d
 
o
t
h
e
r
s
 
a
r
e
 
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
 
[
1
 
-
 
b
i
t
 
f
o
r
 
b
i
t
 
i
n
 
b
i
t
_
f
o
r
m
a
t
]
import unittest


class TestConvertToRingFormat(unittest.TestCase):

    def test_no_holes(self):
        """ Test with no holes provided. """
        holes = []
        expected = [1] * 32  # All positions should be 1
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_single_hole(self):
        """ Test with a single hole position. """
        holes = [5]
        expected = [1] * 32
        expected[5] = 0  # Only position 5 should be 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_multiple_holes(self):
        """ Test with multiple hole positions. """
        holes = [0, 2, 4, 8, 16]
        expected = [1] * 32
        for hole in holes:
            expected[hole] = 0  # Set specified positions to 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_hole_out_of_bounds(self):
        """ Test with some hole positions out of bounds. """
        holes = [-1, 32, 5, 10]  # -1 and 32 are out of bounds
        expected = [1] * 32
        expected[5] = 0  # Only position 5 and 10 should be 0
        expected[10] = 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_all_holes(self):
        """ Test with all positions as holes. """
        holes = list(range(32))  # All positions from 0 to 31
        expected = [0] * 32  # All positions should be 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()