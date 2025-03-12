d
e
f
 
c
o
m
p
u
t
e
_
o
u
t
p
u
t
_
i
n
d
e
x
(
i
d
x
_
1
:
 
i
n
t
,
 
i
d
x
_
2
:
 
i
n
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
m
p
u
t
e
s
 
t
h
e
 
o
u
t
p
u
t
 
i
n
d
e
x
 
f
r
o
m
 
t
w
o
 
g
i
v
e
n
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
M
u
l
t
i
V
e
c
t
o
r
'
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
a
t
i
o
n


 
 
 
 
o
f
 
t
h
e
 
G
_
n
 
o
r
t
h
o
n
o
r
m
a
l
 
b
a
s
i
s
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
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
i
n
t
e
g
e
r
s
 
a
s
 
l
i
t
t
l
e
-
e
n
d
i
a
n
 
b
i
t
s
t
r
i
n
g
s
,
 
t
a
k
e
s
 
t
h
e
i
r
 
X
O
R
,


 
 
 
 
a
n
d
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
r
e
s
u
l
t
 
a
s
 
a
n
 
i
n
t
e
g
e
r
 
i
n
 
l
i
t
t
l
e
-
e
n
d
i
a
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
d
x
_
1
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
1
.


 
 
 
 
 
 
 
 
i
d
x
_
2
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
2
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
 
c
o
m
p
u
t
e
d
 
o
u
t
p
u
t
 
i
n
d
e
x
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
 
i
n
t
(
b
i
n
(
i
d
x
_
1
 
^
 
i
d
x
_
2
)
[
2
:
]
.
z
f
i
l
l
(
n
_
q
u
b
i
t
s
)
,
 
2
)






d
e
f
 
c
o
m
p
u
t
e
_
i
n
p
u
t
_
i
n
d
e
x
(
i
d
x
_
1
:
 
i
n
t
,
 
i
d
x
_
2
:
 
i
n
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
m
p
u
t
e
s
 
t
h
e
 
i
n
p
u
t
 
i
n
d
e
x
 
f
r
o
m
 
t
w
o
 
g
i
v
e
n
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
M
u
l
t
i
V
e
c
t
o
r
'
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
a
t
i
o
n


 
 
 
 
o
f
 
t
h
e
 
G
_
n
 
o
r
t
h
o
n
o
r
m
a
l
 
b
a
s
i
s
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
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
i
n
t
e
g
e
r
s
 
a
s
 
l
i
t
t
l
e
-
e
n
d
i
a
n
 
b
i
t
s
t
r
i
n
g
s
,
 
t
a
k
e
s
 
t
h
e
i
r
 
A
N
D
,


 
 
 
 
a
n
d
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
r
e
s
u
l
t
 
a
s
 
a
n
 
i
n
t
e
g
e
r
 
i
n
 
l
i
t
t
l
e
-
e
n
d
i
a
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
d
x
_
1
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
1
.


 
 
 
 
 
 
 
 
i
d
x
_
2
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
2
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
 
c
o
m
p
u
t
e
d
 
i
n
p
u
t
 
i
n
d
e
x
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
 
i
n
t
(
b
i
n
(
i
d
x
_
1
 
&
 
i
d
x
_
2
)
[
2
:
]
.
z
f
i
l
l
(
n
_
q
u
b
i
t
s
)
,
 
2
)






d
e
f
 
c
o
m
p
u
t
e
_
i
n
p
u
t
_
i
n
d
e
x
_
r
e
v
e
r
s
e
(
i
d
x
_
1
:
 
i
n
t
,
 
i
d
x
_
2
:
 
i
n
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
m
p
u
t
e
s
 
t
h
e
 
i
n
p
u
t
 
i
n
d
e
x
 
f
r
o
m
 
t
w
o
 
g
i
v
e
n
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
M
u
l
t
i
V
e
c
t
o
r
'
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
a
t
i
o
n


 
 
 
 
o
f
 
t
h
e
 
G
_
n
 
o
r
t
h
o
n
o
r
m
a
l
 
b
a
s
i
s
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
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
i
n
t
e
g
e
r
s
 
a
s
 
l
i
t
t
l
e
-
e
n
d
i
a
n
 
b
i
t
s
t
r
i
n
g
s
,
 
t
a
k
e
s
 
t
h
e
i
r
 
A
N
D
,


 
 
 
 
a
n
d
 
i
n
t
e
r
p
r
e
t
s
 
t
h
e
 
r
e
s
u
l
t
 
a
s
 
a
n
 
i
n
t
e
g
e
r
 
i
n
 
l
i
t
t
l
e
-
e
n
d
i
a
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
d
x
_
1
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
1
.


 
 
 
 
 
 
 
 
i
d
x
_
2
 
(
i
n
t
)
:
 
I
n
p
u
t
 
i
n
d
e
x
 
2
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
 
c
o
m
p
u
t
e
d
 
i
n
p
u
t
 
i
n
d
e
x
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
 
i
n
t
(
b
i
n
(
i
d
x
_
2
 
&
 
i
d
x
_
1
)
[
2
:
]
.
z
f
i
l
l
(
n
_
q
u
b
i
t
s
)
,
import unittest


class TestComputeOutputIndex(unittest.TestCase):

    def test_standard_case(self):
        """Test with two standard positive integers."""
        idx_1 = 3  # binary: 11
        idx_2 = 5  # binary: 101
        expected = 6  # 3 XOR 5 = 6
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_identical_indices(self):
        """Test with identical indices (should return 0)."""
        idx_1 = 7  # binary: 111
        idx_2 = 7  # binary: 111
        expected = 0  # 7 XOR 7 = 0
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_zero_index(self):
        """Test with one index as zero."""
        idx_1 = 0  # binary: 0
        idx_2 = 5  # binary: 101
        expected = 5  # 0 XOR 5 = 5
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large integer values."""
        idx_1 = 1024  # binary: 10000000000
        idx_2 = 2048  # binary: 100000000000
        expected = 3072  # 1024 XOR 2048 = 3072
        result = compute_output_index(idx_1, idx_2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()