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
 
b
i
t
s
_
t
o
_
b
y
t
e
s
(
b
i
t
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
)
 
-
>
 
b
y
t
e
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
a
n
 
a
r
r
a
y
 
o
f
 
b
i
n
a
r
y
 
b
i
t
s
 
t
o
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
.
 
T
r
a
v
e
r
s
i
n
g
 
t
h
r
o
u
g
h
 
e
a
c
h
 
b
i
t
,
 
c
o
m
p
o
s
i
n
g
 
t
h
e
s
e
 
b
i
t
s
 
i
n
t
o
 
b
y
t
e
s
,
 
f
o
r
m
i
n
g
 
a
 
b
y
t
e
 
e
v
e
r
y
 
8
 
b
i
t
s
,
 
a
n
d
 
t
h
e
n
 
s
t
o
r
i
n
g
 
t
h
e
s
e
 
b
y
t
e
s
 
i
n
 
a
n
 
a
r
r
a
y
 
a
n
d
 
r
e
t
u
r
n
i
n
g
 
i
t
.
 
I
f
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
b
i
t
 
a
r
r
a
y
 
i
s
 
n
o
t
 
a
 
m
u
l
t
i
p
l
e
 
o
f
 
8
,
 
t
h
e
 
l
a
s
t
 
i
n
c
o
m
p
l
e
t
e
 
b
y
t
e
 
w
i
l
l
 
b
e
 
d
i
s
c
a
r
d
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
t
s
 
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
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
b
i
t
s
 
(
e
a
c
h
 
e
l
e
m
e
n
t
 
s
h
o
u
l
d
 
b
e
 
0
 
o
r
 
1
)
.




 
 
 
 
R
e
t
u
r
n
s
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
 
b
y
t
e
s
 
c
o
n
s
t
r
u
c
t
e
d
 
f
r
o
m
 
t
h
e
 
b
i
t
s
.


 
 
 
 
"
"
"


 
 
 
 
b
y
t
e
s
_
 
=
 
b
y
t
e
a
r
r
a
y
(
)


 
 
 
 
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
0
,
 
l
e
n
(
b
i
t
s
)
,
 
8
)
:


 
 
 
 
 
 
 
 
b
y
t
e
 
=
 
0


 
 
 
 
 
 
 
 
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
8
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
i
 
+
 
j
 
<
 
l
e
n
(
b
i
t
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
y
t
e
 
=
 
(
b
y
t
e
 
<
<
 
1
)
 
|
 
b
i
t
s
[
i
 
+
 
j
]


 
 
 
 
 
 
 
 
b
y
t
e
s
_
.
a
p
p
e
n
d
(
b
y
t
e
)


 
 
 
 
r
e
t
u
r
n
 
b
y
t
e
s
_






d
e
f
 
b
y
t
e
s
_
t
o
_
b
i
t
s
(
b
y
t
e
s
_
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


 
 
 
 
c
o
n
v
e
r
t
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
 
t
o
 
a
n
 
a
r
r
a
y
 
o
f
 
b
i
n
a
r
y
 
b
i
t
s
.
 
T
r
a
v
e
r
s
i
n
g
 
t
h
r
o
u
g
h
 
e
a
c
h
 
b
y
t
e
,
 
c
o
m
p
o
s
i
n
g
 
t
h
e
s
e
 
b
y
t
e
s
 
i
n
t
o
 
b
i
t
s
,
 
f
o
r
m
i
n
g
 
a
 
b
i
t
 
e
v
e
r
y
 
8
 
b
i
t
s
,
 
a
n
d
 
t
h
e
n
 
s
t
o
r
i
n
g
 
t
h
e
s
e
 
b
i
t
s
 
i
n
 
a
n
 
a
r
r
a
y
 
a
n
d
 
r
e
t
u
r
n
i
n
g
 
i
t
.
 
I
f
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
b
y
t
e
 
a
r
r
a
y
 
i
s
 
n
o
t
 
a
 
m
u
l
t
i
p
l
e
 
o
f
 
8
,
 
t
h
e
 
l
a
s
t
 
i
n
c
o
m
p
l
e
t
e
 
b
i
t
 
w
i
l
l
 
b
e
 
d
i
s
c
a
r
d
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
y
t
e
s
_
 
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
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
b
y
t
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


 
 
 
 
 
 
 
 
A
n
 
a
r
r
a
y
 
o
f
 
b
i
t
s
 
c
o
n
s
t
r
u
c
t
e
d
 
f
r
o
m
 
t
h
e
 
b
y
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
b
i
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
b
y
t
e
 
i
n
 
b
y
t
e
s
_
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
8
)
:


 
 
 
 
 
 
 
 
 
 
 
 
b
i
t
s
.
a
p
p
e
n
d
(
(
b
y
t
e
 
>
>
 
i
)
 
&
 
1
)


 
 
 
 
r
e
t
u
r
n
 
b
i
t
s






d
e
f
 
b
y
t
e
s
_
t
o
_
h
e
x
(
b
y
t
e
s
_
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
 
t
o
 
a
 
h
e
x
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
y
t
e
s
_
 
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
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
o
f
 
b
y
t
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


 
 
 
 
 
 
 
 
A
 
h
e
x
 
s
t
r
i
n
g
 
c
o
n
s
t
r
u
c
t
e
d
 
f
r
o
m
 
t
h
e
 
b
y
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
h
e
x
_
 
=
 
"
"


 
 
 
 
f
o
r
 
b
y
t
e
 
i
n
 
b
y
t
e
s
_
:


 
 
 
 
 
 
 
 
h
e
x
_
 
+
=
 
"
%
0
2
x
"
 
%
 
b
y
t
e


 
 
 
 
r
e
t
u
r
n
 
h
e
x
_






d
e
f
 
h
e
x
_
t
o
_
b
y
t
e
s
(
h
e
x
_
:
 
s
t
r
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
import unittest


class TestBitsToBytes(unittest.TestCase):

    def test_exact_multiple_of_eight(self):
        """Test bit arrays that are exact multiples of 8 bits."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
        expected = bytearray([0b10110010, 0b01001111])  # Corrected to match actual byte values
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_incomplete_byte_discarded(self):
        """Test bit arrays where the last bits do not make up a full byte."""
        bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]  # Last two bits should be discarded
        expected = bytearray([0b10110010])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_empty_bit_array(self):
        """Test an empty bit array."""
        bits = []
        expected = bytearray()
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_single_full_byte(self):
        """Test bit arrays that exactly make one byte."""
        bits = [1, 1, 1, 1, 1, 1, 1, 1]  # Represents the byte 0xFF
        expected = bytearray([0xFF])
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)

    def test_no_bits_discarded(self):
        """Test bit arrays with multiple of 8 bits and no extra bits."""
        bits = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
        expected = bytearray([0xCC, 0x77])  # Corrected the second byte from 0xB7 to 0x77
        result = bits_to_bytes(bits)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()