i
m
p
o
r
t
 
m
a
t
h


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
 
p
a
s
c
a
l
_
t
r
i
a
n
g
l
e
_
r
o
w
(
i
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
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
t
h
e
 
i
t
h
 
r
o
w
 
o
f
 
P
a
s
c
a
l
'
s
 
T
r
i
a
n
g
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
 
(
i
n
t
)
:
 
R
o
w
 
i
n
d
e
x
 
(
0
-
i
n
d
e
x
e
d
)




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
l
i
s
t
 
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
 
i
t
h
 
r
o
w
 
o
f
 
P
a
s
c
a
l
'
s
 
T
r
i
a
n
g
l
e


 
 
 
 
"
"
"


 
 
 
 
i
f
 
i
 
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
 
[
1
]


 
 
 
 
e
l
i
f
 
i
 
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
 
[
1
,
 
1
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
o
w
 
=
 
[
1
]
 
*
 
(
i
 
+
 
1
)


 
 
 
 
 
 
 
 
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
1
,
 
i
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
[
j
]
 
=
 
p
a
s
c
a
l
_
t
r
i
a
n
g
l
e
_
r
o
w
(
i
 
-
 
1
)
[
j
 
-
 
1
]
 
+
 
p
a
s
c
a
l
_
t
r
i
a
n
g
l
e
_
r
o
w
(
i
 
-
 
1
)
[
j
]


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
o
w






d
e
f
 
p
a
s
c
a
l
_
t
r
i
a
n
g
l
e
(
n
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
L
i
s
t
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
t
h
e
 
f
i
r
s
t
 
n
 
r
o
w
s
 
o
f
 
P
a
s
c
a
l
'
s
 
T
r
i
a
n
g
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
r
o
w
s
 
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




 
 
 
 
R
e
t
u
r
n
s
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
 
f
i
r
s
t
 
n
 
r
o
w
s
 
o
f
 
P
a
s
c
a
l
'
s
 
T
r
i
a
n
g
l
e


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
[
p
a
s
c
a
l
_
t
r
i
a
n
g
l
e
_
r
o
w
(
i
)
 
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
n
)
]






d
e
f
 
f
a
c
t
o
r
i
a
l
(
n
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
a
c
t
o
r
i
a
l
 
o
f
 
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
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
 
w
h
o
s
e
 
f
a
c
t
o
r
i
a
l
 
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
 
f
a
c
t
o
r
i
a
l
 
o
f
 
n


 
 
 
 
"
"
"


 
 
 
 
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
 
n
 
*
 
f
a
c
t
o
r
i
a
l
(
n
 
-
 
1
)






d
e
f
 
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
n
:
 
i
n
t
,
 
k
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
 
k
-
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
 
o
f
 
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
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
 
o
b
j
e
c
t
s


 
 
 
 
 
 
 
 
k
 
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
 
o
b
j
e
c
t
s
 
t
o
 
c
h
o
o
s
e




 
 
 
 
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
 
k
-
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
 
o
f
 
n


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
a
c
t
o
r
i
a
l
(
n
)
 
/
 
(
f
a
c
t
o
r
i
a
l
(
k
)
 
*
 
f
a
c
t
o
r
i
a
l
(
n
 
-
 
k
)
)
)






d
e
f
 
p
e
r
m
u
t
a
t
i
o
n
(
n
:
 
i
n
t
,
 
k
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
 
k
-
p
e
r
m
u
t
a
t
i
o
n
 
o
f
 
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
T
h
e
import unittest


class TestPascalTriangleRow(unittest.TestCase):

    def test_row_0(self):
        """ Test the 0th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(0), [1])

    def test_row_1(self):
        """ Test the 1st row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(1), [1, 1])

    def test_row_2(self):
        """ Test the 2nd row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(2), [1, 2, 1])

    def test_row_3(self):
        """ Test the 3rd row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(3), [1, 3, 3, 1])

    def test_row_4(self):
        """ Test the 4th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(4), [1, 4, 6, 4, 1])

    def test_row_5(self):
        """ Test the 5th row of Pascal's Triangle. """
        self.assertEqual(pascal_triangle_row(5), [1, 5, 10, 10, 5, 1])

if __name__ == '__main__':
    unittest.main()