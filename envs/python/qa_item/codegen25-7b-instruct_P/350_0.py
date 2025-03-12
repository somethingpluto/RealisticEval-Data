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
 
i
t
s
 
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
a
t
i
o
n
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
 
v
a
l
u
e
s
 
o
f
 
t
h
e
 
b
y
t
e
s
 
i
n
 
t
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
.
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
 
a
r
r
a
y
 
i
s
 
e
m
p
t
y
,
 
r
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y
 
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
 
"
"
.
j
o
i
n
(
[
"
{
:
0
2
x
}
"
.
f
o
r
m
a
t
(
b
)
 
f
o
r
 
b
 
i
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
]
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
i
n
g
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
 
i
t
s
 
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
i
n
g
 
(
s
t
r
)
:
 
A
 
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
 
v
a
l
u
e
s
 
o
f
 
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
e
d
 
b
y
 
t
h
e
 
i
n
p
u
t
 
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
i
n
g
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
w
i
t
h
_
l
e
n
g
t
h
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
:
 
s
t
r
,
 
l
e
n
g
t
h
:
 
i
n
t
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
 
i
t
s
 
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
 
b
y
t
e
 
a
r
r
a
y
 
w
i
t
h
 
a
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
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
i
n
g
 
(
s
t
r
)
:
 
A
 
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
 
v
a
l
u
e
s
 
o
f
 
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


 
 
 
 
 
 
 
 
l
e
n
g
t
h
 
(
i
n
t
)
:
 
T
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
 
t
o
 
b
e
 
c
r
e
a
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
 
w
i
t
h
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
,
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
h
e
 
i
n
p
u
t
 
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
i
n
g
.
z
f
i
l
l
(
l
e
n
g
t
h
 
*
 
2
)
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
_
w
i
t
h
_
l
e
n
g
t
h
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
,
 
l
e
n
g
t
h
:
 
i
n
t
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
 
i
t
s
 
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
a
t
i
o
n
 
w
i
t
h
 
a
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
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


 
 
 
 
 
 
 
 
l
e
n
g
t
h
 
(
i
n
t
)
:
 
T
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
 
t
o
 
b
e
 
c
r
e
a
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
 
v
a
l
u
e
s
 
o
f
 
t
h
e
 
b
y
t
e
s
 
i
n
 
t
h
e
 
i
n
p
u
t
import unittest


class TestAnswer(unittest.TestCase):

    def test_empty_byte_array(self):
        input_data = bytes()  # Empty byte array
        self.assertEqual("", byte_array_to_hex_string(input_data), "Empty array should return empty string")

    def test_single_byte(self):
        input_data = bytes([0x0F])  # 15 in decimal
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["0F", "0f"])

    def test_multiple_bytes(self):
        input_data = bytes([0x01, 0x0A, 0xFF])
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["010aff", "010AFF"])

    def test_zero_bytes(self):
        input_data = bytes([0x00, 0x00, 0x00])
        self.assertEqual("000000", byte_array_to_hex_string(input_data), "Zero bytes should be converted to '000000'")

    def test_negative_bytes(self):
        input_data = bytes([0x80, 0xFF])  # 128 and 255 in signed byte representation
        result = byte_array_to_hex_string(input_data)
        self.assertTrue(result in ["80FF", "80ff"])
if __name__ == '__main__':
    unittest.main()