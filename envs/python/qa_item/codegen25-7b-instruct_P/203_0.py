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
 
r
e
v
e
r
s
e
_
r
a
n
g
e
(
v
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
 
a
:
 
i
n
t
,
 
b
:
 
i
n
t
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
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
s
 
i
n
 
t
h
e
 
l
i
s
t
 
v
 
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
 
[
a
,
 
b
]
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
 
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
 
R
e
f
e
r
e
n
c
e
 
t
o
 
t
h
e
 
l
i
s
t
 
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
 
t
o
 
b
e
 
m
o
d
i
f
i
e
d
.


 
 
 
 
 
 
 
 
a
 
(
i
n
t
)
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
i
n
d
e
x
 
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
 
t
o
 
b
e
 
r
e
v
e
r
s
e
d
.


 
 
 
 
 
 
 
 
b
 
(
i
n
t
)
:
 
T
h
e
 
e
n
d
i
n
g
 
i
n
d
e
x
 
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
 
t
o
 
b
e
 
r
e
v
e
r
s
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




 
 
 
 
"
"
"


 
 
 
 
i
f
 
a
 
<
 
0
 
o
r
 
a
 
>
=
 
l
e
n
(
v
)
 
o
r
 
b
 
<
 
0
 
o
r
 
b
 
>
=
 
l
e
n
(
v
)
 
o
r
 
a
 
>
 
b
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n


 
 
 
 
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
a
,
 
(
a
 
+
 
(
b
 
-
 
a
 
+
 
1
)
 
/
/
 
2
)
)
:


 
 
 
 
 
 
 
 
v
[
i
]
,
 
v
[
b
 
-
 
i
 
+
 
a
]
 
=
 
v
[
b
 
-
 
i
 
+
 
a
]
,
 
v
[
i
]






d
e
f
 
r
e
v
e
r
s
e
_
a
l
l
(
v
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
e
r
 
o
f
 
a
l
l
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
l
i
s
t
 
v
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
 
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
 
R
e
f
e
r
e
n
c
e
 
t
o
 
t
h
e
 
l
i
s
t
 
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
 
t
o
 
b
e
 
m
o
d
i
f
i
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




 
 
 
 
"
"
"


 
 
 
 
r
e
v
e
r
s
e
_
r
a
n
g
e
(
v
,
 
0
,
 
l
e
n
(
v
)
 
-
 
1
)






d
e
f
 
r
e
v
e
r
s
e
_
s
u
b
l
i
s
t
(
v
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
 
a
:
 
i
n
t
,
 
b
:
 
i
n
t
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
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
s
 
i
n
 
t
h
e
 
l
i
s
t
 
v
 
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
 
s
u
b
l
i
s
t
 
[
a
,
 
b
]
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
 
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
 
R
e
f
e
r
e
n
c
e
 
t
o
 
t
h
e
 
l
i
s
t
 
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
 
t
o
 
b
e
 
m
o
d
i
f
i
e
d
.


 
 
 
 
 
 
 
 
a
 
(
i
n
t
)
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
i
n
d
e
x
 
o
f
 
t
h
e
 
s
u
b
l
i
s
t
 
t
o
 
b
e
 
r
e
v
e
r
s
e
d
.


 
 
 
 
 
 
 
 
b
 
(
i
n
t
)
:
 
T
h
e
 
e
n
d
i
n
g
 
i
n
d
e
x
 
o
f
 
t
h
e
 
s
u
b
l
i
s
t
 
t
o
 
b
e
 
r
e
v
e
r
s
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




 
 
 
 
"
"
"


 
 
 
 
i
f
 
a
 
<
 
0
 
o
r
 
a
 
>
=
 
l
e
n
(
v
)
 
o
r
 
b
 
<
 
0
 
o
r
 
b
 
>
=
 
l
e
n
(
v
)
 
o
r
 
a
 
>
 
b
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n


 
 
 
 
r
e
v
e
r
s
e
_
r
a
n
g
e
(
v
,
 
a
,
 
b
)






d
e
f
 
r
e
v
e
r
s
e
_
k
_
g
r
o
u
p
(
v
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
 
k
:
 
i
n
t
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


 
 
 
 
R
e
v
e
r
s
e
 
t
h
e
 
o
r
d
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
s
 
i
n
 
t
h
e
 
l
i
s
t
 
v
 
w
i
t
h
i
n
 
g
r
o
u
p
s
 
o
f
 
k
 
e
l
e
m
e
n
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
 
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
 
R
e
f
e
r
e
n
c
e
 
t
o
 
t
h
e
 
l
i
s
t
 
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
 
t
o
 
b
e
 
m
o
d
i
f
i
e
d
.


 
 
 
 
 
 
 
 
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
 
s
i
z
e
 
o
f
 
t
h
e
 
g
r
o
u
p
s
 
t
o
import unittest


class Tester(unittest.TestCase):

    def test_reverse_entire_vector(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, 0, 4)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(v, expected)

    def test_reverse_subrange_in_the_middle(self):
        v = [1, 2, 3, 4, 5, 6, 7, 8]
        reverse_range(v, 2, 5)
        expected = [1, 2, 6, 5, 4, 3, 7, 8]
        self.assertEqual(v, expected)

    def test_reverse_single_element_range(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, 2, 2)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(v, expected)

    def test_reverse_range_with_invalid_indices(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, -1, 3)  # Invalid start index
        expected = [1, 2, 3, 4, 5]  # No change
        self.assertEqual(v, expected)

    def test_reverse_range_at_end_of_vector(self):
        v = [1, 2, 3, 4, 5, 6]
        reverse_range(v, 3, 5)
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(v, expected)

if __name__ == '__main__':
    unittest.main()