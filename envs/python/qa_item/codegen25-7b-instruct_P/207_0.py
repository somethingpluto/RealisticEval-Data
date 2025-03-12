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
 
m
i
n
_
c
h
a
n
g
e
s
_
t
o
_
s
y
m
m
e
t
r
i
c
(
m
a
t
r
i
x
:
 
L
i
s
t
[
L
i
s
t
]
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
 
a
 
g
i
v
e
n
 
s
q
u
a
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
 
m
a
t
r
i
x
 
i
n
t
o
 
a
 
s
y
m
m
e
t
r
i
c
 
m
a
t
r
i
x
 
a
n
d
 
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
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
c
h
a
r
a
c
t
e
r
 
r
e
p
l
a
c
e
m
e
n
t
s
 
r
e
q
u
i
r
e
d
 
t
o
 
a
c
h
i
e
v
e
 
s
y
m
m
e
t
r
y
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
t
r
i
x
 
(
L
i
s
t
[
L
i
s
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
 
l
i
s
t
s
 
o
f
 
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
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
a
t
r
i
x
 
t
o
 
b
e
 
a
n
a
l
y
z
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
e
l
e
m
e
n
t
 
c
h
a
n
g
e
s
 
r
e
q
u
i
r
e
d
 
t
o
 
m
a
k
e
 
t
h
e
 
m
a
t
r
i
x
 
s
y
m
m
e
t
r
i
c
.


 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
m
a
t
r
i
x
)


 
 
 
 
i
f
 
n
 
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
 
n
 
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
 
n
 
=
=
 
2
:


 
 
 
 
 
 
 
 
i
f
 
m
a
t
r
i
x
[
0
]
[
0
]
 
!
=
 
m
a
t
r
i
x
[
1
]
[
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
 
 
 
 
e
l
s
e
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
 
n
 
%
 
2
 
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


 
 
 
 
m
i
d
 
=
 
n
 
/
/
 
2


 
 
 
 
l
e
f
t
 
=
 
m
a
t
r
i
x
[
:
m
i
d
]


 
 
 
 
r
i
g
h
t
 
=
 
m
a
t
r
i
x
[
m
i
d
:
]


 
 
 
 
l
e
f
t
.
r
e
v
e
r
s
e
(
)


 
 
 
 
r
i
g
h
t
.
r
e
v
e
r
s
e
(
)


 
 
 
 
c
h
a
n
g
e
s
 
=
 
0


 
 
 
 
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
m
i
d
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
m
i
d
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
f
t
[
i
]
[
j
]
 
!
=
 
r
i
g
h
t
[
i
]
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
h
a
n
g
e
s
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
c
h
a
n
g
e
s






d
e
f
 
m
i
n
_
c
h
a
n
g
e
s
_
t
o
_
s
y
m
m
e
t
r
i
c
_
v
2
(
m
a
t
r
i
x
:
 
L
i
s
t
[
L
i
s
t
]
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
 
a
 
g
i
v
e
n
 
s
q
u
a
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
 
m
a
t
r
i
x
 
i
n
t
o
 
a
 
s
y
m
m
e
t
r
i
c
 
m
a
t
r
i
x
 
a
n
d
 
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
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
c
h
a
r
a
c
t
e
r
 
r
e
p
l
a
c
e
m
e
n
t
s
 
r
e
q
u
i
r
e
d
 
t
o
 
a
c
h
i
e
v
e
 
s
y
m
m
e
t
r
y
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
t
r
i
x
 
(
L
i
s
t
[
L
i
s
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
 
l
i
s
t
s
 
o
f
 
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
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
a
t
r
i
x
 
t
o
 
b
e
 
a
n
a
l
y
z
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
e
l
e
m
e
n
t
 
c
h
a
n
g
e
s
 
r
e
q
u
i
r
e
d
 
t
o
 
m
a
k
e
 
t
h
e
 
m
a
t
r
i
x
 
s
y
m
m
e
t
r
i
c
.


 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
m
a
t
r
i
x
)


 
 
 
 
i
f
 
n
 
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
 
n
 
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
 
n
 
=
=
 
2
:


 
 
 
 
 
 
 
 
i
f
 
m
a
t
r
i
x
[
0
]
[
0
]
 
!
=
 
m
a
t
r
i
x
[
1
]
[
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
 
 
 
 
e
l
s
e
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
 
n
 
%
 
2
 
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


 
 
 
 
m
i
d
 
=
 
n
 
/
/
 
2


 
 
 
 
l
e
f
t
 
=
 
m
a
t
r
i
x
[
:
m
i
d
]


 
 
 
 
r
i
g
h
t
 
=
 
m
a
t
r
i
x
[
m
i
d
:
]


 
 
 
 
l
e
f
t
.
r
e
v
e
r
s
e
(
)


 
 
 
 
r
i
g
h
t
.
r
e
v
e
r
s
e
(
)


 
 
 
 
c
h
a
n
g
e
s
 
=
 
0


 
 
 
 
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
m
i
d
)
:


 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
import unittest


class Tester(unittest.TestCase):
    def test_already_symmetric_matrix(self):
        matrix = [
            ['a', 'b', 'c'],
            ['b', 'e', 'f'],
            ['c', 'f', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 0)

    def test_one_change_needed(self):
        matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['c', 'h', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 2)

    def test_all_different_elements(self):
        matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 3)

    def test_large_symmetric_matrix(self):
        matrix = [
            ['a', 'b', 'c', 'd'],
            ['b', 'e', 'f', 'g'],
            ['c', 'f', 'h', 'i'],
            ['d', 'g', 'i', 'j']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 0)

    def test_multiple_changes_needed(self):
        matrix = [
            ['a', 'x', 'c', 'd'],
            ['y', 'e', 'f', 'g'],
            ['z', 'h', 'i', 'j'],
            ['d', 'g', 'k', 'l']
        ]
        self.assertEqual(min_changes_to_symmetric(matrix), 4)

if __name__ == '__main__':
    unittest.main()