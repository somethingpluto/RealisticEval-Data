i
m
p
o
r
t
 
n
u
m
p
y
 
a
s
 
n
p




d
e
f
 
i
m
2
c
o
l
(
i
m
a
g
e
,
 
f
i
l
t
e
r
_
h
e
i
g
h
t
,
 
f
i
l
t
e
r
_
w
i
d
t
h
,
 
s
t
r
i
d
e
=
1
,
 
p
a
d
d
i
n
g
=
0
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
y
 
t
h
e
 
i
m
2
c
o
l
 
o
p
e
r
a
t
i
o
n
 
t
o
 
a
n
 
i
n
p
u
t
 
i
m
a
g
e
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
-
 
i
m
a
g
e
 
(
n
u
m
p
y
 
a
r
r
a
y
)
:
 
T
h
e
 
i
n
p
u
t
 
i
m
a
g
e
 
o
f
 
s
h
a
p
e
 
(
C
,
 
H
,
 
W
)
 
w
h
e
r
e
:


 
 
 
 
 
 
 
 
C
:
 
N
u
m
b
e
r
 
o
f
 
c
h
a
n
n
e
l
s


 
 
 
 
 
 
 
 
H
:
 
H
e
i
g
h
t
 
o
f
 
t
h
e
 
i
m
a
g
e


 
 
 
 
 
 
 
 
W
:
 
W
i
d
t
h
 
o
f
 
t
h
e
 
i
m
a
g
e


 
 
 
 
-
 
f
i
l
t
e
r
_
h
e
i
g
h
t
 
(
i
n
t
)
:
 
H
e
i
g
h
t
 
o
f
 
t
h
e
 
f
i
l
t
e
r


 
 
 
 
-
 
f
i
l
t
e
r
_
w
i
d
t
h
 
(
i
n
t
)
:
 
W
i
d
t
h
 
o
f
 
t
h
e
 
f
i
l
t
e
r


 
 
 
 
-
 
s
t
r
i
d
e
 
(
i
n
t
)
:
 
S
t
r
i
d
e
 
o
f
 
t
h
e
 
f
i
l
t
e
r


 
 
 
 
-
 
p
a
d
d
i
n
g
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
p
i
x
e
l
s
 
t
o
 
p
a
d
 
t
h
e
 
i
n
p
u
t
 
i
m
a
g
e




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
-
 
c
o
l
 
(
n
u
m
p
y
 
a
r
r
a
y
)
:
 
A
 
2
D
 
a
r
r
a
y
 
w
h
e
r
e
 
e
a
c
h
 
c
o
l
u
m
n
 
i
s
 
a
 
f
l
a
t
t
e
n
e
d
 
f
i
l
t
e
r
 
r
e
g
i
o
n


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
d
i
m
e
n
s
i
o
n
s
 
o
f
 
t
h
e
 
i
m
a
g
e


 
 
 
 
C
,
 
H
,
 
W
 
=
 
i
m
a
g
e
.
s
h
a
p
e




 
 
 
 
#
 
G
e
t
 
t
h
e
 
h
e
i
g
h
t
 
a
n
d
 
w
i
d
t
h
 
o
f
 
t
h
e
 
o
u
t
p
u
t


 
 
 
 
o
u
t
_
h
e
i
g
h
t
 
=
 
(
H
 
+
 
2
 
*
 
p
a
d
d
i
n
g
 
-
 
f
i
l
t
e
r
_
h
e
i
g
h
t
)
 
/
/
 
s
t
r
i
d
e
 
+
 
1


 
 
 
 
o
u
t
_
w
i
d
t
h
 
=
 
(
W
 
+
 
2
 
*
 
p
a
d
d
i
n
g
 
-
 
f
i
l
t
e
r
_
w
i
d
t
h
)
 
/
/
 
s
t
r
i
d
e
 
+
 
1




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
o
u
t
p
u
t


 
 
 
 
c
o
l
 
=
 
n
p
.
z
e
r
o
s
(
(
C
,
 
f
i
l
t
e
r
_
h
e
i
g
h
t
 
*
 
f
i
l
t
e
r
_
w
i
d
t
h
,
 
o
u
t
_
h
e
i
g
h
t
 
*
 
o
u
t
_
w
i
d
t
h
)
)




 
 
 
 
#
 
P
a
d
 
t
h
e
 
i
n
p
u
t
 
i
m
a
g
e


 
 
 
 
p
a
d
d
e
d
 
=
 
n
p
.
p
a
d
(
i
m
a
g
e
,
 
(
(
0
,
 
0
)
,
 
(
p
a
d
d
i
n
g
,
 
p
a
d
d
i
n
g
)
,
 
(
p
a
d
d
i
n
g
,
 
p
a
d
d
i
n
g
)
)
,
 
'
c
o
n
s
t
a
n
t
'
)




 
 
 
 
#
 
I
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
o
u
t
p
u
t


 
 
 
 
f
o
r
 
y
 
i
n
 
r
a
n
g
e
(
o
u
t
_
h
e
i
g
h
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
x
 
i
n
 
r
a
n
g
e
(
o
u
t
_
w
i
d
t
h
)
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
G
e
t
 
t
h
e
 
c
u
r
r
e
n
t
 
r
e
g
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
r
e
g
i
o
n
 
=
 
p
a
d
d
e
d
[
:
,
 
y
 
*
 
s
t
r
i
d
e
:
y
 
*
 
s
t
r
i
d
e
 
+
 
f
i
l
t
e
r
_
h
e
i
g
h
t
,
 
x
 
*
 
s
t
r
i
d
e
:
x
 
*
 
s
t
r
i
d
e
 
+
 
f
i
l
t
e
r
_
w
i
d
t
h
]




 
 
 
 
 
 
 
 
 
 
 
 
#
 
R
e
s
h
a
p
e
 
t
h
e
 
r
e
g
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
c
o
l
[
:
,
 
:
,
 
y
 
*
 
o
u
t
_
w
i
d
t
h
 
+
 
x
]
 
=
 
r
e
g
i
o
n
.
r
e
s
h
a
p
e
(
C
,
 
-
1
)




 
 
 
 
r
e
t
u
r
n
 
c
o
l




d
e
f
 
c
o
l
2
i
m
(
c
o
l
,
 
i
m
a
g
e
_
s
h
a
p
e
,
 
f
i
l
t
e
r
_
h
e
i
g
h
t
,
 
f
i
l
t
e
r
_
w
i
d
t
h
,
 
s
t
r
i
d
e
=
1
,
 
p
a
d
d
i
n
g
=
0
)
:


 
 
 
 
"
"
"


 
 
 
 
A
p
p
l
y
 
t
h
e
 
c
o
l
2
i
m
 
o
p
e
r
a
t
i
o
n
 
t
o
 
a
n
 
i
n
p
u
t
 
i
m
a
g
e
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
-
 
c
o
l
 
(
n
u
m
p
y
 
a
r
r
a
y
)
:
 
T
h
e
 
i
n
p
u
t
 
i
m
a
g
e
 
o
f
 
s
h
a
p
e
 
(
C
,
 
f
i
l
t
e
r
_
h
e
i
g
h
t
 
*
 
f
i
l
t
e
r
_
w
i
d
t
h
,
 
o
u
t
_
h
e
i
g
h
t
 
*
 
o
u
t
_
w
i
d
t
h
)
 
w
h
e
r
e
:


 
 
 
 
 
 
 
import unittest

import numpy as np


class TestIm2Col(unittest.TestCase):

    def test_single_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 3, 5, 6, 7, 9, 10, 11],
            [2, 3, 4, 6, 7, 8, 10, 11, 12],
            [5, 6, 7, 9, 10, 11, 13, 14, 15],
            [6, 7, 8, 10, 11, 12, 14, 15, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_single_channel_no_padding_stride_2(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 2
        padding = 0

        expected_output = np.array([
            [1, 3, 9, 11],
            [2, 4, 10, 12],
            [5, 7, 13, 15],
            [6, 8, 14, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_multi_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]
        ])  # Shape (2, 3, 3), 2 channels
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 4, 5],
            [2, 3, 5, 6],
            [4, 5, 7, 8],
            [5, 6, 8, 9],
            [9, 8, 6, 5],
            [8, 7, 5, 4],
            [6, 5, 3, 2],
            [5, 4, 2, 1]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

if __name__ == '__main__':
    unittest.main()