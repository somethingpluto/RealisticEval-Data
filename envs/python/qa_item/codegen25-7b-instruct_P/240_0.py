f
r
o
m
 
d
a
t
e
t
i
m
e
 
i
m
p
o
r
t
 
t
i
m
e
d
e
l
t
a


i
m
p
o
r
t
 
r
e






d
e
f
 
g
e
n
_
t
i
m
e
o
u
t
_
t
i
m
e
d
e
l
t
a
(
t
i
m
e
_
s
t
r
i
n
g
:
 
s
t
r
)
 
-
>
 
t
i
m
e
d
e
l
t
a
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
 
t
i
m
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
 
i
n
t
o
 
a
 
t
i
m
e
d
e
l
t
a
 
o
b
j
e
c
t
.


 
 
 
 
T
h
e
 
i
n
p
u
t
 
s
t
r
i
n
g
 
c
a
n
 
i
n
c
l
u
d
e
 
d
a
y
s
 
(
d
)
,
 
h
o
u
r
s
 
(
h
)
,
 
m
i
n
u
t
e
s
 
(
m
)
,
 
s
e
c
o
n
d
s
 
(
s
)
,
 
a
n
d
 
m
i
l
l
i
s
e
c
o
n
d
s
 
(
m
s
)
.


 
 
 
 
e
g
.
 
"
1
d
 
2
h
 
3
m
 
4
s
 
5
0
0
m
s
"


 
 
 
 
E
a
c
h
 
u
n
i
t
 
s
h
o
u
l
d
 
b
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
 
b
y
 
a
n
 
i
n
t
e
g
e
r
 
f
o
l
l
o
w
e
d
 
b
y
 
i
t
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
u
n
i
t
 
l
e
t
t
e
r
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
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
t
i
m
e
 
d
u
r
a
t
i
o
n
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
i
m
e
d
e
l
t
a
:
 
A
 
t
i
m
e
d
e
l
t
a
 
o
b
j
e
c
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
i
n
g
 
t
h
e
 
i
n
p
u
t
 
d
u
r
a
t
i
o
n
.


 
 
 
 
"
"
"


 
 
 
 
p
a
t
t
e
r
n
 
=
 
r
e
.
c
o
m
p
i
l
e
(
r
"
(
\
d
+
)
(
[
d
h
m
s
]
{
1
}
)
"
)


 
 
 
 
t
i
m
e
_
d
e
l
t
a
 
=
 
t
i
m
e
d
e
l
t
a
(
)


 
 
 
 
f
o
r
 
m
a
t
c
h
 
i
n
 
p
a
t
t
e
r
n
.
f
i
n
d
i
t
e
r
(
t
i
m
e
_
s
t
r
i
n
g
)
:


 
 
 
 
 
 
 
 
t
i
m
e
_
d
e
l
t
a
 
+
=
 
t
i
m
e
d
e
l
t
a
(
*
*
{
m
a
t
c
h
.
g
r
o
u
p
(
2
)
:
 
i
n
t
(
m
a
t
c
h
.
g
r
o
u
p
(
1
)
)
}
)


 
 
 
 
r
e
t
u
r
n
 
t
i
m
e
_
d
e
l
t
a


import unittest
from datetime import timedelta


class TestGenTimeoutTimedelta(unittest.TestCase):
    def test_single_unit_days(self):
        self.assertEqual(gen_timeout_timedelta("5d"), timedelta(days=5))


    def test_single_unit_hours(self):
        self.assertEqual(gen_timeout_timedelta("8h"), timedelta(hours=8))

    def test_single_unit_minutes(self):
        self.assertEqual(gen_timeout_timedelta("45m"), timedelta(minutes=45))

    def test_single_unit_seconds(self):
        self.assertEqual(gen_timeout_timedelta("30s"), timedelta(seconds=30))

    def test_complex_mix(self):
        self.assertEqual(gen_timeout_timedelta("2d 20h 30m"), timedelta(days=2, hours=20, minutes=30))

    def test_no_units(self):
        self.assertEqual(gen_timeout_timedelta(""), timedelta(0))
if __name__ == '__main__':
    unittest.main()