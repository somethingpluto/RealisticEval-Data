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
 
U
n
i
o
n






d
e
f
 
r
e
a
d
_
d
a
t
a
_
f
r
o
m
_
f
i
l
e
(
p
a
t
h
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
]
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
s
 
d
a
t
a
 
f
r
o
m
 
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
 
f
i
l
e
 
a
n
d
 
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
 
t
h
e
 
t
y
p
e
 
o
f
 
e
a
c
h
 
l
i
n
e
.


 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
p
r
o
c
e
s
s
e
s
 
e
a
c
h
 
l
i
n
e
 
o
f
 
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
 
f
i
l
e
 
a
n
d
 
a
t
t
e
m
p
t
s
 
t
o
 
c
o
n
v
e
r
t
 
i
t


 
 
 
 
i
n
t
o
 
e
i
t
h
e
r
 
a
n
 
i
n
t
e
g
e
r
,
 
a
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
,
 
o
r
 
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
 
f
i
l
e
 
t
o
 
b
e
 
r
e
a
d
.
 
T
h
e
 
f
i
l
e
 
s
h
o
u
l
d
 
e
x
i
s
t
 
a
n
d
 
b
e
 
a
c
c
e
s
s
i
b
l
e
 
f
o
r
 
r
e
a
d
i
n
g
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
 
c
o
n
v
e
r
t
e
d
 
v
a
l
u
e
s
 
o
f
 
e
a
c
h
 
l
i
n
e
 
i
n
 
t
h
e
 
f
i
l
e
.
 
E
a
c
h
 
e
l
e
m
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
n
 
b
e
 
a
n
 
i
n
t
,
 
f
l
o
a
t
,
 
o
r
 
s
t
r
,
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
l
i
n
e
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
F
i
l
e
N
o
t
F
o
u
n
d
E
r
r
o
r
:
 
I
f
 
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
 
f
i
l
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 
P
e
r
m
i
s
s
i
o
n
E
r
r
o
r
:
 
I
f
 
t
h
e
 
p
r
o
g
r
a
m
 
l
a
c
k
s
 
p
e
r
m
i
s
s
i
o
n
s
 
t
o
 
r
e
a
d
 
t
h
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 
I
O
E
r
r
o
r
:
 
I
f
 
a
n
 
I
/
O
 
e
r
r
o
r
 
o
c
c
u
r
s
 
w
h
i
l
e
 
r
e
a
d
i
n
g
 
t
h
e
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
p
a
t
h
,
 
'
r
'
)
 
a
s
 
f
i
l
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
c
o
n
v
e
r
t
_
l
i
n
e
_
t
o
_
t
y
p
e
(
l
i
n
e
)
 
f
o
r
 
l
i
n
e
 
i
n
 
f
i
l
e
]






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
l
i
n
e
_
t
o
_
t
y
p
e
(
l
i
n
e
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
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
s
 
a
 
l
i
n
e
 
o
f
 
t
e
x
t
 
i
n
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
,
 
a
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
,
 
o
r
 
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


 
 
 
 
 
 
 
 
l
i
n
e
 
(
s
t
r
)
:
 
T
h
e
 
l
i
n
e
 
o
f
 
t
e
x
t
 
t
o
 
b
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
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
,
 
f
l
o
a
t
,
 
o
r
 
s
t
r
:
 
T
h
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
 
l
i
n
e
.
 
I
f
 
t
h
e
 
l
i
n
e
 
c
a
n
n
o
t
 
b
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
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
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
 
l
i
n
e
 
i
s
 
r
e
t
u
r
n
e
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
l
i
n
e
)


 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
l
o
a
t
(
l
i
n
e
)


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
l
i
n
e






d
e
f
 
w
r
i
t
e
_
d
a
t
a
_
t
o
_
f
i
l
e
(
p
a
t
h
:
 
s
t
r
,
 
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
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
]
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
W
r
i
t
e
s
 
d
a
t
a
 
t
o
 
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
 
f
i
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
i
l
e
 
t
o
 
b
e
 
w
r
i
t
t
e
n
.
 
T
h
e
 
f
i
l
e
 
s
h
o
u
l
d
 
e
x
i
s
t
 
a
n
d
 
b
e
 
a
c
c
e
s
s
i
b
l
e
 
f
o
r
 
w
r
i
t
i
n
g
.


 
 
 
 
 
 
 
 
d
a
t
a
 
(
l
i
s
t
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
 
d
a
t
a
 
t
o
 
b
e
 
w
r
i
t
t
e
n
 
t
o
 
t
h
e
 
f
i
l
e
.
 
E
a
c
h
 
e
l
e
m
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
n
 
b
e
 
a
n
 
i
n
t
,
 
f
l
o
a
t
,
 
o
r
 
s
t
r
,
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
f
i
l
e
.




 
 
 
 
R
a
i
s
e
s
:


import os
import unittest


class Tester(unittest.TestCase):

    def create_test_file(self, file_name, content):
        with open(file_name, 'w') as writer:
            writer.write(content)

    def test_read_valid_integers(self):
        file_path = "valid_integers.txt"
        self.create_test_file(file_path, "42\n-7\n0\n100\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual(42, result[0])
        self.assertEqual(-7, result[1])
        self.assertEqual(0, result[2])
        self.assertEqual(100, result[3])
        os.remove(file_path)  # Clean up the test file

    def test_read_valid_floats(self):
        file_path = "valid_floats.txt"
        self.create_test_file(file_path, "3.14\n-0.001\n2.71828\n0.0\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual(3.14, result[0])
        self.assertEqual(-0.001, result[1])
        self.assertEqual(2.71828, result[2])
        self.assertEqual(0.0, result[3])
        os.remove(file_path)  # Clean up the test file

    def test_read_mixed_data(self):
        file_path = "mixed_data.txt"
        self.create_test_file(file_path, "Hello\n42\n3.14\nWorld\n-19.99\n")
        result = read_data_from_file(file_path)
        self.assertEqual(5, len(result))
        self.assertEqual("Hello", result[0])
        self.assertEqual(42, result[1])
        self.assertEqual(3.14, result[2])
        self.assertEqual("World", result[3])
        self.assertEqual(-19.99, result[4])
        os.remove(file_path)  # Clean up the test file

    def test_read_empty_file(self):
        file_path = "empty_file.txt"
        self.create_test_file(file_path, "")
        result = read_data_from_file(file_path)
        self.assertEqual(0, len(result))
        os.remove(file_path)  # Clean up the test file

    def test_read_invalid_data(self):
        file_path = "invalid_data.txt"
        self.create_test_file(file_path, "Hello\n42a\n3.14.15\nWorld!\n")
        result = read_data_from_file(file_path)
        self.assertEqual(4, len(result))
        self.assertEqual("Hello", result[0])
        self.assertEqual("42a", result[1])
        self.assertEqual("3.14.15", result[2])
        self.assertEqual("World!", result[3])
        os.remove(file_path)  # Clean up the test file

if __name__ == '__main__':
    unittest.main()