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
 
g
e
t
_
p
a
l
i
n
d
r
o
m
e
_
l
i
s
t
(
n
:
 
i
n
t
)
 
-
>
 
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
l
t
e
r
 
o
u
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
p
a
l
i
n
d
r
o
m
e
 
w
i
t
h
i
n
 
a
n
y
 
n
u
m
b
e
r
 
n
.
 
P
a
l
i
n
d
r
o
m
e
 
n
u
m
b
e
r
s
 
a
r
e
 
n
u
m
b
e
r
s
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
c
o
r
r
e
c
t
i
o
n
 
a
n
d
 
r
e
v
e
r
s
e
 
r
e
a
d
i
n
g
s
,
 
s
u
c
h
 
a
s
 
1
2
1
,
 
1
3
3
1




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
r
a
n
g
e
 
n
u
m
b
e
r




 
 
 
 
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
[
i
n
t
]
:
 
P
a
l
i
n
d
r
o
m
e
 
n
u
m
b
e
r
s


 
 
 
 
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
i
 
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
n
)
 
i
f
 
s
t
r
(
i
)
 
=
=
 
s
t
r
(
i
)
[
:
:
-
1
]
]






d
e
f
 
g
e
t
_
p
r
i
m
e
_
l
i
s
t
(
n
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
l
t
e
r
 
o
u
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
p
r
i
m
e
 
w
i
t
h
i
n
 
a
n
y
 
n
u
m
b
e
r
 
n
.
 
P
r
i
m
e
 
n
u
m
b
e
r
s
 
a
r
e
 
n
u
m
b
e
r
s
 
t
h
a
t
 
a
r
e
 
o
n
l
y
 
d
i
v
i
s
i
b
l
e
 
b
y
 
1
 
a
n
d
 
t
h
e
m
s
e
l
v
e
s
,
 
s
u
c
h
 
a
s
 
2
,
 
3
,
 
5
,
 
7
,
 
1
1
,
 
1
3
,
 
1
7
,
 
1
9
,
 
2
3
,
 
2
9
,
 
3
1
,
 
3
7
,
 
4
1
,
 
4
3
,
 
4
7
,
 
5
3
,
 
5
9
,
 
6
1
,
 
6
7
,
 
7
1
,
 
7
3
,
 
7
9
,
 
8
3
,
 
8
9
,
 
9
7




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
r
a
n
g
e
 
n
u
m
b
e
r




 
 
 
 
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
[
i
n
t
]
:
 
P
r
i
m
e
 
n
u
m
b
e
r
s


 
 
 
 
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
i
 
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
n
)
 
i
f
 
i
s
_
p
r
i
m
e
(
i
)
]






d
e
f
 
i
s
_
p
r
i
m
e
(
n
:
 
i
n
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
 
n
u
m
b
e
r
 
i
s
 
p
r
i
m
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
n
u
m
b
e
r
 
t
o
 
c
h
e
c
k




 
 
 
 
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
 
p
r
i
m
e
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
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
2
,
 
i
n
t
(
n
 
*
*
 
0
.
5
)
 
+
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
n
 
%
 
i
 
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
 
F
a
l
s
e


 
 
 
 
r
e
t
u
r
n
 
T
r
u
e






d
e
f
 
g
e
t
_
p
e
r
f
e
c
t
_
s
q
u
a
r
e
_
l
i
s
t
(
n
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
l
t
e
r
 
o
u
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
p
e
r
f
e
c
t
 
s
q
u
a
r
e
 
w
i
t
h
i
n
 
a
n
y
 
n
u
m
b
e
r
 
n
.
 
P
e
r
f
e
c
t
 
s
q
u
a
r
e
 
a
r
e
 
n
u
m
b
e
r
s
 
t
h
a
t
 
a
r
e
 
t
h
e
 
p
e
r
f
e
c
t
 
s
q
u
a
r
e
 
o
f
 
a
n
 
i
n
t
e
g
e
r
,
 
s
u
c
h
 
a
s
 
1
,
 
4
,
 
9
,
 
1
6
,
 
2
5
,
 
3
6
,
 
4
9
,
 
6
4
,
 
8
1
,
 
1
0
0
,
 
1
2
1
,
 
1
4
4
,
 
1
6
9
,
 
1
9
6
,
 
2
2
5
,
 
2
5
6
,
 
2
8
9
,
 
3
2
4
,
 
3
6
1
,
 
4
0
0
,
 
4
4
1
,
 
4
8
4
,
 
5
2
9
,
 
5
7
6
,
 
6
2
5
,
 
6
7
6
,
 
7
2
9
,
 
7
8
4
,
 
8
4
1
,
 
9
0
0
,
 
9
6
1
,
 
1
0
2
4
,
 
1
0
8
9
,
 
1
1
5
6
,
 
1
2
2
5
,
 
1
2
9
6
,
 
1
3
6
9
,
 
1
4
4
4
,
 
1
5
import unittest


class TestNthPalindrome(unittest.TestCase):
    def test_single_digit(self):
        """Test case for the first palindrome"""
        self.assertEqual(get_palindrome_list(1), [0], "The first palindrome should be 0")

    def test_edge_of_single_and_double_digits(self):
        """Test case for the tenth palindrome, transitioning to double digits"""
        self.assertEqual(get_palindrome_list(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "The tenth palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_edge_of_double_and_triple_digits(self):
        """Test case for the 100th palindrome, transitioning to triple digits"""
        self.assertEqual(get_palindrome_list(100), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99],
                         "The 100th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]")

    def test_large_number(self):
        """Test case for a larger number, e.g., the 1000th palindrome"""
        self.assertEqual(get_palindrome_list(1000),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141,
                          151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333,
                          343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525,
                          535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717,
                          727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909,
                          919, 929, 939, 949, 959, 969, 979, 989, 999]
                         ,
                         "The 1000th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]")

if __name__ == '__main__':
    unittest.main()