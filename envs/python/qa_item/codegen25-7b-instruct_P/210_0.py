d
e
f
 
f
i
b
o
n
a
c
c
i
_
r
e
c
u
r
s
i
v
e
(
n
:
 
i
n
t
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
t
h
e
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
W
h
i
c
h
 
F
i
b
o
n
a
c
c
i
 
n
u
m
b
e
r
 
t
o
 
c
a
l
c
u
l
a
t
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
 
f
i
b
o
n
a
c
c
i
 
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
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
 
0


 
 
 
 
e
l
i
f
 
n
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
b
o
n
a
c
c
i
_
r
e
c
u
r
s
i
v
e
(
n
 
-
 
1
)
 
+
 
f
i
b
o
n
a
c
c
i
_
r
e
c
u
r
s
i
v
e
(
n
 
-
 
2
)






d
e
f
 
f
i
b
o
n
a
c
c
i
_
i
t
e
r
a
t
i
v
e
(
n
:
 
i
n
t
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
t
h
e
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
W
h
i
c
h
 
F
i
b
o
n
a
c
c
i
 
n
u
m
b
e
r
 
t
o
 
c
a
l
c
u
l
a
t
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
 
f
i
b
o
n
a
c
c
i
 
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
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
 
0


 
 
 
 
e
l
i
f
 
n
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
0
,
 
1


 
 
 
 
 
 
 
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
2
,
 
n
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
 
=
 
a
 
+
 
b


 
 
 
 
 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
b
,
 
c


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
b






d
e
f
 
f
i
b
o
n
a
c
c
i
_
m
a
t
r
i
x
(
n
:
 
i
n
t
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
t
h
e
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
W
h
i
c
h
 
F
i
b
o
n
a
c
c
i
 
n
u
m
b
e
r
 
t
o
 
c
a
l
c
u
l
a
t
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
 
f
i
b
o
n
a
c
c
i
 
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
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
 
0


 
 
 
 
e
l
i
f
 
n
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
0
,
 
1


 
 
 
 
 
 
 
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
2
,
 
n
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
 
=
 
a
 
+
 
b


 
 
 
 
 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
b
,
 
c


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
b






d
e
f
 
f
i
b
o
n
a
c
c
i
_
m
a
t
r
i
x
_
o
p
t
i
m
i
z
e
d
(
n
:
 
i
n
t
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


 
 
 
 
I
m
p
l
e
m
e
n
t
 
t
h
e
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
 
(
i
n
t
)
:
 
W
h
i
c
h
 
F
i
b
o
n
a
c
c
i
 
n
u
m
b
e
r
 
t
o
 
c
a
l
c
u
l
a
t
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
 
f
i
b
o
n
a
c
c
i
 
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
 
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
 
0


 
 
 
 
e
l
i
f
 
n
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
0
,
 
1


 
 
 
 
 
 
 
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
2
,
 
n
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
 
=
 
a
 
+
 
b


 
 
 
 
 
 
 
 
 
 
 
 
a
,
 
b
 
=
 
b
,
 
c


 
 
 
 
 
 
 
 
r
e
t
u
r
n
import unittest


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        """Test Case 1: Fibonacci of 0 should be 0"""
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_fibonacci_1(self):
        """Test Case 2: Fibonacci of 1 should be 1"""
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fibonacci_5(self):
        """Test Case 3: Fibonacci of 5 should be 5"""
        self.assertEqual(fibonacci_recursive(5), 5)

    def test_fibonacci_10(self):
        """Test Case 4: Fibonacci of 10 should be 55"""
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_fibonacci_20(self):
        """Test Case 5: Fibonacci of 20 should be 6765"""
        self.assertEqual(fibonacci_recursive(20), 6765)

if __name__ == '__main__':
    unittest.main()