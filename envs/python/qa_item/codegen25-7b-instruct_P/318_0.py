d
e
f
 
c
o
u
n
t
_
n
u
m
b
e
r
s
(
s
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
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
n
u
m
e
r
i
c
 
d
i
g
i
t
s
 
i
n
 
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


 
 
 
 
 
 
 
 
s
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
c
o
u
n
t
 
n
u
m
e
r
i
c
 
d
i
g
i
t
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
o
t
a
l
 
c
o
u
n
t
 
o
f
 
n
u
m
e
r
i
c
 
d
i
g
i
t
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
c
 
i
n
 
s
:


 
 
 
 
 
 
 
 
i
f
 
c
.
i
s
d
i
g
i
t
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t






d
e
f
 
c
o
u
n
t
_
v
o
w
e
l
s
(
s
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
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
v
o
w
e
l
s
 
i
n
 
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


 
 
 
 
 
 
 
 
s
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
c
o
u
n
t
 
v
o
w
e
l
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
o
t
a
l
 
c
o
u
n
t
 
o
f
 
v
o
w
e
l
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
c
 
i
n
 
s
:


 
 
 
 
 
 
 
 
i
f
 
c
 
i
n
 
"
a
e
i
o
u
A
E
I
O
U
"
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t






d
e
f
 
c
o
u
n
t
_
c
o
n
s
o
n
a
n
t
s
(
s
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
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
c
o
n
s
o
n
a
n
t
s
 
i
n
 
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


 
 
 
 
 
 
 
 
s
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
c
o
u
n
t
 
c
o
n
s
o
n
a
n
t
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
o
t
a
l
 
c
o
u
n
t
 
o
f
 
c
o
n
s
o
n
a
n
t
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
c
 
i
n
 
s
:


 
 
 
 
 
 
 
 
i
f
 
c
 
i
n
 
"
b
c
d
f
g
h
j
k
l
m
n
p
q
r
s
t
v
w
x
y
z
B
C
D
F
G
H
J
K
L
M
N
P
Q
R
S
T
V
W
X
Y
Z
"
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t






d
e
f
 
c
o
u
n
t
_
u
p
p
e
r
c
a
s
e
(
s
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
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
s
 
i
n
 
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


 
 
 
 
 
 
 
 
s
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
c
o
u
n
t
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
o
t
a
l
 
c
o
u
n
t
 
o
f
 
u
p
p
e
r
c
a
s
e
 
l
e
t
t
e
r
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
f
o
r
 
c
 
i
n
 
s
:


 
 
 
 
 
 
 
 
i
f
 
c
 
i
n
 
"
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
"
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t






d
e
f
 
c
o
u
n
t
_
l
o
w
e
r
c
a
s
e
(
s
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
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r
s
 
i
n
 
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


 
 
 
 
 
 
 
 
s
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
c
o
u
n
t
 
l
o
w
e
r
c
a
s
e
 
l
e
t
t
e
r
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
t
o
t
a
l
 
c
o
u
n
t
 
o
f
 
l
o
w
e
r
import unittest


class TestCountNumbers(unittest.TestCase):

    def test_multiple_numbers(self):
        result = count_numbers('There are 123 numbers in this string.')
        self.assertEqual(result, 3)  # '123' contains three numeric characters

    def test_no_numbers(self):
        result = count_numbers('No numbers here!')
        self.assertEqual(result, 0)  # No numeric characters in 'No numbers here!'

    def test_mixed_characters(self):
        result = count_numbers('Room 101 and Room 102')
        self.assertEqual(result, 6)  # '101' and '102' together contain six numeric characters

    def test_only_numbers(self):
        result = count_numbers('1234567890')
        self.assertEqual(result, 10)  # '1234567890' contains ten numeric characters

    def test_empty_string(self):
        result = count_numbers('')
        self.assertEqual(result, 0)  # An empty string contains no numeric characters

if __name__ == '__main__':
    unittest.main()