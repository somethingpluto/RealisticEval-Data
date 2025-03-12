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
s
e
q
_
n
u
m
_
a
n
d
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
:
 
s
t
r
,
 
w
o
r
d
1
:
 
s
t
r
,
 
w
o
r
d
2
:
 
s
t
r
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
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
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
 
w
o
r
d
s
 
i
n
 
a
 
t
e
x
t
 
f
i
l
e
,
 
c
o
n
s
i
d
e
r
i
n
g
 
e
a
c
h
 
l
i
n
e
 
a
s
 
a
 
s
e
p
a
r
a
t
e
 
s
e
q
u
e
n
c
e
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
 
t
o
 
r
e
a
d
.


 
 
 
 
 
 
 
 
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
 
T
h
e
 
f
i
r
s
t
 
w
o
r
d
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.


 
 
 
 
 
 
 
 
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
 
T
h
e
 
s
e
c
o
n
d
 
w
o
r
d
 
t
o
 
s
e
a
r
c
h
 
f
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
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
 
l
i
n
e
 
n
u
m
b
e
r
 
w
i
t
h
 
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
 
a
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
 
i
t
s
e
l
f
.


 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
(
N
o
n
e
,
 
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
)
 
i
f
 
o
n
e
 
o
r
 
b
o
t
h
 
w
o
r
d
s
 
a
r
e
 
n
o
t
 
f
o
u
n
d
 
i
n
 
a
n
y
 
l
i
n
e
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
 
'
r
'
)
 
a
s
 
f
i
l
e
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
i
l
e
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
s
e
q
_
n
u
m
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
f
o
r
 
i
,
 
l
i
n
e
 
i
n
 
e
n
u
m
e
r
a
t
e
(
l
i
n
e
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
e
q
_
n
u
m
 
=
 
i
 
+
 
1


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
s
e
q
_
n
u
m
 
=
 
s
e
q
_
n
u
m


 
 
 
 
 
 
 
 
i
f
 
m
i
n
_
s
e
q
_
n
u
m
 
i
s
 
N
o
n
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
,
 
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
 
m
i
n
_
s
e
q
_
n
u
m
,
 
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
s
e
q
_
n
u
m
_
a
n
d
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
w
i
t
h
_
r
e
p
l
a
c
e
m
e
n
t
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
,
 
w
o
r
d
1
:
 
s
t
r
,
 
w
o
r
d
2
:
 
s
t
r
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
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
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
 
w
o
r
d
s
 
i
n
 
a
 
t
e
x
t
 
f
i
l
e
,
 
c
o
n
s
i
d
e
r
i
n
g
 
e
a
c
h
 
l
i
n
e
 
a
s
 
a
 
s
e
p
a
r
a
t
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


 
 
 
 
a
n
d
 
a
l
l
o
w
i
n
g
 
r
e
p
l
a
c
e
m
e
n
t
 
o
f
 
w
o
r
d
s
 
i
n
 
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
 
t
o
 
r
e
a
d
.


 
 
 
 
 
 
 
 
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
 
T
h
e
 
f
i
r
s
t
 
w
o
r
d
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.


 
 
 
 
 
 
 
 
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
 
T
h
e
 
s
e
c
o
n
d
 
w
o
r
d
 
t
o
 
s
e
a
r
c
h
 
f
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
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
 
l
i
n
e
 
n
u
m
b
e
r
 
w
i
t
h
 
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
 
a
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
 
i
t
s
e
l
f
.


 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
(
N
o
n
e
,
 
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
)
 
i
f
 
o
n
e
 
o
r
 
b
o
t
h
 
w
o
r
d
s
 
a
r
e
 
n
o
t
 
f
o
u
n
d
 
i
n
import unittest
from unittest.mock import mock_open, patch


class TestGetMinDistance(unittest.TestCase):

    def test_basic_functionality(self):
        """ Test basic functionality with expected input """
        mock_content = "hello world\napple banana apple\norange apple banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (2, 1))


    def test_words_not_present(self):
        """ Test case where one or both words are not present """
        mock_content = "apple orange pear\norange pear apple"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_empty_file(self):
        """ Test an empty file """
        with patch('builtins.open', mock_open(read_data='')):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (None, float('inf')))

    def test_multiple_lines_with_varying_distances(self):
        """ Test multiple lines with varying distances between words """
        mock_content = "apple banana\napple orange orange banana\napple orange orange orange banana"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            line_number, distance = get_min_seq_num_and_distance('dummy_file.txt', 'apple', 'banana')
            self.assertEqual((line_number, distance), (1, 1))
if __name__ == '__main__':
    unittest.main()