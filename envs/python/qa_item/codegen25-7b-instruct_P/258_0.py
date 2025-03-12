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
 
L
i
s
t






d
e
f
 
e
x
t
r
a
c
t
_
c
h
a
r
a
c
t
e
r
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
 
c
h
a
r
:
 
s
t
r
,
 
c
h
a
r
s
e
t
=
'
u
t
f
-
8
'
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
p
o
s
i
t
i
o
n
 
a
n
d
 
b
i
t
s
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
c
h
a
r
a
c
t
e
r
 
f
r
o
m
 
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
 
s
e
a
r
c
h
 
w
i
t
h
i
n


 
 
 
 
 
 
 
 
c
h
a
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
 
c
h
a
r
a
c
t
e
r
 
t
o
 
f
i
n
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


 
 
 
 
 
 
 
 
c
h
a
r
s
e
t
 
(
s
t
r
)
:
 
T
h
e
 
c
h
a
r
a
c
t
e
r
 
e
n
c
o
d
i
n
g
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
t
u
p
l
e
 
o
f
 
(
p
o
s
i
t
i
o
n
,
 
b
i
t
s
)
 
i
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
p
o
s
i
t
i
o
n
 
=
 
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
f
i
n
d
(
c
h
a
r
.
e
n
c
o
d
e
(
c
h
a
r
s
e
t
)
)


 
 
 
 
i
f
 
p
o
s
i
t
i
o
n
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e


 
 
 
 
b
i
t
s
 
=
 
b
i
n
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
[
p
o
s
i
t
i
o
n
]
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
8
)


 
 
 
 
r
e
t
u
r
n
 
p
o
s
i
t
i
o
n
,
 
b
i
t
s






d
e
f
 
e
x
t
r
a
c
t
_
c
h
a
r
a
c
t
e
r
_
b
i
t
s
_
f
r
o
m
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
 
c
h
a
r
:
 
s
t
r
,
 
c
h
a
r
s
e
t
=
'
u
t
f
-
8
'
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
p
o
s
i
t
i
o
n
 
a
n
d
 
b
i
t
s
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
c
h
a
r
a
c
t
e
r
 
f
r
o
m
 
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
 
s
e
a
r
c
h
 
w
i
t
h
i
n


 
 
 
 
 
 
 
 
c
h
a
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
 
c
h
a
r
a
c
t
e
r
 
t
o
 
f
i
n
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


 
 
 
 
 
 
 
 
c
h
a
r
s
e
t
 
(
s
t
r
)
:
 
T
h
e
 
c
h
a
r
a
c
t
e
r
 
e
n
c
o
d
i
n
g
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
t
u
p
l
e
 
o
f
 
(
p
o
s
i
t
i
o
n
,
 
b
i
t
s
)
 
i
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
p
o
s
i
t
i
o
n
 
=
 
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
f
i
n
d
(
c
h
a
r
.
e
n
c
o
d
e
(
c
h
a
r
s
e
t
)
)


 
 
 
 
i
f
 
p
o
s
i
t
i
o
n
 
=
=
 
-
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
N
o
n
e


 
 
 
 
b
i
t
s
 
=
 
b
i
n
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
[
p
o
s
i
t
i
o
n
]
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
8
)


 
 
 
 
r
e
t
u
r
n
 
p
o
s
i
t
i
o
n
,
 
b
i
t
s






d
e
f
 
e
x
t
r
a
c
t
_
c
h
a
r
a
c
t
e
r
_
b
i
t
s
_
f
r
o
m
_
b
y
t
e
s
_
l
i
s
t
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
,
 
c
h
a
r
:
 
s
t
r
,
 
c
h
a
r
s
e
t
=
'
u
t
f
-
8
'
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
p
o
s
i
t
i
o
n
 
a
n
d
 
b
i
t
s
 
o
f
 
a
 
s
p
e
c
i
f
i
c
 
c
h
a
r
a
c
t
e
r
 
f
r
o
m
 
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
 
s
e
a
r
c
h
 
w
i
t
h
i
n


 
 
 
 
 
 
 
 
c
h
a
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
 
c
h
a
r
a
c
t
e
r
 
t
o
 
f
i
n
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


 
 
 
 
 
 
 
 
c
h
a
r
s
e
t
 
(
s
t
r
)
:
 
T
h
e
 
c
h
a
r
a
c
t
e
r
 
e
n
c
o
d
i
n
g
 
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




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
t
u
p
l
e
 
o
f
 
(
p
o
s
i
t
i
o
n
,
 
b
i
t
s
)
 
i
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
s
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
import unittest

# Assuming extract_character_bits is imported from your module
# from your_module import extract_character_bits

class TestExtractCharacterBits(unittest.TestCase):

    def test_case_1_valid_utf8(self):
        byte_array = b'Hello, World!'
        char = 'W'
        result = extract_character_bits(byte_array, char, 'utf-8')
        expected_result = (7, '01010111')  # 'W' is at position 7 with binary bits
        self.assertEqual(result, expected_result)

    def test_case_2_non_existent_character(self):
        byte_array = b'This is a test.'
        char = 'z'
        result = extract_character_bits(byte_array, char, 'utf-8')
        self.assertIsNone(result)  # Character 'z' is not in the byte array

    def test_case_3_invalid_encoding(self):
        byte_array = b'\xff\xfe'
        char = 'A'
        result = extract_character_bits(byte_array, char, 'ascii')  # Invalid bytes for ASCII
        self.assertIsNone(result)  # Should handle UnicodeDecodeError and return None

    def test_case_4_valid_utf16(self):
        byte_array = 'Hello, World!'.encode('utf-16')
        char = '!'
        result = extract_character_bits(byte_array, char, 'utf-16')
        expected_result = (12, '00100001 00000000')  # '!' at position 12 in UTF-16 encoding
        self.assertEqual(result, expected_result)

    def test_case_5_special_characters_utf8(self):
        byte_array = 'Python 🐍 is fun!'.encode('utf-8')
        char = '🐍'
        result = extract_character_bits(byte_array, char, 'utf-8')
        expected_result = (7, '11110000 10011111 10010000 10001101')  # Unicode character 🐍 in UTF-8
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()