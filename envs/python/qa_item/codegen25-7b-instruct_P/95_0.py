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
,
 
A
n
y
,
 
C
a
l
l
a
b
l
e
,
 
D
i
c
t






d
e
f
 
f
i
n
d
_
m
a
t
c
h
i
n
g
_
e
l
e
m
e
n
t
s
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
A
n
y
]
,
 
c
o
m
p
a
r
i
s
o
n
_
f
n
:
 
C
a
l
l
a
b
l
e
[
[
A
n
y
]
,
 
b
o
o
l
]
)
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
m
a
t
c
h
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
 
a
n
d
 
t
h
e
i
r
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
i
n
p
u
t
 
a
r
r
a
y


 
 
 
 
b
a
s
e
d
 
o
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
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
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
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.


 
 
 
 
 
 
 
 
c
o
m
p
a
r
i
s
o
n
_
f
n
 
(
)
:
 
T
h
e
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
 
t
o
 
d
e
t
e
r
m
i
n
e
 
m
a
t
c
h
e
s
.




 
 
 
 
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
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
e
a
c
h
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
m
a
t
c
h
e
d
 
e
l
e
m
e
n
t
 
a
n
d
 
i
t
s
 
i
n
d
e
x
.


 
 
 
 
"
"
"


 
 
 
 
m
a
t
c
h
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
i
,
 
e
l
e
m
e
n
t
 
i
n
 
e
n
u
m
e
r
a
t
e
(
a
r
r
)
:


 
 
 
 
 
 
 
 
i
f
 
c
o
m
p
a
r
i
s
o
n
_
f
n
(
e
l
e
m
e
n
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
m
a
t
c
h
e
s
.
a
p
p
e
n
d
(
{
"
e
l
e
m
e
n
t
"
:
 
e
l
e
m
e
n
t
,
 
"
i
n
d
e
x
"
:
 
i
}
)


 
 
 
 
r
e
t
u
r
n
 
m
a
t
c
h
e
s






d
e
f
 
f
i
n
d
_
m
a
t
c
h
i
n
g
_
e
l
e
m
e
n
t
s
_
w
i
t
h
_
v
a
l
u
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
A
n
y
]
,
 
c
o
m
p
a
r
i
s
o
n
_
f
n
:
 
C
a
l
l
a
b
l
e
[
[
A
n
y
]
,
 
b
o
o
l
]
)
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
m
a
t
c
h
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
 
a
n
d
 
t
h
e
i
r
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
i
n
p
u
t
 
a
r
r
a
y


 
 
 
 
b
a
s
e
d
 
o
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
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
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
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.


 
 
 
 
 
 
 
 
c
o
m
p
a
r
i
s
o
n
_
f
n
 
(
)
:
 
T
h
e
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
 
t
o
 
d
e
t
e
r
m
i
n
e
 
m
a
t
c
h
e
s
.




 
 
 
 
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
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
e
a
c
h
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
m
a
t
c
h
e
d
 
e
l
e
m
e
n
t
 
a
n
d
 
i
t
s
 
i
n
d
e
x
.


 
 
 
 
"
"
"


 
 
 
 
m
a
t
c
h
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
i
,
 
e
l
e
m
e
n
t
 
i
n
 
e
n
u
m
e
r
a
t
e
(
a
r
r
)
:


 
 
 
 
 
 
 
 
i
f
 
c
o
m
p
a
r
i
s
o
n
_
f
n
(
e
l
e
m
e
n
t
)
:


 
 
 
 
 
 
 
 
 
 
 
 
m
a
t
c
h
e
s
.
a
p
p
e
n
d
(
{
"
e
l
e
m
e
n
t
"
:
 
e
l
e
m
e
n
t
,
 
"
i
n
d
e
x
"
:
 
i
}
)


 
 
 
 
r
e
t
u
r
n
 
m
a
t
c
h
e
s






d
e
f
 
f
i
n
d
_
m
a
t
c
h
i
n
g
_
e
l
e
m
e
n
t
s
_
w
i
t
h
_
v
a
l
u
e
_
a
n
d
_
k
e
y
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
A
n
y
]
,
 
c
o
m
p
a
r
i
s
o
n
_
f
n
:
 
C
a
l
l
a
b
l
e
[
[
A
n
y
]
,
 
b
o
o
l
]
)
 
-
>
 
L
i
s
t
[
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
m
a
t
c
h
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
 
a
n
d
 
t
h
e
i
r
 
i
n
d
i
c
e
s
 
i
n
 
t
h
e
 
i
n
p
u
t
 
a
r
r
a
y


 
 
 
 
b
a
s
e
d
 
o
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
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
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
s
t
r
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
t
o
 
s
e
a
r
c
h
 
t
h
r
o
u
g
h
.


 
 
 
 
 
 
 
 
c
o
m
p
a
r
i
s
o
n
_
f
n
 
(
)
:
 
T
h
e
 
c
o
m
p
a
r
i
s
o
n
 
f
u
n
c
t
i
o
n
 
t
o
 
d
e
t
e
r
m
i
n
e
 
m
a
t
c
h
e
s
.




 
 
 
 
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
D
i
c
t
[
s
t
r
,
 
A
n
y
]
]
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
e
a
c
h
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
m
a
t
c
h
e
d
 
e
l
e
m
e
n
t
 
a
n
d
 
i
t
s
 
i
n
d
e
x
.


 
 
 
 
"
"
"


 
 
 
 
m
a
t
c
h
e
s
 
=
 
[
]


import unittest


class TestFindMatchingElements(unittest.TestCase):

    def test_empty_input_array(self):
        result = find_matching_elements([], lambda el: el > 0)
        self.assertEqual(result, [])

    def test_matching_elements_and_indices(self):
        input_array = [1, 2, 3, 4, 5]
        comparison_function = lambda num: num > 3
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 4, 'index': 3},
            {'element': 5, 'index': 4},
        ])

    def test_string_matching_condition(self):
        input_array = ['apple', 'banana', 'cherry', 'date']
        comparison_function = lambda fruit: fruit.startswith('b')
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 'banana', 'index': 1},
        ])

    def test_multiple_elements_with_same_value(self):
        input_array = [1, 2, 2, 3, 2, 4]
        comparison_function = lambda num: num == 2
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': 2, 'index': 1},
            {'element': 2, 'index': 2},
            {'element': 2, 'index': 4},
        ])

    def test_matching_objects_based_on_property(self):
        input_array = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 30},
        ]
        comparison_function = lambda person: person['age'] == 30
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': {'name': 'Bob', 'age': 30}, 'index': 1},
            {'element': {'name': 'Charlie', 'age': 30}, 'index': 2},
        ])

    def test_no_elements_if_no_matches_found(self):
        input_array = [1, 3, 5, 7]
        comparison_function = lambda num: num % 2 == 0  # looking for even numbers
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [])

    def test_negative_numbers_condition(self):
        input_array = [-1, -2, 0, 1, 2]
        comparison_function = lambda num: num < 0
        result = find_matching_elements(input_array, comparison_function)
        self.assertEqual(result, [
            {'element': -1, 'index': 0},
            {'element': -2, 'index': 1},
        ])

if __name__ == '__main__':
    unittest.main()