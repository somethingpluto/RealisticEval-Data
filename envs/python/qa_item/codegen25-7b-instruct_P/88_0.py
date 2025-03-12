d
e
f
 
i
s
_
c
r
o
n
_
b
e
t
w
e
e
n
_
2
_
a
n
d
_
4
_
a
m
(
c
r
o
n
_
e
x
p
r
e
s
s
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
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
 
a
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
a
n
d
 
d
e
t
e
r
m
i
n
e
 
w
h
e
t
h
e
r
 
i
t
 
i
s
 
b
e
t
w
e
e
n
 
2
 
a
.
m
.
 
a
n
d
 
4
 
a
.
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
r
o
n
_
e
x
p
r
e
s
s
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
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
t
o
 
p
a
r
s
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
a
n
y
 
h
o
u
r
 
i
n
 
t
h
e
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
i
s
 
b
e
t
w
e
e
n
 
2
 
a
.
m
.
 
a
n
d
 
4
 
a
.
m
.
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
c
r
o
n
 
=
 
C
r
o
n
T
r
i
g
g
e
r
.
f
r
o
m
_
c
r
o
n
t
a
b
(
c
r
o
n
_
e
x
p
r
e
s
s
i
o
n
)


 
 
 
 
r
e
t
u
r
n
 
a
n
y
(


 
 
 
 
 
 
 
 
[


 
 
 
 
 
 
 
 
 
 
 
 
h
o
u
r
 
>
=
 
2


 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
h
o
u
r
 
<
 
4


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
h
o
u
r
 
i
n
 
c
r
o
n
.
i
t
e
r
_
r
a
n
g
e
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
e
t
i
m
e
.
n
o
w
(
)
,
 
d
a
t
e
t
i
m
e
.
n
o
w
(
)
 
+
 
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
d
a
y
s
=
1
)


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
]


 
 
 
 
)






d
e
f
 
i
s
_
c
r
o
n
_
b
e
t
w
e
e
n
_
6
_
a
n
d
_
8
_
a
m
(
c
r
o
n
_
e
x
p
r
e
s
s
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
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
 
a
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
a
n
d
 
d
e
t
e
r
m
i
n
e
 
w
h
e
t
h
e
r
 
i
t
 
i
s
 
b
e
t
w
e
e
n
 
6
 
a
.
m
.
 
a
n
d
 
8
 
a
.
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
r
o
n
_
e
x
p
r
e
s
s
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
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
t
o
 
p
a
r
s
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
a
n
y
 
h
o
u
r
 
i
n
 
t
h
e
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
i
s
 
b
e
t
w
e
e
n
 
6
 
a
.
m
.
 
a
n
d
 
8
 
a
.
m
.
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
c
r
o
n
 
=
 
C
r
o
n
T
r
i
g
g
e
r
.
f
r
o
m
_
c
r
o
n
t
a
b
(
c
r
o
n
_
e
x
p
r
e
s
s
i
o
n
)


 
 
 
 
r
e
t
u
r
n
 
a
n
y
(


 
 
 
 
 
 
 
 
[


 
 
 
 
 
 
 
 
 
 
 
 
h
o
u
r
 
>
=
 
6


 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
h
o
u
r
 
<
 
8


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
h
o
u
r
 
i
n
 
c
r
o
n
.
i
t
e
r
_
r
a
n
g
e
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
e
t
i
m
e
.
n
o
w
(
)
,
 
d
a
t
e
t
i
m
e
.
n
o
w
(
)
 
+
 
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
d
a
y
s
=
1
)


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
]


 
 
 
 
)






d
e
f
 
i
s
_
c
r
o
n
_
b
e
t
w
e
e
n
_
1
0
_
a
n
d
_
1
2
_
a
m
(
c
r
o
n
_
e
x
p
r
e
s
s
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
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
 
a
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
a
n
d
 
d
e
t
e
r
m
i
n
e
 
w
h
e
t
h
e
r
 
i
t
 
i
s
 
b
e
t
w
e
e
n
 
1
0
 
a
.
m
.
 
a
n
d
 
1
2
 
a
.
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
r
o
n
_
e
x
p
r
e
s
s
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
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
t
o
 
p
a
r
s
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
a
n
y
 
h
o
u
r
 
i
n
 
t
h
e
 
c
r
o
n
 
e
x
p
r
e
s
s
i
o
n
 
i
s
 
b
e
t
w
e
e
n
 
1
0
 
a
.
m
.
 
a
n
d
 
1
2
 
a
.
m
.
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
c
r
o
n
 
=
 
C
r
o
n
T
r
i
g
g
e
r
.
f
r
o
m
_
c
r
o
n
t
a
b
(
c
r
o
n
_
import unittest


class TestIsCronBetween2And4AM(unittest.TestCase):

    def test_specific_hours(self):
        """should return true for specific hours 2, 3, and 4"""
        self.assertTrue(is_cron_between_2_and_4_am('0 2,3,4 * * *'))

    def test_range_includes_2_to_4_am(self):
        """should return false for range that includes 2 to 4 a.m."""
        self.assertFalse(is_cron_between_2_and_4_am('0 1-5 * * *'))

    def test_range_excludes_2_to_4_am(self):
        """should return false for range that excludes 2 to 4 a.m."""
        self.assertFalse(is_cron_between_2_and_4_am('0 0-1,5-23 * * *'))

    def test_wildcard_in_hour_field(self):
        """should return false for wildcard in hour field"""
        self.assertFalse(is_cron_between_2_and_4_am('0 * * * *'))

if __name__ == '__main__':
    unittest.main()