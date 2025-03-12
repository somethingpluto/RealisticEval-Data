i
m
p
o
r
t
 
r
e


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
w
l
a
n
0
'
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
s
 
t
h
e
 
I
P
v
4
 
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
 
l
o
c
a
l
 
c
o
m
p
u
t
e
r
 
o
n
 
a
 
s
p
e
c
i
f
i
c
 
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
,
 
s
u
c
h
 
a
s
 
w
l
a
n
0
,
 
w
h
i
c
h
 
i
s
 
u
s
u
a
l
l
y
 
a
 
w
i
r
e
l
e
s
s
 
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
 
q
u
e
r
y
.
 
D
e
f
a
u
l
t
 
i
s
 
'
w
l
a
n
0
'
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
,
 
o
r
 
a
 
m
e
s
s
a
g
e
 
i
n
d
i
c
a
t
i
n
g
 
n
o
 
I
P
 
w
a
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
i
p
 
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
h
o
s
t
n
a
m
e
'
,
 
'
-
-
a
l
l
-
i
p
-
a
d
d
r
e
s
s
e
s
'
]
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
.
s
t
r
i
p
(
)


 
 
 
 
e
x
c
e
p
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
:


 
 
 
 
 
 
 
 
i
p
 
=
 
'
N
o
 
I
P
 
f
o
u
n
d
'


 
 
 
 
r
e
t
u
r
n
 
i
p






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
h
o
s
t
n
a
m
e
(
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
s
 
t
h
e
 
h
o
s
t
n
a
m
e
 
o
f
 
t
h
e
 
l
o
c
a
l
 
c
o
m
p
u
t
e
r




 
 
 
 
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
 
l
o
c
a
l
 
h
o
s
t
n
a
m
e


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
h
o
s
t
n
a
m
e
 
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
h
o
s
t
n
a
m
e
'
]
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
.
s
t
r
i
p
(
)


 
 
 
 
e
x
c
e
p
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
:


 
 
 
 
 
 
 
 
h
o
s
t
n
a
m
e
 
=
 
'
N
o
 
h
o
s
t
n
a
m
e
 
f
o
u
n
d
'


 
 
 
 
r
e
t
u
r
n
 
h
o
s
t
n
a
m
e






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
h
o
s
t
n
a
m
e
s
(
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


 
 
 
 
g
e
t
s
 
t
h
e
 
h
o
s
t
n
a
m
e
s
 
o
f
 
a
l
l
 
t
h
e
 
c
o
m
p
u
t
e
r
s
 
o
n
 
t
h
e
 
l
o
c
a
l
 
n
e
t
w
o
r
k




 
 
 
 
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
 
h
o
s
t
n
a
m
e
s


 
 
 
 
"
"
"


 
 
 
 
h
o
s
t
n
a
m
e
s
 
=
 
[
]


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
h
o
s
t
n
a
m
e
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
h
o
s
t
n
a
m
e
'
,
 
'
-
-
a
l
l
-
f
q
d
n
s
'
]
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
.
s
t
r
i
p
(
)
.
s
p
l
i
t
(
'
\
n
'
)


 
 
 
 
e
x
c
e
p
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
:


 
 
 
 
 
 
 
 
h
o
s
t
n
a
m
e
s
 
=
 
[
'
N
o
 
h
o
s
t
n
a
m
e
s
 
f
o
u
n
d
'
]


 
 
 
 
r
e
t
u
r
n
 
h
o
s
t
n
a
m
e
s






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
m
a
c
_
a
d
d
r
e
s
s
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
w
l
a
n
0
'
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
g
e
t
s
 
t
h
e
 
M
A
C
 
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
 
l
o
c
a
l
 
c
o
m
p
u
t
e
r
 
o
n
 
a
 
s
p
e
c
i
f
i
c
 
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
,
 
s
u
c
h
 
a
s
 
w
l
a
n
0
,
 
w
h
i
c
h
 
i
s
 
u
s
u
a
l
l
y
 
a
 
w
i
r
e
l
e
s
s
 
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
 
q
u
e
r
y
.
 
D
e
f
a
u
l
t
 
i
s
 
'
w
l
a
n
0
'
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
 
l
o
c
a
l
 
M
A
C
 
a
d
d
r
e
s
s
,
 
o
r
 
a
 
m
e
s
s
a
g
e
 
i
n
d
i
c
a
t
i
n
g
 
n
o
 
M
A
C
 
w
a
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
m
a
c
 
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
import unittest
from unittest.mock import patch, MagicMock


class TestGetLocalIp(unittest.TestCase):
    def setUp(self):
        # Sample IP command output for a wlan0 interface
        self.sample_output = "3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000\n" \
                             "    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0\n" \
                             "       valid_lft 86394sec preferred_lft 86394sec\n"

    @patch('subprocess.run')
    def test_successful_ip_retrieval(self, mock_run):
        # Configure the mock to return a successful output
        mock_run.return_value = MagicMock(stdout=self.sample_output, check=True)
        # Test function with wlan0 interface
        ip = get_local_ip('wlan0')
        self.assertEqual(ip, '192.168.1.100')

    @patch('subprocess.run')
    def test_command_failure(self, mock_run):
        # Simulate a subprocess failure
        mock_run.side_effect = subprocess.CalledProcessError(1, ['ip', 'addr', 'show', 'wlan0'])
        self.assertRaises(Exception)
    @patch('subprocess.run')
    def test_different_interface(self, mock_run):
        # Configure the mock for a different interface
        mock_run.return_value = MagicMock(
            stdout="3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n    inet 10.0.0.1/24", check=True)
        ip = get_local_ip('eth0')
        self.assertEqual(ip, '10.0.0.1')
if __name__ == '__main__':
    unittest.main()