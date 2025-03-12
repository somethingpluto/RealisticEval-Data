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
[
i
n
t
]
,
 
l
e
f
t
:
 
i
n
t
,
 
r
i
g
h
t
:
 
i
n
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
 
p
o
r
t
i
o
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
[
i
n
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
 
i
n
t
e
g
e
r
s
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
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


 
 
 
 
 
 
 
 
l
e
f
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
 
p
o
r
t
i
o
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


 
 
 
 
 
 
 
 
r
i
g
h
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
 
p
o
r
t
i
o
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
f
t
 
<
 
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
,
 
l
e
f
t
,
 
m
i
d
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
a
r
r
,
 
m
i
d
 
+
 
1
,
 
r
i
g
h
t
)


 
 
 
 
 
 
 
 
m
e
r
g
e
(
a
r
r
,
 
l
e
f
t
,
 
m
i
d
,
 
r
i
g
h
t
)






d
e
f
 
m
e
r
g
e
(
a
r
r
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
 
l
e
f
t
:
 
i
n
t
,
 
m
i
d
:
 
i
n
t
,
 
r
i
g
h
t
:
 
i
n
t
)
:


 
 
 
 
"
"
"


 
 
 
 
M
e
r
g
e
s
 
t
w
o
 
p
o
r
t
i
o
n
s
 
o
f
 
a
n
 
a
r
r
a
y
 
i
n
t
o
 
a
 
s
i
n
g
l
e
 
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
[
i
n
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
 
i
n
t
e
g
e
r
s
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
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


 
 
 
 
 
 
 
 
l
e
f
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
 
p
o
r
t
i
o
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


 
 
 
 
 
 
 
 
m
i
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
 
m
i
d
d
l
e
 
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
 
p
o
r
t
i
o
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


 
 
 
 
 
 
 
 
r
i
g
h
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
 
p
o
r
t
i
o
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


 
 
 
 
t
e
m
p
 
=
 
[
0
]
 
*
 
(
r
i
g
h
t
 
-
 
l
e
f
t
 
+
 
1
)


 
 
 
 
i
 
=
 
l
e
f
t


 
 
 
 
j
 
=
 
m
i
d
 
+
 
1


 
 
 
 
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
=
 
m
i
d
 
a
n
d
 
j
 
<
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
i
f
 
a
r
r
[
i
]
 
<
=
 
a
r
r
[
j
]
:


 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
[
k
]
 
=
 
a
r
r
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


 
 
 
 
 
 
 
 
 
 
 
 
t
e
m
p
[
k
]
 
=
 
a
r
r
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
=
 
m
i
d
:


 
 
 
 
 
 
 
 
t
e
m
p
[
k
]
 
=
 
a
r
r
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
=
 
r
i
g
h
t
:


 
 
 
 
 
 
 
 
t
e
m
p
[
k
]
 
=
 
a
r
r
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
f
t
,
 
r
i
g
h
t
 
+
 
1
)
:


 
 
 
 
 
 
 
 
a
r
r
[
i
]
 
=
 
t
e
m
p
[
i
 
-
 
l
e
f
t
]






d
e
f
 
b
i
n
a
r
y
_
s
e
a
r
c
h
(
a
r
r
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


 
 
 
 
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
t
a
r
g
e
t
 
i
n
t
e
g
e
r
 
i
n
 
a
import unittest


class Tester(unittest.TestCase):

    def test_sort_empty_array(self):
        """Test sorting an empty array."""
        empty_array = []
        merge_sort(empty_array, 0, len(empty_array) - 1)
        self.assertTrue(len(empty_array) == 0)  # Assert that the array is still empty

    def test_sort_single_element_array(self):
        """Test sorting a single element array."""
        single_element = [1]
        merge_sort(single_element, 0, len(single_element) - 1)
        self.assertEqual(single_element, [1])  # Assert that it remains the same

    def test_sort_sorted_array(self):
        """Test sorting a sorted array."""
        sorted_array = [1, 2, 3, 4, 5]
        merge_sort(sorted_array, 0, len(sorted_array) - 1)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])  # Correct the expected value

    def test_sort_reverse_sorted_array(self):
        """Test sorting a reverse sorted array."""
        reverse_sorted_array = [5, 4, 3, 2, 1]
        merge_sort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1)
        self.assertEqual(reverse_sorted_array, [1, 2, 3, 4, 5])  # Assert it sorts correctly

    def test_sort_random_integers(self):
        """Test sorting an array with random integers."""
        random_array = [38, 27, 43, 3, 9, 82, 10]
        expected_sorted_array = [3, 9, 10, 27, 38, 43, 82]
        merge_sort(random_array, 0, len(random_array) - 1)
        self.assertEqual(random_array, expected_sorted_array)  # Assert the sorted array is correct

if __name__ == '__main__':
    unittest.main()