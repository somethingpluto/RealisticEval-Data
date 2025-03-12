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
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
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
 
U
n
i
o
n
[
i
n
t
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


 
 
 
 
f
i
n
d
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
a
 
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
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
i
t
 
t
h
a
t
 
i
s
 
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
0
 
o
r
 
5


 
 
 
 
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
 
T
h
e
 
u
p
p
e
r
 
b
o
u
n
d
 
o
f
 
t
h
e
 
r
a
n
g
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


 
 
 
 
 
 
 
 
T
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
n
 
t
h
a
t
 
i
s
 
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
 
5
,
 
o
r


 
 
 
 
 
 
 
 
 
N
o
n
e
 
i
f
 
n
o
 
s
u
c
h
 
n
u
m
b
e
r
 
e
x
i
s
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
<
 
1
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


 
 
 
 
i
f
 
n
 
%
 
5
 
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
 
n


 
 
 
 
i
f
 
n
 
%
 
1
0
 
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
 
n
 
/
/
 
1
0


 
 
 
 
r
e
t
u
r
n
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
(
n
 
/
/
 
1
0
)






d
e
f
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
_
2
(
n
:
 
i
n
t
)
 
-
>
 
U
n
i
o
n
[
i
n
t
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


 
 
 
 
f
i
n
d
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
a
 
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
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
i
t
 
t
h
a
t
 
i
s
 
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
0
 
o
r
 
5


 
 
 
 
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
 
T
h
e
 
u
p
p
e
r
 
b
o
u
n
d
 
o
f
 
t
h
e
 
r
a
n
g
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


 
 
 
 
 
 
 
 
T
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
n
 
t
h
a
t
 
i
s
 
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
 
5
,
 
o
r


 
 
 
 
 
 
 
 
 
N
o
n
e
 
i
f
 
n
o
 
s
u
c
h
 
n
u
m
b
e
r
 
e
x
i
s
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
<
 
1
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


 
 
 
 
i
f
 
n
 
%
 
5
 
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
 
n


 
 
 
 
i
f
 
n
 
%
 
1
0
 
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
 
n
 
/
/
 
1
0


 
 
 
 
r
e
t
u
r
n
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
_
2
(
n
 
/
/
 
1
0
)






d
e
f
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
_
3
(
n
:
 
i
n
t
)
 
-
>
 
U
n
i
o
n
[
i
n
t
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


 
 
 
 
f
i
n
d
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
a
 
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
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
i
t
 
t
h
a
t
 
i
s
 
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
0
 
o
r
 
5


 
 
 
 
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
 
T
h
e
 
u
p
p
e
r
 
b
o
u
n
d
 
o
f
 
t
h
e
 
r
a
n
g
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


 
 
 
 
 
 
 
 
T
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
n
 
t
h
a
t
 
i
s
 
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
 
5
,
 
o
r


 
 
 
 
 
 
 
 
 
N
o
n
e
 
i
f
 
n
o
 
s
u
c
h
 
n
u
m
b
e
r
 
e
x
i
s
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
<
 
1
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


 
 
 
 
i
f
 
n
 
%
 
5
 
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
 
n


 
 
 
 
i
f
 
n
 
%
 
1
0
 
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
 
n
 
/
/
 
1
0


 
 
 
 
r
e
t
u
r
n
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
_
3
(
n
 
/
/
 
1
0
)






d
e
f
 
f
i
n
d
_
l
a
r
g
e
s
t
_
d
i
v
i
s
i
b
l
e
_
4
(
n
:
 
i
n
t
)
 
-
>
 
U
n
i
o
n
[
i
n
t
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


 
 
 
 
f
i
n
d
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
b
e
t
w
e
e
n
 
a
 
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
 
n
 
a
n
d
 
h
a
l
f
 
o
f
 
i
t
import unittest


class TestFindLargestDivisible(unittest.TestCase):
    def test_typical_case(self):
        """Test with a typical input where the largest divisible number should be found."""
        self.assertEqual(find_largest_divisible(50), 50)
        self.assertEqual(find_largest_divisible(47), 45)

    def test_no_divisible_found(self):
        """Test a case where no divisible number is found within the range."""
        self.assertIsNone(find_largest_divisible(4))

    def test_exact_half_divisible(self):
        """Test when the half of n is exactly divisible by 5."""
        self.assertEqual(find_largest_divisible(10), 10)

    def test_large_number(self):
        """Test with a large number to ensure performance and correctness."""
        self.assertEqual(find_largest_divisible(1000), 1000)

    def test_lower_bound(self):
        """Test the function with the lowest bound that should find a divisible number."""
        self.assertEqual(find_largest_divisible(5), 5)

if __name__ == '__main__':
    unittest.main()