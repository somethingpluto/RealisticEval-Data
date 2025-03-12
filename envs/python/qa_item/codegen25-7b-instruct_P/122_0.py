d
e
f
 
s
a
f
e
_
s
p
l
i
c
e
(
i
n
p
u
t
_
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
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
,
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
,
 
r
e
p
l
a
c
e
_
w
i
t
h
=
N
o
n
e
)
:


 
 
 
 
"
"
"


 
 
 
 
S
a
f
e
l
y
 
s
p
l
i
c
e
s
 
a
n
 
a
r
r
a
y
 
b
y
 
r
e
m
o
v
i
n
g
 
a
 
s
p
e
c
i
f
i
e
d
 
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
 
f
r
o
m
 
a
 
g
i
v
e
n
 
i
n
d
e
x
,


 
 
 
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
r
e
p
l
a
c
e
s
 
t
h
e
m
 
w
i
t
h
 
a
 
n
e
w
 
e
l
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


 
 
 
 
 
 
 
 
i
n
p
u
t
_
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
 
o
r
i
g
i
n
a
l
 
a
r
r
a
y
 
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
m
o
u
n
t
_
t
o
_
r
e
m
o
v
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
 
r
e
m
o
v
e
 
f
r
o
m
 
t
h
e
 
a
r
r
a
y
.


 
 
 
 
 
 
 
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
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
 
i
n
d
e
x
 
a
t
 
w
h
i
c
h
 
t
o
 
s
t
a
r
t
 
r
e
m
o
v
i
n
g
 
e
l
e
m
e
n
t
s
.


 
 
 
 
 
 
 
 
r
e
p
l
a
c
e
_
w
i
t
h
 
(
a
n
y
,
 
o
p
t
i
o
n
a
l
)
:
 
T
h
e
 
e
l
e
m
e
n
t
 
t
o
 
r
e
p
l
a
c
e
 
t
h
e
 
r
e
m
o
v
e
d
 
e
l
e
m
e
n
t
s
 
w
i
t
h
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
 
A
 
n
e
w
 
a
r
r
a
y
 
w
i
t
h
 
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
 
e
l
e
m
e
n
t
s
 
r
e
m
o
v
e
d
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
r
e
p
l
a
c
e
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
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
 
i
n
p
u
t
_
a
r
r
a
y


 
 
 
 
i
f
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
<
 
0
:


 
 
 
 
 
 
 
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
=
 
l
e
n
(
i
n
p
u
t
_
a
r
r
a
y
)
 
+
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e


 
 
 
 
i
f
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
<
 
0
 
o
r
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
>
=
 
l
e
n
(
i
n
p
u
t
_
a
r
r
a
y
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
_
a
r
r
a
y


 
 
 
 
i
f
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
<
 
0
:


 
 
 
 
 
 
 
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
=
 
l
e
n
(
i
n
p
u
t
_
a
r
r
a
y
)
 
-
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e


 
 
 
 
i
f
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
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
 
i
n
p
u
t
_
a
r
r
a
y


 
 
 
 
i
f
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
>
 
l
e
n
(
i
n
p
u
t
_
a
r
r
a
y
)
 
-
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
:


 
 
 
 
 
 
 
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
=
 
l
e
n
(
i
n
p
u
t
_
a
r
r
a
y
)
 
-
 
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e


 
 
 
 
i
f
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
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
 
i
n
p
u
t
_
a
r
r
a
y


 
 
 
 
i
f
 
r
e
p
l
a
c
e
_
w
i
t
h
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
_
a
r
r
a
y
[
:
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
]
 
+
 
i
n
p
u
t
_
a
r
r
a
y
[
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
+
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
:
]


 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t
_
a
r
r
a
y
[
:
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
]
 
+
 
[
r
e
p
l
a
c
e
_
w
i
t
h
]
 
*
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
 
+
 
i
n
p
u
t
_
a
r
r
a
y
[
i
n
d
e
x
_
t
o
_
r
e
m
o
v
e
 
+
 
a
m
o
u
n
t
_
t
o
_
r
e
m
o
v
e
:
]




d
e
f
 
s
a
f
e
_
i
n
d
e
x
(
i
n
p
u
t
_
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
 
e
l
e
m
e
n
t
,
 
s
t
a
r
t
=
0
,
 
e
n
d
=
N
o
n
e
)
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
 
t
h
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
 
f
i
r
s
t
 
o
c
c
u
r
r
e
n
c
e
 
o
f
 
a
n
 
e
l
e
m
e
n
t
 
w
i
t
h
i
n
 
a
 
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
 
o
f
 
a
n
 
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


 
 
 
 
 
 
 
 
i
n
p
u
t
_
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
 
o
r
i
g
i
n
a
l
 
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
e
a
r
c
h
e
d
.


 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
 
(
a
n
y
)
:
 
T
h
e
 
e
l
e
m
e
n
t
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
w
i
t
h
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
import unittest


class TestSafeSplice(unittest.TestCase):

    def test_replaces_removed_elements_with_a_new_element(self):
        input_array = ['a', 'b', 'c', 'd', 'e']
        expected = ['a', 'z', 'e']
        result = safe_splice(input_array, 3, 1, 'z')
        self.assertEqual(result, expected)

    def test_removes_specified_elements_and_replaces_with_new_element(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 2
        index_to_remove = 1
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [1, 99, 4, 5])

    def test_handles_removing_elements_from_the_end_of_the_array(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 2
        index_to_remove = 3
        result = safe_splice(input_array, amount_to_remove, index_to_remove)
        self.assertEqual(result, [1, 2, 3])

    def test_handles_case_where_no_elements_are_removed(self):
        input_array = [1, 2, 3, 4, 5]
        amount_to_remove = 0
        index_to_remove = 2
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [1, 2, 99, 3, 4, 5])

    def test_handles_edge_case_with_empty_input_array(self):
        input_array = []
        amount_to_remove = 1
        index_to_remove = 0
        replace_with = 99
        result = safe_splice(input_array, amount_to_remove, index_to_remove, replace_with)
        self.assertEqual(result, [99])

if __name__ == '__main__':
    unittest.main()