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
,
 
T
u
p
l
e




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
 
g
e
t
_
T
_
i
n
_
l
o
g
1
0
_
K
e
l
v
i
n
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
l
o
g
1
0
(
T
_
k
e
V
)
 
+
 
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
k
e
V
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
l
o
g
1
0
(
T
)
 
+
 
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
k
e
V
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
f
"
T
_
k
e
V
 
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
 
o
r
 
a
 
t
u
p
l
e
,
 
n
o
t
 
{
t
y
p
e
(
T
_
k
e
V
)
}
"
)






d
e
f
 
g
e
t
_
T
_
i
n
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
e
l
v
i
n
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
e
l
v
i
n
 
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
e
l
v
i
n
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
 
1
0
 
*
*
 
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
e
l
v
i
n
 
-
 
k
import unittest

import numpy as np

k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K


class TestGetTInLog10Kelvin(unittest.TestCase):

    # Existing test cases here...

    def test_scalar_input_high_temperature(self):
        """Test with a high scalar input."""
        T_keV = 100.0
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_scalar_input_low_temperature(self):
        """Test with a low scalar input."""
        T_keV = 0.01
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input_large_range(self):
        """Test with a tuple of temperatures over a large range."""
        T_keV = (0.1, 1.0, 10.0, 100.0, 1000.0)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

    def test_tuple_input_repeated_values(self):
        """Test with a tuple of repeated temperature values."""
        T_keV = (1.0, 1.0, 1.0)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

    def test_scalar_input_non_integer(self):
        """Test with a non-integer scalar input."""
        T_keV = 2.5
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input_floating_point(self):
        """Test with a tuple of floating-point temperatures."""
        T_keV = (1.5, 2.5, 3.5)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)


    def test_large_tuple_input(self):
        """Test with a large tuple of temperature values."""
        T_keV = tuple(np.arange(1, 1001, 1))  # Temperatures from 1 keV to 1000 keV
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

if __name__ == '__main__':
    unittest.main()