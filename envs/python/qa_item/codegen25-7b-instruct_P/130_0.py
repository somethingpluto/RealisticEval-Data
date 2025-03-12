d
e
f
 
c
o
m
p
u
t
e
_
p
i
(
d
i
g
i
t
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
m
p
u
t
i
n
g
 
P
I
 
(
π
)
 
U
s
i
n
g
 
G
a
u
s
s
-
L
e
g
e
n
d
r
e
 
A
l
g
o
r
i
t
h
m
 
w
i
t
h
 
H
i
g
h
-
p
r
e
c
i
s
i
o
n
 
A
r
i
t
h
m
e
t
i
c
 
L
i
b
r
a
r
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
g
i
t
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
 
n
u
m
b
e
r
 
o
f
 
d
e
c
i
m
a
l
 
d
i
g
i
t
s
 
t
o
 
c
o
m
p
u
t
e
 
π
 
t
o
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
 
v
a
l
u
e
 
o
f
 
π
 
t
o
 
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
u
m
b
e
r
 
o
f
 
d
i
g
i
t
s
.


 
 
 
 
"
"
"


 
 
 
 
p
i
 
=
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
0
)


 
 
 
 
k
 
=
 
0


 
 
 
 
w
h
i
l
e
 
T
r
u
e
:


 
 
 
 
 
 
 
 
t
e
r
m
 
=
 
(


 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
1
)
 
/
 
(
1
6
 
*
*
 
k
)
 
*


 
 
 
 
 
 
 
 
 
 
 
 
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
4
)
 
/
 
(
8
 
*
 
k
 
+
 
1
)
 
-


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
2
)
 
/
 
(
8
 
*
 
k
 
+
 
4
)
 
-


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
1
)
 
/
 
(
8
 
*
 
k
 
+
 
5
)
 
-


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
1
)
 
/
 
(
8
 
*
 
k
 
+
 
6
)


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
p
i
 
+
=
 
t
e
r
m


 
 
 
 
 
 
 
 
i
f
 
t
e
r
m
.
i
s
_
z
e
r
o
:


 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k


 
 
 
 
 
 
 
 
k
 
+
=
 
1


 
 
 
 
p
i
 
=
 
p
i
.
s
q
r
t
(
)


 
 
 
 
p
i
 
=
 
p
i
.
q
u
a
n
t
i
z
e
(
d
e
c
i
m
a
l
.
D
e
c
i
m
a
l
(
1
0
)
 
*
*
 
(
-
d
i
g
i
t
s
)
)


 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
p
i
)






d
e
f
 
m
a
i
n
(
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
m
a
i
n
 
f
u
n
c
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


 
 
 
 
 
 
 
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
d
i
g
i
t
s
 
=
 
i
n
t
(
i
n
p
u
t
(
'
E
n
t
e
r
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
d
e
c
i
m
a
l
 
d
i
g
i
t
s
 
t
o
 
c
o
m
p
u
t
e
 
π
 
t
o
:
 
'
)
)


 
 
 
 
p
i
 
=
 
c
o
m
p
u
t
e
_
p
i
(
d
i
g
i
t
s
)


 
 
 
 
p
r
i
n
t
(
f
'
π
 
t
o
 
{
d
i
g
i
t
s
}
 
d
e
c
i
m
a
l
 
d
i
g
i
t
s
 
i
s
:
 
{
p
i
}
'
)






i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
'
_
_
m
a
i
n
_
_
'
:


 
 
 
 
m
a
i
n
(
)


import unittest


class TestComputePi(unittest.TestCase):

    def test_calculate_pi_5_decimal_places(self):
        digits = 5
        expected = '3.14159'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_10_decimal_places(self):
        digits = 10
        expected = '3.1415926536'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_15_decimal_places(self):
        digits = 15
        expected = '3.141592653589793'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_20_decimal_places(self):
        digits = 20
        expected = '3.14159265358979323846'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

    def test_calculate_pi_30_decimal_places(self):
        digits = 30
        expected = '3.141592653589793238462643383280'
        result = compute_pi(digits)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()