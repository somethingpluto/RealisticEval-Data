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
 
O
p
t
i
o
n
a
l




d
e
f
 
c
o
n
v
e
r
t
_
c
s
v
_
v
a
l
u
e
s
(
r
o
w
:
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
s
t
r
]
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
 
n
u
m
e
r
i
c
 
v
a
l
u
e
s
 
i
n
 
a
 
C
S
V
 
r
o
w
 
f
r
o
m
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
t
o
 
a
 
s
t
a
n
d
a
r
d
i
z
e
d
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
 
(
D
i
c
t
[
s
t
r
,
 
s
t
r
]
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
 
a
 
r
o
w
 
o
f
 
C
S
V
 
d
a
t
a
 
w
h
e
r
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
k
e
y
s
 
a
r
e
 
c
o
l
u
m
n
 
n
a
m
e
s
 
a
n
d
 
v
a
l
u
e
s
 
a
r
e
 
s
t
r
i
n
g
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
s
t
r
]
]
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
 
w
i
t
h
 
v
a
l
u
e
s
 
c
o
n
v
e
r
t
e
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
h
a
v
e
 
c
o
m
m
a
s
 
r
e
p
l
a
c
e
d
 
w
i
t
h
 
d
o
t
s
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
o
n
-
n
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
a
r
e
 
s
e
t
 
t
o
 
N
o
n
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


 
 
 
 
 
 
 
 
c
o
l
u
m
n
:
 
N
o
n
e
 
i
f
 
n
o
t
 
v
a
l
u
e
.
i
s
n
u
m
e
r
i
c
(
)
 
e
l
s
e
 
v
a
l
u
e
.
r
e
p
l
a
c
e
(
"
,
"
,
 
"
.
"
)


 
 
 
 
 
 
 
 
f
o
r
 
c
o
l
u
m
n
,
 
v
a
l
u
e
 
i
n
 
r
o
w
.
i
t
e
m
s
(
)


 
 
 
 
}




d
e
f
 
c
o
n
v
e
r
t
_
c
s
v
_
v
a
l
u
e
s
_
t
o
_
f
l
o
a
t
(
r
o
w
:
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
f
l
o
a
t
]
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
 
n
u
m
e
r
i
c
 
v
a
l
u
e
s
 
i
n
 
a
 
C
S
V
 
r
o
w
 
f
r
o
m
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
t
o
 
a
 
f
l
o
a
t
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
 
(
D
i
c
t
[
s
t
r
,
 
s
t
r
]
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
 
a
 
r
o
w
 
o
f
 
C
S
V
 
d
a
t
a
 
w
h
e
r
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
k
e
y
s
 
a
r
e
 
c
o
l
u
m
n
 
n
a
m
e
s
 
a
n
d
 
v
a
l
u
e
s
 
a
r
e
 
s
t
r
i
n
g
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
f
l
o
a
t
]
]
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
 
w
i
t
h
 
v
a
l
u
e
s
 
c
o
n
v
e
r
t
e
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
a
r
e
 
c
o
n
v
e
r
t
e
d
 
t
o
 
f
l
o
a
t
s
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
o
n
-
n
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
a
r
e
 
s
e
t
 
t
o
 
N
o
n
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


 
 
 
 
 
 
 
 
c
o
l
u
m
n
:
 
N
o
n
e
 
i
f
 
n
o
t
 
v
a
l
u
e
.
i
s
n
u
m
e
r
i
c
(
)
 
e
l
s
e
 
f
l
o
a
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
f
o
r
 
c
o
l
u
m
n
,
 
v
a
l
u
e
 
i
n
 
r
o
w
.
i
t
e
m
s
(
)


 
 
 
 
}




d
e
f
 
c
o
n
v
e
r
t
_
c
s
v
_
v
a
l
u
e
s
_
t
o
_
i
n
t
(
r
o
w
:
 
D
i
c
t
[
s
t
r
,
 
s
t
r
]
)
 
-
>
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
i
n
t
]
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
 
n
u
m
e
r
i
c
 
v
a
l
u
e
s
 
i
n
 
a
 
C
S
V
 
r
o
w
 
f
r
o
m
 
s
t
r
i
n
g
 
f
o
r
m
a
t
 
t
o
 
a
n
 
i
n
t
e
g
e
r
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
o
w
 
(
D
i
c
t
[
s
t
r
,
 
s
t
r
]
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
 
a
 
r
o
w
 
o
f
 
C
S
V
 
d
a
t
a
 
w
h
e
r
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
k
e
y
s
 
a
r
e
 
c
o
l
u
m
n
 
n
a
m
e
s
 
a
n
d
 
v
a
l
u
e
s
 
a
r
e
 
s
t
r
i
n
g
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
O
p
t
i
o
n
a
l
[
i
n
t
]
]
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
 
w
i
t
h
 
v
a
l
u
e
s
 
c
o
n
v
e
r
t
e
d
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
a
r
e
 
c
o
n
v
e
r
t
e
d
 
t
o
 
i
n
t
e
g
e
r
s
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
-
 
N
o
n
-
n
u
m
e
r
i
c
 
s
t
r
i
n
g
s
 
a
r
e
 
s
e
t
 
t
o
 
N
o
n
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


import unittest


class TestConvertCsvValues(unittest.TestCase):

    def test_valid_numeric_strings(self):
        """Test with valid numeric strings including commas."""
        row = {'value1': '1,234', 'value2': '5,678', 'value3': '9,876'}
        expected = {'value1': '1.234', 'value2': '5.678', 'value3': '9.876'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_non_numeric_strings(self):
        """Test with non-numeric strings."""
        row = {'value1': 'not_a_number', 'value2': 'hello', 'value3': 'world'}
        expected = {'value1': None, 'value2': None, 'value3': None}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_mixed_values(self):
        """Test with a mix of numeric and non-numeric strings."""
        row = {'value1': '1,234', 'value2': 'not_a_number', 'value3': '3,14159'}
        expected = {'value1': '1.234', 'value2': None, 'value3': '3.14159'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_no_values(self):
        row = {'value1': 'aaaa', 'value2': 'not_a_number', 'value3': '3,14'}
        expected = {'value1': None, 'value2': None, 'value3': '3.14'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

    def test_edge_cases(self):
        """Test edge cases with empty strings and negative numbers."""
        row = {'value1': '', 'value2': '0.0', 'value3': '1,23'}
        expected = {'value1': None, 'value2': '0.0', 'value3': '1.23'}
        result = convert_csv_values(row)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()