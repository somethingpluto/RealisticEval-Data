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
f
i
l
e
_
s
i
z
e
(
s
i
z
e
_
b
y
t
e
s
:
 
i
n
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
f
i
l
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
t
o
 
a
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
1
2
0


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
2
K
B


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
i
z
e
_
b
y
t
e
s
 
(
i
n
t
)
:
 
T
h
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
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
 
s
i
z
e
 
i
n
 
a
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
 
(
e
.
g
.
,
 
"
2
K
B
"
,
 
"
1
M
B
"
)
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
s
i
z
e
_
b
y
t
e
s
 
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
 
"
0
B
"


 
 
 
 
s
i
z
e
_
n
a
m
e
 
=
 
(
"
B
"
,
 
"
K
B
"
,
 
"
M
B
"
,
 
"
G
B
"
,
 
"
T
B
"
,
 
"
P
B
"
,
 
"
E
B
"
,
 
"
Z
B
"
,
 
"
Y
B
"
)


 
 
 
 
i
 
=
 
i
n
t
(
m
a
t
h
.
f
l
o
o
r
(
m
a
t
h
.
l
o
g
(
s
i
z
e
_
b
y
t
e
s
,
 
1
0
2
4
)
)
)


 
 
 
 
p
 
=
 
m
a
t
h
.
p
o
w
(
1
0
2
4
,
 
i
)


 
 
 
 
s
 
=
 
r
o
u
n
d
(
s
i
z
e
_
b
y
t
e
s
 
/
 
p
,
 
2
)


 
 
 
 
r
e
t
u
r
n
 
"
%
s
%
s
"
 
%
 
(
s
,
 
s
i
z
e
_
n
a
m
e
[
i
]
)






d
e
f
 
g
e
t
_
f
i
l
e
_
s
i
z
e
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
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
o
f
 
a
 
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
 
f
i
l
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
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
 
o
s
.
p
a
t
h
.
g
e
t
s
i
z
e
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
e
f
 
g
e
t
_
f
i
l
e
_
s
i
z
e
_
s
t
r
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


 
 
 
 
G
e
t
s
 
t
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
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
 
f
i
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
 
(
e
.
g
.
,
 
"
2
K
B
"
,
 
"
1
M
B
"
)
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
 
c
o
n
v
e
r
t
_
f
i
l
e
_
s
i
z
e
(
g
e
t
_
f
i
l
e
_
s
i
z
e
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
)






d
e
f
 
g
e
t
_
f
i
l
e
_
e
x
t
e
n
s
i
o
n
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


 
 
 
 
G
e
t
s
 
t
h
e
 
f
i
l
e
 
e
x
t
e
n
s
i
o
n
 
o
f
 
a
 
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
 
f
i
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
i
l
e
 
e
x
t
e
n
s
i
o
n
 
(
e
.
g
.
,
 
"
.
t
x
t
"
,
 
"
.
j
p
g
"
)
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
 
o
s
.
p
a
t
h
.
s
p
l
i
t
e
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
)
[
1
]






d
e
f
 
g
e
t
_
f
i
l
e
_
e
x
t
e
n
s
i
o
n
# Unit test class
import unittest


class TestFileSizeConverter(unittest.TestCase):


    def test_zero_bytes(self):
        self.assertEqual(convert_file_size(0), "0B")

    def test_bytes_less_than_1KB(self):
        self.assertEqual(convert_file_size(512), "512B")

    def test_exactly_1KB(self):
        self.assertEqual(convert_file_size(1024), "1KB")

    def test_2KB(self):
        self.assertEqual(convert_file_size(2048), "2KB")

    def test_exactly_1MB(self):
        self.assertEqual(convert_file_size(1048576), "1MB")

    def test_5MB(self):
        self.assertEqual(convert_file_size(5242880), "5MB")

    def test_exactly_1GB(self):
        self.assertEqual(convert_file_size(1073741824), "1GB")
if __name__ == '__main__':
    unittest.main()