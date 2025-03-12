i
m
p
o
r
t
 
s
t
r
u
c
t


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




d
e
f
 
c
o
n
v
e
r
t
_
d
e
c
i
m
a
l
_
t
o
_
b
i
n
a
r
y
(
d
e
c
i
m
a
l
_
v
a
l
u
e
:
 
f
l
o
a
t
,
 
b
i
t
_
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
 
U
n
i
o
n
[
s
t
r
,
 
N
o
n
e
]
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
 
d
e
c
i
m
a
l
 
n
u
m
b
e
r
 
t
o
 
i
t
s
 
b
i
n
a
r
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
a
t
i
o
n
 
i
n
 
e
i
t
h
e
r
 
3
2
-
b
i
t
 
o
r
 
6
4
-
b
i
t
 
f
o
r
m
a
t
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
d
e
c
i
m
a
l
 
3
.
1
4
 
b
i
t
 
3
2


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
0
1
0
0
0
0
0
0
0
1
0
0
1
0
0
0
1
1
1
1
0
1
0
1
1
1
0
0
0
0
1
1




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
_
v
a
l
u
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
d
e
c
i
m
a
l
 
n
u
m
b
e
r
 
t
o
 
c
o
n
v
e
r
t
.


 
 
 
 
 
 
 
 
b
i
t
_
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
 
d
e
s
i
r
e
d
 
b
i
t
 
l
e
n
g
t
h
 
f
o
r
 
t
h
e
 
b
i
n
a
r
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
a
t
i
o
n
 
(
3
2
 
o
r
 
6
4
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


 
 
 
 
 
 
 
 
U
n
i
o
n
[
s
t
r
,
 
N
o
n
e
]
:
 
T
h
e
 
b
i
n
a
r
y
 
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
 
d
e
c
i
m
a
l
 
n
u
m
b
e
r
 
i
f
 
t
h
e
 
b
i
t
 
l
e
n
g
t
h


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
s
 
v
a
l
i
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
 
`
N
o
n
e
`
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
b
i
t
_
l
e
n
g
t
h
 
=
=
 
3
2
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
_
f
o
r
m
a
t
 
=
 
'
f
'


 
 
 
 
e
l
i
f
 
b
i
t
_
l
e
n
g
t
h
 
=
=
 
6
4
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
_
f
o
r
m
a
t
 
=
 
'
d
'


 
 
 
 
e
l
s
e
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
n
a
r
y
_
s
t
r
i
n
g
 
=
 
s
t
r
u
c
t
.
p
a
c
k
(
b
i
n
a
r
y
_
f
o
r
m
a
t
,
 
d
e
c
i
m
a
l
_
v
a
l
u
e
)


 
 
 
 
b
i
n
a
r
y
_
s
t
r
i
n
g
 
=
 
'
'
.
j
o
i
n
(
f
o
r
m
a
t
(
b
y
t
e
,
 
'
0
8
b
'
)
 
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
i
n
a
r
y
_
s
t
r
i
n
g
)


 
 
 
 
r
e
t
u
r
n
 
b
i
n
a
r
y
_
s
t
r
i
n
g




d
e
f
 
c
o
n
v
e
r
t
_
b
i
n
a
r
y
_
t
o
_
d
e
c
i
m
a
l
(
b
i
n
a
r
y
_
v
a
l
u
e
:
 
s
t
r
)
 
-
>
 
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
 
N
o
n
e
]
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
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
i
t
s
 
d
e
c
i
m
a
l
 
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


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
0
1
0
0
0
0
0
0
0
1
0
0
1
0
0
0
1
1
1
1
0
1
0
1
1
1
0
0
0
0
1
1


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
3
.
1
4




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
_
v
a
l
u
e
 
(
s
t
r
)
:
 
T
h
e
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
c
o
n
v
e
r
t
.




 
 
 
 
R
e
t
u
r
n
s
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
 
N
o
n
e
]
:
 
T
h
e
 
d
e
c
i
m
a
l
 
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
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
i
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
 
i
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
a
l
i
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
 
`
N
o
n
e
`
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
_
v
a
l
u
e
 
=
 
s
t
r
u
c
t
.
u
n
p
a
c
k
(
'
f
'
,
 
s
t
r
u
c
t
.
p
a
c
k
(
'
I
'
,
 
i
n
t
(
b
i
n
a
r
y
_
v
a
l
u
e
,
 
2
)
)
)
[
0
]


 
 
 
 
e
x
c
e
p
t
 
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


 
 
 
 
r
e
t
u
r
n
 
d
e
c
i
m
a
l
_
v
a
l
u
e




d
e
f
 
c
o
n
v
e
r
t
_
b
i
n
a
r
y
_
t
o
_
h
e
x
(
b
i
n
a
r
y
_
v
a
l
u
e
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
 
N
o
n
e
]
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
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
i
t
s
 
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


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
0
1
0
0
0
0
0
0
0
1
0
0
1
0
0
0
1
1
1
1
0
1
0
1
1
1
0
0
0
0
1
1


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
3
F
8
0
0
0
0
0




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
import unittest


class TestConvertDecimalToBinary(unittest.TestCase):
    def test_basic_32_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 32),
                         '01000000010010001111010111000011',
                         "3.14 should be correctly converted to 32-bit binary")

    def test_basic_64_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 64),
                         '0100000000001001000111101011100001010001111010111000010100011111',
                         "3.14 should be correctly converted to 64-bit binary")

    def test_advance_32_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(1.5, 32), '00111111110000000000000000000000',
                         "1.5 should be correctly converted to 32-bit binary")

    def test_advance_64_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(1.5, 64),
                         '0011111111111000000000000000000000000000000000000000000000000000',
                         "1.5 should be correctly converted to 32-bit binary")

if __name__ == '__main__':
    unittest.main()