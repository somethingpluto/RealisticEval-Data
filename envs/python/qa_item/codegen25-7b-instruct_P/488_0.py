i
m
p
o
r
t
 
s
u
b
p
r
o
c
e
s
s


i
m
p
o
r
t
 
r
e


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
 
O
p
t
i
o
n
a
l






d
e
f
 
g
e
t
_
l
o
c
a
l
_
i
p
(
i
n
t
e
r
f
a
c
e
:
 
s
t
r
 
=
 
'
W
i
-
F
i
'
)
 
-
>
 
O
p
t
i
o
n
a
l
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
r
i
e
v
e
 
t
h
e
 
l
o
c
a
l
 
I
P
 
a
d
d
r
e
s
s
 
o
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
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
o
n
 
W
i
n
d
o
w
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
t
e
r
f
a
c
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
 
n
a
m
e
 
o
f
 
t
h
e
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
t
o
 
c
h
e
c
k
 
(
d
e
f
a
u
l
t
 
i
s
 
'
W
i
-
F
i
'
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
s
t
r
]
:
 
T
h
e
 
l
o
c
a
l
 
I
P
 
a
d
d
r
e
s
s
 
i
f
 
f
o
u
n
d
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
I
P
 
a
d
d
r
e
s
s
 
o
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
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
i
p
_
a
d
d
r
e
s
s
 
=
 
s
u
b
p
r
o
c
e
s
s
.
c
h
e
c
k
_
o
u
t
p
u
t
(
[
'
i
p
c
o
n
f
i
g
'
,
 
'
/
a
l
l
'
]
,
 
s
h
e
l
l
=
T
r
u
e
)
.
d
e
c
o
d
e
(
'
u
t
f
-
8
'
)


 
 
 
 
 
 
 
 
i
p
_
a
d
d
r
e
s
s
 
=
 
r
e
.
s
e
a
r
c
h
(
r
f
'
I
P
v
4
 
A
d
d
r
e
s
s
.
+
:
 
(
{
r
e
.
e
s
c
a
p
e
(
i
n
t
e
r
f
a
c
e
)
}
\
s
.
+
)
'
,
 
i
p
_
a
d
d
r
e
s
s
)
.
g
r
o
u
p
(
1
)


 
 
 
 
e
x
c
e
p
t
 
(
s
u
b
p
r
o
c
e
s
s
.
C
a
l
l
e
d
P
r
o
c
e
s
s
E
r
r
o
r
,
 
A
t
t
r
i
b
u
t
e
E
r
r
o
r
)
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




 
 
 
 
#
 
R
e
m
o
v
e
 
a
n
y
 
l
e
a
d
i
n
g
 
a
n
d
 
t
r
a
i
l
i
n
g
 
s
p
a
c
e
s
 
a
n
d
 
n
e
w
l
i
n
e
s


 
 
 
 
i
p
_
a
d
d
r
e
s
s
 
=
 
i
p
_
a
d
d
r
e
s
s
.
s
t
r
i
p
(
)




 
 
 
 
r
e
t
u
r
n
 
i
p
_
a
d
d
r
e
s
s


import subprocess
import unittest
from unittest.mock import patch, MagicMock


class TestGetLocalIP(unittest.TestCase):

    @patch('subprocess.run')
    def test_local_ip_found(self, mock_run):
        # Mock the output of ipconfig for a case where a local IP is found
        mock_run.return_value = MagicMock(stdout='192.168.1.10\n')
        result = get_local_ip()
        self.assertEqual(result, '192.168.1.10')

    @patch('subprocess.run')
    def test_no_local_ip_found(self, mock_run):
        # Mock the output of ipconfig for a case where no local IP is found
        mock_run.return_value = MagicMock(stdout='10.0.0.5\n')
        result = get_local_ip()
        self.assertIsNone(result)

    @patch('subprocess.run')
    def test_multiple_ips_found(self, mock_run):
        # Mock the output with multiple local IPs
        mock_run.return_value = MagicMock(stdout='10.0.0.5\n'
                                                  '192.168.1.10\n')
        result = get_local_ip()
        self.assertEqual(result, '192.168.1.10')

    @patch('subprocess.run')
    def test_invalid_command(self, mock_run):
        # Simulate a case where subprocess.run raises a CalledProcessError
        mock_run.side_effect = subprocess.CalledProcessError(1, 'ipconfig')
        result = get_local_ip()
        self.assertIsNone(result)

    @patch('subprocess.run')
    def test_unexpected_error(self, mock_run):
        # Simulate an unexpected error
        mock_run.side_effect = Exception("Unexpected error")
        result = get_local_ip()
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()