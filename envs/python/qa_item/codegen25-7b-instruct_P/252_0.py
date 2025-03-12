i
m
p
o
r
t
 
j
s
o
n






c
l
a
s
s
 
B
i
t
S
e
q
u
e
n
c
e
E
n
c
o
d
e
r
(
j
s
o
n
.
J
S
O
N
E
n
c
o
d
e
r
)
:


 
 
 
 
"
"
"


 
 
 
 
W
r
i
t
e
 
a
 
J
S
O
N
 
d
e
c
o
d
i
n
g
 
c
l
a
s
s
 
t
h
a
t
 
i
n
h
e
r
i
t
s
 
f
r
o
m
 
j
s
o
n
.
J
S
O
N
E
n
c
o
d
e
r
.
 
W
h
e
n
 
e
n
c
o
d
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
 
i
n
t
o
 
j
s
o
n
 
f
o
r
m
a
t
,
 
t
h
e
 
m
a
i
n
 
f
u
n
c
t
i
o
n
a
l
 
b
i
t
s
 
o
f
 
t
h
i
s
 
c
l
a
s
s
 
s
p
e
c
i
f
i
c
a
l
l
y
 
h
a
n
d
l
e
 
k
e
y
s
 
i
d
e
n
t
i
f
i
e
d
 
a
s
 
b
i
t
s
,
 
a
n
d
 
c
o
n
v
e
r
t
 
t
h
e
m
 
t
o
 
b
i
n
a
r
y
 
f
o
r
m
 
i
f
 
t
h
e
i
r
 
v
a
l
u
e
 
i
s
 
a
n
 
i
n
t
e
g
e
r


 
 
 
 
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
 
'
b
i
t
s
'
:
 
2
5
5
 
a
f
t
e
r
 
e
n
c
o
d
e
r
 
"
b
i
t
s
"
:
 
"
1
1
1
1
1
1
1
1
"




 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
e
n
c
o
d
e
(
s
e
l
f
,
 
o
b
j
)
:


 
 
 
 
 
 
 
 
p
a
s
s




c
l
a
s
s
 
B
i
t
S
e
q
u
e
n
c
e
D
e
c
o
d
e
r
(
j
s
o
n
.
J
S
O
N
D
e
c
o
d
e
r
)
:


 
 
 
 
"
"
"


 
 
 
 
W
r
i
t
e
 
a
 
J
S
O
N
 
d
e
c
o
d
i
n
g
 
c
l
a
s
s
 
t
h
a
t
 
i
n
h
e
r
i
t
s
 
f
r
o
m
 
j
s
o
n
.
J
S
O
N
D
e
c
o
d
e
r
.
 
W
h
e
n
 
d
e
c
o
d
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
 
f
r
o
m
 
j
s
o
n
 
f
o
r
m
a
t
,
 
t
h
e
 
m
a
i
n
 
f
u
n
c
t
i
o
n
a
l
 
b
i
t
s
 
o
f
 
t
h
i
s
 
c
l
a
s
s
 
s
p
e
c
i
f
i
c
a
l
l
y
 
h
a
n
d
l
e
 
k
e
y
s
 
i
d
e
n
t
i
f
i
e
d
 
a
s
 
b
i
t
s
,
 
a
n
d
 
c
o
n
v
e
r
t
 
t
h
e
m
 
f
r
o
m
 
b
i
n
a
r
y
 
f
o
r
m
 
i
f
 
t
h
e
i
r
 
v
a
l
u
e
 
i
s
 
a
 
s
t
r
i
n
g


 
 
 
 
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
 
'
b
i
t
s
'
:
 
"
1
1
1
1
1
1
1
1
"
 
a
f
t
e
r
 
d
e
c
o
d
e
r
 
"
b
i
t
s
"
:
 
2
5
5


 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
d
e
c
o
d
e
(
s
e
l
f
,
 
o
b
j
)
:


 
 
 
 
 
 
 
 
p
a
s
s




c
l
a
s
s
 
B
i
t
S
e
q
u
e
n
c
e
:


 
 
 
 
"
"
"


 
 
 
 
W
r
i
t
e
 
a
 
c
l
a
s
s
 
t
h
a
t
 
d
e
f
i
n
e
s
 
a
 
b
i
t
 
s
e
q
u
e
n
c
e
.
 
T
h
e
 
c
l
a
s
s
 
s
h
o
u
l
d
 
h
a
v
e
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
p
r
o
p
e
r
t
i
e
s
:


 
 
 
 
1
.
 
b
i
t
s
:
 
t
h
e
 
s
e
q
u
e
n
c
e
 
o
f
 
b
i
t
s
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
1


 
 
 
 
2
.
 
l
e
n
g
t
h
:
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
n
 
i
n
t
e
g
e
r


 
 
 
 
3
.
 
b
i
n
a
r
y
:
 
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
 
o
f
 
t
h
e
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
s
t
r
i
n
g


 
 
 
 
4
.
 
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
:
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
s
t
r
i
n
g


 
 
 
 
5
.
 
o
c
t
a
l
:
 
t
h
e
 
o
c
t
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
s
t
r
i
n
g


 
 
 
 
6
.
 
d
e
c
i
m
a
l
:
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
n
 
i
n
t
e
g
e
r


 
 
 
 
7
.
 
b
i
n
a
r
y
_
l
i
s
t
:
 
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
 
o
f
 
t
h
e
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
1


 
 
 
 
8
.
 
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
_
l
i
s
t
:
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
1
5


 
 
 
 
9
.
 
o
c
t
a
l
_
l
i
s
t
:
 
t
h
e
 
o
c
t
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
7


 
 
 
 
1
0
.
 
d
e
c
i
m
a
l
_
l
i
s
t
:
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
2
5
5


 
 
 
 
1
1
.
 
b
i
t
s
_
l
i
s
t
:
 
t
h
e
 
b
i
t
s
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
1


 
 
 
 
1
2
.
 
b
i
t
s
_
d
i
c
t
:
 
t
h
e
 
b
i
t
s
 
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
 
s
e
q
u
e
n
c
e
,
 
w
h
i
c
h
 
i
s
 
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
 
w
i
t
h
 
k
e
y
s
 
a
s
 
b
i
t
s
 
a
n
d
 
v
a
l
u
e
s
 
a
s
 
i
n
t
e
g
e
r
s
 
f
r
o
m
 
0
 
t
o
 
1


 
 
 
import unittest
import json

class TestBitSequenceEncoder(unittest.TestCase):
    def test_basic_encoding(self):
        """ Test encoding with simple dictionary containing 'bits'. """
        data = {'name': 'Processor', 'bits': 255}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Processor", "bits": "11111111"}')

    def test_nested_encoding(self):
        """ Test encoding with nested dictionary containing 'bits'. """
        data = {'component': {'name': 'ALU', 'bits': 128}, 'bits': 1}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"component": {"name": "ALU", "bits": "10000000"}, "bits": "00000001"}')

    def test_non_bits_key(self):
        """ Test encoding with dictionary not containing 'bits' key. """
        data = {'name': 'Processor', 'value': 123}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Processor", "value": 123}')

    def test_no_bits_conversion_needed(self):
        """ Test encoding with dictionary where 'bits' key needs no conversion. """
        data = {'name': 'Unit', 'bits': 'Already binary'}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Unit", "bits": "Already binary"}')

    def test_complex_structure_with_bits(self):
        """ Test encoding a complex dictionary structure containing multiple 'bits' keys. """
        data = {
            'processor': {'bits': 3, 'type': 'A'},
            'memory': {'bits': 255, 'size': 16},
            'ports': {'count': 2, 'bits': 128}
        }
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"processor": {"bits": "00000011", "type": "A"}, "memory": {"bits": "11111111", "size": 16}, "ports": {"count": 2, "bits": "10000000"}}')

if __name__ == '__main__':
    unittest.main()