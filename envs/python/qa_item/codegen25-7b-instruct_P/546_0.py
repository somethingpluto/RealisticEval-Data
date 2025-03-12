i
m
p
o
r
t
 
c
s
v


i
m
p
o
r
t
 
s
y
s






d
e
f
 
r
e
a
d
_
t
s
v
_
f
r
o
m
_
s
t
d
i
n
(
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
 
t
a
b
-
s
e
p
a
r
a
t
e
d
 
v
a
l
u
e
s
 
(
T
S
V
)
 
f
r
o
m
 
s
t
a
n
d
a
r
d
 
i
n
p
u
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
s
 
a
 
l
i
s
t
 
o
f
 
r
o
w
s
.




 
 
 
 
E
a
c
h
 
r
o
w
 
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
 
a
s
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
.
 
I
f
 
r
o
w
s
 
h
a
v
e
 
u
n
e
q
u
a
l
 
l
e
n
g
t
h
s
,


 
 
 
 
t
h
e
y
 
a
r
e
 
p
a
d
d
e
d
 
w
i
t
h
 
e
m
p
t
y
 
s
t
r
i
n
g
s
 
t
o
 
e
n
s
u
r
e
 
a
l
l
 
r
o
w
s
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
l
e
n
g
t
h
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
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
i
n
n
e
r
 
l
i
s
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
s
 
a
 
r
o
w
 
o
f
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
r
e
a
d
e
r
 
=
 
c
s
v
.
r
e
a
d
e
r
(
s
y
s
.
s
t
d
i
n
,
 
d
e
l
i
m
i
t
e
r
=
"
\
t
"
)


 
 
 
 
r
o
w
s
 
=
 
[
r
o
w
 
f
o
r
 
r
o
w
 
i
n
 
r
e
a
d
e
r
]


 
 
 
 
r
e
t
u
r
n
 
r
o
w
s






d
e
f
 
r
e
a
d
_
t
s
v
_
f
r
o
m
_
f
i
l
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
 
t
a
b
-
s
e
p
a
r
a
t
e
d
 
v
a
l
u
e
s
 
(
T
S
V
)
 
f
r
o
m
 
a
 
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
s
 
a
 
l
i
s
t
 
o
f
 
r
o
w
s
.




 
 
 
 
E
a
c
h
 
r
o
w
 
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
 
a
s
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
.
 
I
f
 
r
o
w
s
 
h
a
v
e
 
u
n
e
q
u
a
l
 
l
e
n
g
t
h
s
,


 
 
 
 
t
h
e
y
 
a
r
e
 
p
a
d
d
e
d
 
w
i
t
h
 
e
m
p
t
y
 
s
t
r
i
n
g
s
 
t
o
 
e
n
s
u
r
e
 
a
l
l
 
r
o
w
s
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
l
e
n
g
t
h
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
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
i
n
n
e
r
 
l
i
s
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
s
 
a
 
r
o
w
 
o
f
 
d
a
t
a
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
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
r
e
a
d
e
r
 
=
 
c
s
v
.
r
e
a
d
e
r
(
f
,
 
d
e
l
i
m
i
t
e
r
=
"
\
t
"
)


 
 
 
 
 
 
 
 
r
o
w
s
 
=
 
[
r
o
w
 
f
o
r
 
r
o
w
 
i
n
 
r
e
a
d
e
r
]


 
 
 
 
r
e
t
u
r
n
 
r
o
w
s






d
e
f
 
w
r
i
t
e
_
t
s
v
_
t
o
_
s
t
d
o
u
t
(
r
o
w
s
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
s
 
t
a
b
-
s
e
p
a
r
a
t
e
d
 
v
a
l
u
e
s
 
(
T
S
V
)
 
t
o
 
s
t
a
n
d
a
r
d
 
o
u
t
p
u
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
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
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
i
n
n
e
r
 
l
i
s
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
s
 
a
 
r
o
w
 
o
f
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
w
r
i
t
e
r
 
=
 
c
s
v
.
w
r
i
t
e
r
(
s
y
s
.
s
t
d
o
u
t
,
 
d
e
l
i
m
i
t
e
r
=
"
\
t
"
)


 
 
 
 
w
r
i
t
e
r
.
w
r
i
t
e
r
o
w
s
(
r
o
w
s
)






d
e
f
 
w
r
i
t
e
_
t
s
v
_
t
o
_
f
i
l
e
(
r
o
w
s
,
 
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


 
 
 
 
W
r
i
t
e
s
 
t
a
b
-
s
e
p
a
r
a
t
e
d
 
v
a
l
u
e
s
 
(
T
S
V
)
 
t
o
 
a
 
f
i
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
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
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
i
n
n
e
r
 
l
i
s
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
s
 
a
 
r
o
w
 
o
f
 
d
a
t
a
.


 
 
 
 
 
 
 
 
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
 
w
r
i
t
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
 
"
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
w
r
i
t
e
r
 
=
 
c
s
v
.
w
r
i
t
e
r
(
import unittest
import sys
import io
from unittest.mock import patch


class TestReadTsvFromStdin(unittest.TestCase):

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_basic_tsv_input(self, mock_stdin):
        mock_stdin.write("col1\tcol2\tcol3\nval1\tval2\tval3\n")
        mock_stdin.seek(0)  # Move to the start of the StringIO object
        expected_output = [['col1', 'col2', 'col3'], ['val1', 'val2', 'val3']]
        self.assertEqual(read_tsv_from_stdin(), expected_output)


    @patch('sys.stdin', new_callable=io.StringIO)
    def test_single_column(self, mock_stdin):
        mock_stdin.write("col1\nval1\nval2\n")
        mock_stdin.seek(0)
        expected_output = [['col1'], ['val1'], ['val2']]
        self.assertEqual(read_tsv_from_stdin(), expected_output)

if __name__ == '__main__':
    unittest.main()