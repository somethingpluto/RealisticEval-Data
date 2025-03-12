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
 
L
i
s
t






d
e
f
 
t
w
o
_
s
u
m
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
,
 
t
a
r
g
e
t
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


 
 
 
 
F
i
n
d
s
 
t
w
o
 
i
n
d
i
c
e
s
 
o
f
 
n
u
m
b
e
r
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
t
h
a
t
 
s
u
m
 
u
p
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
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
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
e
r
s
.


 
 
 
 
 
 
 
 
t
a
r
g
e
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
 
t
a
r
g
e
t
 
s
u
m
 
v
a
l
u
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


 
 
 
 
 
 
 
 
l
i
s
t
[
i
n
t
]
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
 
t
h
e
 
i
n
d
i
c
e
s
 
o
f
 
t
h
e
 
t
w
o
 
n
u
m
b
e
r
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
 
n
o
 
s
u
c
h
 
i
n
d
i
c
e
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
n
u
m
s
)
)
:


 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
i
 
+
 
1
,
 
l
e
n
(
n
u
m
s
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
n
u
m
s
[
i
]
 
+
 
n
u
m
s
[
j
]
 
=
=
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
i
,
 
j
]


 
 
 
 
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
N
o
 
s
u
c
h
 
i
n
d
i
c
e
s
 
f
o
u
n
d
.
"
)






d
e
f
 
t
w
o
_
s
u
m
_
h
a
s
h
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
,
 
t
a
r
g
e
t
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
t
w
o
 
i
n
d
i
c
e
s
 
o
f
 
n
u
m
b
e
r
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
t
h
a
t
 
s
u
m
 
u
p
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
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
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
e
r
s
.


 
 
 
 
 
 
 
 
t
a
r
g
e
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
 
t
a
r
g
e
t
 
s
u
m
 
v
a
l
u
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


 
 
 
 
 
 
 
 
l
i
s
t
[
i
n
t
]
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
 
t
h
e
 
i
n
d
i
c
e
s
 
o
f
 
t
h
e
 
t
w
o
 
n
u
m
b
e
r
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
 
n
o
 
s
u
c
h
 
i
n
d
i
c
e
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
h
a
s
h
_
m
a
p
 
=
 
{
}


 
 
 
 
f
o
r
 
i
,
 
n
u
m
 
i
n
 
e
n
u
m
e
r
a
t
e
(
n
u
m
s
)
:


 
 
 
 
 
 
 
 
c
o
m
p
l
e
m
e
n
t
 
=
 
t
a
r
g
e
t
 
-
 
n
u
m


 
 
 
 
 
 
 
 
i
f
 
c
o
m
p
l
e
m
e
n
t
 
i
n
 
h
a
s
h
_
m
a
p
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
h
a
s
h
_
m
a
p
[
c
o
m
p
l
e
m
e
n
t
]
,
 
i
]


 
 
 
 
 
 
 
 
h
a
s
h
_
m
a
p
[
n
u
m
]
 
=
 
i


 
 
 
 
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
N
o
 
s
u
c
h
 
i
n
d
i
c
e
s
 
f
o
u
n
d
.
"
)






d
e
f
 
t
w
o
_
s
u
m
_
b
r
u
t
e
_
f
o
r
c
e
(
n
u
m
s
:
 
L
i
s
t
[
i
n
t
]
,
 
t
a
r
g
e
t
:
 
i
n
t
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
t
w
o
 
i
n
d
i
c
e
s
 
o
f
 
n
u
m
b
e
r
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
t
h
a
t
 
s
u
m
 
u
p
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
s
 
(
L
i
s
t
[
i
n
t
]
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
 
a
r
r
a
y
 
o
f
 
i
n
t
e
g
e
r
s
.


 
 
 
 
 
 
 
 
t
a
r
g
e
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
 
t
a
r
g
e
t
 
s
u
m
 
v
a
l
u
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


 
 
 
 
 
 
 
 
l
i
s
t
[
i
n
t
]
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
 
t
h
e
 
i
n
d
i
c
e
s
 
o
f
 
t
h
e
 
t
w
o
 
n
u
m
b
e
r
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
 
n
o
 
s
u
c
h
 
i
n
d
i
c
e
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
n
u
m
s
)
)
:


 
 
 
 
 
 
 
 
f
o
r
import unittest


class TestAnswer(unittest.TestCase):
    def test_valid_pair(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]  # 2 + 7 = 9
        self.assertEqual(expected, two_sum(nums, target))

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]  # -3 + -5 = -8
        self.assertEqual(expected, two_sum(nums, target))

    def test_zero_sum(self):
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]  # 0 + 0 = 0
        self.assertEqual(expected, two_sum(nums, target))

    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        with self.assertRaises(Exception):
            two_sum(nums, target)

    def test_same_number_twice(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]  # 3 + 3 = 6
        self.assertEqual(expected, two_sum(nums, target))

    def test_large_numbers(self):
        nums = [2147483647, -2147483648, 0, 1]
        target = 1
        expected = [2, 3]  # 0 + 1 = 1
        self.assertEqual(expected, two_sum(nums, target))
if __name__ == '__main__':
    unittest.main()