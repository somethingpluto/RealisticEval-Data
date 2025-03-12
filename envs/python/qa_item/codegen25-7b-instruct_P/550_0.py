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
 
T
u
p
l
e
,
 
U
n
i
o
n




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




#
 
D
e
f
i
n
e
 
t
h
e
 
c
o
n
s
t
a
n
t
 
f
o
r
 
c
o
n
v
e
r
s
i
o
n
:
 
B
o
l
t
z
m
a
n
n
 
c
o
n
s
t
a
n
t
 
i
n
 
k
e
V
/
K


k
_
B
_
o
v
e
r
_
k
e
V
 
=
 
8
.
6
1
7
3
3
3
2
6
2
1
4
5
e
-
5
 
 
#
 
e
V
/
K
 
t
o
 
k
e
V
/
K






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
l
o
g
1
0
_
K
_
t
o
_
k
e
V
(
T
_
l
o
g
1
0
_
K
:
 
U
n
i
o
n
[
f
l
o
a
t
,
 
T
u
p
l
e
]
)
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
s
 
t
e
m
p
e
r
a
t
u
r
e
 
f
r
o
m
 
l
o
g
1
0
(
K
)
 
t
o
 
k
e
V
 
f
o
r
 
a
 
g
i
v
e
n
 
i
n
p
u
t
 
(
s
c
a
l
a
r
 
o
r
 
t
u
p
l
e
)
.
k
_
B
_
o
v
e
r
_
k
e
V
 
=
 
8
.
6
1
7
3
3
3
2
6
2
1
4
5
e
-
5




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
T
_
l
o
g
1
0
_
K
 
(
f
l
o
a
t
 
o
r
 
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
 
t
e
m
p
e
r
a
t
u
r
e
 
i
n
 
l
o
g
1
0
(
K
)
.
 
C
a
n
 
b
e
 
a
 
s
c
a
l
a
r
 
o
r
 
a
 
t
u
p
l
e
 
o
f
 
t
e
m
p
e
r
a
t
u
r
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
 
o
r
 
t
u
p
l
e
:
 
T
h
e
 
t
e
m
p
e
r
a
t
u
r
e
(
s
)
 
i
n
 
k
e
V
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
i
n
p
u
t
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
i
n
p
u
t
 
i
s
 
n
o
t
 
a
 
s
c
a
l
a
r
 
(
i
n
t
 
o
r
 
f
l
o
a
t
)
 
o
r
 
a
 
t
u
p
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
T
_
l
o
g
1
0
_
K
,
 
(
i
n
t
,
 
f
l
o
a
t
)
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
p
.
p
o
w
e
r
(
1
0
,
 
T
_
l
o
g
1
0
_
K
)
 
*
 
k
_
B
_
o
v
e
r
_
k
e
V


 
 
 
 
e
l
i
f
 
i
s
i
n
s
t
a
n
c
e
(
T
_
l
o
g
1
0
_
K
,
 
t
u
p
l
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
t
u
p
l
e
(
n
p
.
p
o
w
e
r
(
1
0
,
 
T
)
 
*
 
k
_
B
_
o
v
e
r
_
k
e
V
 
f
o
r
 
T
 
i
n
 
T
_
l
o
g
1
0
_
K
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
"
T
h
e
 
i
n
p
u
t
 
t
e
m
p
e
r
a
t
u
r
e
 
m
u
s
t
 
b
e
 
a
 
s
c
a
l
a
r
 
(
i
n
t
 
o
r
 
f
l
o
a
t
)
 
o
r
 
a
 
t
u
p
l
e
 
o
f
 
s
c
a
l
a
r
s
.
"


 
 
 
 
 
 
 
 
)






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
k
e
V
_
t
o
_
l
o
g
1
0
_
K
(
T
_
k
e
V
:
 
U
n
i
o
n
[
f
l
o
a
t
,
 
T
u
p
l
e
]
)
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
s
 
t
e
m
p
e
r
a
t
u
r
e
 
f
r
o
m
 
k
e
V
 
t
o
 
l
o
g
1
0
(
K
)
 
f
o
r
 
a
 
g
i
v
e
n
 
i
n
p
u
t
 
(
s
c
a
l
a
r
 
o
r
 
t
u
p
l
e
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
T
_
k
e
V
 
(
f
l
o
a
t
 
o
r
 
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
 
t
e
m
p
e
r
a
t
u
r
e
 
i
n
 
k
e
V
.
 
C
a
n
 
b
e
 
a
 
s
c
a
l
a
r
 
o
r
 
a
 
t
u
p
l
e
 
o
f
 
t
e
m
p
e
r
a
t
u
r
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
 
o
r
 
t
u
p
l
e
:
 
T
h
e
 
t
e
m
p
e
r
a
t
u
r
e
(
s
)
 
i
n
 
l
o
g
1
0
(
K
)
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
i
n
p
u
t
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
t
h
e
 
i
n
p
u
t
 
i
s
 
n
o
t
 
a
 
s
c
a
l
a
r
 
(
i
n
t
 
o
r
 
f
l
o
a
t
)
 
o
r
 
a
 
t
u
p
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
T
_
k
e
V
import unittest

k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K
class TestConvertLog10KToKeV(unittest.TestCase):

    def test_scalar_input(self):
        """Test conversion of a single scalar log10(K) value."""
        T_log10_K = 3.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input(self):
        """Test conversion of a tuple of log10(K) values."""
        T_log10_K = (2.0, 3.0, 4.0)
        expected_results = tuple(10 ** t * k_B_over_keV for t in T_log10_K)
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertEqual(result, expected_results)

    def test_zero_input(self):
        """Test conversion of log10(K) = 0."""
        T_log10_K = 0.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_negative_input(self):
        """Test conversion of a negative log10(K) value."""
        T_log10_K = -1.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_large_tuple_input(self):
        """Test conversion of a large tuple of log10(K) values."""
        T_log10_K = (1.0, 2.0, 3.0, 4.0, 5.0)
        expected_results = tuple(10 ** t * k_B_over_keV for t in T_log10_K)
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertEqual(result, expected_results)

    def test_single_large_value(self):
        """Test conversion of a large log10(K) value."""
        T_log10_K = 10.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_invalid_input(self):
        """Test conversion with invalid input (string)."""
        T_log10_K = "invalid"
        with self.assertRaises(ValueError):
            convert_log10_K_to_keV(T_log10_K)

if __name__ == '__main__':
    unittest.main()