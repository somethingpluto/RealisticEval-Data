d
e
f
 
f
i
n
d
_
p
r
i
m
e
s
(
l
o
w
e
r
_
b
o
u
n
d
:
 
i
n
t
,
 
u
p
p
e
r
_
b
o
u
n
d
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"
F
i
n
d
 
a
l
l
 
p
r
i
m
e
 
n
u
m
b
e
r
s
 
w
i
t
h
i
n
 
a
 
s
p
e
c
i
f
i
e
d
 
r
a
n
g
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
w
e
r
_
b
o
u
n
d
 
(
i
n
t
)
:
 
T
h
e
 
l
o
w
e
r
 
l
i
m
i
t
 
o
f
 
t
h
e
 
r
a
n
g
e
 
(
i
n
c
l
u
s
i
v
e
)
.


 
 
 
 
 
 
 
 
u
p
p
e
r
_
b
o
u
n
d
 
(
i
n
t
)
:
 
T
h
e
 
u
p
p
e
r
 
l
i
m
i
t
 
o
f
 
t
h
e
 
r
a
n
g
e
 
(
i
n
c
l
u
s
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
p
r
i
m
e
 
n
u
m
b
e
r
s
 
w
i
t
h
i
n
 
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
 
r
a
n
g
e
.


 
 
 
 
"
"
"


 
 
 
 
p
r
i
m
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
n
u
m
 
i
n
 
r
a
n
g
e
(
l
o
w
e
r
_
b
o
u
n
d
,
 
u
p
p
e
r
_
b
o
u
n
d
 
+
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
p
r
i
m
e
(
n
u
m
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
m
e
s
.
a
p
p
e
n
d
(
n
u
m
)


 
 
 
 
r
e
t
u
r
n
 
p
r
i
m
e
s


`
`
`




T
h
e
 
`
i
s
_
p
r
i
m
e
(
)
`
 
f
u
n
c
t
i
o
n
 
c
h
e
c
k
s
 
w
h
e
t
h
e
r
 
a
 
g
i
v
e
n
 
n
u
m
b
e
r
 
i
s
 
p
r
i
m
e
 
o
r
 
n
o
t
.
 
I
t
 
w
o
r
k
s
 
b
y
 
c
h
e
c
k
i
n
g
 
a
l
l
 
n
u
m
b
e
r
s
 
f
r
o
m
 
2
 
t
o
 
t
h
e
 
s
q
u
a
r
e
 
r
o
o
t
 
o
f
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
 
(
r
o
u
n
d
e
d
 
u
p
 
t
o
 
t
h
e
 
n
e
a
r
e
s
t
 
i
n
t
e
g
e
r
)
 
a
n
d
 
c
h
e
c
k
i
n
g
 
i
f
 
a
n
y
 
o
f
 
t
h
e
m
 
d
i
v
i
d
e
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
 
e
v
e
n
l
y
.
 
I
f
 
n
o
n
e
 
o
f
 
t
h
e
m
 
d
o
,
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
 
i
s
 
p
r
i
m
e
.




T
h
e
 
`
f
i
n
d
_
p
r
i
m
e
s
(
)
`
 
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
 
i
n
 
a
 
l
o
w
e
r
 
b
o
u
n
d
 
a
n
d
 
a
n
 
u
p
p
e
r
 
b
o
u
n
d
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
p
r
i
m
e
 
n
u
m
b
e
r
s
 
w
i
t
h
i
n
 
t
h
a
t
 
r
a
n
g
e
.
 
I
t
 
w
o
r
k
s
 
b
y
 
i
t
e
r
a
t
i
n
g
 
o
v
e
r
 
a
l
l
 
n
u
m
b
e
r
s
 
w
i
t
h
i
n
 
t
h
e
 
r
a
n
g
e
 
a
n
d
 
c
h
e
c
k
i
n
g
 
i
f
 
t
h
e
y
 
a
r
e
 
p
r
i
m
e
 
u
s
i
n
g
 
t
h
e
 
`
i
s
_
p
r
i
m
e
(
)
`
 
f
u
n
c
t
i
o
n
.
 
I
f
 
a
 
n
u
m
b
e
r
 
i
s
 
p
r
i
m
e
,
 
i
t
 
i
s
 
a
d
d
e
d
 
t
o
 
t
h
e
 
`
p
r
i
m
e
s
`
 
l
i
s
t
.
 
F
i
n
a
l
l
y
,
 
t
h
e
 
`
p
r
i
m
e
s
`
 
l
i
s
t
 
i
s
 
r
e
t
u
r
n
e
d
.




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
 
`
m
a
t
h
.
s
q
r
t
(
)
`
 
f
u
n
c
t
i
o
n
 
i
s
 
u
s
e
d
 
t
o
 
c
a
l
c
u
l
a
t
e
 
t
h
e
 
s
q
u
a
r
e
 
r
o
o
t
 
o
f
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
.
 
T
h
i
s
 
i
s
 
b
e
c
a
u
s
e
 
t
h
e
 
s
q
u
a
r
e
 
r
o
o
t
 
o
f
 
a
 
n
u
m
b
e
r
 
i
s
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
t
h
a
t
 
i
s
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
t
h
e
 
s
q
u
a
r
e
 
r
o
o
t
 
o
f
 
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
 
n
u
m
b
e
r
.
 
F
o
r
 
e
x
a
m
p
l
e
,
 
t
h
e
 
s
q
u
a
r
e
 
r
o
o
t
 
o
f
 
1
6
 
i
s
 
4
,
 
b
u
t
 
t
h
e
 
l
a
r
g
e
s
t
 
i
n
t
e
g
e
r
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
4
 
t
h
a
t
 
i
s
 
a
l
s
o
 
l
e
s
s
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
1
6
 
i
s
 
4
.
 
T
h
e
r
e
f
o
r
e
,
 
`
m
a
t
h
.
s
q
r
t
(
1
6
)
`
 
r
e
t
u
r
n
s
 
4
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
 
a
l
l
 
p
o
s
s
i
b
l
e
 
c
o
m
b
i
n
a
t
i
o
n
s
 
o
f
 
t
h
e
 
l
e
t
t
e
r
s
 
i
n
 
t
h
e
 
w
o
r
d
 
"
f
o
o
t
"
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
s
e
n
t
e
n
c
e
 
"
I
 
w
a
n
t
 
t
o
 
t
a
k
e
 
m
y
 
f
o
o
t
"
 
u
s
i
n
g
 
t
h
e
 
f
o
r
m
u
l
a
 
f
o
r
 
g
e
n
e
r
a
t
i
n
g
 
c
o
m
b
i
n
a
t
i
o
n
s
?


H
e
r
e
'
s
 
t
h
e
 
f
o
r
m
u
l
a
:


n
!
 
/
 
r
!
(
n
-
r
)
!


w
h
e
r
e
 
n
 
i
s
 
t
h
e
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
l
e
t
t
e
r
s
 
i
n
 
t
h
e
 
w
o
r
d
 
"
f
o
o
t
"
 
(
e
.
g
.
 
4
)
 
a
n
d
 
r
 
i
s
 
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
 
l
e
t
t
e
r
s
 
i
n
 
e
a
c
h
 
g
e
n
e
r
a
t
e
d
 
c
o
m
b
i
n
a
t
i
o
n
 
(
e
.
g
.
 
4
 
c
o
m
b
i
n
a
t
i
o
n
s
 
f
o
r
 
a
 
4
-
l
e
t
t
e
r
 
w
o
r
d
)
.


H
e
r
e
'
s
 
t
h
e
 
C
#
import unittest


class TestFindPrimesInRange(unittest.TestCase):
    def test_find_primes_in_range(self):
        expected = [2, 3, 5, 7, 11]
        self.assertEqual(find_primes(1, 12), expected, "Check primes between 1 and 12")

    def test_find_primes_single_prime(self):
        expected = [29]
        self.assertEqual(find_primes(29, 29), expected, "Check single prime number")

    def test_find_primes_in_big_range(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes(1, 100), expected, "Check primes between 1 and 100")

    def test_find_primes_no_primes(self):
        expected = []
        self.assertEqual(find_primes(0, 1), expected, "Check range with no primes")

if __name__ == '__main__':
    unittest.main()