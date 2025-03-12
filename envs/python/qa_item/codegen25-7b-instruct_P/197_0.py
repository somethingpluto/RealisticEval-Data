d
e
f
 
j
o
s
e
p
h
u
s
(
n
:
 
i
n
t
,
 
k
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


 
 
 
 
S
i
m
u
l
a
t
e
s
 
t
h
e
 
J
o
s
e
p
h
u
s
 
p
r
o
b
l
e
m
 
u
s
i
n
g
 
a
 
l
i
s
t
 
t
o
 
r
e
p
r
e
s
e
n
t
 
t
h
e
 
c
i
r
c
l
e
 
o
f
 
p
e
o
p
l
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
 
T
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
 
p
e
o
p
l
e
 
i
n
 
t
h
e
 
c
i
r
c
l
e
 
(
1
 
t
o
 
n
)
.


 
 
 
 
 
 
 
 
k
 
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
t
e
p
 
c
o
u
n
t
 
(
e
v
e
r
y
 
k
-
t
h
 
p
e
r
s
o
n
 
w
i
l
l
 
b
e
 
e
l
i
m
i
n
a
t
e
d
)
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
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
e
 
l
a
s
t
 
p
e
r
s
o
n
 
r
e
m
a
i
n
i
n
g
 
(
1
-
i
n
d
e
x
e
d
)
.


 
 
 
 
"
"
"


 
 
 
 
p
e
o
p
l
e
 
=
 
l
i
s
t
(
r
a
n
g
e
(
1
,
 
n
 
+
 
1
)
)


 
 
 
 
w
h
i
l
e
 
l
e
n
(
p
e
o
p
l
e
)
 
>
 
1
:


 
 
 
 
 
 
 
 
p
e
o
p
l
e
 
=
 
p
e
o
p
l
e
[
k
 
-
 
1
 
:
:
 
k
]
 
+
 
p
e
o
p
l
e
[
:
 
k
 
-
 
1
 
:
]


 
 
 
 
r
e
t
u
r
n
 
p
e
o
p
l
e
[
0
]






d
e
f
 
j
o
s
e
p
h
u
s
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
,
 
k
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


 
 
 
 
S
i
m
u
l
a
t
e
s
 
t
h
e
 
J
o
s
e
p
h
u
s
 
p
r
o
b
l
e
m
 
u
s
i
n
g
 
r
e
c
u
r
s
i
o
n
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
 
T
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
 
p
e
o
p
l
e
 
i
n
 
t
h
e
 
c
i
r
c
l
e
 
(
1
 
t
o
 
n
)
.


 
 
 
 
 
 
 
 
k
 
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
t
e
p
 
c
o
u
n
t
 
(
e
v
e
r
y
 
k
-
t
h
 
p
e
r
s
o
n
 
w
i
l
l
 
b
e
 
e
l
i
m
i
n
a
t
e
d
)
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
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
e
 
l
a
s
t
 
p
e
r
s
o
n
 
r
e
m
a
i
n
i
n
g
 
(
1
-
i
n
d
e
x
e
d
)
.


 
 
 
 
"
"
"


 
 
 
 
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


 
 
 
 
r
e
t
u
r
n
 
(
j
o
s
e
p
h
u
s
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
,
 
k
)
 
+
 
k
 
-
 
1
)
 
%
 
n
 
+
 
1






d
e
f
 
j
o
s
e
p
h
u
s
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
_
m
e
m
o
(
n
:
 
i
n
t
,
 
k
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


 
 
 
 
S
i
m
u
l
a
t
e
s
 
t
h
e
 
J
o
s
e
p
h
u
s
 
p
r
o
b
l
e
m
 
u
s
i
n
g
 
r
e
c
u
r
s
i
o
n
 
a
n
d
 
m
e
m
o
i
z
a
t
i
o
n
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
 
T
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
 
p
e
o
p
l
e
 
i
n
 
t
h
e
 
c
i
r
c
l
e
 
(
1
 
t
o
 
n
)
.


 
 
 
 
 
 
 
 
k
 
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
t
e
p
 
c
o
u
n
t
 
(
e
v
e
r
y
 
k
-
t
h
 
p
e
r
s
o
n
 
w
i
l
l
 
b
e
 
e
l
i
m
i
n
a
t
e
d
)
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
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
e
 
l
a
s
t
 
p
e
r
s
o
n
 
r
e
m
a
i
n
i
n
g
 
(
1
-
i
n
d
e
x
e
d
)
.


 
 
 
 
"
"
"


 
 
 
 
m
e
m
o
 
=
 
{
}




 
 
 
 
d
e
f
 
j
o
s
e
p
h
u
s
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
_
m
e
m
o
_
h
e
l
p
e
r
(
n
:
 
i
n
t
,
 
k
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


 
 
 
 
 
 
 
 
i
f
 
n
 
i
n
 
m
e
m
o
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
m
o
[
n
]


 
 
 
 
 
 
 
 
m
e
m
o
[
n
]
 
=
 
(
j
o
s
e
p
h
u
s
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
_
m
e
m
o
_
h
e
l
p
e
r
(
n
 
-
 
1
,
 
k
)
 
+
 
k
 
-
 
1
)
 
%
 
n
 
+
 
1


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
m
o
[
n
]




 
 
 
 
r
e
t
u
r
n
 
j
# Unit Test Class
import unittest


class TestJosephusProblem(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(josephus(7, 3), 4)  # Standard case

    def test_case_2(self):
        self.assertEqual(josephus(1, 1), 1)  # Only one person

    def test_case_3(self):
        self.assertEqual(josephus(5, 2), 3)  # Smaller group, step 2

    def test_case_4(self):
        self.assertEqual(josephus(10, 5), 3)  # Larger group, step 5

    def test_case_5(self):
        self.assertEqual(josephus(6, 1), 6)  # Eliminate every 1st person

    def test_case_6(self):
        self.assertEqual(josephus(8, 4), 6)  # Step 4 in a group of 8

    def test_case_7(self):
        self.assertEqual(josephus(12, 7), 12)  # Larger group, arbitrary step
if __name__ == '__main__':
    unittest.main()