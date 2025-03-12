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
 
D
i
c
t
,
 
L
i
s
t






d
e
f
 
d
i
c
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
_
t
o
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
d
i
c
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
:
 
D
i
c
t
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
]
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
 
o
f
 
l
i
s
t
s
 
i
n
t
o
 
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
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
c
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
d
i
c
t
)
:
 
A
 
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
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
h
a
s
 
a
 
l
i
s
t
 
a
s
 
i
t
s
 
v
a
l
u
e
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
 
o
f
 
d
i
c
t
s
:
 
A
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
i
t
e
m
 
i
s
 
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
 
f
o
r
m
e
d
 
b
y
 
c
o
r
r
e
s
p
o
n
d
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
 
o
f
 
l
i
s
t
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
 
[
{
k
:
 
v
 
f
o
r
 
k
,
 
v
 
i
n
 
z
i
p
(
d
i
c
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
.
k
e
y
s
(
)
,
 
v
a
l
u
e
s
)
}
 
f
o
r
 
v
a
l
u
e
s
 
i
n
 
z
i
p
(
*
d
i
c
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
]






d
e
f
 
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
_
t
o
_
d
i
c
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
]
)
 
-
>
 
D
i
c
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
 
i
n
t
o
 
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
 
o
f
 
l
i
s
t
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
s
)
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
 
o
f
 
l
i
s
t
s
:
 
A
 
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
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
h
a
s
 
a
 
l
i
s
t
 
a
s
 
i
t
s
 
v
a
l
u
e
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
 
{
k
:
 
[
d
[
k
]
 
f
o
r
 
d
 
i
n
 
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
]
 
f
o
r
 
k
 
i
n
 
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
[
0
]
.
k
e
y
s
(
)
}






d
e
f
 
d
i
c
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
_
t
o
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
_
w
i
t
h
_
k
e
y
s
(
d
i
c
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
:
 
D
i
c
t
,
 
k
e
y
s
:
 
L
i
s
t
[
s
t
r
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
]
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
 
o
f
 
l
i
s
t
s
 
i
n
t
o
 
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
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
c
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
d
i
c
t
)
:
 
A
 
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
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
h
a
s
 
a
 
l
i
s
t
 
a
s
 
i
t
s
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 
k
e
y
s
 
(
l
i
s
t
 
o
f
 
s
t
r
)
:
 
T
h
e
 
k
e
y
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
h
e
 
o
u
t
p
u
t
 
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
 
o
f
 
d
i
c
t
s
:
 
A
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
i
t
e
m
 
i
s
 
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
 
f
o
r
m
e
d
 
b
y
 
c
o
r
r
e
s
p
o
n
d
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
 
o
f
 
l
i
s
t
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
 
[
{
k
:
 
v
 
f
o
r
 
k
,
 
v
 
i
n
 
z
i
p
(
k
e
y
s
,
 
v
a
l
u
e
s
)
}
 
f
o
r
 
v
a
l
u
e
s
 
i
n
 
z
i
p
(
*
[
d
i
c
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
[
k
]
 
f
o
r
 
k
 
i
n
 
k
e
y
s
]
)
]






d
e
f
 
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
_
t
o
_
d
i
c
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
_
w
i
t
h
_
k
e
y
s
(
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
]
,
 
k
e
y
s
:
 
L
i
s
t
[
s
t
r
]
)
import unittest


class TestDictOfListsToListOfDicts(unittest.TestCase):
    def test_standard_conversion(self):
        """Test standard conversion with equal length lists."""
        dict_of_lists = {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "city": ["New York", "Los Angeles", "Chicago"]
        }
        expected_result = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'},
            {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
            {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
        ]
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

    def test_empty_lists(self):
        """Test the function with empty lists."""
        dict_of_lists = {
            "name": [],
            "age": [],
            "city": []
        }
        expected_result = []
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

    def test_single_element_lists(self):
        """Test the function with single-element lists."""
        dict_of_lists = {
            "name": ["Alice"],
            "age": [25],
            "city": ["New York"]
        }
        expected_result = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'}
        ]
        result = dict_of_lists_to_list_of_dicts(dict_of_lists)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()