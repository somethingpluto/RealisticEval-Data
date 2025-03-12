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
t
i
m
e
(
d
u
r
a
t
i
o
n
:
 
s
t
r
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
 
I
S
O
 
8
6
0
1
 
d
u
r
a
t
i
o
n
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
m
o
r
e
 
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
 
(
s
t
r
)
:
 
T
h
e
 
I
S
O
 
8
6
0
1
 
d
u
r
a
t
i
o
n
 
s
t
r
i
n
g
 
(
e
.
g
.
,
 
"
P
T
1
H
2
3
M
4
5
.
6
7
8
S
"
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
d
u
r
a
t
i
o
n
 
s
t
r
i
n
g
 
(
e
.
g
.
,
 
"
1
h
2
3
m
4
5
s
6
7
8
m
s
"
)
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
d
u
r
a
t
i
o
n
 
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
 
"
-
"


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
d
u
r
a
t
i
o
n
.
r
e
p
l
a
c
e
(
"
P
T
"
,
 
"
"
)


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
d
u
r
a
t
i
o
n
.
r
e
p
l
a
c
e
(
"
H
"
,
 
"
h
"
)


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
d
u
r
a
t
i
o
n
.
r
e
p
l
a
c
e
(
"
M
"
,
 
"
m
"
)


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
d
u
r
a
t
i
o
n
.
r
e
p
l
a
c
e
(
"
S
"
,
 
"
s
"
)


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
d
u
r
a
t
i
o
n
.
r
e
p
l
a
c
e
(
"
.
"
,
 
"
m
s
"
)


 
 
 
 
r
e
t
u
r
n
 
d
u
r
a
t
i
o
n






d
e
f
 
g
e
t
_
d
u
r
a
t
i
o
n
(
s
t
a
r
t
:
 
d
a
t
e
t
i
m
e
,
 
e
n
d
:
 
d
a
t
e
t
i
m
e
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


 
 
 
 
C
a
l
c
u
l
a
t
e
s
 
t
h
e
 
d
u
r
a
t
i
o
n
 
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
 
d
a
t
e
t
i
m
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
s
t
a
r
t
 
d
a
t
e
t
i
m
e
.


 
 
 
 
 
 
 
 
e
n
d
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
e
n
d
 
d
a
t
e
t
i
m
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
d
u
r
a
t
i
o
n
 
b
e
t
w
e
e
n
 
t
h
e
 
t
w
o
 
d
a
t
e
t
i
m
e
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
s
t
a
r
t
 
i
s
 
N
o
n
e
 
o
r
 
e
n
d
 
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
 
"
-
"


 
 
 
 
d
u
r
a
t
i
o
n
 
=
 
e
n
d
 
-
 
s
t
a
r
t


 
 
 
 
r
e
t
u
r
n
 
c
o
n
v
e
r
t
_
t
i
m
e
(
d
u
r
a
t
i
o
n
.
i
s
o
f
o
r
m
a
t
(
)
)






d
e
f
 
g
e
t
_
d
u
r
a
t
i
o
n
_
f
r
o
m
_
t
i
m
e
s
t
a
m
p
s
(
t
i
m
e
s
t
a
m
p
s
:
 
L
i
s
t
[
i
n
t
]
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


 
 
 
 
C
a
l
c
u
l
a
t
e
s
 
t
h
e
 
d
u
r
a
t
i
o
n
 
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
 
t
i
m
e
s
t
a
m
p
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
s
 
(
L
i
s
t
[
i
n
t
]
)
:
 
T
h
e
 
t
i
m
e
s
t
a
m
p
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
 
d
u
r
a
t
i
o
n
 
b
e
t
w
e
e
n
 
t
h
e
 
t
w
o
 
t
i
m
e
s
t
a
m
p
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
t
i
m
e
s
t
a
m
p
s
 
i
s
 
N
o
n
e
 
o
r
 
l
e
n
(
t
i
m
e
s
t
a
m
p
s
)
 
!
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
-
"


 
 
 
 
s
t
a
r
t
 
=
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
s
[
0
]
 
/
 
1
0
0
0
)


 
 
 
 
e
n
d
 
=
 
d
a
t
e
t
i
m
e
.
f
r
o
m
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
s
[
1
]
 
/
 
1
0
0
0
)


 
 
 
 
r
e
t
u
r
n
 
g
e
t
_
d
u
r
a
t
i
o
n
(
s
t
a
r
t
,
 
e
n
d
)






d
e
f
 
g
e
t
_
d
u
r
a
t
i
o
n
_
f
r
o
m
_
t
i
m
e
s
t
a
m
p
(
t
i
m
e
s
t
a
m
p
:
 
i
n
t
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


 
 
 
 
C
a
l
c
u
l
a
t
e
s
 
t
h
e
 
d
u
r
a
t
i
o
n
 
b
e
t
w
e
e
n
 
a
 
t
i
m
e
s
t
a
m
p
 
a
n
d
 
t
h
e
 
c
u
r
r
e
n
t
 
t
i
m
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
s
t
a
m
p
 
(
i
n
t
)
:
 
T
h
e
 
t
i
m
e
s
t
a
m
p
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
 
d
u
r
a
t
i
o
n
 
b
e
t
w
e
e
n
 
t
h
e
 
t
i
m
e
s
t
a
m
p
 
a
n
d
 
t
h
e
import unittest


class TestConvertTimeFunction(unittest.TestCase):

    def test_full_iso_duration(self):
        """Test converting full ISO 8601 duration with hours, minutes, seconds, and milliseconds."""
        self.assertEqual(convert_time('PT1H23M45.678S'), '1h23m45s678ms')

    def test_duration_with_seconds_and_milliseconds(self):
        """Test converting duration with only seconds and milliseconds."""
        self.assertEqual(convert_time('PT45.5S'), '45s500ms')

    def test_duration_with_hours_and_minutes_no_seconds(self):
        """Test converting duration with hours and minutes, but no seconds."""
        self.assertEqual(convert_time('PT2H5M'), '2h5m')

    def test_duration_with_only_seconds_no_milliseconds(self):
        """Test converting duration with only seconds, no milliseconds."""
        self.assertEqual(convert_time('PT20S'), '20s')

if __name__ == '__main__':
    unittest.main()