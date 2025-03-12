d
e
f
 
f
i
n
d
_
p
o
w
e
r
s
(
n
u
m
:
 
i
n
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


 
 
 
 
F
i
n
d
 
t
h
e
 
p
o
w
e
r
s
 
o
f
 
2
 
a
n
d
 
3
 
t
h
a
t
 
m
u
l
t
i
p
l
y
 
t
o
 
p
r
o
d
u
c
e
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
(
i
n
t
)
:
 
A
 
p
o
s
i
t
i
v
e
 
i
n
t
e
g
e
r
 
g
r
e
a
t
e
r
 
t
h
a
n
 
z
e
r
o
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
(
n
,
 
m
)
 
w
h
e
r
e
 
n
 
i
s
 
t
h
e
 
p
o
w
e
r
 
o
f
 
2
 
a
n
d
 
m
 
i
s
 
t
h
e
 
p
o
w
e
r
 
o
f
 
3
.


 
 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
N
o
n
e
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
i
s
 
z
e
r
o
 
o
r
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
h
a
s
 
p
r
i
m
e
 
f
a
c
t
o
r
s
 
o
t
h
e
r
 
t
h
a
n
 
2
 
a
n
d
 
3
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
 
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
 
N
o
n
e


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
(
0
,
 
0
)


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
(
1
,
 
0
)


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
3
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
(
0
,
 
1
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
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
 
n
u
m
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
u
m
 
%
 
i
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
i
 
=
=
 
2
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
j
 
=
 
n
u
m
 
/
/
 
i


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
j
 
%
 
3
 
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
 
(
i
,
 
j
 
/
/
 
3
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
i
 
=
=
 
3
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
k
 
=
 
n
u
m
 
/
/
 
i


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
k
 
%
 
2
 
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
 
(
i
,
 
k
 
/
/
 
2
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
 
f
i
n
d
_
p
r
i
m
e
_
f
a
c
t
o
r
s
(
n
u
m
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
t
h
e
 
p
r
i
m
e
 
f
a
c
t
o
r
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
(
i
n
t
)
:
 
A
 
p
o
s
i
t
i
v
e
 
i
n
t
e
g
e
r
 
g
r
e
a
t
e
r
 
t
h
a
n
 
z
e
r
o
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
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
 
p
r
i
m
e
 
f
a
c
t
o
r
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
N
o
n
e
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
i
s
 
z
e
r
o
 
o
r
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
h
a
s
 
p
r
i
m
e
 
f
a
c
t
o
r
s
 
o
t
h
e
r
 
t
h
a
n
 
2
 
a
n
d
 
3
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
 
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
 
N
o
n
e


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
2
]


 
 
 
 
e
l
i
f
 
n
u
m
 
=
=
 
3
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
3
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
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
 
n
u
m
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
u
m
 
%
 
i
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
i
 
=
=
 
2
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
j
 
=
 
n
u
m
 
/
/
 
i


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
j
 
%
 
3
 
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
 
[
2
,
 
j
 
/
/
 
3
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
l
i
f
 
i
 
=
=
 
3
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
k
 
=
 
n
u
m
 
/
/
 
i


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
k
 
%
 
2
 
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
 
[
3
,
 
k
 
/
/
 
2
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
r
e
t
u
r
n
import unittest


class TestFindPowers(unittest.TestCase):

    def test_valid_cases(self):
        """Test valid numbers with only 2's and 3's as prime factors."""
        self.assertEqual(find_powers(18), (1, 2))  # 18 = 2^1 * 3^2
        self.assertEqual(find_powers(8), (3, 0))   # 8 = 2^3 * 3^0
        self.assertEqual(find_powers(27), (0, 3))  # 27 = 2^0 * 3^3
        self.assertEqual(find_powers(12), (2, 1))  # 12 = 2^2 * 3^1
        self.assertEqual(find_powers(1), (0, 0))    # 1 = 2^0 * 3^0

    def test_invalid_cases(self):
        """Test numbers with prime factors other than 2 and 3."""
        self.assertIsNone(find_powers(7))    # 7 is a prime factor
        self.assertIsNone(find_powers(14))   # 14 = 2^1 * 7^1 (contains 7)
        self.assertIsNone(find_powers(10))   # 10 = 2^1 * 5^1 (contains 5)


    def test_large_numbers(self):
        """Test large numbers that have only 2 and 3 as prime factors."""
        self.assertEqual(find_powers(864), (5, 3))  # 864 = 2^5 * 3^3
        self.assertEqual(find_powers(729), (0, 6))  # 729 = 2^0 * 3^6

    def test_edge_cases(self):
        """Test edge cases for minimal inputs."""
        self.assertEqual(find_powers(2), (1, 0))   # 2 = 2^1 * 3^0
        self.assertEqual(find_powers(3), (0, 1))   # 3 = 2^0 * 3^1
if __name__ == '__main__':
    unittest.main()