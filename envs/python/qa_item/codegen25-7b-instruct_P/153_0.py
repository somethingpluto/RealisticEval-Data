d
e
f
 
c
o
m
p
r
e
s
s
_
h
a
s
h
(
h
a
s
h
_
b
y
t
e
s
:
 
b
y
t
e
s
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
r
e
s
s
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
 
h
a
s
h
 
b
u
f
f
e
r
 
i
n
t
o
 
a
 
s
t
r
i
n
g
 
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
 
a
t
 
l
e
a
s
t
 
l
e
n
g
t
h
 
5
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
a
s
h
_
b
y
t
e
s
 
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
 
b
u
f
f
e
r
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
c
o
m
p
r
e
s
s
e
d
 
s
t
r
i
n
g
 
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
 
h
a
s
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
o
u
t
p
u
t
 
s
t
r
i
n
g
 
w
i
l
l
 
h
a
v
e
 
a
 
l
e
n
g
t
h
 
n
o
 
l
e
s
s
 
t
h
a
n
 
5
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
h
a
s
h
_
b
y
t
e
s
)
.
h
e
x
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
 
c
o
m
p
r
e
s
s
_
h
a
s
h
_
l
i
s
t
(
h
a
s
h
_
l
i
s
t
:
 
L
i
s
t
[
b
y
t
e
s
]
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
r
e
s
s
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
 
l
i
s
t
 
o
f
 
h
a
s
h
 
b
u
f
f
e
r
s
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
 
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
s
 
o
f
 
a
t
 
l
e
a
s
t
 
l
e
n
g
t
h
 
5
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
a
s
h
_
l
i
s
t
 
(
L
i
s
t
[
b
y
t
e
s
]
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
h
a
s
h
 
b
u
f
f
e
r
s
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
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


 
 
 
 
 
 
 
 
L
i
s
t
[
s
t
r
]
:
 
A
 
l
i
s
t
 
o
f
 
c
o
m
p
r
e
s
s
e
d
 
s
t
r
i
n
g
 
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
s
 
o
f
 
t
h
e
 
h
a
s
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
o
u
t
p
u
t
 
l
i
s
t
 
w
i
l
l
 
h
a
v
e
 
a
 
l
e
n
g
t
h
 
n
o
 
l
e
s
s
 
t
h
a
n
 
5
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
 
[
c
o
m
p
r
e
s
s
_
h
a
s
h
(
h
a
s
h
_
b
y
t
e
s
)
 
f
o
r
 
h
a
s
h
_
b
y
t
e
s
 
i
n
 
h
a
s
h
_
l
i
s
t
]






d
e
f
 
c
o
m
p
r
e
s
s
_
h
a
s
h
_
d
i
c
t
(
h
a
s
h
_
d
i
c
t
:
 
D
i
c
t
[
s
t
r
,
 
b
y
t
e
s
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
r
e
s
s
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
 
h
a
s
h
 
d
i
c
t
i
o
n
a
r
y
 
i
n
t
o
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
s
t
r
i
n
g
 
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
s
 
o
f
 
a
t
 
l
e
a
s
t
 
l
e
n
g
t
h
 
5
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
a
s
h
_
d
i
c
t
 
(
D
i
c
t
[
s
t
r
,
 
b
y
t
e
s
]
)
:
 
T
h
e
 
h
a
s
h
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
c
o
m
p
r
e
s
s
e
d
 
s
t
r
i
n
g
 
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
s
 
o
f
 
t
h
e
 
h
a
s
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
o
u
t
p
u
t
 
d
i
c
t
i
o
n
a
r
y
 
w
i
l
l
 
h
a
v
e
 
a
 
l
e
n
g
t
h
 
n
o
 
l
e
s
s
 
t
h
a
n
 
5
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
 
{
k
e
y
:
 
c
o
m
p
r
e
s
s
_
h
a
s
h
(
h
a
s
h
_
b
y
t
e
s
)
 
f
o
r
 
k
e
y
,
 
h
a
s
h
_
b
y
t
e
s
 
i
n
 
h
a
s
h
_
d
i
c
t
.
i
t
e
m
s
(
)
}






d
e
f
 
c
o
m
p
r
e
s
s
_
h
a
s
h
_
l
i
s
t
_
d
i
c
t
(
h
a
s
h
_
l
i
s
t
_
d
i
c
t
:
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
b
y
t
e
s
]
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
s
t
r
]
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
m
p
r
e
s
s
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
 
h
a
s
h
 
l
i
s
t
 
d
i
c
t
i
o
n
a
r
y
 
i
n
t
o
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
 
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
s
 
o
f
 
a
t
 
l
e
a
s
t
 
l
e
n
g
t
h
 
5
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
a
s
h
_
l
i
s
t
_
d
i
c
t
 
(
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
b
y
t
e
s
]
]
)
:
 
T
h
e
 
h
a
s
h
 
l
i
s
t
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
L
i
s
t
[
s
t
r
]
]
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
c
o
m
p
r
e
s
s
e
d
 
s
t
r
i
n
g
 
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
s
 
o
f
 
t
h
e
 
h
a
s
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
o
u
t
p
u
t
 
d
i
c
t
i
o
n
a
r
y
 
w
i
l
l
 
h
a
v
e
 
a
 
l
e
n
g
t
h
 
n
o
import hashlib
import unittest


class TestCompressHash(unittest.TestCase):

    def test_length_of_result(self):
        """should return a string of length 5"""
        hash_bytes = hashlib.sha256(b'test').digest()
        result = compress_hash(hash_bytes)
        self.assertEqual(len(result), 5)

    def test_different_inputs(self):
        """should return different strings for different inputs"""
        hash1 = hashlib.sha256(b'test1').digest()
        hash2 = hashlib.sha256(b'test2').digest()
        result1 = compress_hash(hash1)
        result2 = compress_hash(hash2)
        self.assertNotEqual(result1, result2)

    def test_consistent_result_for_same_input(self):
        """should return a consistent result for the same input"""
        hash_bytes = hashlib.sha256(b'test').digest()
        result1 = compress_hash(hash_bytes)
        result2 = compress_hash(hash_bytes)
        self.assertEqual(result1, result2)

    def test_all_zeros(self):
        """should handle a hash of all zeros"""
        hash_bytes = bytes([0] * 32)  # 32 bytes of zeros
        result = compress_hash(hash_bytes)
        self.assertRegex(result, r'^[0-9a-zA-Z]{5}$')

    def test_all_ones(self):
        """should handle a hash of all ones"""
        hash_bytes = bytes([255] * 32)  # 32 bytes of 0xFF (255 in decimal)
        result = compress_hash(hash_bytes)
        self.assertRegex(result, r'^[0-9a-zA-Z]{5}$')

if __name__ == '__main__':
    unittest.main()