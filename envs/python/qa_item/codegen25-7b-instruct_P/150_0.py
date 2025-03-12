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
 
D
i
c
t






d
e
f
 
r
g
b
_
t
o
_
h
e
x
(
r
g
b
:
 
D
i
c
t
)
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
 
a
n
 
R
G
B
 
c
o
l
o
r
 
o
b
j
e
c
t
 
t
o
 
a
 
H
E
X
 
c
o
l
o
r
 
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


 
 
 
 
 
 
 
 
r
g
b
 
(
d
i
c
t
)
:
 
A
n
 
o
b
j
e
c
t
 
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
 
r
e
d
,
 
g
r
e
e
n
,
 
a
n
d
 
b
l
u
e
 
c
o
m
p
o
n
e
n
t
s
 
o
f
 
t
h
e
 
c
o
l
o
r
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
E
x
a
m
p
l
e
:
 
{
'
r
'
:
 
2
5
5
,
 
'
g
'
:
 
0
,
 
'
b
'
:
 
0
}




 
 
 
 
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
 
H
E
X
 
c
o
l
o
r
 
c
o
d
e
.


 
 
 
 
 
 
 
 
 
 
 
 
 
E
x
a
m
p
l
e
:
 
"
#
F
F
0
0
0
0
"
 
f
o
r
 
r
e
d
.


 
 
 
 
"
"
"






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
r
g
b
(
h
e
x
_
c
o
l
o
r
:
 
s
t
r
)
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
 
a
 
H
E
X
 
c
o
l
o
r
 
s
t
r
i
n
g
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r
 
o
b
j
e
c
t
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
c
o
l
o
r
 
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
 
H
E
X
 
c
o
l
o
r
 
c
o
d
e
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
E
x
a
m
p
l
e
:
 
"
#
F
F
0
0
0
0
"
 
f
o
r
 
r
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


 
 
 
 
 
 
 
 
d
i
c
t
 
o
r
 
N
o
n
e
:
 
A
n
 
o
b
j
e
c
t
 
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
 
r
e
d
,
 
g
r
e
e
n
,
 
a
n
d
 
b
l
u
e
 
c
o
m
p
o
n
e
n
t
s
 
o
f
 
t
h
e
 
c
o
l
o
r
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
N
o
n
e
 
i
f
 
t
h
e
 
H
E
X
 
c
o
d
e
 
i
s
 
i
n
v
a
l
i
d
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
E
x
a
m
p
l
e
:
 
{
'
r
'
:
 
2
5
5
,
 
'
g
'
:
 
0
,
 
'
b
'
:
 
0
}
 
f
o
r
 
r
e
d
.


 
 
 
 
"
"
"


import unittest

class TestColorConversion(unittest.TestCase):
    def test_rgb_to_hex(self):
        rgb = {'r': 255, 'g': 99, 'b': 71}
        result = rgbToHex(rgb)
        self.assertEqual(result, '#ff6347')  # Expected HEX code for RGB(255, 99, 71)

    def test_hex_to_rgb(self):
        hex_code = '#ff6347'
        result = hexToRgb(hex_code)
        self.assertEqual(result, {'r': 255, 'g': 99, 'b': 71})  # Expected RGB object for HEX #ff6347

    def test_invalid_rgb_components(self):
        rgb = {'r': 300, 'g': -10, 'b': 128}
        result = rgbToHex(rgb)
        self.assertEqual(result, '#00c080')  # Clamped values should be "00", valid value should convert to "80"

    def test_invalid_hex_string(self):
        invalid_hex = '#ggg123'
        result = hexToRgb(invalid_hex)
        self.assertIsNone(result)  # Invalid HEX code should return None

    def test_boundary_values_rgb(self):
        rgb_black = {'r': 0, 'g': 0, 'b': 0}
        result_black = rgbToHex(rgb_black)
        self.assertEqual(result_black, '#000000')  # RGB(0, 0, 0) should convert to #000000
        
        rgb_white = {'r': 255, 'g': 255, 'b': 255}
        result_white = rgbToHex(rgb_white)
        self.assertEqual(result_white, '#ffffff')  # RGB(255, 255, 255) should convert to #ffffff

if __name__ == '__main__':
    unittest.main()