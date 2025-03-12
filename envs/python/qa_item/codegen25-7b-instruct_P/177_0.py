i
m
p
o
r
t
 
h
a
s
h
l
i
b


i
m
p
o
r
t
 
o
s






d
e
f
 
h
a
s
h
_
p
a
s
s
w
o
r
d
_
w
i
t
h
_
s
a
l
t
(
p
a
s
s
w
o
r
d
:
 
s
t
r
)
 
-
>
 
b
y
t
e
s
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
 
1
6
-
b
y
t
e
 
r
a
n
d
o
m
 
s
a
l
t
 
v
a
l
u
e
,
 
h
a
s
h
e
s
 
t
h
e
 
p
r
o
v
i
d
e
d
 
p
a
s
s
w
o
r
d
 
w
i
t
h
 
t
h
a
t
 
s
a
l
t


 
 
 
 
u
s
i
n
g
 
t
h
e
 
S
H
A
-
2
5
6
 
h
a
s
h
 
a
l
g
o
r
i
t
h
m
,
 
a
n
d
 
r
e
t
u
r
n
s
 
t
h
e
 
c
o
m
b
i
n
e
d
 
s
a
l
t
 
a
n
d
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
s
s
w
o
r
d
 
(
s
t
r
)
:
 
T
h
e
 
p
a
s
s
w
o
r
d
 
t
o
 
b
e
 
h
a
s
h
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
b
y
t
e
s
:
 
A
 
b
y
t
e
 
a
r
r
a
y
 
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
 
t
h
e
 
s
a
l
t
 
f
o
l
l
o
w
e
d
 
b
y
 
t
h
e
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
.


 
 
 
 
"
"
"


 
 
 
 
s
a
l
t
 
=
 
o
s
.
u
r
a
n
d
o
m
(
1
6
)


 
 
 
 
r
e
t
u
r
n
 
s
a
l
t
 
+
 
h
a
s
h
l
i
b
.
s
h
a
2
5
6
(
p
a
s
s
w
o
r
d
.
e
n
c
o
d
e
(
)
 
+
 
s
a
l
t
)
.
d
i
g
e
s
t
(
)






d
e
f
 
v
e
r
i
f
y
_
p
a
s
s
w
o
r
d
(
p
a
s
s
w
o
r
d
:
 
s
t
r
,
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
:
 
b
y
t
e
s
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


 
 
 
 
V
e
r
i
f
i
e
s
 
t
h
a
t
 
t
h
e
 
p
r
o
v
i
d
e
d
 
p
a
s
s
w
o
r
d
 
m
a
t
c
h
e
s
 
t
h
e
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
s
s
w
o
r
d
 
(
s
t
r
)
:
 
T
h
e
 
p
a
s
s
w
o
r
d
 
t
o
 
b
e
 
v
e
r
i
f
i
e
d
.


 
 
 
 
 
 
 
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
 
(
b
y
t
e
s
)
:
 
T
h
e
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
 
t
o
 
b
e
 
c
o
m
p
a
r
e
d
 
t
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
 
t
h
e
 
p
a
s
s
w
o
r
d
 
m
a
t
c
h
e
s
 
t
h
e
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
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
.


 
 
 
 
"
"
"


 
 
 
 
s
a
l
t
 
=
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
[
:
1
6
]


 
 
 
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
 
=
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
[
1
6
:
]


 
 
 
 
r
e
t
u
r
n
 
h
a
s
h
e
d
_
p
a
s
s
w
o
r
d
 
=
=
 
h
a
s
h
l
i
b
.
s
h
a
2
5
6
(
p
a
s
s
w
o
r
d
.
e
n
c
o
d
e
(
)
 
+
 
s
a
l
t
)
.
d
i
g
e
s
t
(
)


import unittest


class Tester(unittest.TestCase):
    def test_hashPasswordWithSaltLength(self):
        """Test that the hashPasswordWithSalt method returns a byte array with the correct length."""
        password = "testPassword"
        result = hash_password_with_salt(password)
        # SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
        self.assertEqual(len(result), 48, "The combined salt and hashed password length should be 48 bytes.")

    def test_saltIsIncludedInResult(self):
        """Test that the salt is correctly generated and included in the hash result."""
        password = "testPassword"
        result = hash_password_with_salt(password)
        salt = result[:16]  # First 16 bytes represent the salt
        self.assertIsNotNone(salt, "Salt should not be None.")
        self.assertEqual(len(salt), 16, "Salt length should be 16 bytes.")

    def test_differentPasswordsProduceDifferentHashes(self):
        """Test that two different passwords produce different hashes, even with the same salt."""
        password1 = "password123"
        password2 = "password456"
        hash1 = hash_password_with_salt(password1)
        hash2 = hash_password_with_salt(password2)
        self.assertNotEqual(hash1, hash2, "Different passwords should produce different hashes.")

    def test_samePasswordDifferentSalts(self):
        """Test that the same password produces different hashes when hashed with different salts."""
        password = "password123"
        hash1 = hash_password_with_salt(password)
        hash2 = hash_password_with_salt(password)
        # The salt is generated randomly, so the hashes should be different.
        self.assertNotEqual(hash1, hash2, "The same password should produce different hashes with different salts.")
if __name__ == '__main__':
    unittest.main()