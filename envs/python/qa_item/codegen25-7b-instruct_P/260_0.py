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






d
e
f
 
p
r
o
c
e
s
s
_
c
s
v
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
,
 
o
u
t
p
u
t
_
p
a
t
h
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
c
e
s
s
e
s
 
a
 
C
S
V
 
f
i
l
e
 
a
n
d
 
r
e
m
o
v
e
s
 
r
o
w
s
 
w
i
t
h
 
t
w
o
 
o
r
 
m
o
r
e
 
e
m
p
t
y
 
c
o
l
u
m
n
s
.
I
f
 
f
i
l
e
 
i
s
 
e
m
p
t
y
 
r
e
t
u
r
n
 
e
m
p
t
y
 
s
t
r




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
C
S
V
 
f
i
l
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
p
r
o
c
e
s
s
e
d
 
C
S
V
 
f
i
l
e
 
w
i
l
l
 
b
e
 
s
a
v
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
_
p
a
t
h
)


 
 
 
 
d
f
 
=
 
d
f
.
d
r
o
p
n
a
(
a
x
i
s
=
0
,
 
h
o
w
=
'
a
l
l
'
,
 
t
h
r
e
s
h
=
2
)


 
 
 
 
d
f
.
t
o
_
c
s
v
(
o
u
t
p
u
t
_
p
a
t
h
,
 
i
n
d
e
x
=
F
a
l
s
e
)






d
e
f
 
p
r
o
c
e
s
s
_
x
l
s
x
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
,
 
o
u
t
p
u
t
_
p
a
t
h
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
c
e
s
s
e
s
 
a
n
 
E
x
c
e
l
 
f
i
l
e
 
a
n
d
 
r
e
m
o
v
e
s
 
r
o
w
s
 
w
i
t
h
 
t
w
o
 
o
r
 
m
o
r
e
 
e
m
p
t
y
 
c
o
l
u
m
n
s
.
 
I
f
 
f
i
l
e
 
i
s
 
e
m
p
t
y
 
r
e
t
u
r
n
 
e
m
p
t
y
 
s
t
r




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
E
x
c
e
l
 
f
i
l
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
p
r
o
c
e
s
s
e
d
 
E
x
c
e
l
 
f
i
l
e
 
w
i
l
l
 
b
e
 
s
a
v
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
e
x
c
e
l
(
f
i
l
e
_
p
a
t
h
)


 
 
 
 
d
f
 
=
 
d
f
.
d
r
o
p
n
a
(
a
x
i
s
=
0
,
 
h
o
w
=
'
a
l
l
'
,
 
t
h
r
e
s
h
=
2
)


 
 
 
 
d
f
.
t
o
_
e
x
c
e
l
(
o
u
t
p
u
t
_
p
a
t
h
,
 
i
n
d
e
x
=
F
a
l
s
e
)






d
e
f
 
p
r
o
c
e
s
s
_
p
d
f
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
,
 
o
u
t
p
u
t
_
p
a
t
h
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
c
e
s
s
e
s
 
a
 
P
D
F
 
f
i
l
e
 
a
n
d
 
r
e
m
o
v
e
s
 
r
o
w
s
 
w
i
t
h
 
t
w
o
 
o
r
 
m
o
r
e
 
e
m
p
t
y
 
c
o
l
u
m
n
s
.
 
I
f
 
f
i
l
e
 
i
s
 
e
m
p
t
y
 
r
e
t
u
r
n
 
e
m
p
t
y
 
s
t
r




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
P
D
F
 
f
i
l
e
.


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
p
r
o
c
e
s
s
e
d
 
P
D
F
 
f
i
l
e
 
w
i
l
l
 
b
e
 
s
a
v
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
_
p
a
t
h
,
 
s
e
p
=
'
\
t
'
)


 
 
 
 
d
f
 
=
 
d
f
.
d
r
o
p
n
a
(
a
x
i
s
=
0
,
 
h
o
w
=
'
a
l
l
'
,
 
t
h
r
e
s
h
=
2
)


 
 
 
 
d
f
.
t
o
_
c
s
v
(
o
u
t
p
u
t
_
p
a
t
h
,
 
i
n
d
e
x
=
F
a
l
s
e
)






d
e
f
 
p
r
o
c
e
s
s
_
t
x
t
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
,
 
o
u
t
p
u
t
_
p
a
t
h
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
c
e
s
s
e
s
 
a
 
T
X
T
 
f
i
l
e
 
a
n
d
 
r
e
m
o
v
e
s
 
r
o
w
s
 
w
i
t
h
 
t
w
o
 
o
r
 
m
o
r
e
 
e
m
p
t
y
 
c
o
l
u
m
n
s
.
 
I
f
 
f
i
l
e
 
i
s
 
e
m
p
t
y
 
r
e
t
u
r
n
 
e
m
p
t
y
 
s
t
r




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
import unittest
import pandas as pd
from io import StringIO

import os


# Assuming process_csv function is imported from the module
# from your_module import process_csv

class TestProcessCSV(unittest.TestCase):

    def setUp(self):
        self.input_data_1 = """A,B,C
1,2,3
4,,6
7,8,
9,10,11"""


        self.input_data_2 = """A,B,C,D
,,
1,,3,4
2,3,,5
,,,"""


        self.input_data_3 = """A
1
2
3"""


    def process_data(self, input_data):
        input_file = StringIO(input_data)
        output_file = StringIO()
        input_file_path = "input.csv"
        output_file_path = "output.csv"

        # Write input data to a temp CSV file
        with open(input_file_path, 'w') as f:
            f.write(input_data)

        # Process the CSV
        process_csv(input_file_path, output_file_path)

        # Read the output
        with open(output_file_path, 'r') as f:
            output_data = f.read()

        # Clean up temp files
        os.remove(input_file_path)
        os.remove(output_file_path)

        return output_data

    def test_case_1(self):
        output = self.process_data(self.input_data_1)
        expected_output = """A,B,C\n1,2.0,3.0\n4,,6.0\n7,8.0,\n9,10.0,11.0\n"""
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        output = self.process_data(self.input_data_2)
        expected_output = """A,B,C,D\n1.0,,3.0,4.0\n2.0,3.0,,5.0\n"""
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        output = self.process_data(self.input_data_3)
        expected_output = """A\n1\n2\n3\n"""  # Single-column CSV should remain unchanged
        self.assertEqual(output, expected_output)
if __name__ == '__main__':
    unittest.main()