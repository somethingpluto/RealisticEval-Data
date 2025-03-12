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
 
c
a
l
c
u
l
a
t
e
_
c
o
l
u
m
n
_
w
i
d
t
h
s
(
d
a
t
a
:
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
C
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
a
x
i
m
u
m
 
w
i
d
t
h
 
o
f
 
e
a
c
h
 
c
o
l
u
m
n
 
i
n
 
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
 
w
h
e
r
e
 
e
a
c
h
 
s
u
b
-
l
i
s
t
 
r
e
p
r
e
s
e
n
t
s
 
a
 
r
o
w
 
o
f
 
t
a
b
l
e
 
d
a
t
a
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
(
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
)
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
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
 
r
o
w
s
 
o
f
 
d
a
t
a
,
 
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
n
n
e
r
 
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
s
 
s
t
r
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
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
e
a
c
h
 
c
o
l
u
m
n
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
i
n
t
]
:
 
A
 
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
 
m
a
x
i
m
u
m
 
w
i
d
t
h
 
(
i
n
 
c
h
a
r
a
c
t
e
r
s
)
 
o
f
 
e
a
c
h
 
c
o
l
u
m
n
 
a
c
r
o
s
s
 
a
l
l
 
r
o
w
s
.
 
T
h
e
 
w
i
d
t
h
 
o
f
 
a
 
c
o
l
u
m
n
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
t
h
e
 
l
o
n
g
e
s
t
 
s
t
r
i
n
g
 
p
r
e
s
e
n
t
 
i
n
 
t
h
a
t
 
c
o
l
u
m
n
.


 
 
 
 
"
"
"


 
 
 
 
c
o
l
u
m
n
_
w
i
d
t
h
s
 
=
 
[
0
]
 
*
 
l
e
n
(
d
a
t
a
[
0
]
)


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
f
o
r
 
i
,
 
v
a
l
u
e
 
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
r
o
w
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
v
a
l
u
e
)
 
>
 
c
o
l
u
m
n
_
w
i
d
t
h
s
[
i
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
l
u
m
n
_
w
i
d
t
h
s
[
i
]
 
=
 
l
e
n
(
v
a
l
u
e
)


 
 
 
 
r
e
t
u
r
n
 
c
o
l
u
m
n
_
w
i
d
t
h
s






d
e
f
 
f
o
r
m
a
t
_
r
o
w
(
v
a
l
u
e
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
,
 
c
o
l
u
m
n
_
w
i
d
t
h
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
F
o
r
m
a
t
 
a
 
r
o
w
 
o
f
 
d
a
t
a
 
i
n
t
o
 
a
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
s
 
(
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
:
 
A
 
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
 
s
t
r
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
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
e
a
c
h
 
c
o
l
u
m
n
.


 
 
 
 
 
 
 
 
c
o
l
u
m
n
_
w
i
d
t
h
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
 
A
 
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
 
m
a
x
i
m
u
m
 
w
i
d
t
h
 
(
i
n
 
c
h
a
r
a
c
t
e
r
s
)
 
o
f
 
e
a
c
h
 
c
o
l
u
m
n
 
a
c
r
o
s
s
 
a
l
l
 
r
o
w
s
.
 
T
h
e
 
w
i
d
t
h
 
o
f
 
a
 
c
o
l
u
m
n
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
t
h
e
 
l
o
n
g
e
s
t
 
s
t
r
i
n
g
 
p
r
e
s
e
n
t
 
i
n
 
t
h
a
t
 
c
o
l
u
m
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
s
t
r
i
n
g
 
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
 
f
o
r
m
a
t
t
e
d
 
r
o
w
 
o
f
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
f
o
r
m
a
t
t
e
d
_
v
a
l
u
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
 
v
a
l
u
e
 
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
v
a
l
u
e
s
)
:


 
 
 
 
 
 
 
 
f
o
r
m
a
t
t
e
d
_
v
a
l
u
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
v
a
l
u
e
.
l
j
u
s
t
(
c
o
l
u
m
n
_
w
i
d
t
h
s
[
i
]
)
)


 
 
 
 
r
e
t
u
r
n
 
"
|
 
"
 
+
 
"
 
|
 
"
.
j
o
i
n
(
f
o
r
m
a
t
t
e
d
_
v
a
l
u
e
s
)
 
+
 
"
 
|
"






d
e
f
 
f
o
r
m
a
t
_
t
a
b
l
e
(
d
a
t
a
:
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
,
 
c
o
l
u
m
n
_
w
i
d
t
h
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
F
o
r
m
a
t
 
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
 
i
n
t
o
 
a
 
t
a
b
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
a
t
a
 
(
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
)
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
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
 
r
o
w
s
 
o
f
 
d
a
t
a
,
 
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
n
n
e
r
 
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
s
 
s
t
r
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
 
t
h
e
 
v
a
l
u
e
s
 
i
n
 
e
a
c
h
 
c
o
l
u
m
n
.


 
 
 
 
 
 
 
 
c
o
l
u
m
n
_
w
i
d
t
h
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
 
A
 
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
 
m
a
x
i
m
u
m
 
w
i
d
t
h
 
(
i
n
 
c
h
a
r
a
c
t
e
r
s
)
 
o
f
import unittest


class TestCalculateColumnWidths(unittest.TestCase):

    def test_standard_case(self):
        data = [["Name", "Age", "City"],
                ["Alice", "22", "New York"],
                ["Bob", "30", "San Francisco"]]
        expected = [5, 3, 13]
        self.assertEqual(calculate_column_widths(data), expected)


    def test_single_element(self):
        data = [["Name"]]
        expected = [4]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_varied_length(self):
        data = [["a", "bb", "ccc"],
                ["dddd", "ee", "f"]]
        expected = [4, 2, 3]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_all_empty_strings(self):
        data = [["", "", ""],
                ["", "", ""]]
        expected = [0, 0, 0]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_mixed_content(self):
        data = [["1234", "567", "890"],
                ["abc", "defg", "h"]]
        expected = [4, 4, 3]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_single_column_multiple_rows(self):
        data = [["one"],
                ["two"],
                ["three"]]
        expected = [5]
        self.assertEqual(calculate_column_widths(data), expected)

if __name__ == '__main__':
    unittest.main()