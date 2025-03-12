d
e
f
 
h
e
x
_
s
t
r
i
n
g
_
t
o
_
b
y
t
e
_
a
r
r
a
y
(
h
e
x
_
s
t
r
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
C
o
n
v
e
r
t
s
 
a
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
b
y
t
e
 
a
r
r
a
y
.
 
H
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
s
 
a
r
e
 
o
f
t
e
n
 
u
s
e
d
 
t
o
 
r
e
p
r
e
s
e
n
t
 
b
i
n
a
r
y
 
d
a
t
a


 
 
 
 
i
n
 
a
 
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
,
 
e
s
p
e
c
i
a
l
l
y
 
i
n
 
n
e
t
w
o
r
k
i
n
g
,
 
c
r
y
p
t
o
g
r
a
p
h
y
,
 
a
n
d
 
s
y
s
t
e
m
s
 
p
r
o
g
r
a
m
m
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
e
x
_
s
t
r
 
(
s
t
r
)
:
 
T
h
e
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
.
 
T
h
i
s
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
o
n
l
y
 
c
o
n
t
a
i
n
 
h
e
x
a
d
e
c
i
m
a
l
 
c
h
a
r
a
c
t
e
r
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
0
-
9
,
 
A
-
F
,
 
a
-
f
)
.
 
I
f
 
t
h
e
 
s
t
r
i
n
g
 
h
a
s
 
a
n
 
o
d
d
 
n
u
m
b
e
r
 
o
f
 
c
h
a
r
a
c
t
e
r
s
,
 
a
 
l
e
a
d
i
n
g
 
z
e
r
o
 
i
s
 
a
d
d
e
d
 
t
o
 
e
n
s
u
r
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
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
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
b
i
n
a
r
y
 
d
a
t
a
 
e
n
c
o
d
e
d
 
i
n
 
t
h
e
 
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


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
h
e
x
_
s
t
r
)
 
%
 
2
 
=
=
 
1
:


 
 
 
 
 
 
 
 
h
e
x
_
s
t
r
 
=
 
"
0
"
 
+
 
h
e
x
_
s
t
r


 
 
 
 
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
.
f
r
o
m
h
e
x
(
h
e
x
_
s
t
r
)






d
e
f
 
b
y
t
e
_
a
r
r
a
y
_
t
o
_
h
e
x
_
s
t
r
i
n
g
(
b
y
t
e
_
a
r
r
a
y
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
n
v
e
r
t
s
 
a
 
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
n
t
o
 
a
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
.
 
B
y
t
e
 
a
r
r
a
y
s
 
a
r
e
 
c
o
m
m
o
n
l
y
 
u
s
e
d
 
i
n
 
s
y
s
t
e
m
s
 
p
r
o
g
r
a
m
m
i
n
g
 
t
o


 
 
 
 
r
e
p
r
e
s
e
n
t
 
b
i
n
a
r
y
 
d
a
t
a
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
_
a
r
r
a
y
 
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
 
b
y
t
e
 
a
r
r
a
y
 
t
o
 
b
e
 
c
o
n
v
e
r
t
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
 
h
e
x
a
d
e
c
i
m
a
l
 
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
i
n
g
 
t
h
e
 
b
i
n
a
r
y
 
d
a
t
a
 
e
n
c
o
d
e
d
 
i
n
 
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
 
b
y
t
e
_
a
r
r
a
y
.
h
e
x
(
)






d
e
f
 
h
e
x
_
s
t
r
i
n
g
_
t
o
_
b
a
s
e
6
4
_
s
t
r
i
n
g
(
h
e
x
_
s
t
r
:
 
s
t
r
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
n
v
e
r
t
s
 
a
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
b
a
s
e
6
4
 
s
t
r
i
n
g
.
 
B
a
s
e
6
4
 
s
t
r
i
n
g
s
 
a
r
e
 
c
o
m
m
o
n
l
y
 
u
s
e
d
 
i
n
 
d
a
t
a
 
e
n
c
o
d
i
n
g
 
t
o


 
 
 
 
r
e
p
r
e
s
e
n
t
 
b
i
n
a
r
y
 
d
a
t
a
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
e
x
_
s
t
r
 
(
s
t
r
)
:
 
T
h
e
 
h
e
x
a
d
e
c
i
m
a
l
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
.
 
T
h
i
s
 
s
t
r
i
n
g
 
s
h
o
u
l
d
 
o
n
l
y
 
c
o
n
t
a
i
n
 
h
e
x
a
d
e
c
i
m
a
l
 
c
h
a
r
a
c
t
e
r
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
0
-
9
,
 
A
-
F
,
 
a
-
f
)
.
 
I
f
 
t
h
e
 
s
t
r
i
n
g
 
h
a
s
 
a
n
 
o
d
d
 
n
u
m
b
e
r
 
o
f
 
c
h
a
r
a
c
t
e
r
s
,
 
a
 
l
e
a
d
i
n
g
 
z
e
r
o
 
i
s
 
a
d
d
e
d
 
t
o
 
e
n
s
u
r
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
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
 
b
a
s
e
6
4
 
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
i
n
g
 
t
h
e
 
b
i
n
a
r
y
 
d
a
t
a
 
e
n
c
o
d
e
d
 
i
n
 
t
h
e
 
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


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
b
a
s
e
6
4
.
b
6
4
e
n
c
o
d
e
(
h
e
x
_
s
t
r
i
n
g
_
t
o
_
b
y
t
e
_
a
r
r
a
y
(
h
e
x
_
s
t
r
)
)
.
d
e
c
o
d
e
(
)






d
e
f
 
b
a
s
e
6
4
_
s
t
r
i
n
g
_
t
o
_
h
e
x
_
s
t
r
i
n
g
(
b
a
s
e
6
4
_
s
t
r
:
 
s
t
r
)
 
-
>
 
s
t
r
:


 
 
 
import unittest


class TestHexStringToByteArray(unittest.TestCase):
    def test_normal_hex_string(self):
        hex_str = "1a3f"
        expected = bytes([0x1A, 0x3F])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should correctly convert a normal hex string")

    def test_odd_length_hex_string(self):
        hex_str = "123"
        expected = bytes([0x01, 0x23])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should handle odd-length hex strings by prepending zero")

    def test_empty_string(self):
        hex_str = ""
        expected = bytes()
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should return an empty array for an empty string")

    def test_hex_string_with_uppercase(self):
        hex_str = "1A3F"
        expected = bytes([0x1A, 0x3F])
        self.assertEqual(expected, hex_string_to_byte_array(hex_str),
                         "Should correctly handle hex strings with uppercase letters")

if __name__ == '__main__':
    unittest.main()