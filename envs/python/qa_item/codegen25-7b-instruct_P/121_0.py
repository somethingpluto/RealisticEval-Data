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
 
a
d
j
u
s
t
_
a
r
r
a
y
_
l
e
n
g
t
h
(
t
a
r
g
e
t
_
l
e
n
g
t
h
:
 
i
n
t
,
 
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


 
 
 
 
A
d
j
u
s
t
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
g
i
v
e
n
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
I
f
 
t
h
e
 
c
u
r
r
e
n
t
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
l
o
n
g
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
,


 
 
 
 
t
h
e
 
f
i
r
s
t
 
p
a
r
t
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
i
n
t
e
r
c
e
p
t
e
d
 
t
o
 
m
a
t
c
h
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
I
f
 
t
h
e
 
c
u
r
r
e
n
t
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
s
h
o
r
t
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
,


 
 
 
 
t
h
e
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
a
r
e
 
r
e
p
e
a
t
e
d
 
u
n
t
i
l
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
 
i
s
 
r
e
a
c
h
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
l
e
n
g
t
h
 
(
i
n
t
)
:
 
T
h
e
 
d
e
s
i
r
e
d
 
l
e
n
g
t
h
 
f
o
r
 
t
h
e
 
a
r
r
a
y
.


 
 
 
 
 
 
 
 
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
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
t
o
 
b
e
 
a
d
j
u
s
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
:
 
A
 
n
e
w
 
a
r
r
a
y
 
t
h
a
t
 
h
a
s
 
b
e
e
n
 
a
d
j
u
s
t
e
d
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
a
r
r
a
y
)
 
>
 
t
a
r
g
e
t
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
r
r
a
y
[
:
t
a
r
g
e
t
_
l
e
n
g
t
h
]


 
 
 
 
e
l
i
f
 
l
e
n
(
a
r
r
a
y
)
 
<
 
t
a
r
g
e
t
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
r
r
a
y
 
*
 
(
t
a
r
g
e
t
_
l
e
n
g
t
h
 
/
/
 
l
e
n
(
a
r
r
a
y
)
)
 
+
 
a
r
r
a
y
[
:
t
a
r
g
e
t
_
l
e
n
g
t
h
 
%
 
l
e
n
(
a
r
r
a
y
)
]


 
 
 
 
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
 
a
r
r
a
y






d
e
f
 
a
d
j
u
s
t
_
a
r
r
a
y
_
l
e
n
g
t
h
_
w
i
t
h
_
p
a
d
d
i
n
g
(
t
a
r
g
e
t
_
l
e
n
g
t
h
:
 
i
n
t
,
 
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
,
 
p
a
d
d
i
n
g
:
 
i
n
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


 
 
 
 
A
d
j
u
s
t
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
g
i
v
e
n
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
I
f
 
t
h
e
 
c
u
r
r
e
n
t
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
l
o
n
g
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
,


 
 
 
 
t
h
e
 
f
i
r
s
t
 
p
a
r
t
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
i
n
t
e
r
c
e
p
t
e
d
 
t
o
 
m
a
t
c
h
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
I
f
 
t
h
e
 
c
u
r
r
e
n
t
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
s
h
o
r
t
e
r
 
t
h
a
n
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
,


 
 
 
 
t
h
e
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
a
r
r
a
y
 
a
r
e
 
r
e
p
e
a
t
e
d
 
u
n
t
i
l
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
 
i
s
 
r
e
a
c
h
e
d
.


 
 
 
 
I
f
 
t
h
e
 
l
e
n
g
t
h
 
o
f
 
t
h
e
 
a
r
r
a
y
 
i
s
 
e
q
u
a
l
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
,
 
t
h
e
 
a
r
r
a
y
 
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
 
a
s
 
i
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
a
r
g
e
t
_
l
e
n
g
t
h
 
(
i
n
t
)
:
 
T
h
e
 
d
e
s
i
r
e
d
 
l
e
n
g
t
h
 
f
o
r
 
t
h
e
 
a
r
r
a
y
.


 
 
 
 
 
 
 
 
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
)
:
 
T
h
e
 
i
n
p
u
t
 
a
r
r
a
y
 
t
o
 
b
e
 
a
d
j
u
s
t
e
d
.


 
 
 
 
 
 
 
 
p
a
d
d
i
n
g
 
(
i
n
t
)
:
 
T
h
e
 
v
a
l
u
e
 
t
o
 
b
e
 
u
s
e
d
 
f
o
r
 
p
a
d
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


 
 
 
 
 
 
 
 
L
i
s
t
:
 
A
 
n
e
w
 
a
r
r
a
y
 
t
h
a
t
 
h
a
s
 
b
e
e
n
 
a
d
j
u
s
t
e
d
 
t
o
 
t
h
e
 
t
a
r
g
e
t
 
l
e
n
g
t
h
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
a
r
r
a
y
)
 
>
 
t
a
r
g
e
t
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
r
r
a
y
[
:
t
a
r
g
e
t
_
l
e
n
g
t
h
]


 
 
 
 
e
l
i
f
 
l
e
n
(
a
r
r
a
y
)
 
<
 
t
a
r
g
e
t
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
r
r
a
y
 
*
 
(
t
a
r
g
e
t
_
l
e
n
g
t
h
 
/
/
 
l
e
n
(
a
r
r
a
y
)
)
 
+
 
a
r
r
a
y
[
:
t
a
r
g
e
t
_
l
e
n
g
t
h
 
%
 
l
e
n
(
a
r
r
a
y
)
]
 
+
 
[
p
a
d
d
i
n
g
]
 
*
 
(
t
a
r
g
e
t
_
l
e
n
g
t
h
 
-
 
l
e
n
(
import unittest


class TestAdjustArrayLength(unittest.TestCase):

    def test_array_length_equal_to_target_length(self):
        result = adjust_array_length(5, [1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_array_length_shorter_than_target_length(self):
        result = adjust_array_length(8, [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 1, 2, 3, 1, 2])

    def test_array_length_shorter_than_target_length_multiple(self):
        result = adjust_array_length(6, [10, 20])
        self.assertEqual(result, [10, 20, 10, 20, 10, 20])

    def test_array_length_shorter_than_target_length_not_multiple(self):
        result = adjust_array_length(7, [7, 14, 21])
        self.assertEqual(result, [7, 14, 21, 7, 14, 21, 7])

if __name__ == '__main__':
    unittest.main()