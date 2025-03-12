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
 
n
e
x
t
_
g
r
e
a
t
e
s
t
_
l
e
t
t
e
r
(
l
e
t
t
e
r
s
:
 
L
i
s
t
[
s
t
r
]
,
 
t
a
r
g
e
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


 
 
 
 
F
i
n
d
s
 
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
 
t
h
e
 
s
m
a
l
l
e
s
t
 
l
e
t
t
e
r
 
i
n
 
a
 
s
o
r
t
e
d
 
a
r
r
a
y
 
t
h
a
t
 
i
s
 
l
a
r
g
e
r
 
t
h
a
n
 
t
h
e
 
g
i
v
e
n
 
t
a
r
g
e
t
 
l
e
t
t
e
r
.


 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
 
i
s
 
g
r
e
a
t
e
r
 
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
 
a
l
l
 
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
 
a
r
r
a
y
,
 
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
 
r
e
t
u
r
n
s


 
 
 
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
e
t
t
e
r
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
A
 
s
o
r
t
e
d
 
a
r
r
a
y
 
o
f
 
l
e
t
t
e
r
s
 
(
a
s
s
u
m
e
d
 
t
o
 
b
e
 
u
n
i
q
u
e
 
a
n
d
 
l
o
w
e
r
c
a
s
e
)
.


 
 
 
 
 
 
 
 
t
a
r
g
e
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
 
t
a
r
g
e
t
 
l
e
t
t
e
r
 
t
o
 
f
i
n
d
 
t
h
e
 
n
e
x
t
 
g
r
e
a
t
e
s
t
 
l
e
t
t
e
r
 
f
o
r
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
 
s
m
a
l
l
e
s
t
 
l
e
t
t
e
r
 
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
 
i
s
 
l
a
r
g
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
.


 
 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
i
s
 
g
r
e
a
t
e
r
 
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
 
a
l
l
 
l
e
t
t
e
r
s
,
 
r
e
t
u
r
n
s
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
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
.


 
 
 
 
"
"
"


 
 
 
 
#
 
E
d
g
e
 
c
a
s
e
:
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
i
s
 
g
r
e
a
t
e
r
 
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
 
a
l
l
 
l
e
t
t
e
r
s
,
 
r
e
t
u
r
n
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
.


 
 
 
 
i
f
 
t
a
r
g
e
t
 
>
=
 
l
e
t
t
e
r
s
[
-
1
]
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
l
e
t
t
e
r
s
[
0
]




 
 
 
 
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
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
.


 
 
 
 
l
e
f
t
,
 
r
i
g
h
t
 
=
 
0
,
 
l
e
n
(
l
e
t
t
e
r
s
)
 
-
 
1


 
 
 
 
w
h
i
l
e
 
l
e
f
t
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
m
i
d
 
=
 
(
l
e
f
t
 
+
 
r
i
g
h
t
)
 
/
/
 
2


 
 
 
 
 
 
 
 
i
f
 
l
e
t
t
e
r
s
[
m
i
d
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
 
l
e
t
t
e
r
s
[
m
i
d
 
+
 
1
]


 
 
 
 
 
 
 
 
e
l
i
f
 
l
e
t
t
e
r
s
[
m
i
d
]
 
<
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
 
 
 
 
l
e
f
t
 
=
 
m
i
d
 
+
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
i
g
h
t
 
=
 
m
i
d
 
-
 
1




 
 
 
 
#
 
I
f
 
w
e
 
g
e
t
 
h
e
r
e
,
 
i
t
 
m
e
a
n
s
 
t
h
a
t
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
 
i
s
 
n
o
t
 
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
.


 
 
 
 
#
 
I
n
 
t
h
i
s
 
c
a
s
e
,
 
w
e
 
r
e
t
u
r
n
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
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
.


 
 
 
 
r
e
t
u
r
n
 
l
e
t
t
e
r
s
[
0
]






d
e
f
 
n
e
x
t
_
s
m
a
l
l
e
s
t
_
l
e
t
t
e
r
(
l
e
t
t
e
r
s
:
 
L
i
s
t
[
s
t
r
]
,
 
t
a
r
g
e
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


 
 
 
 
F
i
n
d
s
 
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
 
l
e
t
t
e
r
 
i
n
 
a
 
s
o
r
t
e
d
 
a
r
r
a
y
 
t
h
a
t
 
i
s
 
s
m
a
l
l
e
r
 
t
h
a
n
 
t
h
e
 
g
i
v
e
n
 
t
a
r
g
e
t
 
l
e
t
t
e
r
.


 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
 
i
s
 
s
m
a
l
l
e
r
 
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
 
a
l
l
 
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
 
a
r
r
a
y
,
 
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
 
r
e
t
u
r
n
s


 
 
 
 
t
h
e
 
l
a
s
t
 
l
e
t
t
e
r
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
e
t
t
e
r
s
 
(
L
i
s
t
[
s
t
r
]
)
:
 
A
 
s
o
r
t
e
d
 
a
r
r
a
y
 
o
f
 
l
e
t
t
e
r
s
 
(
a
s
s
u
m
e
d
 
t
o
 
b
e
 
u
n
i
q
u
e
 
a
n
d
 
l
o
w
e
r
c
a
s
e
)
.


 
 
 
 
 
 
 
 
t
a
r
g
e
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
 
t
a
r
g
e
t
 
l
e
t
t
e
r
 
t
o
 
f
i
n
d
 
t
h
e
 
n
e
x
t
 
s
m
a
l
l
e
s
t
 
l
e
t
t
e
r
 
f
o
r
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
 
l
a
r
g
e
s
t
 
l
e
t
t
e
r
 
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
 
i
s
 
s
m
a
l
l
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
t
t
e
r
.


 
 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
t
a
r
g
e
t
 
i
s
 
s
m
a
l
l
e
r
 
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
 
a
l
l
 
l
e
t
t
e
r
s
,
 
r
e
t
u
r
n
s
 
t
h
e
 
l
a
s
t
 
l
e
t
t
e
r
import unittest


class TestNextGreatestLetter(unittest.TestCase):

    def test_target_greater_than_all_letters(self):
        letters = ['c', 'f', 'j']
        target = 'j'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'c')  # Expected output: 'c'

    def test_typical_input(self):
        letters = ['c', 'f', 'j']
        target = 'a'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'c')  # Expected output: 'c'

    def test_edge_case_between_two_letters(self):
        letters = ['c', 'f', 'j']
        target = 'd'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'f')  # Expected output: 'f'

    def test_target_equal_to_largest_letter(self):
        letters = ['a', 'b', 'c', 'd']
        target = 'd'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'a')  # Expected output: 'a'

    def test_single_letter_array(self):
        letters = ['a']
        target = 'z'
        result = next_greatest_letter(letters, target)
        self.assertEqual(result, 'a')  # Expected output: 'a'
if __name__ == '__main__':
    unittest.main()