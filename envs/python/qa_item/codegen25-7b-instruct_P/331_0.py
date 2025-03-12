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
f
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
p
r
i
c
e
:
 
s
t
r
,
 
d
i
s
c
o
u
n
t
:
 
s
t
r
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
 
f
i
n
a
l
 
p
r
i
c
e
 
a
f
t
e
r
 
a
p
p
l
y
i
n
g
 
a
 
d
i
s
c
o
u
n
t
 
t
o
 
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
.


 
 
 
 
B
o
t
h
 
p
r
i
c
e
 
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
 
a
r
e
 
e
x
p
e
c
t
e
d
 
a
s
 
s
t
r
i
n
g
s
 
a
n
d
 
s
h
o
u
l
d
 
r
e
p
r
e
s
e
n
t
 
v
a
l
i
d
 
n
u
m
b
e
r
s
.


 
 
 
 
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
 
s
h
o
u
l
d
 
b
e
 
a
 
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
 
v
a
l
u
e
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
0
0
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
r
i
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
 
a
s
 
a
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
d
i
s
c
o
u
n
t
 
(
s
t
r
)
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
 
a
s
 
a
 
s
t
r
i
n
g
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
 
f
i
n
a
l
 
p
r
i
c
e
 
a
f
t
e
r
 
a
p
p
l
y
i
n
g
 
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
 
W
i
l
l
 
t
h
r
o
w
 
a
n
 
e
r
r
o
r
 
i
f
 
p
r
i
c
e
 
o
r
 
d
i
s
c
o
u
n
t
 
a
r
e
n
'
t
 
v
a
l
i
d
 
n
u
m
b
e
r
s
 
o
r
 
i
f
 
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
 
i
s
 
o
u
t
 
o
f
 
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
 
r
a
n
g
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
p
r
i
c
e
 
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
 
a
r
e
 
v
a
l
i
d
 
n
u
m
b
e
r
s


 
 
 
 
i
f
 
n
o
t
 
i
s
_
v
a
l
i
d
_
n
u
m
b
e
r
(
p
r
i
c
e
)
 
o
r
 
n
o
t
 
i
s
_
v
a
l
i
d
_
n
u
m
b
e
r
(
d
i
s
c
o
u
n
t
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
P
r
i
c
e
 
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
 
m
u
s
t
 
b
e
 
v
a
l
i
d
 
n
u
m
b
e
r
s
.
"
)




 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
d
i
s
c
o
u
n
t
 
i
s
 
a
 
v
a
l
i
d
 
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
 
v
a
l
u
e


 
 
 
 
i
f
 
n
o
t
 
i
s
_
v
a
l
i
d
_
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
(
d
i
s
c
o
u
n
t
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
D
i
s
c
o
u
n
t
 
m
u
s
t
 
b
e
 
a
 
v
a
l
i
d
 
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
 
v
a
l
u
e
 
b
e
t
w
e
e
n
 
0
 
a
n
d
 
1
0
0
.
"
)




 
 
 
 
#
 
C
o
n
v
e
r
t
 
p
r
i
c
e
 
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
 
t
o
 
f
l
o
a
t


 
 
 
 
p
r
i
c
e
 
=
 
f
l
o
a
t
(
p
r
i
c
e
)


 
 
 
 
d
i
s
c
o
u
n
t
 
=
 
f
l
o
a
t
(
d
i
s
c
o
u
n
t
)




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
f
i
n
a
l
 
p
r
i
c
e
 
a
f
t
e
r
 
a
p
p
l
y
i
n
g
 
d
i
s
c
o
u
n
t


 
 
 
 
f
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
 
p
r
i
c
e
 
-
 
(
p
r
i
c
e
 
*
 
(
d
i
s
c
o
u
n
t
 
/
 
1
0
0
)
)




 
 
 
 
#
 
R
o
u
n
d
 
f
i
n
a
l
 
p
r
i
c
e
 
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


 
 
 
 
f
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
 
r
o
u
n
d
(
f
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
 
2
)




 
 
 
 
r
e
t
u
r
n
 
f
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


`
`
`




H
e
r
e
'
s
 
a
n
 
e
x
a
m
p
l
e
 
o
f
 
h
o
w
 
t
o
 
u
s
e
 
t
h
e
 
f
u
n
c
t
i
o
n
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


#
 
E
x
a
m
p
l
e
 
u
s
a
g
e


p
r
i
c
e
 
=
 
"
1
5
0
.
0
0
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
 
"
2
0
"


f
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
f
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
p
r
i
c
e
,
 
d
i
s
c
o
u
n
t
)


p
r
i
n
t
(
f
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
)
 
 
#
 
1
2
6
.
0
0


`
`
`




N
o
t
e
 
t
h
a
t
 
t
h
e
 
f
u
n
c
t
i
o
n
 
a
l
s
o
 
i
n
c
l
u
d
e
s
 
e
r
r
o
r
 
h
a
n
d
l
i
n
g
 
f
o
r
 
i
n
v
a
l
i
d
 
i
n
p
u
t
s
,
 
s
u
c
h
 
a
s
 
n
o
n
-
n
u
m
e
r
i
c
 
v
a
l
u
e
s
 
o
r
 
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
s
 
o
u
t
s
i
d
e
 
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
 
r
a
n
g
e
.
 
Y
o
u
 
c
a
n
 
m
o
d
i
f
y
 
t
h
e
 
f
u
n
c
t
i
o
n
 
t
o
 
s
u
i
t
 
y
o
u
r
 
s
p
e
c
i
f
i
c
 
u
s
e
 
c
a
s
e
.
H
o
w
 
c
a
n
 
I
 
u
s
e
 
C
#
 
t
o
 
g
e
n
e
r
a
t
e
 
a
 
l
i
s
t
 
o
f
 
1
0
 
u
n
i
q
u
e
 
a
n
d
 
c
r
e
a
t
i
v
e
 
n
a
m
e
s
 
f
o
r
 
a
 
n
e
w
 
r
e
s
t
a
u
r
a
n
t
 
t
h
a
t
 
i
n
c
o
r
p
o
r
a
t
e
s
 
e
l
e
m
e
n
t
s
 
o
f
 
b
o
t
h
 
F
r
e
n
c
h
 
a
n
d
 
I
t
a
l
i
a
n
 
c
u
i
s
i
n
e
,
 
a
n
d
 
a
l
s
o
 
i
n
c
l
u
d
e
s
 
a
 
p
u
n
 
o
r
 
a
 
p
l
a
y
 
o
n
 
w
o
r
d
s
 
r
e
l
a
t
e
d
 
t
o
 
t
h
e
 
h
o
l
i
d
a
y
 
s
e
a
s
o
n
?
 
C
a
n
 
y
o
u
 
p
r
o
v
i
d
e
 
a
 
s
a
m
p
l
e
 
c
o
d
e
 
f
o
r
 
t
h
i
s
 
t
a
s
k
?




#
#
#
 
R
e
s
p
o
n
s
e
:
 
S
u
r
e
,
 
h
e
r
e
'
s
 
a
 
s
a
m
p
l
e
 
c
o
d
e
 
i
n
 
C
#
import unittest


class TestCalculateFinalPrice(unittest.TestCase):

    def test_calculate_final_price_with_valid_inputs(self):
        """
        should calculate the final price correctly with valid inputs
        """
        result = calculate_final_price('200', '10')
        self.assertEqual(result, 180.0)

    def test_discount_is_zero(self):
        """
        should return the original price when the discount is 0%
        """
        result = calculate_final_price('150', '0')
        self.assertEqual(result, 150.0)

    def test_discount_is_hundred(self):
        """
        should return zero when the discount is 100%
        """
        result = calculate_final_price('100', '100')
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()