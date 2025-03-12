d
e
f
 
p
r
i
n
t
_
m
e
m
o
r
y
_
b
i
t
s
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
:
 
b
y
t
e
s
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
i
n
t
s
 
t
h
e
 
s
t
a
t
u
s
 
o
f
 
e
a
c
h
 
b
i
t
 
(
0
 
o
r
 
1
)
 
i
n
 
t
h
e
 
g
i
v
e
n
 
s
e
c
t
i
o
n
 
o
f
 
m
e
m
o
r
y
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
b
1
0
1
0
1
0
1
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
1
0
1
0
1
0
1
0


 
 
 
 
I
f
 
h
a
v
e
 
m
u
l
t
i
p
l
e
 
b
y
t
e
s
 
u
s
e
 
\
n
 
s
p
l
i
t


 
 
 
 
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
 
[
0
b
1
1
0
0
1
1
0
0
,
 
0
b
1
1
1
1
0
0
0
0
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
1
1
0
0
1
1
0
0
\
n
1
1
1
1
0
0
0
0




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
e
m
o
r
y
_
s
e
c
t
i
o
n
 
(
b
y
t
e
s
)
:
 
A
 
b
y
t
e
s
 
o
b
j
e
c
t
 
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
 
s
e
c
t
i
o
n
 
o
f
 
m
e
m
o
r
y
 
t
o
 
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




 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
s
e
c
t
i
o
n
 
i
n
 
m
e
m
o
r
y
_
s
e
c
t
i
o
n
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
_
m
e
m
o
r
y
_
b
i
t
s
(
s
e
c
t
i
o
n
)


 
 
 
 
e
l
s
e
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
l
e
n
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
b
i
n
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
[
i
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
,
 
e
n
d
=
"
 
"
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
)






d
e
f
 
p
r
i
n
t
_
m
e
m
o
r
y
_
h
e
x
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
:
 
b
y
t
e
s
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
i
n
t
s
 
t
h
e
 
s
t
a
t
u
s
 
o
f
 
e
a
c
h
 
b
y
t
e
 
(
0
-
2
5
5
)
 
i
n
 
t
h
e
 
g
i
v
e
n
 
s
e
c
t
i
o
n
 
o
f
 
m
e
m
o
r
y
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
 
b
'
\
x
0
1
\
x
0
2
\
x
0
3
'


 
 
 
 
 
 
 
 
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
2
 
0
3


 
 
 
 
I
f
 
h
a
v
e
 
m
u
l
t
i
p
l
e
 
b
y
t
e
s
 
u
s
e
 
\
n
 
s
p
l
i
t


 
 
 
 
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
 
[
b
'
\
x
0
1
\
x
0
2
\
x
0
3
'
,
 
b
'
\
x
0
4
\
x
0
5
\
x
0
6
'
]


 
 
 
 
 
 
 
 
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
2
 
0
3
\
n
0
4
 
0
5
 
0
6




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
e
m
o
r
y
_
s
e
c
t
i
o
n
 
(
b
y
t
e
s
)
:
 
A
 
b
y
t
e
s
 
o
b
j
e
c
t
 
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
 
s
e
c
t
i
o
n
 
o
f
 
m
e
m
o
r
y
 
t
o
 
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




 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
f
o
r
 
s
e
c
t
i
o
n
 
i
n
 
m
e
m
o
r
y
_
s
e
c
t
i
o
n
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
_
m
e
m
o
r
y
_
h
e
x
(
s
e
c
t
i
o
n
)


 
 
 
 
e
l
s
e
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
l
e
n
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
h
e
x
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
[
i
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
2
)
,
 
e
n
d
=
"
 
"
)


 
 
 
 
 
 
 
 
p
r
i
n
t
(
)






d
e
f
 
p
r
i
n
t
_
m
e
m
o
r
y
_
a
s
c
i
i
(
m
e
m
o
r
y
_
s
e
c
t
i
o
n
:
 
b
y
t
e
s
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
i
n
t
s
 
t
h
e
 
s
t
a
t
u
s
 
o
f
 
e
a
c
h
 
b
y
t
e
 
(
0
-
2
5
5
)
 
i
n
 
t
h
e
 
g
i
v
e
n
 
s
e
c
t
i
o
n
 
o
f
 
m
e
m
o
r
y
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
 
b
'
\
x
0
1
\
x
0
2
\
x
0
3
'


 
 
 
 
 
 
 
 
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
2
 
0
3


 
 
 
import unittest
from io import StringIO
import sys


class TestPrintMemoryBits(unittest.TestCase):

    def setUp(self):
        # Capture the output during each test
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore the normal stdout
        sys.stdout = sys.__stdout__

    def test_single_byte(self):
        memory_section = bytes([0b10101010])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "10101010"
        self.assertEqual(output, expected_output)

    def test_multiple_bytes(self):
        memory_section = bytes([0b11001100, 0b11110000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "11001100\n11110000"
        self.assertEqual(output, expected_output)

    def test_all_zeros(self):
        memory_section = bytes([0b00000000])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "00000000"
        self.assertEqual(output, expected_output)

    def test_all_ones(self):
        memory_section = bytes([0b11111111])
        print_memory_bits(memory_section)
        output = self.held_stdout.getvalue().strip()
        expected_output = "11111111"
        self.assertEqual(output, expected_output)
if __name__ == '__main__':
    unittest.main()