d
e
f
 
s
h
u
f
f
l
e
(
a
r
r
a
y
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
a
n
d
o
m
l
y
 
s
h
u
f
f
l
e
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
 
o
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
i
n
 
p
l
a
c
e
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
l
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
h
u
f
f
l
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
s
h
u
f
f
l
e
d
 
l
i
s
t
 
w
i
t
h
 
i
t
s
 
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
 
r
a
n
d
o
m
 
o
r
d
e
r
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
a
r
r
a
y
)
)
:


 
 
 
 
 
 
 
 
j
 
=
 
r
a
n
d
o
m
.
r
a
n
d
i
n
t
(
i
,
 
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
 
-
 
1
)


 
 
 
 
 
 
 
 
a
r
r
a
y
[
i
]
,
 
a
r
r
a
y
[
j
]
 
=
 
a
r
r
a
y
[
j
]
,
 
a
r
r
a
y
[
i
]


 
 
 
 
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






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
s
u
b
s
e
t
(
a
r
r
a
y
:
 
l
i
s
t
,
 
s
i
z
e
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
a
 
r
a
n
d
o
m
 
s
u
b
s
e
t
 
o
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
o
f
 
s
i
z
e
 
'
s
i
z
e
'
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
l
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
h
u
f
f
l
e
d
.


 
 
 
 
 
 
 
 
s
i
z
e
 
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
 
s
u
b
s
e
t
 
t
o
 
b
e
 
r
e
t
u
r
n
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
s
u
b
s
e
t
 
o
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
o
f
 
s
i
z
e
 
'
s
i
z
e
'
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
r
a
n
d
o
m
.
s
a
m
p
l
e
(
a
r
r
a
y
,
 
s
i
z
e
)






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
s
u
b
s
e
t
_
w
i
t
h
_
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
(
a
r
r
a
y
:
 
l
i
s
t
,
 
s
i
z
e
:
 
i
n
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
a
 
r
a
n
d
o
m
 
s
u
b
s
e
t
 
o
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
o
f
 
s
i
z
e
 
'
s
i
z
e
'
 
w
i
t
h
 
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
l
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
h
u
f
f
l
e
d
.


 
 
 
 
 
 
 
 
s
i
z
e
 
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
 
s
u
b
s
e
t
 
t
o
 
b
e
 
r
e
t
u
r
n
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
s
u
b
s
e
t
 
o
f
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
o
f
 
s
i
z
e
 
'
s
i
z
e
'
 
w
i
t
h
 
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
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
a
r
r
a
y
,
 
k
=
s
i
z
e
)






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
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
a
r
r
a
y
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
a
 
r
a
n
d
o
m
 
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
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
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
l
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
h
u
f
f
l
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
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
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
r
a
n
d
o
m
.
s
a
m
p
l
e
(
a
r
r
a
y
,
 
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
)






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
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
_
w
i
t
h
_
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
(
a
r
r
a
y
:
 
l
i
s
t
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
a
 
r
a
n
d
o
m
 
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
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
w
i
t
h
 
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
l
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
h
u
f
f
l
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
T
h
e
 
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
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
w
i
t
h
 
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
.
import unittest


class TestShuffleFunction(unittest.TestCase):

    def test_shuffles_array_of_numbers(self):
        array = [1, 2, 3, 4, 5]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))
        self.assertEqual(len(set(shuffled_array)), len(set(array)))  # Ensure no duplicates

    def test_shuffles_array_of_strings(self):
        array = ["apple", "banana", "cherry", "date", "elderberry"]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))

    def test_shuffles_array_with_duplicate_elements(self):
        array = [1, 1, 2, 2, 3, 3]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))

    def test_shuffles_array_with_single_element(self):
        array = [42]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(shuffled_array, array)

    def test_shuffles_empty_array(self):
        array = []
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), 0)

if __name__ == '__main__':
    unittest.main()