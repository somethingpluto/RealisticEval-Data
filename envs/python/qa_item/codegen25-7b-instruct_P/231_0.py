d
e
f
 
r
e
a
d
_
l
o
g
(
l
o
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
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
a
 
l
o
g
 
f
i
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
 
J
S
O
N
 
e
n
t
r
i
e
s
 
a
n
d
 
e
x
t
r
a
c
t
s
 
t
r
a
i
n
i
n
g
 
l
o
s
s
 
a
n
d
 
t
e
s
t
 
a
c
c
u
r
a
c
y
.


 
 
 
 
J
s
o
n
 
e
n
t
r
i
e
s
 
s
u
c
h
 
a
s
 
{
"
t
e
s
t
_
a
c
c
1
"
:
 
8
8
.
5
,
 
"
t
r
a
i
n
_
l
o
s
s
"
:
 
0
.
7
5
}


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
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
 
l
o
g
 
f
i
l
e
 
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
w
o
 
l
i
s
t
s
:


 
 
 
 
 
 
 
 
 
 
 
 
-
 
t
r
a
i
n
_
l
o
s
s
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
)
:
 
A
 
l
i
s
t
 
o
f
 
t
r
a
i
n
i
n
g
 
l
o
s
s
 
v
a
l
u
e
s
 
e
x
t
r
a
c
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
 
l
o
g
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
t
e
s
t
_
a
c
c
1
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
)
:
 
A
 
l
i
s
t
 
o
f
 
t
e
s
t
 
a
c
c
u
r
a
c
y
 
v
a
l
u
e
s
 
e
x
t
r
a
c
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
 
l
o
g
.


 
 
 
 
"
"
"


 
 
 
 
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
 
=
 
[
]


 
 
 
 
t
e
s
t
_
a
c
c
1
_
l
i
s
t
 
=
 
[
]


 
 
 
 
w
i
t
h
 
o
p
e
n
(
l
o
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
 
'
r
'
)
 
a
s
 
l
o
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
f
o
r
 
l
i
n
e
 
i
n
 
l
o
g
_
f
i
l
e
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
.
s
t
r
i
p
(
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
.
s
t
a
r
t
s
w
i
t
h
(
'
{
'
)
 
a
n
d
 
l
i
n
e
.
e
n
d
s
w
i
t
h
(
'
}
'
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
j
s
o
n
_
e
n
t
r
y
 
=
 
j
s
o
n
.
l
o
a
d
s
(
l
i
n
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
.
a
p
p
e
n
d
(
j
s
o
n
_
e
n
t
r
y
[
'
t
r
a
i
n
_
l
o
s
s
'
]
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
e
s
t
_
a
c
c
1
_
l
i
s
t
.
a
p
p
e
n
d
(
j
s
o
n
_
e
n
t
r
y
[
'
t
e
s
t
_
a
c
c
1
'
]
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
K
e
y
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 
r
e
t
u
r
n
 
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
,
 
t
e
s
t
_
a
c
c
1
_
l
i
s
t






d
e
f
 
p
l
o
t
_
l
o
g
s
(
l
o
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
s
,
 
o
u
t
p
u
t
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
:


 
 
 
 
"
"
"


 
 
 
 
P
l
o
t
s
 
t
h
e
 
t
r
a
i
n
i
n
g
 
l
o
s
s
 
a
n
d
 
t
e
s
t
 
a
c
c
u
r
a
c
y
 
o
f
 
s
e
v
e
r
a
l
 
l
o
g
 
f
i
l
e
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
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
 
p
a
t
h
s
 
t
o
 
l
o
g
 
f
i
l
e
s
 
t
o
 
b
e
 
p
l
o
t
t
e
d
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
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
 
o
u
t
p
u
t
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
f
i
g
,
 
a
x
1
 
=
 
p
l
t
.
s
u
b
p
l
o
t
s
(
)


 
 
 
 
a
x
2
 
=
 
a
x
1
.
t
w
i
n
x
(
)


 
 
 
 
f
o
r
 
l
o
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
 
i
n
 
l
o
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
s
:


 
 
 
 
 
 
 
 
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
,
 
t
e
s
t
_
a
c
c
1
_
l
i
s
t
 
=
 
r
e
a
d
_
l
o
g
(
l
o
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


 
 
 
 
 
 
 
 
e
p
o
c
h
s
 
=
 
l
i
s
t
(
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
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
)
)
)


 
 
 
 
 
 
 
 
a
x
1
.
p
l
o
t
(
e
p
o
c
h
s
,
 
t
r
a
i
n
_
l
o
s
s
_
l
i
s
t
,
 
l
a
b
e
l
=
l
o
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


 
 
 
 
 
 
 
 
a
x
2
.
p
l
o
t
(
e
p
o
c
h
s
,
 
t
e
s
t
_
a
c
c
1
_
l
i
s
t
import json
import unittest
from unittest.mock import mock_open, patch


class TestReadLog(unittest.TestCase):

    def test_read_correct_data(self):
        """ Test reading correctly formatted JSON lines """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\n' \
                            '{"test_acc1": 89.0, "train_loss": 0.70}'
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("dummy_path.json")
            self.assertEqual(train_loss, [0.75, 0.70])
            self.assertEqual(test_acc1, [88.5, 89.0])

    def test_read_correct_data_single(self):
        """ Test reading correctly formatted JSON lines """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}'
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("dummy_path.json")
            self.assertEqual(train_loss, [0.75])
            self.assertEqual(test_acc1, [88.5])
    def test_empty_file(self):
        """ Test reading an empty file """
        with patch('builtins.open', mock_open(read_data="")):
            train_loss, test_acc1 = read_log("empty_file.json")
            self.assertEqual(train_loss, [])
            self.assertEqual(test_acc1, [])

    def test_partial_data_entries(self):
        """ Test file with missing fields in some entries """
        mock_file_content = '{"test_acc1": 88.5, "train_loss": 0.75}\n' \
                            '{"test_acc1": 90.0,"train_loss": 0.75,"f1":0.91}'  # Missing train_loss
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            train_loss, test_acc1 = read_log("partial_data_file.json")
            self.assertEqual(train_loss, [0.75, 0.75])  # Only one complete entry
            self.assertEqual(test_acc1, [88.5, 90.0])

if __name__ == '__main__':
    unittest.main()