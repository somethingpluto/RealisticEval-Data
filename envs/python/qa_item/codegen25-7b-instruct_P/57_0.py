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
p
n
g
_
t
o
_
i
c
o
(
p
n
g
_
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
 
i
c
o
_
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
 
i
c
o
n
_
s
i
z
e
s
=
[
(
3
2
,
 
3
2
)
]
)
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
 
p
n
g
 
i
m
a
g
e
s
 
t
o
 
i
c
o
 
f
i
l
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
n
g
_
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
 
P
a
t
h
 
t
o
 
t
h
e
 
s
o
u
r
c
e
 
P
N
G
 
i
m
a
g
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 
i
c
o
_
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
 
P
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
 
I
C
O
 
f
i
l
e
.


 
 
 
 
 
 
 
 
i
c
o
n
_
s
i
z
e
s
 
(
l
i
s
t
)
:
 
L
i
s
t
 
o
f
 
t
u
p
l
e
s
 
s
p
e
c
i
f
y
i
n
g
 
t
h
e
 
s
i
z
e
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
h
e
 
I
C
O
 
f
i
l
e
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


 
 
 
 
f
r
o
m
 
P
I
L
 
i
m
p
o
r
t
 
I
m
a
g
e


 
 
 
 
i
m
p
o
r
t
 
w
i
n
3
2
a
p
i


 
 
 
 
i
m
p
o
r
t
 
w
i
n
3
2
c
o
n


 
 
 
 
i
m
p
o
r
t
 
w
i
n
3
2
g
u
i


 
 
 
 
i
m
p
o
r
t
 
w
i
n
3
2
u
i




 
 
 
 
h
w
n
d
 
=
 
w
i
n
3
2
g
u
i
.
G
e
t
D
e
s
k
t
o
p
W
i
n
d
o
w
(
)


 
 
 
 
h
w
n
d
D
C
 
=
 
w
i
n
3
2
g
u
i
.
G
e
t
W
i
n
d
o
w
D
C
(
h
w
n
d
)


 
 
 
 
m
f
c
D
C
 
=
 
w
i
n
3
2
u
i
.
C
r
e
a
t
e
D
C
F
r
o
m
H
a
n
d
l
e
(
h
w
n
d
D
C
)


 
 
 
 
s
a
v
e
D
C
 
=
 
m
f
c
D
C
.
C
r
e
a
t
e
C
o
m
p
a
t
i
b
l
e
D
C
(
)




 
 
 
 
i
m
g
 
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
p
n
g
_
f
i
l
e
_
p
a
t
h
)


 
 
 
 
i
n
f
o
 
=
 
i
m
g
.
i
n
f
o


 
 
 
 
i
m
g
 
=
 
i
m
g
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
R
G
B
"
)




 
 
 
 
h
 
=
 
w
i
n
3
2
a
p
i
.
G
e
t
S
y
s
t
e
m
M
e
t
r
i
c
s
(
w
i
n
3
2
c
o
n
.
S
M
_
C
Y
I
C
O
N
)


 
 
 
 
w
 
=
 
h


 
 
 
 
i
f
 
h
 
>
 
3
2
:


 
 
 
 
 
 
 
 
h
 
=
 
3
2


 
 
 
 
i
f
 
w
 
>
 
3
2
:


 
 
 
 
 
 
 
 
w
 
=
 
3
2




 
 
 
 
h
 
=
 
h
 
*
 
2


 
 
 
 
w
 
=
 
w
 
*
 
2




 
 
 
 
h
 
=
 
h
 
*
 
2


 
 
 
 
w
 
=
 
w
 
*
 
2




 
 
 
 
i
c
o
n
_
i
n
f
o
 
=
 
w
i
n
3
2
g
u
i
.
M
a
k
e
I
c
o
n
I
n
f
o
(
(
0
,
 
0
)
,
 
(
w
,
 
h
)
)


 
 
 
 
i
c
o
n
_
i
n
f
o
_
l
i
s
t
 
=
 
[
i
c
o
n
_
i
n
f
o
]


 
 
 
 
f
l
a
g
s
 
=
 
w
i
n
3
2
c
o
n
.
L
R
_
L
O
A
D
F
R
O
M
F
I
L
E
 
|
 
w
i
n
3
2
c
o
n
.
L
R
_
D
E
F
A
U
L
T
S
I
Z
E




 
 
 
 
h
I
c
o
n
 
=
 
w
i
n
3
2
g
u
i
.
L
o
a
d
I
m
a
g
e
(


 
 
 
 
 
 
 
 
N
o
n
e
,
 
p
n
g
_
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
 
w
i
n
3
2
c
o
n
.
I
M
A
G
E
_
I
C
O
N
,
 
w
,
 
h
,
 
f
l
a
g
s


 
 
 
 
)


 
 
 
 
h
d
c
 
=
 
w
i
n
3
2
g
u
i
.
G
e
t
D
C
(
h
w
n
d
)


 
 
 
 
h
d
c
O
b
j
 
=
 
w
i
n
3
2
u
i
.
C
r
e
a
t
e
D
C
F
r
o
m
H
a
n
d
l
e
(
h
d
c
)


 
 
 
 
s
a
v
e
B
i
t
M
a
p
 
=
 
w
i
n
3
2
u
i
.
C
r
e
a
t
e
B
i
t
m
a
p
(
)


 
 
 
 
s
a
v
e
B
i
t
M
a
p
.
C
r
e
a
t
e
C
o
m
p
a
t
i
b
l
e
B
i
t
m
a
p
(
h
d
c
O
b
j
,
 
w
,
 
h
)


 
 
 
 
h
d
c
O
b
j
.
S
e
l
e
c
t
O
b
j
e
c
t
(
s
a
v
e
B
i
t
M
a
p
)


 
 
 
 
h
import unittest
from unittest.mock import patch, MagicMock


class TestConvertPngToIco(unittest.TestCase):
    @patch('PIL.Image.open')
    def test_single_icon_size(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico', [(64, 64)])
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(64, 64)])

    @patch('PIL.Image.open')
    def test_multiple_icon_sizes(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico', [(16, 16), (32, 32), (64, 64)])
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(16, 16), (32, 32), (64, 64)])

    @patch('PIL.Image.open')
    def test_default_icon_size(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico')
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(32, 32)])

    @patch('PIL.Image.open')
    def test_file_handling(self, mock_open):
        mock_image = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_image
        convert_png_to_ico('source.png', 'output.ico')
        # Check if save was called correctly
        mock_image.save.assert_called_once_with('output.ico', format='ICO', sizes=[(32, 32)])

    @patch('PIL.Image.open')
    def test_invalid_image_path(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            convert_png_to_ico('invalid.png', 'output.ico')

if __name__ == '__main__':
    unittest.main()