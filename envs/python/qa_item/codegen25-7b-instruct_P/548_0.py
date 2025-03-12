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






d
e
f
 
r
e
a
d
_
t
x
t
_
a
d
d
_
j
s
o
n
_
b
r
a
c
k
e
t
(
f
i
l
e
n
a
m
e
:
s
t
r
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
 
t
e
x
t
 
f
i
l
e
,
 
w
r
a
p
s
 
i
t
s
 
c
o
n
t
e
n
t
 
i
n
 
J
S
O
N
 
b
r
a
c
k
e
t
s
,
 
a
n
d
 
p
a
r
s
e
s
 
i
t
 
i
n
t
o
 
a
 
P
y
t
h
o
n
 
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


 
 
 
 
 
 
 
 
f
i
l
e
n
a
m
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
 
p
a
t
h
 
t
o
 
t
h
e
 
t
e
x
t
 
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
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
J
S
O
N
 
c
o
n
t
e
n
t
 
w
r
a
p
p
e
d
 
i
n
 
b
r
a
c
k
e
t
s
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
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
E
r
r
o
r
:
 
I
f
 
t
h
e
 
c
o
n
t
e
n
t
 
c
a
n
n
o
t
 
b
e
 
p
a
r
s
e
d
 
a
s
 
J
S
O
N
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
n
a
m
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
t
 
=
 
f
.
r
e
a
d
(
)


 
 
 
 
r
e
t
u
r
n
 
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
'
[
'
 
+
 
c
o
n
t
e
n
t
 
+
 
'
]
'
)






d
e
f
 
r
e
a
d
_
t
x
t
_
a
d
d
_
j
s
o
n
_
b
r
a
c
k
e
t
_
t
o
_
l
i
s
t
(
f
i
l
e
n
a
m
e
:
s
t
r
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
 
t
e
x
t
 
f
i
l
e
,
 
w
r
a
p
s
 
i
t
s
 
c
o
n
t
e
n
t
 
i
n
 
J
S
O
N
 
b
r
a
c
k
e
t
s
,
 
a
n
d
 
p
a
r
s
e
s
 
i
t
 
i
n
t
o
 
a
 
P
y
t
h
o
n
 
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


 
 
 
 
 
 
 
 
f
i
l
e
n
a
m
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
 
p
a
t
h
 
t
o
 
t
h
e
 
t
e
x
t
 
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
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
J
S
O
N
 
c
o
n
t
e
n
t
 
w
r
a
p
p
e
d
 
i
n
 
b
r
a
c
k
e
t
s
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
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
E
r
r
o
r
:
 
I
f
 
t
h
e
 
c
o
n
t
e
n
t
 
c
a
n
n
o
t
 
b
e
 
p
a
r
s
e
d
 
a
s
 
J
S
O
N
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
n
a
m
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
t
 
=
 
f
.
r
e
a
d
(
)


 
 
 
 
r
e
t
u
r
n
 
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
c
o
n
t
e
n
t
)






d
e
f
 
r
e
a
d
_
t
x
t
_
a
d
d
_
j
s
o
n
_
b
r
a
c
k
e
t
_
t
o
_
l
i
s
t
_
o
f
_
d
i
c
t
s
(
f
i
l
e
n
a
m
e
:
s
t
r
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
 
t
e
x
t
 
f
i
l
e
,
 
w
r
a
p
s
 
i
t
s
 
c
o
n
t
e
n
t
 
i
n
 
J
S
O
N
 
b
r
a
c
k
e
t
s
,
 
a
n
d
 
p
a
r
s
e
s
 
i
t
 
i
n
t
o
 
a
 
P
y
t
h
o
n
 
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


 
 
 
 
 
 
 
 
f
i
l
e
n
a
m
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
 
p
a
t
h
 
t
o
 
t
h
e
 
t
e
x
t
 
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
 
d
i
c
t
i
o
n
a
r
i
e
s
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
J
S
O
N
 
c
o
n
t
e
n
t
 
w
r
a
p
p
e
d
 
i
n
 
b
r
a
c
k
e
t
s
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
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
E
r
r
o
r
:
 
I
f
 
t
h
e
 
c
o
n
t
e
n
t
 
c
a
n
n
o
t
 
b
e
 
p
a
r
s
e
d
 
a
s
 
J
S
O
N
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
n
a
m
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
c
o
n
t
e
n
t
 
=
 
f
.
r
e
a
d
(
)


 
 
 
 
r
e
t
u
r
n
 
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
c
o
n
t
e
n
t
)






d
e
f
 
r
e
a
d
_
t
x
t
_
a
d
d
_
j
s
o
n
_
b
r
a
c
k
e
t
_
t
o
_
l
i
s
t
_
o
f
_
d
i
c
t
import os
import unittest
from unittest.mock import patch, mock_open


class TestReadTxtAddJsonBracket(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_valid_json(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_empty_json_array(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [[]])  # Should return an empty list

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}\n')
    def test_valid_json_with_newline(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])


    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_json_with_array(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])

if __name__ == '__main__':
    unittest.main()