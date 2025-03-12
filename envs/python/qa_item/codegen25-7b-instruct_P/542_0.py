d
e
f
 
c
a
l
c
u
l
a
t
e
_
d
i
s
c
o
u
n
t
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
:
 
f
l
o
a
t
,
 
a
c
t
u
a
l
_
p
r
i
c
e
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
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
i
s
c
o
u
n
t
 
p
e
r
c
e
n
t
a
g
e
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
p
r
i
c
e
 
a
n
d
 
t
h
e
 
a
c
t
u
a
l
 
p
r
i
c
e
 
p
a
i
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
o
r
i
g
i
n
a
l
 
p
r
i
c
e
 
o
f
 
t
h
e
 
i
t
e
m
.


 
 
 
 
 
 
 
 
a
c
t
u
a
l
_
p
r
i
c
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
a
c
t
u
a
l
 
p
r
i
c
e
 
p
a
i
d
 
f
o
r
 
t
h
e
 
i
t
e
m
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
d
i
s
c
o
u
n
t
 
p
e
r
c
e
n
t
a
g
e
,
 
r
o
u
n
d
e
d
 
t
o
 
t
w
o
 
d
e
c
i
m
a
l
 
p
l
a
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
d
i
s
c
o
u
n
t
 
=
 
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
-
 
a
c
t
u
a
l
_
p
r
i
c
e
)
 
/
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
*
 
1
0
0


 
 
 
 
r
e
t
u
r
n
 
r
o
u
n
d
(
d
i
s
c
o
u
n
t
,
 
2
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
t
a
x
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
:
 
f
l
o
a
t
,
 
t
a
x
_
r
a
t
e
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
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
 
t
a
x
 
a
m
o
u
n
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
g
i
v
e
n
 
p
r
i
c
e
 
a
n
d
 
t
a
x
 
r
a
t
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
o
r
i
g
i
n
a
l
 
p
r
i
c
e
 
o
f
 
t
h
e
 
i
t
e
m
.


 
 
 
 
 
 
 
 
t
a
x
_
r
a
t
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
t
a
x
 
r
a
t
e
 
t
o
 
a
p
p
l
y
 
t
o
 
t
h
e
 
i
t
e
m
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
t
a
x
 
a
m
o
u
n
t
,
 
r
o
u
n
d
e
d
 
t
o
 
t
w
o
 
d
e
c
i
m
a
l
 
p
l
a
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
t
a
x
 
=
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
*
 
t
a
x
_
r
a
t
e
 
/
 
1
0
0


 
 
 
 
r
e
t
u
r
n
 
r
o
u
n
d
(
t
a
x
,
 
2
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
t
o
t
a
l
_
p
r
i
c
e
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
:
 
f
l
o
a
t
,
 
a
c
t
u
a
l
_
p
r
i
c
e
:
 
f
l
o
a
t
,
 
t
a
x
_
r
a
t
e
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
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
 
t
o
t
a
l
 
p
r
i
c
e
 
o
f
 
t
h
e
 
i
t
e
m
,
 
i
n
c
l
u
d
i
n
g
 
t
a
x
 
a
n
d
 
d
i
s
c
o
u
n
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
o
r
i
g
i
n
a
l
 
p
r
i
c
e
 
o
f
 
t
h
e
 
i
t
e
m
.


 
 
 
 
 
 
 
 
a
c
t
u
a
l
_
p
r
i
c
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
a
c
t
u
a
l
 
p
r
i
c
e
 
p
a
i
d
 
f
o
r
 
t
h
e
 
i
t
e
m
.


 
 
 
 
 
 
 
 
t
a
x
_
r
a
t
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
t
a
x
 
r
a
t
e
 
t
o
 
a
p
p
l
y
 
t
o
 
t
h
e
 
i
t
e
m
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
t
o
t
a
l
 
p
r
i
c
e
,
 
r
o
u
n
d
e
d
 
t
o
 
t
w
o
 
d
e
c
i
m
a
l
 
p
l
a
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
d
i
s
c
o
u
n
t
 
=
 
c
a
l
c
u
l
a
t
e
_
d
i
s
c
o
u
n
t
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
,
 
a
c
t
u
a
l
_
p
r
i
c
e
)


 
 
 
 
t
a
x
 
=
 
c
a
l
c
u
l
a
t
e
_
t
a
x
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
,
 
t
a
x
_
r
a
t
e
)


 
 
 
 
t
o
t
a
l
_
p
r
i
c
e
 
=
 
o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
-
 
d
i
s
c
o
u
n
t
 
+
 
t
a
x


 
 
 
 
r
e
t
u
r
n
 
r
o
u
n
d
(
t
o
t
a
l
_
p
r
i
c
e
,
 
2
)


`
`
`




T
o
 
u
s
e
 
t
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
,
 
y
o
u
 
c
a
n
 
c
a
l
l
 
i
t
 
w
i
t
h
 
t
h
e
 
o
r
i
g
i
n
a
l
 
p
r
i
c
e
,
 
a
c
t
u
a
l
 
p
r
i
c
e
 
p
a
i
d
,
 
a
n
d
 
t
a
x
 
r
a
t
e
:




`
`
`
p
y
t
h
o
n


o
r
i
g
i
n
a
l
_
p
r
i
c
e
 
=
 
1
0
0


a
c
t
u
a
l
_
p
r
i
c
e
 
=
 
8
0


t
a
x
_
r
a
t
e
 
=
 
1
0




t
o
t
a
l
_
p
r
i
c
e
 
=
 
c
a
l
c
u
l
a
t
e
_
t
o
t
a
l
_
p
r
i
c
e
(
o
r
i
g
i
n
a
l
_
p
r
i
c
e
,
 
a
c
t
u
a
l
_
p
r
i
c
e
,
 
t
a
x
_
r
a
t
e
)


p
r
i
n
t
(
f
"
T
o
t
a
l
 
p
r
i
c
e
:
 
$
{
import unittest


class TestCalculateDiscount(unittest.TestCase):

    def test_discount_25_percent(self):
        self.assertEqual(calculate_discount(100, 75), 25.00)

    def test_discount_0_percent(self):
        self.assertEqual(calculate_discount(50, 50), 0.00)

    def test_discount_100_percent(self):
        self.assertEqual(calculate_discount(100, 0), 100.00)

    def test_discount_50_percent(self):
        self.assertEqual(calculate_discount(200, 100), 50.00)

if __name__ == '__main__':
    unittest.main()