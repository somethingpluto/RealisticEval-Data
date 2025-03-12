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
o
_
r
o
m
a
n
(
n
u
m
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
s
 
a
n
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
 
t
o
 
i
t
s
 
R
o
m
a
n
 
n
u
m
e
r
a
l
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
(
i
n
t
)
:
 
T
h
e
 
n
u
m
b
e
r
 
t
o
 
c
o
n
v
e
r
t
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
 
R
o
m
a
n
 
n
u
m
e
r
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
i
n
p
u
t
 
n
u
m
b
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
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
n
u
m
,
 
i
n
t
)
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
T
y
p
e
E
r
r
o
r
(
"
I
n
p
u
t
 
m
u
s
t
 
b
e
 
a
n
 
i
n
t
e
g
e
r
.
"
)


 
 
 
 
i
f
 
n
o
t
 
(
0
 
<
 
n
u
m
 
<
 
4
0
0
0
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
"
I
n
p
u
t
 
m
u
s
t
 
b
e
 
b
e
t
w
e
e
n
 
1
 
a
n
d
 
3
9
9
9
.
"
)




 
 
 
 
r
o
m
a
n
_
n
u
m
e
r
a
l
 
=
 
"
"


 
 
 
 
r
o
m
a
n
_
m
a
p
 
=
 
[


 
 
 
 
 
 
 
 
(
1
0
0
0
,
 
"
M
"
)
,


 
 
 
 
 
 
 
 
(
9
0
0
,
 
"
C
M
"
)
,


 
 
 
 
 
 
 
 
(
5
0
0
,
 
"
D
"
)
,


 
 
 
 
 
 
 
 
(
4
0
0
,
 
"
C
D
"
)
,


 
 
 
 
 
 
 
 
(
1
0
0
,
 
"
C
"
)
,


 
 
 
 
 
 
 
 
(
9
0
,
 
"
X
C
"
)
,


 
 
 
 
 
 
 
 
(
5
0
,
 
"
L
"
)
,


 
 
 
 
 
 
 
 
(
4
0
,
 
"
X
L
"
)
,


 
 
 
 
 
 
 
 
(
1
0
,
 
"
X
"
)
,


 
 
 
 
 
 
 
 
(
9
,
 
"
I
X
"
)
,


 
 
 
 
 
 
 
 
(
5
,
 
"
V
"
)
,


 
 
 
 
 
 
 
 
(
4
,
 
"
I
V
"
)
,


 
 
 
 
 
 
 
 
(
1
,
 
"
I
"
)
,


 
 
 
 
]




 
 
 
 
f
o
r
 
a
r
a
b
i
c
,
 
r
o
m
a
n
 
i
n
 
r
o
m
a
n
_
m
a
p
:


 
 
 
 
 
 
 
 
w
h
i
l
e
 
n
u
m
 
>
=
 
a
r
a
b
i
c
:


 
 
 
 
 
 
 
 
 
 
 
 
r
o
m
a
n
_
n
u
m
e
r
a
l
 
+
=
 
r
o
m
a
n


 
 
 
 
 
 
 
 
 
 
 
 
n
u
m
 
-
=
 
a
r
a
b
i
c




 
 
 
 
r
e
t
u
r
n
 
r
o
m
a
n
_
n
u
m
e
r
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
t
o
_
a
r
a
b
i
c
(
r
o
m
a
n
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
 
R
o
m
a
n
 
n
u
m
e
r
a
l
 
t
o
 
i
t
s
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
m
a
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
 
R
o
m
a
n
 
n
u
m
e
r
a
l
 
t
o
 
c
o
n
v
e
r
t
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
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
i
n
p
u
t
 
R
o
m
a
n
 
n
u
m
e
r
a
l
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
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
r
o
m
a
n
,
 
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
 
T
y
p
e
E
r
r
o
r
(
"
I
n
p
u
t
 
m
u
s
t
 
b
e
 
a
 
s
t
r
i
n
g
.
"
)


 
 
 
 
i
f
 
n
o
t
 
r
o
m
a
n
.
i
s
a
l
p
h
a
(
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
"
I
n
p
u
t
 
m
u
s
t
 
c
o
n
s
i
s
t
 
o
f
 
o
n
l
y
 
l
e
t
t
e
r
s
 
f
r
o
m
 
t
h
e
 
R
o
m
a
n
 
a
l
p
h
a
b
e
t
.
"
)




 
 
 
 
a
r
a
b
i
c
_
n
u
m
e
r
a
l
 
=
 
0


 
 
 
 
r
o
m
a
n
_
m
a
p
 
=
 
[


 
 
 
 
 
 
 
 
(
"
M
"
,
 
1
0
0
0
)
,


 
 
 
 
 
 
 
 
(
"
C
M
"
,
 
9
0
0
)
,


 
 
 
 
 
 
 
 
(
"
D
"
,
 
5
0
0
)
,


 
 
 
 
 
 
 
 
(
"
C
D
"
,
 
4
0
0
)
,


 
 
 
 
 
 
 
 
(
"
C
"
,
 
1
0
0
)
,


 
 
 
 
 
 
 
 
(
"
X
C
"
,
 
9
0
)
,


 
 
 
 
 
 
 
 
(
"
L
"
,
 
5
0
)
,


 
 
 
 
 
 
 
 
(
"
X
L
"
,
 
4
0
)
,


 
 
 
 
 
 
 
 
(
"
X
"
,
 
1
0
)
,


 
 
 
 
 
 
 
 
(
"
I
X
"
,
 
9
)
,


 
 
 
 
 
 
 
 
(
"
import unittest


class TestConvertToRoman(unittest.TestCase):
    def test_typical_number(self):
        result = convert_to_roman(1987)
        self.assertEqual(result, 'MCMLXXXVII')  # 1987 = M + CM + LXXX + VII

    def test_minimum_value(self):
        result = convert_to_roman(1)
        self.assertEqual(result, 'I')  # 1 = I

    def test_large_number(self):
        result = convert_to_roman(3999)
        self.assertEqual(result, 'MMMCMXCIX')  # 3999 = MMM + CM + XC + IX

    def test_different_numeral_repeats(self):
        result = convert_to_roman(1666)
        self.assertEqual(result, 'MDCLXVI')  # 1666 = M + D + CLX + VI

    def test_no_fives_and_ones(self):
        result = convert_to_roman(2000)
        self.assertEqual(result, 'MM')  # 2000 = MM

if __name__ == '__main__':
    unittest.main()