d
e
f
 
h
i
d
e
_
b
a
n
k
_
a
c
c
o
u
n
t
(
a
c
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
H
i
d
e
s
 
t
h
e
 
s
e
n
s
i
t
i
v
e
 
p
a
r
t
 
o
f
 
a
 
b
a
n
k
 
a
c
c
o
u
n
t
 
n
u
m
b
e
r
 
w
i
t
h
 
1
7
 
d
i
g
i
t
s
,
 
s
h
o
w
i
n
g
 
o
n
l
y
 
t
h
e
 
l
a
s
t
 
4
 
c
h
a
r
a
c
t
e
r
s
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
:


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
*
*
*
*
4
5
6
7




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
c
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
 
b
a
n
k
 
a
c
c
o
u
n
t
 
n
u
m
b
e
r
 
t
o
 
h
i
d
e
.
 
T
h
i
s
 
m
u
s
t
 
b
e
 
e
x
a
c
t
l
y
 
1
7
 
c
h
a
r
a
c
t
e
r
s
 
l
o
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
b
a
n
k
 
a
c
c
o
u
n
t
 
n
u
m
b
e
r
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
p
a
r
t
 
h
i
d
d
e
n
,
 
f
o
r
m
a
t
t
e
d
 
a
s
 
"
*
*
*
*
X
X
X
X
"
,


 
 
 
 
 
 
 
 
 
 
 
 
 
w
h
e
r
e
 
"
X
X
X
X
"
 
a
r
e
 
t
h
e
 
l
a
s
t
 
f
o
u
r
 
d
i
g
i
t
s
 
o
f
 
t
h
e
 
a
c
c
o
u
n
t
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
 
a
c
c
o
u
n
t
 
n
u
m
b
e
r
 
i
s
 
n
o
t
 
e
x
a
c
t
l
y
 
1
7
 
c
h
a
r
a
c
t
e
r
s
 
l
o
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
a
c
c
o
u
n
t
)
 
!
=
 
1
7
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
B
a
n
k
 
a
c
c
o
u
n
t
 
n
u
m
b
e
r
 
m
u
s
t
 
b
e
 
e
x
a
c
t
l
y
 
1
7
 
c
h
a
r
a
c
t
e
r
s
 
l
o
n
g
.
"
)




 
 
 
 
r
e
t
u
r
n
 
f
"
*
*
*
*
{
a
c
c
o
u
n
t
[
-
4
:
]
}
"






d
e
f
 
h
i
d
e
_
c
r
e
d
i
t
_
c
a
r
d
(
c
a
r
d
_
n
u
m
b
e
r
:
 
s
t
r
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


 
 
 
 
H
i
d
e
s
 
t
h
e
 
s
e
n
s
i
t
i
v
e
 
p
a
r
t
 
o
f
 
a
 
c
r
e
d
i
t
 
c
a
r
d
 
n
u
m
b
e
r
 
w
i
t
h
 
1
6
 
o
r
 
m
o
r
e
 
d
i
g
i
t
s
,
 
s
h
o
w
i
n
g
 
o
n
l
y
 
t
h
e
 
l
a
s
t
 
4
 
a
n
d
 
5
 
c
h
a
r
a
c
t
e
r
s
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
:


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
*
*
*
*
3
4
5
6




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
a
r
d
_
n
u
m
b
e
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
 
c
r
e
d
i
t
 
c
a
r
d
 
n
u
m
b
e
r
 
t
o
 
h
i
d
e
.
 
T
h
i
s
 
m
u
s
t
 
b
e
 
e
x
a
c
t
l
y
 
1
6
 
o
r
 
m
o
r
e
 
c
h
a
r
a
c
t
e
r
s
 
l
o
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
r
e
d
i
t
 
c
a
r
d
 
n
u
m
b
e
r
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
p
a
r
t
 
h
i
d
d
e
n
,
 
f
o
r
m
a
t
t
e
d
 
a
s
 
"
*
*
*
*
X
X
X
X
"
,


 
 
 
 
 
 
 
 
 
 
 
 
 
w
h
e
r
e
 
"
X
X
X
X
"
 
a
r
e
 
t
h
e
 
l
a
s
t
 
f
o
u
r
 
a
n
d
 
f
i
v
e
 
d
i
g
i
t
s
 
o
f
 
t
h
e
 
c
a
r
d
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
 
c
a
r
d
 
n
u
m
b
e
r
 
i
s
 
n
o
t
 
e
x
a
c
t
l
y
 
1
6
 
o
r
 
m
o
r
e
 
c
h
a
r
a
c
t
e
r
s
 
l
o
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
c
a
r
d
_
n
u
m
b
e
r
)
 
<
 
1
6
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
C
r
e
d
i
t
 
c
a
r
d
 
n
u
m
b
e
r
 
m
u
s
t
 
b
e
 
e
x
a
c
t
l
y
 
1
6
 
o
r
 
m
o
r
e
 
c
h
a
r
a
c
t
e
r
s
 
l
o
n
g
.
"
)




 
 
 
 
r
e
t
u
r
n
 
f
"
*
*
*
*
{
c
a
r
d
_
n
u
m
b
e
r
[
-
4
:
]
}
"


import unittest


class TestHideBankAccount(unittest.TestCase):
    def test_should_return_hidden_part_for_valid_account(self):
        self.assertEqual(hide_bank_account('12345678901234567'), '****4567')

    def test_should_return_hidden_part_for_another_valid_account(self):
        self.assertEqual(hide_bank_account('98765432109876543'), '****6543')

    def test_should_return_hidden_part_for_yet_another_valid_account(self):
        self.assertEqual(hide_bank_account('11111111111111100'), '****1100')

    def test_should_throw_error_for_shorter_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('1234567890123456')

    def test_should_throw_error_for_longer_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('123456789012345678')

    def test_should_throw_error_for_empty_account(self):
        with self.assertRaises(Exception):
            hide_bank_account('')

if __name__ == '__main__':
    unittest.main()