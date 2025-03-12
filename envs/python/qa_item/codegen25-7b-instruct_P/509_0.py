d
e
f
 
m
o
d
_
e
x
p
(
b
a
s
e
:
i
n
t
,
 
e
x
p
o
n
e
n
t
:
i
n
t
,
 
m
o
d
u
l
u
s
:
i
n
t
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


 
 
 
 
P
e
r
f
o
r
m
 
m
o
d
u
l
a
r
 
e
x
p
o
n
e
n
t
i
a
t
i
o
n
:
 
(
b
a
s
e
^
e
x
p
o
n
e
n
t
)
 
%
 
m
o
d
u
l
u
s
 
e
f
f
i
c
i
e
n
t
l
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
a
s
e
 
(
i
n
t
)
:
 
T
h
e
 
b
a
s
e
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 
e
x
p
o
n
e
n
t
 
(
i
n
t
)
:
 
T
h
e
 
e
x
p
o
n
e
n
t
 
v
a
l
u
e
 
(
s
h
o
u
l
d
 
b
e
 
n
o
n
-
n
e
g
a
t
i
v
e
)
.


 
 
 
 
 
 
 
 
m
o
d
u
l
u
s
 
(
i
n
t
)
:
 
T
h
e
 
m
o
d
u
l
u
s
 
v
a
l
u
e
 
(
s
h
o
u
l
d
 
b
e
 
p
o
s
i
t
i
v
e
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
r
e
s
u
l
t
 
o
f
 
(
b
a
s
e
^
e
x
p
o
n
e
n
t
)
 
%
 
m
o
d
u
l
u
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
m
o
d
u
l
u
s
 
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
 
0


 
 
 
 
i
f
 
m
o
d
u
l
u
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
i
f
 
e
x
p
o
n
e
n
t
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
i
f
 
e
x
p
o
n
e
n
t
 
<
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
o
d
_
i
n
v
(
b
a
s
e
,
 
m
o
d
u
l
u
s
)
 
*
 
m
o
d
_
e
x
p
(
b
a
s
e
,
 
-
e
x
p
o
n
e
n
t
,
 
m
o
d
u
l
u
s
)
 
%
 
m
o
d
u
l
u
s


 
 
 
 
i
f
 
e
x
p
o
n
e
n
t
 
%
 
2
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
o
d
_
e
x
p
(
b
a
s
e
 
*
 
b
a
s
e
 
%
 
m
o
d
u
l
u
s
,
 
e
x
p
o
n
e
n
t
 
/
/
 
2
,
 
m
o
d
u
l
u
s
)
 
%
 
m
o
d
u
l
u
s


 
 
 
 
r
e
t
u
r
n
 
b
a
s
e
 
*
 
m
o
d
_
e
x
p
(
b
a
s
e
,
 
e
x
p
o
n
e
n
t
 
-
 
1
,
 
m
o
d
u
l
u
s
)
 
%
 
m
o
d
u
l
u
s






d
e
f
 
m
o
d
_
i
n
v
(
a
:
i
n
t
,
 
m
o
d
u
l
u
s
:
i
n
t
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


 
 
 
 
P
e
r
f
o
r
m
 
m
o
d
u
l
a
r
 
i
n
v
e
r
s
e
 
e
f
f
i
c
i
e
n
t
l
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
 
(
i
n
t
)
:
 
T
h
e
 
v
a
l
u
e
 
t
o
 
f
i
n
d
 
t
h
e
 
i
n
v
e
r
s
e
 
o
f
.


 
 
 
 
 
 
 
 
m
o
d
u
l
u
s
 
(
i
n
t
)
:
 
T
h
e
 
m
o
d
u
l
u
s
 
v
a
l
u
e
 
(
s
h
o
u
l
d
 
b
e
 
p
o
s
i
t
i
v
e
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
i
n
v
e
r
s
e
 
o
f
 
a
 
m
o
d
 
m
o
d
u
l
u
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
m
o
d
u
l
u
s
 
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
 
0


 
 
 
 
i
f
 
m
o
d
u
l
u
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
i
f
 
a
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
i
f
 
a
 
<
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
o
d
_
i
n
v
(
-
a
,
 
m
o
d
u
l
u
s
)
 
*
 
m
o
d
u
l
u
s
 
+
 
m
o
d
u
l
u
s


 
 
 
 
i
f
 
a
 
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
 
1


 
 
 
 
i
f
 
a
 
=
=
 
m
o
d
u
l
u
s
 
-
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a


 
 
 
 
#
 
B
i
n
a
r
y
 
s
e
a
r
c
h
 
f
o
r
 
S
 
a
n
d
 
Z
 
s
u
c
h
 
t
h
a
t
 
S
 
*
 
2
^
r
 
=
 
a
 
(
m
o
d
 
m
o
d
u
l
u
s
)


 
 
 
 
S
 
=
 
a


 
 
 
 
Z
 
=
 
m
o
d
u
l
u
s


 
 
 
 
r
 
=
 
0


 
 
 
 
w
h
i
l
e
 
S
 
!
=
 
1
:


 
 
 
 
 
 
 
 
S
 
=
 
S
 
*
 
S
 
%
 
m
o
d
u
l
u
s


 
 
 
 
 
 
 
 
r
 
+
=
 
1


 
 
 
 
 
 
 
 
i
f
 
S
 
=
=
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k


 
 
 
 
 
 
 
 
Z
 
=
 
Z
 
*
 
Z
 
%
 
m
o
d
u
l
u
s


 
 
 
 
i
f
 
S
 
!
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0


 
 
 
 
#
 
S
e
a
r
c
h
 
f
o
r
 
m
 
s
u
c
h
 
t
h
a
t
 
(
a
^
(
2
^
import unittest


class TestModExp(unittest.TestCase):
    def test_case_1(self):
        """ Test with base = 2, exponent = 10, modulus = 1000 """
        self.assertEqual(mod_exp(2, 10, 1000), 24)

    def test_case_2(self):
        """ Test with base = 3, exponent = 7, modulus = 50 """
        self.assertEqual(mod_exp(3, 7, 50), 37)

    def test_case_3(self):
        """ Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1) """
        self.assertEqual(mod_exp(5, 0, 13), 1)

    def test_case_4(self):
        """ Test with base = 7, exponent = 5, modulus = 20 """
        self.assertEqual(mod_exp(7, 5, 20), 7)  # 7^5 = 16807, 16807 % 20 = 7

    def test_case_5(self):
        """ Test with base = 10, exponent = 5, modulus = 6 """
        self.assertEqual(mod_exp(10, 5, 6), 4)  # 10^5 = 100000, 100000 % 6 = 4
if __name__ == '__main__':
    unittest.main()