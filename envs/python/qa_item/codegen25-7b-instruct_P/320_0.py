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
 
g
e
t
_
a
r
r
a
y
_
a
v
e
r
a
g
e
(
a
r
r
a
y
:
 
L
i
s
t
[
f
l
o
a
t
]
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
 
t
h
e
 
a
v
e
r
a
g
e
 
o
f
 
a
n
 
a
r
r
a
y
 
o
f
 
n
u
m
b
e
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
a
y
 
(
L
i
s
t
[
f
l
o
a
t
]
)
:
 
A
 
l
i
s
t
 
o
f
 
n
u
m
b
e
r
s
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
a
v
e
r
a
g
e
 
i
s
 
t
o
 
b
e
 
c
a
l
c
u
l
a
t
e
d
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
 
a
v
e
r
a
g
e
 
(
m
e
a
n
)
 
o
f
 
t
h
e
 
a
r
r
a
y
'
s
 
e
l
e
m
e
n
t
s
,
 
o
r
 
f
l
o
a
t
(
'
n
a
n
'
)
 
i
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
e
m
p
t
y
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
r
r
a
y
)
 
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
 
f
l
o
a
t
(
'
n
a
n
'
)


 
 
 
 
r
e
t
u
r
n
 
s
u
m
(
a
r
r
a
y
)
 
/
 
l
e
n
(
a
r
r
a
y
)






d
e
f
 
g
e
t
_
a
r
r
a
y
_
m
e
d
i
a
n
(
a
r
r
a
y
:
 
L
i
s
t
[
f
l
o
a
t
]
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
 
t
h
e
 
m
e
d
i
a
n
 
o
f
 
a
n
 
a
r
r
a
y
 
o
f
 
n
u
m
b
e
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
a
y
 
(
L
i
s
t
[
f
l
o
a
t
]
)
:
 
A
 
l
i
s
t
 
o
f
 
n
u
m
b
e
r
s
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
m
e
d
i
a
n
 
i
s
 
t
o
 
b
e
 
c
a
l
c
u
l
a
t
e
d
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
 
m
e
d
i
a
n
 
o
f
 
t
h
e
 
a
r
r
a
y
'
s
 
e
l
e
m
e
n
t
s
,
 
o
r
 
f
l
o
a
t
(
'
n
a
n
'
)
 
i
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
e
m
p
t
y
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
r
r
a
y
)
 
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
 
f
l
o
a
t
(
'
n
a
n
'
)


 
 
 
 
a
r
r
a
y
.
s
o
r
t
(
)


 
 
 
 
i
f
 
l
e
n
(
a
r
r
a
y
)
 
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
 
(
a
r
r
a
y
[
l
e
n
(
a
r
r
a
y
)
 
/
/
 
2
 
-
 
1
]
 
+
 
a
r
r
a
y
[
l
e
n
(
a
r
r
a
y
)
 
/
/
 
2
]
)
 
/
 
2


 
 
 
 
r
e
t
u
r
n
 
a
r
r
a
y
[
l
e
n
(
a
r
r
a
y
)
 
/
/
 
2
]






d
e
f
 
g
e
t
_
a
r
r
a
y
_
m
o
d
e
(
a
r
r
a
y
:
 
L
i
s
t
[
f
l
o
a
t
]
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
 
t
h
e
 
m
o
d
e
 
o
f
 
a
n
 
a
r
r
a
y
 
o
f
 
n
u
m
b
e
r
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
a
y
 
(
L
i
s
t
[
f
l
o
a
t
]
)
:
 
A
 
l
i
s
t
 
o
f
 
n
u
m
b
e
r
s
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
m
o
d
e
 
i
s
 
t
o
 
b
e
 
c
a
l
c
u
l
a
t
e
d
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
 
m
o
d
e
 
o
f
 
t
h
e
 
a
r
r
a
y
'
s
 
e
l
e
m
e
n
t
s
,
 
o
r
 
f
l
o
a
t
(
'
n
a
n
'
)
 
i
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
e
m
p
t
y
 
o
r
 
c
o
n
t
a
i
n
s
 
n
o
 
d
u
p
l
i
c
a
t
e
s
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
r
r
a
y
)
 
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
 
f
l
o
a
t
(
'
n
a
n
'
)


 
 
 
 
f
r
e
q
 
=
 
{
}


 
 
 
 
f
o
r
 
n
u
m
 
i
n
 
a
r
r
a
y
:


 
 
 
 
 
 
 
 
i
f
 
n
u
m
 
i
n
 
f
r
e
q
:


 
 
 
 
 
 
 
 
 
 
 
 
f
r
e
q
[
n
u
m
]
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
f
r
e
q
[
n
u
m
]
 
=
 
1


 
 
 
 
m
a
x
_
f
r
e
q
 
=
 
m
a
x
(
f
r
e
q
.
v
a
l
u
e
s
(
)
)


 
 
 
 
i
f
 
m
a
x
_
f
r
e
q
 
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
 
f
l
o
a
t
(
'
n
a
n
'
)


 
 
 
 
r
e
t
u
r
n
 
m
a
x
(
(
n
u
m
 
f
o
r
 
n
u
m
 
i
n
 
f
r
e
q
 
i
f
 
f
r
e
q
[
n
u
m
]
 
=
=
 
m
a
x
_
f
r
e
q
)
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
f
r
e
q
[
x
]
)






import unittest


class TestGetArrayAverage(unittest.TestCase):

    def test_average_of_positive_integers(self):
        result = get_array_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)  # (1 + 2 + 3 + 4 + 5) / 5 = 3

    def test_average_with_negative_numbers(self):
        result = get_array_average([-1, -2, -3, -4, -5])
        self.assertEqual(result, -3)  # (-1 + -2 + -3 + -4 + -5) / 5 = -3

    def test_average_with_mixed_numbers(self):
        result = get_array_average([1, -1, 2, -2, 3, -3])
        self.assertEqual(result, 0)  # (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0

    def test_empty_array(self):
        result = get_array_average([])
        self.assertTrue(math.isnan(result))  # Division by zero, expected result is NaN

    def test_single_element_array(self):
        result = get_array_average([7])
        self.assertEqual(result, 7)  # The average of [7] is 7

if __name__ == '__main__':
    unittest.main()