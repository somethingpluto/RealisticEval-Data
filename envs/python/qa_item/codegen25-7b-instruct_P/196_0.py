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
n
e
r
a
t
e
_
p
r
i
m
e
s
(
l
i
m
i
t
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
n
d
 
a
l
l
 
p
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
 
t
h
a
t
 
a
r
e
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
l
i
m
i
t
 
u
s
i
n
g
 
t
h
e
 
E
i
c
h
l
e
r
 
s
i
e
v
e
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
m
i
t
 
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
 
(
i
n
c
l
u
s
i
v
e
)
 
f
o
r
 
f
i
n
d
i
n
g
 
p
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
[
i
n
t
]
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
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
p
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
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
t
h
e
 
l
i
m
i
t
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
i
m
i
t
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
p
r
i
m
e
s
 
=
 
[
T
r
u
e
]
 
*
 
(
l
i
m
i
t
 
+
 
1
)


 
 
 
 
p
r
i
m
e
s
[
0
]
 
=
 
p
r
i
m
e
s
[
1
]
 
=
 
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
l
i
m
i
t
 
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
 
p
r
i
m
e
s
[
i
]
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
i
 
*
 
i
,
 
l
i
m
i
t
 
+
 
1
,
 
i
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
m
e
s
[
j
]
 
=
 
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
l
i
m
i
t
 
+
 
1
)
 
i
f
 
p
r
i
m
e
s
[
i
]
]






d
e
f
 
g
e
n
e
r
a
t
e
_
p
r
i
m
e
s
_
2
(
l
i
m
i
t
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
n
d
 
a
l
l
 
p
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
 
t
h
a
t
 
a
r
e
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
l
i
m
i
t
 
u
s
i
n
g
 
t
h
e
 
t
r
i
a
l
 
d
i
v
i
s
i
o
n
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
m
i
t
 
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
 
(
i
n
c
l
u
s
i
v
e
)
 
f
o
r
 
f
i
n
d
i
n
g
 
p
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
[
i
n
t
]
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
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
p
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
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
t
h
e
 
l
i
m
i
t
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
i
m
i
t
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
 
p
r
i
m
e
s
 
=
 
[
]




 
 
 
 
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
 
l
i
m
i
t
 
+
 
1
)
:


 
 
 
 
 
 
 
 
i
s
_
p
r
i
m
e
 
=
 
T
r
u
e


 
 
 
 
 
 
 
 
f
o
r
 
j
 
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
i
 
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
 
i
 
%
 
j
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
s
_
p
r
i
m
e
 
=
 
F
a
l
s
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k


 
 
 
 
 
 
 
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
m
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
 
p
r
i
m
e
s






d
e
f
 
g
e
n
e
r
a
t
e
_
p
r
i
m
e
s
_
3
(
l
i
m
i
t
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
n
d
 
a
l
l
 
p
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
 
t
h
a
t
 
a
r
e
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
l
i
m
i
t
 
u
s
i
n
g
 
t
h
e
 
w
h
e
e
l
 
f
a
c
t
o
r
i
z
a
t
i
o
n
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
m
i
t
 
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
 
(
i
n
c
l
u
s
i
v
e
)
 
f
o
r
 
f
i
n
d
i
n
g
 
p
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
[
i
n
t
]
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
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
p
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
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
t
h
e
 
l
i
m
i
t
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
i
m
i
t
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]




 
 
 
import unittest


class Tester(unittest.TestCase):

    def test_small_limit(self):
        """Test Case 1: Small limit (10)"""
        expected = [2, 3, 5, 7]
        self.assertEqual(generate_primes(10), expected)

    def test_prime_limit(self):
        """Test Case 2: Prime limit (29)"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(generate_primes(29), expected)

    def test_non_prime_limit(self):
        """Test Case 3: Non-prime limit (30)"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(generate_primes(30), expected)

    def test_limit_of_two(self):
        """Test Case 4: Limit of 2 (smallest prime)"""
        expected = [2]
        self.assertEqual(generate_primes(2), expected)

    def test_invalid_limit(self):
        """Test Case 5: Invalid limit (1, should throw an exception)"""
        with self.assertRaises(ValueError):  # Catch ValueError instead of std::invalid_argument
            generate_primes(1)

if __name__ == '__main__':
    unittest.main()