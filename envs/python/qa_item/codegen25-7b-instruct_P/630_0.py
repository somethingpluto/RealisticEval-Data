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
 
i
n
s
e
r
t
i
o
n
_
s
o
r
t
(
a
r
r
:
L
i
s
t
)
:


 
 
 
 
"
"
"


 
 
 
 
S
o
r
t
s
 
a
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r
 
u
s
i
n
g
 
t
h
e
 
i
n
s
e
r
t
i
o
n
 
s
o
r
t
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
 
(
L
i
s
t
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
t
o
 
b
e
 
s
o
r
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
1
,
 
l
e
n
(
a
r
r
)
)
:


 
 
 
 
 
 
 
 
k
e
y
 
=
 
a
r
r
[
i
]


 
 
 
 
 
 
 
 
j
 
=
 
i
 
-
 
1


 
 
 
 
 
 
 
 
w
h
i
l
e
 
j
 
>
=
 
0
 
a
n
d
 
k
e
y
 
<
 
a
r
r
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
j
 
+
 
1
]
 
=
 
a
r
r
[
j
]


 
 
 
 
 
 
 
 
 
 
 
 
j
 
-
=
 
1


 
 
 
 
 
 
 
 
a
r
r
[
j
 
+
 
1
]
 
=
 
k
e
y


 
 
 
 
r
e
t
u
r
n
 
a
r
r






d
e
f
 
m
e
r
g
e
_
s
o
r
t
(
a
r
r
:
L
i
s
t
)
:


 
 
 
 
"
"
"


 
 
 
 
S
o
r
t
s
 
a
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r
 
u
s
i
n
g
 
t
h
e
 
m
e
r
g
e
 
s
o
r
t
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
 
(
L
i
s
t
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
t
o
 
b
e
 
s
o
r
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
)
 
>
 
1
:


 
 
 
 
 
 
 
 
m
i
d
 
=
 
l
e
n
(
a
r
r
)
 
/
/
 
2


 
 
 
 
 
 
 
 
l
e
f
t
_
h
a
l
f
 
=
 
a
r
r
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
_
h
a
l
f
 
=
 
a
r
r
[
m
i
d
:
]




 
 
 
 
 
 
 
 
m
e
r
g
e
_
s
o
r
t
(
l
e
f
t
_
h
a
l
f
)


 
 
 
 
 
 
 
 
m
e
r
g
e
_
s
o
r
t
(
r
i
g
h
t
_
h
a
l
f
)




 
 
 
 
 
 
 
 
i
 
=
 
j
 
=
 
k
 
=
 
0




 
 
 
 
 
 
 
 
w
h
i
l
e
 
i
 
<
 
l
e
n
(
l
e
f
t
_
h
a
l
f
)
 
a
n
d
 
j
 
<
 
l
e
n
(
r
i
g
h
t
_
h
a
l
f
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
f
t
_
h
a
l
f
[
i
]
 
<
 
r
i
g
h
t
_
h
a
l
f
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
k
]
 
=
 
l
e
f
t
_
h
a
l
f
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
 
+
=
 
1


 
 
 
 
 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
k
]
 
=
 
r
i
g
h
t
_
h
a
l
f
[
j
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
j
 
+
=
 
1


 
 
 
 
 
 
 
 
 
 
 
 
k
 
+
=
 
1




 
 
 
 
 
 
 
 
w
h
i
l
e
 
i
 
<
 
l
e
n
(
l
e
f
t
_
h
a
l
f
)
:


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
k
]
 
=
 
l
e
f
t
_
h
a
l
f
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
i
 
+
=
 
1


 
 
 
 
 
 
 
 
 
 
 
 
k
 
+
=
 
1




 
 
 
 
 
 
 
 
w
h
i
l
e
 
j
 
<
 
l
e
n
(
r
i
g
h
t
_
h
a
l
f
)
:


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
[
k
]
 
=
 
r
i
g
h
t
_
h
a
l
f
[
j
]


 
 
 
 
 
 
 
 
 
 
 
 
j
 
+
=
 
1


 
 
 
 
 
 
 
 
 
 
 
 
k
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
a
r
r






d
e
f
 
q
u
i
c
k
_
s
o
r
t
(
a
r
r
:
L
i
s
t
)
:


 
 
 
 
"
"
"


 
 
 
 
S
o
r
t
s
 
a
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r
 
u
s
i
n
g
 
t
h
e
 
q
u
i
c
k
 
s
o
r
t
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
r
r
 
(
L
i
s
t
)
:
 
T
h
e
 
l
i
s
t
 
o
f
 
f
l
o
a
t
s
 
t
o
 
b
e
 
s
o
r
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
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
r
r


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
p
i
v
o
t
 
=
 
a
r
r
[
0
]


 
 
 
 
 
 
 
 
l
e
s
s
 
=
 
[
i
 
f
o
r
 
i
 
i
n
 
a
r
r
[
1
:
]
 
i
f
import unittest


class TestAnswer(unittest.TestCase):
    def test_basic_unsorted_array(self):
        """Test case 1: Basic unsorted array."""
        arr = [12.4, 11.2, 13.5, 5.6, 6.7]
        expected = [5.6, 6.7, 11.2, 12.4, 13.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_already_sorted_array(self):
        """Test case 2: Already sorted array."""
        arr = [1.1, 2.2, 3.3, 4.4, 5.5]
        expected = [1.1, 2.2, 3.3, 4.4, 5.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_reverse_sorted_array(self):
        """Test case 3: Reverse sorted array."""
        arr = [5.5, 4.4, 3.3, 2.2, 1.1]
        expected = [1.1, 2.2, 3.3, 4.4, 5.5]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_empty_array(self):
        """Test case 4: Empty array."""
        arr = []
        expected = []
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_single_element_array(self):
        """Test case 5: Single element array."""
        arr = [3.3]
        expected = [3.3]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_array_with_duplicates(self):
        """Test case 6: Array with duplicate values."""
        arr = [2.2, 3.3, 2.2, 1.1, 3.3]
        expected = [1.1, 2.2, 2.2, 3.3, 3.3]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

    def test_large_numbers(self):
        """Test case 7: Large numbers."""
        arr = [1e10, 1e9, 1e11, 1e8]
        expected = [1e8, 1e9, 1e10, 1e11]
        insertion_sort(arr)
        self.assertEqual(expected, arr)

if __name__ == '__main__':
    unittest.main()