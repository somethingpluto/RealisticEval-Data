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
 
g
e
t
_
c
o
m
m
o
n
_
c
o
l
u
m
n
s
_
f
r
o
m
_
c
s
v
s
(
d
i
r
e
c
t
o
r
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
:


 
 
 
 
"
"
"


 
 
 
 
f
i
n
d
 
t
h
e
 
c
o
m
m
o
n
 
c
o
l
u
m
n
s
 
o
f
 
a
l
l
 
c
s
v
 
f
i
l
e
s
 
i
n
 
a
 
d
i
r
e
c
t
o
r
y
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
s
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
s
 
a
 
l
i
s
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
 
(
s
t
r
)
:
 
d
i
r
e
c
t
o
r
y
 
p
a
t
h




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
s
a
m
e
 
c
o
l
u
m
n
 
l
i
s
t


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
o
s


 
 
 
 
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


 
 
 
 
i
m
p
o
r
t
 
g
l
o
b




 
 
 
 
f
i
l
e
s
 
=
 
g
l
o
b
.
g
l
o
b
(
o
s
.
p
a
t
h
.
j
o
i
n
(
d
i
r
e
c
t
o
r
y
,
 
'
*
.
c
s
v
'
)
)


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
c
s
v
(
f
i
l
e
s
[
0
]
)


 
 
 
 
c
o
l
u
m
n
s
 
=
 
d
f
.
c
o
l
u
m
n
s
.
t
o
l
i
s
t
(
)


 
 
 
 
f
o
r
 
f
i
l
e
 
i
n
 
f
i
l
e
s
[
1
:
]
:


 
 
 
 
 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
c
s
v
(
f
i
l
e
)


 
 
 
 
 
 
 
 
c
o
l
u
m
n
s
 
=
 
l
i
s
t
(
s
e
t
(
c
o
l
u
m
n
s
)
 
&
 
s
e
t
(
d
f
.
c
o
l
u
m
n
s
.
t
o
l
i
s
t
(
)
)
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
s






d
e
f
 
g
e
t
_
c
o
m
m
o
n
_
c
o
l
u
m
n
s
_
f
r
o
m
_
c
s
v
s
_
w
i
t
h
_
e
x
c
l
u
s
i
o
n
(
d
i
r
e
c
t
o
r
y
:
 
s
t
r
,
 
e
x
c
l
u
s
i
o
n
_
l
i
s
t
:
 
L
i
s
t
)
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
f
i
n
d
 
t
h
e
 
c
o
m
m
o
n
 
c
o
l
u
m
n
s
 
o
f
 
a
l
l
 
c
s
v
 
f
i
l
e
s
 
i
n
 
a
 
d
i
r
e
c
t
o
r
y
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
s
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
s
 
a
 
l
i
s
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
 
(
s
t
r
)
:
 
d
i
r
e
c
t
o
r
y
 
p
a
t
h


 
 
 
 
 
 
 
 
e
x
c
l
u
s
i
o
n
_
l
i
s
t
 
(
L
i
s
t
)
:
 
l
i
s
t
 
o
f
 
c
o
l
u
m
n
s
 
t
o
 
e
x
c
l
u
d
e




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
s
a
m
e
 
c
o
l
u
m
n
 
l
i
s
t


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
o
s


 
 
 
 
i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d


 
 
 
 
i
m
p
o
r
t
 
g
l
o
b




 
 
 
 
f
i
l
e
s
 
=
 
g
l
o
b
.
g
l
o
b
(
o
s
.
p
a
t
h
.
j
o
i
n
(
d
i
r
e
c
t
o
r
y
,
 
'
*
.
c
s
v
'
)
)


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
c
s
v
(
f
i
l
e
s
[
0
]
)


 
 
 
 
c
o
l
u
m
n
s
 
=
 
d
f
.
c
o
l
u
m
n
s
.
t
o
l
i
s
t
(
)


 
 
 
 
f
o
r
 
f
i
l
e
 
i
n
 
f
i
l
e
s
[
1
:
]
:


 
 
 
 
 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
c
s
v
(
f
i
l
e
)


 
 
 
 
 
 
 
 
c
o
l
u
m
n
s
 
=
 
l
i
s
t
(
s
e
t
(
c
o
l
u
m
n
s
)
 
&
 
s
e
t
(
d
f
.
c
o
l
u
m
n
s
.
t
o
l
i
s
t
(
)
)
)


 
 
 
 
c
o
l
u
m
n
s
 
=
 
[
c
o
l
 
f
o
r
 
c
o
l
 
i
n
 
c
o
l
u
m
n
s
 
i
f
 
c
o
l
 
n
o
t
 
i
n
 
e
x
c
l
u
s
i
o
n
_
l
i
s
t
]


 
 
 
 
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
s






d
e
f
 
g
e
t
_
c
o
m
m
o
n
_
c
o
l
u
m
n
s
_
f
r
o
m
_
c
s
v
s
_
w
i
t
h
_
e
x
c
l
u
s
i
o
n
_
a
n
d
_
p
r
e
f
i
x
(
d
i
r
e
c
t
o
r
y
:
 
s
t
r
,
 
e
x
c
l
u
s
i
o
n
_
l
i
s
t
:
 
L
i
s
t
,
 
p
r
e
f
i
x
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
:


 
 
 
 
"
"
"


 
 
 
 
f
i
n
d
 
t
h
e
 
c
o
m
m
o
n
 
c
o
l
u
m
n
s
 
o
f
 
a
l
l
 
c
s
v
 
f
i
l
e
s
 
i
n
 
a
 
d
i
r
e
c
t
o
r
y
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
s
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
s
 
a
 
l
i
s
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
 
(
s
t
r
)
:
 
d
i
r
e
c
t
o
r
y
 
p
a
t
h


 
 
 
 
 
 
 
 
e
x
c
l
u
s
i
o
n
_
l
i
s
t
 
(
L
i
s
t
)
:
 
l
i
s
t
import unittest
import pandas as pd
import os


class TestCommonColumns(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove created files and directory after each test.js
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def test_all_same_columns(self):
        # All CSV files have the same columns
        data1 = "A,B,C\n1,2,3"
        data2 = "A,B,C\n4,5,6"
        data3 = "A,B,C\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(set(get_common_columns_from_csvs(self.test_dir)), set(['C', 'B', 'A']))

    def test_no_common_columns(self):
        # No common columns
        data1 = "A,B,C\n1,2,3"
        data2 = "D,E,F\n4,5,6"
        data3 = "G,H,I\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(get_common_columns_from_csvs(self.test_dir), [])

    def test_some_common_columns(self):
        # Some common columns
        data1 = "A,B,C\n1,2,3"
        data2 = "B,C,D\n4,5,6"
        data3 = "C,D,E\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(get_common_columns_from_csvs(self.test_dir), ['C'])

    def test_mixed_common_and_unique_columns(self):
        # Mixed common and unique columns
        data1 = "A,B,C\n1,2,3"
        data2 = "B,C,D\n4,5,6"
        data3 = "B,C,E\n7,8,9"
        filenames = ['file1.csv', 'file2.csv', 'file3.csv']
        datas = [data1, data2, data3]
        for filename, data in zip(filenames, datas):
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(data)
        self.assertEqual(set(get_common_columns_from_csvs(self.test_dir)), set(['B', 'C']))

if __name__ == '__main__':
    unittest.main()