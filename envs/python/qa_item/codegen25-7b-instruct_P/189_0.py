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
e
n
c
o
d
e
(
d
a
t
a
:
 
b
y
t
e
a
r
r
a
y
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


 
 
 
 
E
n
c
o
d
e
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
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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


 
 
 
 
 
 
 
 
d
a
t
a
 
(
b
y
t
e
a
r
r
a
y
)
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
 
i
n
p
u
t
 
d
a
t
a
 
t
o
 
b
e
 
e
n
c
o
d
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
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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
 
i
n
p
u
t
 
d
a
t
a
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
d
a
t
a
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
d
e
c
o
d
e
(
d
a
t
a
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
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
D
e
c
o
d
e
s
 
a
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
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
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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
 
i
n
p
u
t
 
d
a
t
a
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
a
r
r
a
y
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
 
d
e
c
o
d
e
d
 
i
n
p
u
t
 
d
a
t
a
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
d
e
c
o
d
e
(
d
a
t
a
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
e
n
c
o
d
e
_
t
o
_
f
i
l
e
(
d
a
t
a
:
 
b
y
t
e
a
r
r
a
y
,
 
f
i
l
e
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
E
n
c
o
d
e
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
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
t
 
t
o
 
a
 
f
i
l
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
(
b
y
t
e
a
r
r
a
y
)
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
 
i
n
p
u
t
 
d
a
t
a
 
t
o
 
b
e
 
e
n
c
o
d
e
d
.


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
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
t
h
 
t
o
 
t
h
e
 
f
i
l
e
 
t
o
 
w
h
i
c
h
 
t
h
e
 
e
n
c
o
d
e
d
 
d
a
t
a
 
s
h
o
u
l
d
 
b
e
 
w
r
i
t
t
e
n
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
b
a
s
e
6
4
_
e
n
c
o
d
e
(
d
a
t
a
)
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
d
e
c
o
d
e
_
f
r
o
m
_
f
i
l
e
(
f
i
l
e
_
p
a
t
h
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
a
r
r
a
y
:


 
 
 
 
"
"
"


 
 
 
 
D
e
c
o
d
e
s
 
a
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
f
r
o
m
 
a
 
f
i
l
e
 
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
 
i
t
 
a
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
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
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
t
h
 
t
o
 
t
h
e
 
f
i
l
e
 
f
r
o
m
 
w
h
i
c
h
 
t
h
e
 
e
n
c
o
d
e
d
 
d
a
t
a
 
s
h
o
u
l
d
 
b
e
 
r
e
a
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
a
r
r
a
y
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
 
d
e
c
o
d
e
d
 
i
n
p
u
t
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
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
_
d
e
c
o
d
e
(
f
.
r
e
a
d
(
)
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
e
n
c
o
d
e
_
t
o
_
f
i
l
e
_
f
r
o
m
_
s
t
r
i
n
g
(
d
a
t
a
:
 
s
t
r
,
 
f
i
l
e
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
E
n
c
o
d
e
s
 
a
 
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
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
a
n
d
 
w
r
i
t
e
s
 
i
t
 
t
o
 
a
import unittest


class Tester(unittest.TestCase):
    """Unit tests for Base64 encoding function."""

    def test_empty_input(self):
        """Empty input should return empty string."""
        input_data = bytearray([])
        self.assertEqual(base64_encode(input_data), "")
    
    def test_encode_hello(self):
        """Encoding 'hello' should return 'aGVsbG8='."""
        input_data = bytearray([ord('h'), ord('e'), ord('l'), ord('l'), ord('o')])
        self.assertEqual(base64_encode(input_data), "aGVsbG8=")
    
    def test_encode_world(self):
        """Encoding 'world' should return 'd29ybGQ='."""
        input_data = bytearray([ord('w'), ord('o'), ord('r'), ord('l'), ord('d')])
        self.assertEqual(base64_encode(input_data), "d29ybGQ=")

    def test_encode_foobar(self):
        """Encoding 'foobar' should return 'Zm9vYmFy'."""
        input_data = bytearray([ord('f'), ord('o'), ord('o'), ord('b'), ord('a'), ord('r')])
        self.assertEqual(base64_encode(input_data), "Zm9vYmFy")

    def test_encode_catch2(self):
        """Encoding 'Catch2' should return 'Q2F0Y2gy'."""
        input_data = bytearray([ord('C'), ord('a'), ord('t'), ord('c'), ord('h'), ord('2')])
        self.assertEqual(base64_encode(input_data), "Q2F0Y2gy")
    
    def test_encode_single_byte(self):
        """Encoding single byte 'A' should return 'QQ=='."""
        input_data = bytearray([ord('A')])
        self.assertEqual(base64_encode(input_data), "QQ==")

if __name__ == '__main__':
    unittest.main()