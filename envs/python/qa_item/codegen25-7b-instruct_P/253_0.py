d
e
f
 
l
o
g
(
i
t
e
m
:
 
a
n
y
)
 
-
>
 
a
n
y
:


 
 
 
 
"
"
"


 
 
 
 
L
o
g
s
 
a
n
 
i
t
e
m
 
b
y
 
p
r
i
n
t
i
n
g
 
i
t
.
 
H
a
n
d
l
e
s
 
s
t
r
i
n
g
s
,
 
n
u
m
b
e
r
s
,
 
l
i
s
t
s
,
 
a
n
d
 
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
 
b
y
 
p
r
i
n
t
i
n
g


 
 
 
 
t
h
e
m
 
d
i
r
e
c
t
l
y
 
o
r
 
a
s
 
a
 
J
S
O
N
-
f
o
r
m
a
t
t
e
d
 
s
t
r
i
n
g
.
 
O
t
h
e
r
 
t
y
p
e
s
 
a
r
e
 
r
e
p
o
r
t
e
d
 
a
s
 
e
r
r
o
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
t
e
m
 
(
a
n
y
)
:
 
T
h
e
 
i
t
e
m
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
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


 
 
 
 
 
 
 
 
i
t
e
m
:
 
T
h
e
 
i
t
e
m
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
e
.


 
 
 
 
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
i
t
e
m
,
 
s
t
r
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
i
t
e
m
)


 
 
 
 
e
l
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
i
t
e
m
,
 
(
i
n
t
,
 
f
l
o
a
t
)
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
i
t
e
m
)


 
 
 
 
e
l
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
i
t
e
m
,
 
l
i
s
t
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
i
t
e
m
)


 
 
 
 
e
l
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
i
t
e
m
,
 
d
i
c
t
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
j
s
o
n
.
d
u
m
p
s
(
i
t
e
m
,
 
i
n
d
e
n
t
=
4
)
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
f
"
E
R
R
O
R
:
 
{
i
t
e
m
}
 
i
s
 
n
o
t
 
a
 
s
t
r
i
n
g
,
 
n
u
m
b
e
r
,
 
l
i
s
t
,
 
o
r
 
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
.
"
)


 
 
 
 
r
e
t
u
r
n
 
i
t
e
m






d
e
f
 
l
o
g
_
l
i
s
t
(
i
t
e
m
s
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
L
o
g
s
 
a
 
l
i
s
t
 
o
f
 
i
t
e
m
s
 
b
y
 
p
r
i
n
t
i
n
g
 
t
h
e
m
.
 
H
a
n
d
l
e
s
 
s
t
r
i
n
g
s
,
 
n
u
m
b
e
r
s
,
 
l
i
s
t
s
,
 
a
n
d
 
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
 
b
y
 
p
r
i
n
t
i
n
g


 
 
 
 
t
h
e
m
 
d
i
r
e
c
t
l
y
 
o
r
 
a
s
 
a
 
J
S
O
N
-
f
o
r
m
a
t
t
e
d
 
s
t
r
i
n
g
.
 
O
t
h
e
r
 
t
y
p
e
s
 
a
r
e
 
r
e
p
o
r
t
e
d
 
a
s
 
e
r
r
o
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
t
e
m
s
 
(
l
i
s
t
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
i
t
e
m
s
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
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


 
 
 
 
 
 
 
 
i
t
e
m
s
:
 
T
h
e
 
l
i
s
t
 
o
f
 
i
t
e
m
s
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
e
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
i
t
e
m
 
i
n
 
i
t
e
m
s
:


 
 
 
 
 
 
 
 
l
o
g
(
i
t
e
m
)


 
 
 
 
r
e
t
u
r
n
 
i
t
e
m
s






d
e
f
 
l
o
g
_
d
i
c
t
(
i
t
e
m
s
:
 
d
i
c
t
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
L
o
g
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
 
o
f
 
i
t
e
m
s
 
b
y
 
p
r
i
n
t
i
n
g
 
i
t
.
 
H
a
n
d
l
e
s
 
s
t
r
i
n
g
s
,
 
n
u
m
b
e
r
s
,
 
l
i
s
t
s
,
 
a
n
d
 
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
 
b
y
 
p
r
i
n
t
i
n
g


 
 
 
 
t
h
e
m
 
d
i
r
e
c
t
l
y
 
o
r
 
a
s
 
a
 
J
S
O
N
-
f
o
r
m
a
t
t
e
d
 
s
t
r
i
n
g
.
 
O
t
h
e
r
 
t
y
p
e
s
 
a
r
e
 
r
e
p
o
r
t
e
d
 
a
s
 
e
r
r
o
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
t
e
m
s
 
(
d
i
c
t
)
:
 
T
h
e
 
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
 
o
f
 
i
t
e
m
s
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
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


 
 
 
 
 
 
 
 
i
t
e
m
s
:
 
T
h
e
 
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
 
o
f
 
i
t
e
m
s
 
t
o
 
b
e
 
l
o
g
g
e
d
.
 
C
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
e
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
k
e
y
,
 
v
a
l
u
e
 
i
n
 
i
t
e
m
s
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
l
o
g
(
f
"
{
k
e
y
}
:
 
{
v
a
l
u
e
}
"
)


 
 
 
 
r
e
t
u
r
n
 
i
t
e
m
s






d
e
f
 
l
o
g
_
j
s
o
n
(
i
t
e
m
s
:
 
d
i
c
t
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
L
o
g
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
 
o
f
 
i
t
e
m
s
 
a
s
 
J
S
O
N
.
 
H
a
n
d
l
e
s
import unittest
from unittest.mock import patch


class TestLogFunction(unittest.TestCase):
    @patch('builtins.print')
    def test_log_string(self, mock_print):
        """ Test logging a simple string """
        log("Hello, world!")
        mock_print.assert_called_once_with("Hello, world!")

    @patch('builtins.print')
    def test_log_number(self, mock_print):
        """ Test logging a number """
        log(123.456)
        mock_print.assert_called_once_with(123.456)

    @patch('builtins.print')
    def test_log_dictionary(self, mock_print):
        """ Test logging a dictionary as JSON """
        log({"key": "value", "number": 42})
        expected_json_output = '{\n    "key": "value",\n    "number": 42\n}'
        mock_print.assert_called_once_with(expected_json_output)

    @patch('builtins.print')
    def test_log_list(self, mock_print):
        """ Test logging a list as JSON """
        log([1, 2, 3, 4, 5])
        expected_json_output = '[\n    1,\n    2,\n    3,\n    4,\n    5\n]'
        mock_print.assert_called_once_with(expected_json_output)
if __name__ == '__main__':
    unittest.main()