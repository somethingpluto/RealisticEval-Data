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
 
p
e
r
f
o
r
m
_
p
o
l
y
n
o
m
i
a
l
_
d
e
c
r
y
p
t
i
o
n
(
d
e
g
r
e
e
:
 
i
n
t
,
 
m
o
d
u
l
u
s
:
 
i
n
t
,
 
k
e
y
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
,
 
e
n
c
r
y
p
t
e
d
_
d
a
t
a
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
d
e
c
r
y
p
t
i
o
n
 
b
a
s
e
d
 
o
n
 
p
o
l
y
n
o
m
i
a
l
s
 
a
n
d
 
k
e
y
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
g
r
e
e
 
(
i
n
t
)
:
 
T
h
e
 
h
i
g
h
e
s
t
 
d
e
g
r
e
e
 
o
f
 
a
 
p
o
l
y
n
o
m
i
a
l
 
i
s
 
a
d
d
e
d
 
b
y
 
o
n
e


 
 
 
 
 
 
 
 
m
o
d
u
l
u
s
 
(
i
n
t
)
:
 
M
o
d
u
l
u
s
 
t
o
 
u
s
e
 
w
h
e
n
 
e
n
c
r
y
p
t
i
n
g
 
q
u
e
s
t
i
o
n


 
 
 
 
 
 
 
 
k
e
y
 
(
L
i
s
t
[
i
n
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
e
n
c
r
y
p
t
e
d
 
k
e
y
s


 
 
 
 
 
 
 
 
e
n
c
r
y
p
t
e
d
_
d
a
t
a
 
(
L
i
s
t
[
i
n
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
e
n
c
r
y
p
t
e
d
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
d
e
c
r
y
p
t
e
d
 
q
u
e
s
t
i
o
n




 
 
 
 
"
"
"


 
 
 
 
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
 
v
a
r
i
a
b
l
e
s


 
 
 
 
n
 
=
 
l
e
n
(
e
n
c
r
y
p
t
e
d
_
d
a
t
a
)


 
 
 
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a
 
=
 
[
0
]
 
*
 
n


 
 
 
 
#
 
P
e
r
f
o
r
m
 
d
e
c
r
y
p
t
i
o
n


 
 
 
 
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
:


 
 
 
 
 
 
 
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a
[
i
]
 
=
 
p
e
r
f
o
r
m
_
p
o
l
y
n
o
m
i
a
l
_
d
e
c
r
y
p
t
i
o
n
_
s
i
n
g
l
e
(
d
e
g
r
e
e
,
 
m
o
d
u
l
u
s
,
 
k
e
y
,
 
e
n
c
r
y
p
t
e
d
_
d
a
t
a
[
i
]
)


 
 
 
 
r
e
t
u
r
n
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a






d
e
f
 
p
e
r
f
o
r
m
_
p
o
l
y
n
o
m
i
a
l
_
d
e
c
r
y
p
t
i
o
n
_
s
i
n
g
l
e
(
d
e
g
r
e
e
:
 
i
n
t
,
 
m
o
d
u
l
u
s
:
 
i
n
t
,
 
k
e
y
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
,
 
e
n
c
r
y
p
t
e
d
_
d
a
t
a
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
d
e
c
r
y
p
t
i
o
n
 
b
a
s
e
d
 
o
n
 
p
o
l
y
n
o
m
i
a
l
s
 
a
n
d
 
k
e
y
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
g
r
e
e
 
(
i
n
t
)
:
 
T
h
e
 
h
i
g
h
e
s
t
 
d
e
g
r
e
e
 
o
f
 
a
 
p
o
l
y
n
o
m
i
a
l
 
i
s
 
a
d
d
e
d
 
b
y
 
o
n
e


 
 
 
 
 
 
 
 
m
o
d
u
l
u
s
 
(
i
n
t
)
:
 
M
o
d
u
l
u
s
 
t
o
 
u
s
e
 
w
h
e
n
 
e
n
c
r
y
p
t
i
n
g
 
q
u
e
s
t
i
o
n


 
 
 
 
 
 
 
 
k
e
y
 
(
L
i
s
t
[
i
n
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
e
n
c
r
y
p
t
e
d
 
k
e
y
s


 
 
 
 
 
 
 
 
e
n
c
r
y
p
t
e
d
_
d
a
t
a
 
(
i
n
t
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
e
n
c
r
y
p
t
e
d
 
q
u
e
s
t
i
o
n




 
 
 
 
R
e
t
u
r
n
s
:
 
d
e
c
r
y
p
t
e
d
 
q
u
e
s
t
i
o
n




 
 
 
 
"
"
"


 
 
 
 
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
 
v
a
r
i
a
b
l
e
s


 
 
 
 
n
 
=
 
l
e
n
(
k
e
y
)


 
 
 
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a
 
=
 
0


 
 
 
 
#
 
P
e
r
f
o
r
m
 
d
e
c
r
y
p
t
i
o
n


 
 
 
 
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
:


 
 
 
 
 
 
 
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a
 
=
 
(
d
e
c
r
y
p
t
e
d
_
d
a
t
a
 
+
 
p
o
w
(
e
n
c
r
y
p
t
e
d
_
d
a
t
a
,
 
d
e
g
r
e
e
 
-
 
i
,
 
m
o
d
u
l
u
s
)
 
*
 
k
e
y
[
i
]
)
 
%
 
m
o
d
u
l
u
s


 
 
 
 
r
e
t
u
r
n
 
d
e
c
r
y
p
t
e
d
_
d
a
t
a






d
e
f
 
p
e
r
f
o
r
m
_
p
o
l
y
n
o
m
i
a
l
_
e
n
c
r
y
p
t
i
o
n
(
d
e
g
r
e
e
:
 
i
n
t
,
 
m
o
d
u
l
u
s
:
 
i
n
t
,
 
p
u
b
l
i
c
_
k
e
y
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
,
 
d
a
t
a
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
e
n
c
r
y
p
t
i
o
n
 
b
a
s
e
d
 
o
n
 
p
o
l
y
n
o
m
i
a
l
s
 
a
n
d
 
k
e
y
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
g
r
e
e
 
(
i
n
t
)
:
 
T
h
e
 
h
i
g
h
e
s
t
 
d
e
g
r
e
e
 
o
f
 
a
 
p
o
l
y
n
o
m
i
a
l
 
i
s
 
a
d
d
e
d
 
b
y
 
o
n
e


 
 
 
 
 
 
 
 
m
o
d
u
l
u
s
 
(
import unittest


class TestDecryptFunction(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(perform_polynomial_decryption(4, 5, [1, 2, 3, 4], [5, 6, 7, 8]), [4, 4, 4, 4])

    def test_zero_secret_key(self):
        self.assertEqual(perform_polynomial_decryption(3, 7, [0, 0, 0], [6, 13, 20]), [6, 6, 6])

    def test_zero_ciphertext(self):
        self.assertEqual(perform_polynomial_decryption(3, 9, [1, 2, 3], [0, 0, 0]), [8, 7, 6])

    def test_large_values(self):
        self.assertEqual(perform_polynomial_decryption(2, 1000, [500, 500], [1000, 1000]), [500, 500])


def perform_polynomial_decryption(degree, modulus, key, encrypted_data):
    # Decrypts the polynomial based encryption by reversing the encryption steps
    decrypted_data = [0] * degree

    for index in range(degree):
        # Reversing encryption: subtract key and take modulo
        decrypted_data[index] = (encrypted_data[index] - key[index]) % modulus

    return decrypted_data

if __name__ == '__main__':
    unittest.main()