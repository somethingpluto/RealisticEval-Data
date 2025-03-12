d
e
f
 
g
e
t
_
m
i
n
_
d
i
s
t
a
n
c
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
,
 
w
o
r
d
1
,
 
w
o
r
d
2
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
s
p
e
c
i
f
i
e
d
 
w
o
r
d
s
 
(
w
o
r
d
1
 
a
n
d
 
w
o
r
d
2
)
 
f
r
o
m
 
t
h
e
 
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
 
i
n
 
w
h
i
c
h
 
l
i
n
e
 
t
h
e
 
d
i
s
t
a
n
c
e
 
o
c
c
u
r
r
e
d




 
 
 
 
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


 
 
 
 
 
 
 
 
w
o
r
d
1
 
(
s
t
r
)
:


 
 
 
 
 
 
 
 
w
o
r
d
2
 
(
s
t
r
)
:




 
 
 
 
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
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
.
r
e
a
d
l
i
n
e
s
(
)


 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
 
=
 
f
l
o
a
t
(
'
i
n
f
'
)


 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
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
l
i
n
e
s
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
l
i
n
e
 
=
 
l
i
n
e
s
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
w
o
r
d
s
 
=
 
l
i
n
e
.
s
p
l
i
t
(
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
w
o
r
d
1
 
i
n
 
w
o
r
d
s
 
a
n
d
 
w
o
r
d
2
 
i
n
 
w
o
r
d
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
 
=
 
a
b
s
(
w
o
r
d
s
.
i
n
d
e
x
(
w
o
r
d
1
)
 
-
 
w
o
r
d
s
.
i
n
d
e
x
(
w
o
r
d
2
)
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
d
i
s
t
a
n
c
e
 
<
 
m
i
n
_
d
i
s
t
a
n
c
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
 
=
 
d
i
s
t
a
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e
 
=
 
i


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e






d
e
f
 
g
e
t
_
m
i
n
_
d
i
s
t
a
n
c
e
_
f
r
o
m
_
l
i
s
t
(
l
i
s
t
_
o
f
_
w
o
r
d
s
,
 
w
o
r
d
1
,
 
w
o
r
d
2
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
s
p
e
c
i
f
i
e
d
 
w
o
r
d
s
 
(
w
o
r
d
1
 
a
n
d
 
w
o
r
d
2
)
 
f
r
o
m
 
t
h
e
 
l
i
s
t
 
a
n
d
 
r
e
t
u
r
n
 
i
n
 
w
h
i
c
h
 
l
i
n
e
 
t
h
e
 
d
i
s
t
a
n
c
e
 
o
c
c
u
r
r
e
d




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
s
t
_
o
f
_
w
o
r
d
s
 
(
l
i
s
t
)
:


 
 
 
 
 
 
 
 
w
o
r
d
1
 
(
s
t
r
)
:


 
 
 
 
 
 
 
 
w
o
r
d
2
 
(
s
t
r
)
:




 
 
 
 
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


 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
 
=
 
f
l
o
a
t
(
'
i
n
f
'
)


 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e
 
=
 
N
o
n
e


 
 
 
 
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
l
i
s
t
_
o
f
_
w
o
r
d
s
)
)
:


 
 
 
 
 
 
 
 
l
i
n
e
 
=
 
l
i
s
t
_
o
f
_
w
o
r
d
s
[
i
]


 
 
 
 
 
 
 
 
w
o
r
d
s
 
=
 
l
i
n
e
.
s
p
l
i
t
(
)


 
 
 
 
 
 
 
 
i
f
 
w
o
r
d
1
 
i
n
 
w
o
r
d
s
 
a
n
d
 
w
o
r
d
2
 
i
n
 
w
o
r
d
s
:


 
 
 
 
 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
 
=
 
a
b
s
(
w
o
r
d
s
.
i
n
d
e
x
(
w
o
r
d
1
)
 
-
 
w
o
r
d
s
.
i
n
d
e
x
(
w
o
r
d
2
)
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
d
i
s
t
a
n
c
e
 
<
 
m
i
n
_
d
i
s
t
a
n
c
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
 
=
 
d
i
s
t
a
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e
 
=
 
i


 
 
 
 
r
e
t
u
r
n
 
m
i
n
_
d
i
s
t
a
n
c
e
_
l
i
n
e






d
e
f
 
g
e
t
_
m
i
n
_
d
i
s
t
a
n
c
e
_
f
r
o
m
_
l
i
s
t
_
o
f
_
l
i
s
t
s
(
l
i
s
t
_
o
f
_
l
i
s
t
s
,
 
w
o
r
d
1
,
 
w
o
r
d
2
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
d
i
s
t
a
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
s
p
e
c
i
f
i
e
d
 
w
o
r
d
s
 
(
w
o
r
d
1
 
a
n
d
 
w
o
r
d
2
)
 
f
r
o
m
 
t
h
e
 
l
i
s
t
 
o
f
 
l
i
s
t
s
 
a
n
d
 
r
e
t
u
r
n
 
i
n
 
w
h
i
c
h
 
l
i
n
e
 
t
h
e
 
d
i
s
t
a
n
c
e
 
o
c
c
u
r
r
e
d




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
i
s
t
_
o
f
_
l
i
s
t
s
 
(
l
i
s
t
)
:


import unittest
from unittest.mock import patch


class TestGetMinDistance(unittest.TestCase):
    @patch('builtins.open')
    def test_simple_case(self, mock_open):
        # Mock the file read operation
        mock_open.return_value.__enter__.return_value = iter([
            "hello world",
            "hello hello world",
            "world hello"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 1))


    @patch('builtins.open')
    def test_multiple_lines(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello planet",
            "world hello planet",
            "hello world planet"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (1, 1))

    @patch('builtins.open')
    def test_large_distance(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 27))

    @patch('builtins.open')
    def test_adjacent_words(self, mock_open):
        mock_open.return_value.__enter__.return_value = iter([
            "hello world",
            "hello hello world world",
            "world hello"
        ])
        self.assertEqual(get_min_distance("dummy_file.txt", "hello", "world"), (0, 1))

if __name__ == '__main__':
    unittest.main()