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
r
e
m
o
v
a
l
s
_
t
o
_
m
a
k
e
_
u
n
i
q
u
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


 
 
 
 
G
i
v
e
n
 
a
n
 
i
n
t
e
g
e
r
 
a
r
r
a
y
,
 
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
 
e
l
e
m
e
n
t
s
 
t
o
 
d
e
l
e
t
e
 
s
o
 
t
h
a
t
 
t
h
e
 
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
 
a
r
r
a
y
 
a
r
e
 
n
o
t
 
d
u
p
l
i
c
a
t
e
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
3
,
 
3
,
 
1
,
 
2
,
 
2
,
 
1
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
3




 
 
 
 
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
 
i
n
t
e
g
e
r
 
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
s




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
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
 
m
o
v
e
s
 
t
o
 
m
a
k
e
 
e
v
e
r
y
 
v
a
l
u
e
 
i
n
 
n
u
m
s
 
u
n
i
q
u
e


 
 
 
 
"
"
"


 
 
 
 
n
u
m
s
_
s
e
t
 
=
 
s
e
t
(
n
u
m
s
)


 
 
 
 
r
e
t
u
r
n
 
l
e
n
(
n
u
m
s
)
 
-
 
l
e
n
(
n
u
m
s
_
s
e
t
)






d
e
f
 
m
i
n
_
r
e
m
o
v
a
l
s
_
t
o
_
m
a
k
e
_
u
n
i
q
u
e
_
2
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


 
 
 
 
G
i
v
e
n
 
a
n
 
i
n
t
e
g
e
r
 
a
r
r
a
y
,
 
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
 
e
l
e
m
e
n
t
s
 
t
o
 
d
e
l
e
t
e
 
s
o
 
t
h
a
t
 
t
h
e
 
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
 
a
r
r
a
y
 
a
r
e
 
n
o
t
 
d
u
p
l
i
c
a
t
e
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
3
,
 
3
,
 
1
,
 
2
,
 
2
,
 
1
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
3




 
 
 
 
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
 
i
n
t
e
g
e
r
 
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
s




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
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
 
m
o
v
e
s
 
t
o
 
m
a
k
e
 
e
v
e
r
y
 
v
a
l
u
e
 
i
n
 
n
u
m
s
 
u
n
i
q
u
e


 
 
 
 
"
"
"


 
 
 
 
n
u
m
s
_
d
i
c
t
 
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
 
n
u
m
s
:


 
 
 
 
 
 
 
 
i
f
 
n
u
m
 
i
n
 
n
u
m
s
_
d
i
c
t
:


 
 
 
 
 
 
 
 
 
 
 
 
n
u
m
s
_
d
i
c
t
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


 
 
 
 
 
 
 
 
 
 
 
 
n
u
m
s
_
d
i
c
t
[
n
u
m
]
 
=
 
1




 
 
 
 
n
u
m
s
_
d
i
c
t
_
v
a
l
u
e
s
 
=
 
l
i
s
t
(
n
u
m
s
_
d
i
c
t
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


 
 
 
 
n
u
m
s
_
d
i
c
t
_
v
a
l
u
e
s
.
s
o
r
t
(
)


 
 
 
 
m
i
n
_
r
e
m
o
v
a
l
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
l
e
n
(
n
u
m
s
_
d
i
c
t
_
v
a
l
u
e
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
_
d
i
c
t
_
v
a
l
u
e
s
[
i
]
 
>
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
r
e
m
o
v
a
l
s
 
+
=
 
n
u
m
s
_
d
i
c
t
_
v
a
l
u
e
s
[
i
]
 
-
 
1


 
 
 
 
r
e
t
u
r
n
 
m
i
n
_
r
e
m
o
v
a
l
s






d
e
f
 
m
i
n
_
r
e
m
o
v
a
l
s
_
t
o
_
m
a
k
e
_
u
n
i
q
u
e
_
3
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


 
 
 
 
G
i
v
e
n
 
a
n
 
i
n
t
e
g
e
r
 
a
r
r
a
y
,
 
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
 
e
l
e
m
e
n
t
s
 
t
o
 
d
e
l
e
t
e
 
s
o
 
t
h
a
t
 
t
h
e
 
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
 
a
r
r
a
y
 
a
r
e
 
n
o
t
 
d
u
p
l
i
c
a
t
e
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
[
3
,
 
3
,
 
1
,
 
2
,
 
2
,
 
1
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
3




 
 
 
import unittest


class TestMinRemovalsToMakeUnique(unittest.TestCase):
    def test_basic_array(self):
        """Test with a basic array where multiple removals are needed."""
        self.assertEqual(min_removals_to_make_unique([3, 3, 1, 2, 2, 1]), 3)

    def test_all_identical(self):
        """Test an array where all elements are identical."""
        self.assertEqual(min_removals_to_make_unique([4, 4, 4, 4]), 3)

    def test_all_unique(self):
        """Test an array where all elements are already unique."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 3, 4]), 0)

    def test_empty_array(self):
        """Test an empty array."""
        self.assertEqual(min_removals_to_make_unique([]), 0)

    def test_complex_case(self):
        """Test a more complex case with a larger array."""
        self.assertEqual(min_removals_to_make_unique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 6)
if __name__ == '__main__':
    unittest.main()