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
i
m
a
g
e
_
t
o
_
b
i
t
s
(
i
m
a
g
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
n
 
i
m
a
g
e
 
t
o
 
a
 
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
.
C
o
n
v
e
r
t
 
t
h
e
 
i
m
a
g
e
 
t
o
 
b
l
a
c
k
 
a
n
d
 
w
h
i
t
e
 
m
o
d
e
,
 
t
h
a
t
 
i
s
,
 
e
a
c
h
 
p
i
x
e
l
 
i
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
e
d
 
b
y
 
o
n
l
y
 
1
 
b
i
t
,
 
w
i
t
h
 
a
 
w
h
i
t
e
 
p
i
x
e
l
 
v
a
l
u
e
 
o
f
 
2
5
5
 
a
n
d
 
a
 
b
l
a
c
k
 
p
i
x
e
l
 
v
a
l
u
e
 
o
f
 
0




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
m
a
g
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
 
f
i
l
e
 
p
a
t
h
 
o
f
 
t
h
e
 
i
m
a
g
e
 
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
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
i
n
g
 
t
h
e
 
i
m
a
g
e
,
 
w
h
e
r
e
 
1
 
i
s
 
f
o
r
 
w
h
i
t
e
 
p
i
x
e
l
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
0
 
i
s
 
f
o
r
 
b
l
a
c
k
 
p
i
x
e
l
s
.


 
 
 
 
"
"
"


 
 
 
 
i
m
a
g
e
 
=
 
I
m
a
g
e
.
o
p
e
n
(
i
m
a
g
e
_
p
a
t
h
)


 
 
 
 
i
m
a
g
e
 
=
 
i
m
a
g
e
.
c
o
n
v
e
r
t
(
"
L
"
)


 
 
 
 
i
m
a
g
e
 
=
 
i
m
a
g
e
.
p
o
i
n
t
(
l
a
m
b
d
a
 
x
:
 
0
 
i
f
 
x
 
<
 
1
2
8
 
e
l
s
e
 
2
5
5
,
 
"
1
"
)


 
 
 
 
r
e
t
u
r
n
 
l
i
s
t
(
i
m
a
g
e
.
g
e
t
d
a
t
a
(
)
)






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
t
s
_
t
o
_
i
m
a
g
e
(
b
i
t
s
:
 
l
i
s
t
,
 
o
u
t
p
u
t
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
 
l
i
s
t
 
o
f
 
b
i
t
s
 
t
o
 
a
n
 
i
m
a
g
e
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
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
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
i
n
g
 
t
h
e
 
i
m
a
g
e
,
 
w
h
e
r
e
 
1
 
i
s
 
f
o
r
 
w
h
i
t
e
 
p
i
x
e
l
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
0
 
i
s
 
f
o
r
 
b
l
a
c
k
 
p
i
x
e
l
s
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
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
 
f
i
l
e
 
p
a
t
h
 
t
o
 
s
a
v
e
 
t
h
e
 
i
m
a
g
e
 
t
o
.


 
 
 
 
"
"
"


 
 
 
 
i
m
a
g
e
 
=
 
I
m
a
g
e
.
n
e
w
(
"
L
"
,
 
(
i
n
t
(
l
e
n
(
b
i
t
s
)
 
*
*
 
0
.
5
)
,
 
i
n
t
(
l
e
n
(
b
i
t
s
)
 
*
*
 
0
.
5
)
)
)


 
 
 
 
i
m
a
g
e
.
p
u
t
d
a
t
a
(
b
i
t
s
)


 
 
 
 
i
m
a
g
e
.
s
a
v
e
(
o
u
t
p
u
t
_
p
a
t
h
)






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
t
s
_
t
o
_
t
e
x
t
(
b
i
t
s
:
 
l
i
s
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
s
 
a
 
l
i
s
t
 
o
f
 
b
i
t
s
 
t
o
 
t
e
x
t
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
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
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
i
n
g
 
t
h
e
 
t
e
x
t
,
 
w
h
e
r
e
 
1
 
i
s
 
f
o
r
 
w
h
i
t
e
 
p
i
x
e
l
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
0
 
i
s
 
f
o
r
 
b
l
a
c
k
 
p
i
x
e
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
t
e
x
t
 
t
h
a
t
 
w
a
s
 
c
o
n
v
e
r
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


 
 
 
 
t
e
x
t
 
=
 
"
"


 
 
 
 
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
 
b
i
t
s
[
i
 
:
 
i
 
+
 
8
]


 
 
 
 
 
 
 
 
c
h
a
r
 
=
 
c
h
r
(
i
n
t
(
"
"
.
j
o
i
n
(
[
s
t
r
(
b
i
t
)
 
f
o
r
 
b
i
t
 
i
n
 
b
y
t
e
]
)
,
 
2
)
)


 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
!
=
 
"
\
x
0
0
"
:


 
 
 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
+
=
 
c
h
a
r


 
 
 
 
r
e
t
u
r
n
 
t
e
x
t






d
e
f
 
h
i
d
e
_
t
e
x
t
_
i
n
_
i
m
a
g
e
(
i
m
a
g
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
,
 
t
e
x
t
:
 
s
t
r
,
 
o
u
t
p
u
t
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
:


 
 
 
 
"
"
"


 
 
 
 
H
i
d
e
 
t
e
x
t
 
i
n
 
a
n
 
i
m
a
g
e
.
import os
import unittest

from PIL import Image


class TestConvertImageToBits(unittest.TestCase):

    def setUp(self):
        """Create test images before each test."""
        # Create a white image (all pixels white)
        self.white_image_path = 'white_image.bmp'
        white_image = Image.new('1', (2, 2), color=1)  # 1 is for white
        white_image.save(self.white_image_path)

        # Create a black image (all pixels black)
        self.black_image_path = 'black_image.bmp'
        black_image = Image.new('1', (2, 2), color=0)  # 0 is for black
        black_image.save(self.black_image_path)

        # Create a mixed image (half white, half black)
        self.mixed_image_path = 'mixed_image.bmp'
        mixed_image = Image.new('1', (2, 2))
        mixed_image.putpixel((0, 0), 1)  # White
        mixed_image.putpixel((0, 1), 0)  # Black
        mixed_image.putpixel((1, 0), 0)  # Black
        mixed_image.putpixel((1, 1), 1)  # White
        mixed_image.save(self.mixed_image_path)

    def tearDown(self):
        """Remove the test images after each test."""
        os.remove(self.white_image_path)
        os.remove(self.black_image_path)
        os.remove(self.mixed_image_path)

    def test_white_image(self):
        """Test converting a white image."""
        expected_output = [1, 1, 1, 1]  # All pixels should be 1 (white)
        result = convert_image_to_bits(self.white_image_path)
        self.assertEqual(result, expected_output)

    def test_black_image(self):
        """Test converting a black image."""
        expected_output = [0, 0, 0, 0]  # All pixels should be 0 (black)
        result = convert_image_to_bits(self.black_image_path)
        self.assertEqual(result, expected_output)

    def test_mixed_image(self):
        """Test converting a mixed image."""
        expected_output = [1, 0, 0, 1]  # 1 white, 3 black
        result = convert_image_to_bits(self.mixed_image_path)
        self.assertEqual(result, expected_output)

    def test_invalid_image_path(self):
        """Test converting an invalid image path."""
        with self.assertRaises(FileNotFoundError):
            convert_image_to_bits('invalid_image_path.bmp')

    def test_large_image(self):
        """Test converting a larger image."""
        # Create a larger image (3x3)
        large_image_path = 'large_image.bmp'
        large_image = Image.new('1', (3, 3))
        large_image.putpixel((0, 0), 1)
        large_image.putpixel((1, 1), 1)
        large_image.putpixel((2, 2), 1)
        large_image.save(large_image_path)

        expected_output = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]
        result = convert_image_to_bits(large_image_path)
        self.assertEqual(result, expected_output)

        # Clean up
        os.remove(large_image_path)

if __name__ == '__main__':
    unittest.main()