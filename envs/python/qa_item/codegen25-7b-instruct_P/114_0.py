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
 
D
i
c
t






d
e
f
 
s
o
r
t
_
b
y
_
t
i
m
e
s
t
a
m
p
(
a
r
r
a
y
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
y
 
t
h
e
 
'
t
i
m
e
s
t
a
m
p
'
 
p
r
o
p
e
r
t
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
a
y
 
(
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
 
T
h
e
 
s
o
r
t
e
d
 
l
i
s
t
,
 
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
 
'
t
i
m
e
s
t
a
m
p
'
 
p
r
o
p
e
r
t
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
 
s
o
r
t
e
d
(
a
r
r
a
y
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
'
t
i
m
e
s
t
a
m
p
'
]
)






d
e
f
 
s
o
r
t
_
b
y
_
t
i
m
e
s
t
a
m
p
_
d
e
s
c
(
a
r
r
a
y
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
y
 
t
h
e
 
'
t
i
m
e
s
t
a
m
p
'
 
p
r
o
p
e
r
t
y
 
i
n
 
d
e
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
 
T
h
e
 
s
o
r
t
e
d
 
l
i
s
t
,
 
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
 
'
t
i
m
e
s
t
a
m
p
'
 
p
r
o
p
e
r
t
y
 
i
n
 
d
e
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
 
s
o
r
t
e
d
(
a
r
r
a
y
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
'
t
i
m
e
s
t
a
m
p
'
]
,
 
r
e
v
e
r
s
e
=
T
r
u
e
)






d
e
f
 
s
o
r
t
_
b
y
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
a
y
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
:
 
s
t
r
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
y
 
t
h
e
 
v
a
l
u
e
 
o
f
 
a
 
g
i
v
e
n
 
k
e
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
a
y
 
(
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
 
b
e
 
s
o
r
t
e
d
.


 
 
 
 
 
 
 
 
k
e
y
 
(
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
 
t
o
 
s
o
r
t
 
b
y
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
]
:
 
T
h
e
 
s
o
r
t
e
d
 
l
i
s
t
,
 
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
 
v
a
l
u
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
k
e
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
 
s
o
r
t
e
d
(
a
r
r
a
y
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
k
e
y
]
)






d
e
f
 
s
o
r
t
_
b
y
_
v
a
l
u
e
_
d
e
s
c
(
a
r
r
a
y
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
:
 
s
t
r
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
y
 
t
h
e
 
v
a
l
u
e
 
o
f
 
a
 
g
i
v
e
n
 
k
e
y
 
i
n
 
d
e
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
 
b
e
 
s
o
r
t
e
d
.


 
 
 
 
 
 
 
 
k
e
y
 
(
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
 
t
o
 
s
o
r
t
 
b
y
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
]
:
 
T
h
e
 
s
o
r
t
e
d
 
l
i
s
t
,
 
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
 
v
a
l
u
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
k
e
y
 
i
n
 
d
e
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
 
s
o
r
t
e
d
(
a
r
r
a
y
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
k
e
y
]
,
 
r
e
v
e
r
s
e
=
T
r
u
e
)






d
e
f
 
s
o
r
t
_
b
y
_
import unittest


class TestSortByTimestamp(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_by_timestamp([]), [])

    def test_single_element_array(self):
        single_element_array = [{'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}]
        self.assertEqual(sort_by_timestamp(single_element_array), [{'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}])

    def test_sort_multiple_elements(self):
        test_data = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 1, 'timestamp': "2021-07-03T12:00:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"}
        ]
        expected = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"},
            {'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}
        ]
        self.assertEqual(sort_by_timestamp(test_data), expected)

    def test_already_sorted_array(self):
        sorted_array = [
            {'id': 1, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"},
            {'id': 3, 'timestamp': "2021-07-03T12:00:00Z"}
        ]
        self.assertEqual(sort_by_timestamp(sorted_array), sorted_array)

    def test_mixed_format_timestamps(self):
        mixed_formats = [
            {'id': 1, 'timestamp': "2021/07/03 12:00:00"},
            {'id': 2, 'timestamp': "July 2, 2021 15:30:00"},
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"}
        ]
        expected = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "July 2, 2021 15:30:00"},
            {'id': 1, 'timestamp': "2021/07/03 12:00:00"}
        ]
        self.assertEqual(sort_by_timestamp(mixed_formats), expected)

if __name__ == '__main__':
    unittest.main()