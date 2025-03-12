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
_
h
m
s
_
s
t
r
i
n
g
_
t
o
_
m
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
 
i
n
t
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
 
"
X
h
Y
m
Z
s
"
 
(
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
 
s
e
c
o
n
d
s
)
 
i
n
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
i
m
e
 
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
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
V
a
l
u
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
 
d
o
e
s
 
n
o
t
 
m
a
t
c
h
 
t
h
e
 
e
x
p
e
c
t
e
d
 
f
o
r
m
a
t
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
r
e
.
m
a
t
c
h
(
r
"
^
\
d
+
h
\
d
+
m
\
d
+
s
$
"
,
 
t
i
m
e
_
s
t
r
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
f
"
I
n
v
a
l
i
d
 
t
i
m
e
 
s
t
r
i
n
g
:
 
{
t
i
m
e
_
s
t
r
}
"
)


 
 
 
 
t
i
m
e
_
s
t
r
_
s
p
l
i
t
 
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


 
 
 
 
t
i
m
e
_
i
n
_
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
t
i
m
e
_
s
t
r
_
s
p
l
i
t
[
0
]
)
 
*
 
3
6
0
0
 
+
 
i
n
t
(
t
i
m
e
_
s
t
r
_
s
p
l
i
t
[
1
]
.
s
p
l
i
t
(
"
m
"
)
[
0
]
)
 
*
 
6
0
 
+
 
i
n
t
(


 
 
 
 
 
 
 
 
t
i
m
e
_
s
t
r
_
s
p
l
i
t
[
1
]
.
s
p
l
i
t
(
"
m
"
)
[
1
]
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
[
0
]
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
i
n
_
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


import unittest


class TestConvertTimeHmsStringToMs(unittest.TestCase):

    def test_converts_typical_time_string_correctly(self):
        result = convert_time_hms_string_to_ms('1h30m15s')
        self.assertEqual(result, 5415000)  # 1 hour + 30 minutes + 15 seconds in ms

    def test_correctly_converts_string_with_zero_values(self):
        result = convert_time_hms_string_to_ms('0h0m0s')
        self.assertEqual(result, 0)  # 0 ms

    def test_converts_maximum_single_digit_values(self):
        result = convert_time_hms_string_to_ms('9h59m59s')
        self.assertEqual(result, 35999000)  # 9 hours + 59 minutes + 59 seconds in ms

    def test_handles_large_values(self):
        result = convert_time_hms_string_to_ms('100h0m0s')
        self.assertEqual(result, 360000000)  # 100 hours in ms

    def test_correctly_converts_strings_with_leading_zeros(self):
        result = convert_time_hms_string_to_ms('01h01m01s')
        self.assertEqual(result, 3661000)  # 1 hour + 1 minute + 1 second in ms

if __name__ == '__main__':
    unittest.main()