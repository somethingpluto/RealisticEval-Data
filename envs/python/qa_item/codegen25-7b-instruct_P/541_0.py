d
e
f
 
f
i
l
t
e
r
_
a
r
r
a
y
(
u
n
f
i
l
t
e
r
e
d
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
 
i
s
_
q
u
a
l
i
f
i
e
d
:
 
c
a
l
l
a
b
l
e
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


 
 
 
 
F
i
l
t
e
r
s
 
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
n
 
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
 
a
 
q
u
a
l
i
f
i
c
a
t
i
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


 
 
 
 
 
 
 
 
u
n
f
i
l
t
e
r
e
d
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
 
a
r
r
a
y
 
t
o
 
f
i
l
t
e
r
.


 
 
 
 
 
 
 
 
i
s
_
q
u
a
l
i
f
i
e
d
 
(
c
a
l
l
a
b
l
e
)
:
 
A
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
d
e
t
e
r
m
i
n
e
s
 
i
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
 
q
u
a
l
i
f
i
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
n
e
w
 
l
i
s
t
 
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
 
e
l
e
m
e
n
t
s
 
t
h
a
t
 
q
u
a
l
i
f
y
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
t
e
r
e
d
_
a
r
r
a
y
 
=
 
[
]


 
 
 
 
f
o
r
 
e
l
e
m
e
n
t
 
i
n
 
u
n
f
i
l
t
e
r
e
d
_
a
r
r
a
y
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
q
u
a
l
i
f
i
e
d
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


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
a
r
r
a
y
.
a
p
p
e
n
d
(
e
l
e
m
e
n
t
)


 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
e
d
_
a
r
r
a
y






d
e
f
 
f
i
l
t
e
r
_
d
i
c
t
(
u
n
f
i
l
t
e
r
e
d
_
d
i
c
t
:
 
d
i
c
t
,
 
i
s
_
q
u
a
l
i
f
i
e
d
:
 
c
a
l
l
a
b
l
e
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
F
i
l
t
e
r
s
 
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
 
d
i
c
t
i
o
n
a
r
y
 
b
a
s
e
d
 
o
n
 
a
 
q
u
a
l
i
f
i
c
a
t
i
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


 
 
 
 
 
 
 
 
u
n
f
i
l
t
e
r
e
d
_
d
i
c
t
 
(
d
i
c
t
)
:
 
T
h
e
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
f
i
l
t
e
r
.


 
 
 
 
 
 
 
 
i
s
_
q
u
a
l
i
f
i
e
d
 
(
c
a
l
l
a
b
l
e
)
:
 
A
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
d
e
t
e
r
m
i
n
e
s
 
i
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
 
q
u
a
l
i
f
i
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


 
 
 
 
 
 
 
 
d
i
c
t
:
 
A
 
n
e
w
 
d
i
c
t
i
o
n
a
r
y
 
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
 
e
l
e
m
e
n
t
s
 
t
h
a
t
 
q
u
a
l
i
f
y
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
t
e
r
e
d
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
 
k
e
y
,
 
v
a
l
u
e
 
i
n
 
u
n
f
i
l
t
e
r
e
d
_
d
i
c
t
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
q
u
a
l
i
f
i
e
d
(
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
d
i
c
t
[
k
e
y
]
 
=
 
v
a
l
u
e


 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
e
d
_
d
i
c
t






d
e
f
 
f
i
l
t
e
r
_
l
i
s
t
_
o
f
_
d
i
c
t
s
(
u
n
f
i
l
t
e
r
e
d
_
l
i
s
t
:
 
l
i
s
t
,
 
i
s
_
q
u
a
l
i
f
i
e
d
:
 
c
a
l
l
a
b
l
e
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


 
 
 
 
F
i
l
t
e
r
s
 
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
 
b
a
s
e
d
 
o
n
 
a
 
q
u
a
l
i
f
i
c
a
t
i
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


 
 
 
 
 
 
 
 
u
n
f
i
l
t
e
r
e
d
_
l
i
s
t
 
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
 
t
o
 
f
i
l
t
e
r
.


 
 
 
 
 
 
 
 
i
s
_
q
u
a
l
i
f
i
e
d
 
(
c
a
l
l
a
b
l
e
)
:
 
A
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
d
e
t
e
r
m
i
n
e
s
 
i
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
 
q
u
a
l
i
f
i
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
n
e
w
 
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
 
e
l
e
m
e
n
t
s
 
t
h
a
t
 
q
u
a
l
i
f
y
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
t
e
r
e
d
_
l
i
s
t
 
=
 
[
]


 
 
 
 
f
o
r
 
e
l
e
m
e
n
t
 
i
n
 
u
n
f
i
l
t
e
r
e
d
_
l
i
s
t
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
q
u
a
l
i
f
i
e
d
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


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
l
i
s
t
.
a
p
p
e
n
d
(
e
l
e
m
e
n
t
)


 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
e
d
_
l
i
s
t






d
e
f
 
f
i
l
t
e
r
_
l
i
s
t
_
o
f
_
l
i
s
t
s
(
u
n
f
i
l
t
e
r
e
d
_
l
i
s
t
:
 
l
i
s
t
,
 
i
s
_
q
u
a
l
i
f
i
e
d
:
 
c
a
l
l
a
b
l
e
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


 
 
 
 
F
i
l
t
e
r
s
 
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
 
b
a
s
e
d
 
o
n
 
a
 
q
u
a
l
i
f
i
c
a
t
i
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


 
 
 
 
 
 
 
 
u
n
f
i
l
t
e
r
e
d
_
l
i
s
t
 
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
 
l
i
s
t
s
import unittest


class TestFilterArray(unittest.TestCase):

    def test_filters_out_numbers_less_than_or_equal_to_ten(self):
        unfiltered_array = [5, 12, 3, 18, 7, 10, 15]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [12, 18, 15])

    def test_returns_empty_array_when_all_elements_are_disqualified(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [])

    def test_returns_same_array_when_all_elements_are_qualified(self):
        unfiltered_array = [11, 12, 15, 20]
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [11, 12, 15, 20])

    def test_handles_empty_array_input(self):
        unfiltered_array = []
        result = filter_array(unfiltered_array, lambda x: x > 10)
        self.assertEqual(result, [])

    def test_filters_out_strings_based_on_length(self):
        unfiltered_array = ['a', 'ab', 'abc', 'abcd', 'abcde']
        result = filter_array(unfiltered_array, lambda x: len(x)>3)
        self.assertEqual(result, ['abcd', 'abcde'])

    def test_correctly_filters_array_with_mixed_types(self):
        unfiltered_array = [1, 'hello', True, 'world', None]
        result = filter_array(unfiltered_array, lambda x: isinstance(x, str))
        self.assertEqual(result, ['hello', 'world'])

    def test_filters_based_on_object_property(self):
        unfiltered_array = [{'value': 3}, {'value': 5}, {'value': 7}]
        result = filter_array(unfiltered_array, lambda x: x > 5)
        self.assertEqual(result, [{'value': 7}])

    def test_returns_empty_array_when_no_qualifying_function_provided(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, lambda x: False)  # Always returns false
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()