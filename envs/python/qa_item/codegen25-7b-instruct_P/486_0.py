c
l
a
s
s
 
C
a
l
c
u
l
a
t
o
r
:


 
 
 
 
d
e
f
 
a
d
d
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
s
u
m
 
o
f
 
a
 
a
n
d
 
b
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
s
u
b
t
r
a
c
t
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
 
o
f
 
a
 
a
n
d
 
b
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
m
u
l
t
i
p
l
y
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
p
r
o
d
u
c
t
 
o
f
 
a
 
a
n
d
 
b
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
d
i
v
i
d
e
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
q
u
o
t
i
e
n
t
 
o
f
 
a
 
a
n
d
 
b
.


 
 
 
 
 
 
 
 
R
a
i
s
e
s
 
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
 
i
f
 
b
 
i
s
 
z
e
r
o
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
a
s
s




c
l
a
s
s
 
C
a
l
c
u
l
a
t
o
r
I
m
p
l
e
m
e
n
t
a
t
i
o
n
(
C
a
l
c
u
l
a
t
o
r
)
:


 
 
 
 
d
e
f
 
a
d
d
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
 
+
 
b




 
 
 
 
d
e
f
 
s
u
b
t
r
a
c
t
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
 
-
 
b




 
 
 
 
d
e
f
 
m
u
l
t
i
p
l
y
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
 
*
 
b




 
 
 
 
d
e
f
 
d
i
v
i
d
e
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
i
f
 
b
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
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
(
"
C
a
n
n
o
t
 
d
i
v
i
d
e
 
b
y
 
z
e
r
o
"
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
 
/
 
b




c
l
a
s
s
 
C
a
l
c
u
l
a
t
o
r
A
d
a
p
t
e
r
(
C
a
l
c
u
l
a
t
o
r
)
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
c
a
l
c
u
l
a
t
o
r
:
 
C
a
l
c
u
l
a
t
o
r
I
m
p
l
e
m
e
n
t
a
t
i
o
n
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
 
=
 
c
a
l
c
u
l
a
t
o
r




 
 
 
 
d
e
f
 
a
d
d
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
.
a
d
d
(
a
,
 
b
)




 
 
 
 
d
e
f
 
s
u
b
t
r
a
c
t
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
.
s
u
b
t
r
a
c
t
(
a
,
 
b
)




 
 
 
 
d
e
f
 
m
u
l
t
i
p
l
y
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
.
m
u
l
t
i
p
l
y
(
a
,
 
b
)




 
 
 
 
d
e
f
 
d
i
v
i
d
e
(
s
e
l
f
,
 
a
:
 
f
l
o
a
t
,
 
b
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
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
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
.
d
i
v
i
d
e
(
a
,
 
b
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
 
s
e
l
f
.
c
a
l
c
u
l
a
t
o
r
.
a
d
d
(
a
,
 
b
)




c
l
a
s
s
 
C
a
l
c
u
l
a
t
o
r
C
o
m
p
o
s
i
t
i
o
n
(
C
a
l
c
u
l
a
t
o
r
)
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
c
a
l
c
u
l
a
t
o
r
1
:
 
C
a
l
c
u
l
a
t
o
r
,
 
c
a
l
c
u
l
a
t
o
r
2
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of Calculator before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the addition method."""
        result = self.calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        """Test the subtraction method."""
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        """Test the multiplication method."""
        result = self.calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        """Test the division method."""
        result = self.calculator.divide(10, 5)
        self.assertEqual(result, 2.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        self.assertRaises(Exception)
if __name__ == '__main__':
    unittest.main()