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
 
c
o
n
v
e
r
t
_
h
m
s
_
t
o
_
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
t
i
m
e
_
s
t
r
:
 
s
t
r
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
i
n
t
]
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
h
e
 
f
o
r
m
a
t
 
'
X
h
Y
m
i
n
Z
s
'
 
t
o
 
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
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
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
,
 
w
h
e
r
e
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
,
 
a
n
d
 
s
e
c
o
n
d
s


 
 
 
 
a
r
e
 
o
p
t
i
o
n
a
l
l
y
 
p
r
o
v
i
d
e
d
,
 
a
n
d
 
c
o
n
v
e
r
t
s
 
t
h
i
s
 
d
u
r
a
t
i
o
n
 
i
n
t
o
 
t
h
e
 
e
q
u
i
v
a
l
e
n
t
 
n
u
m
b
e
r
 
o
f
 
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
,
 
e
.
g
.
,
 
'
1
h
2
0
m
i
n
3
0
s
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


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
i
n
t
]
:
 
T
h
e
 
e
q
u
i
v
a
l
e
n
t
 
d
u
r
a
t
i
o
n
 
i
n
 
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
,
 
o
r
 
N
o
n
e
 
i
f
 
t
h
e
 
i
n
p
u
t
 
i
s
 
i
n
v
a
l
i
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
t
i
m
e
_
s
t
r
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
 
S
p
l
i
t
 
t
h
e
 
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
 
i
t
s
 
c
o
m
p
o
n
e
n
t
 
p
a
r
t
s


 
 
 
 
p
a
r
t
s
 
=
 
t
i
m
e
_
s
t
r
.
s
p
l
i
t
(
"
h
"
)


 
 
 
 
i
f
 
l
e
n
(
p
a
r
t
s
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
p
a
r
t
s
 
=
 
t
i
m
e
_
s
t
r
.
s
p
l
i
t
(
"
m
i
n
"
)


 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
p
a
r
t
s
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
t
s
 
=
 
t
i
m
e
_
s
t
r
.
s
p
l
i
t
(
"
s
"
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
p
a
r
t
s
)
 
=
=
 
1
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
 
C
o
n
v
e
r
t
 
t
h
e
 
h
o
u
r
s
 
t
o
 
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


 
 
 
 
h
o
u
r
s
 
=
 
i
n
t
(
p
a
r
t
s
[
0
]
)


 
 
 
 
h
o
u
r
s
_
m
i
l
l
i
s
 
=
 
h
o
u
r
s
 
*
 
6
0
 
*
 
6
0
 
*
 
1
0
0
0




 
 
 
 
#
 
I
f
 
t
h
e
r
e
 
a
r
e
 
n
o
 
m
i
n
u
t
e
s
,
 
r
e
t
u
r
n
 
t
h
e
 
h
o
u
r
s
 
v
a
l
u
e


 
 
 
 
i
f
 
l
e
n
(
p
a
r
t
s
)
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
h
o
u
r
s
_
m
i
l
l
i
s




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
m
i
n
u
t
e
s
 
t
o
 
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


 
 
 
 
m
i
n
u
t
e
s
 
=
 
i
n
t
(
p
a
r
t
s
[
1
]
)


 
 
 
 
m
i
n
u
t
e
s
_
m
i
l
l
i
s
 
=
 
m
i
n
u
t
e
s
 
*
 
6
0
 
*
 
1
0
0
0




 
 
 
 
#
 
I
f
 
t
h
e
r
e
 
a
r
e
 
n
o
 
s
e
c
o
n
d
s
,
 
r
e
t
u
r
n
 
t
h
e
 
m
i
n
u
t
e
s
 
v
a
l
u
e


 
 
 
 
i
f
 
l
e
n
(
p
a
r
t
s
)
 
=
=
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
h
o
u
r
s
_
m
i
l
l
i
s
 
+
 
m
i
n
u
t
e
s
_
m
i
l
l
i
s




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
s
e
c
o
n
d
s
 
t
o
 
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


 
 
 
 
s
e
c
o
n
d
s
 
=
 
i
n
t
(
p
a
r
t
s
[
2
]
)


 
 
 
 
s
e
c
o
n
d
s
_
m
i
l
l
i
s
 
=
 
s
e
c
o
n
d
s
 
*
 
1
0
0
0




 
 
 
 
#
 
R
e
t
u
r
n
 
t
h
e
 
t
o
t
a
l
 
d
u
r
a
t
i
o
n
 
i
n
 
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


 
 
 
 
r
e
t
u
r
n
 
h
o
u
r
s
_
m
i
l
l
i
s
 
+
 
m
i
n
u
t
e
s
_
m
i
l
l
i
s
 
+
 
s
e
c
o
n
d
s
_
m
i
l
l
i
s






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
_
t
o
_
h
m
s
(
m
i
l
l
i
s
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
o
n
v
e
r
t
 
a
 
d
u
r
a
t
i
o
n
 
i
n
 
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
 
t
o
 
a
 
s
t
r
i
n
g
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
'
X
h
Y
m
i
n
Z
s
'
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
d
u
r
a
t
i
o
n
 
i
n
 
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
 
a
n
d
 
c
o
n
v
e
r
t
s
 
i
t
 
i
n
t
o
 
a
 
s
t
r
i
n
g
 
i
n
 
t
h
e
 
f
o
r
m
a
t


 
 
 
 
'
X
h
Y
m
i
n
Z
s
'
,
 
w
h
e
r
e
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
,
 
a
n
d
 
s
e
c
o
n
d
s
 
a
r
e
 
o
p
t
i
o
n
a
l
l
y
 
p
r
o
v
i
d
e
d
.




 
 
 
 
A
r
g
s
:


import unittest

class TestConvertHmsToMilliseconds(unittest.TestCase):

    def test_basic_conversion(self):
        self.assertEqual(convert_hms_to_milliseconds("1h20min30s"), 4830000, "Should convert 1h20min30s to 4830000 milliseconds")

    def test_no_hours_or_minutes(self):
        self.assertEqual(convert_hms_to_milliseconds("30s"), 30000, "Should convert 30s to 30000 milliseconds")

    def test_invalid_format(self):
        self.assertIsNone(convert_hms_to_milliseconds("1hour20minutes"), "Should return None for invalid time format")

    def test_edge_case_max_one_day(self):
        self.assertEqual(convert_hms_to_milliseconds("23h59min59s"), 86399000, "Should convert 23h59min59s to 86399000 milliseconds")

    def test_exceeding_one_day(self):
        self.assertEqual(convert_hms_to_milliseconds("24h1min"), 86460000,
                         "Should correctly convert 24h1min to 86460000 milliseconds")
if __name__ == '__main__':
    unittest.main()