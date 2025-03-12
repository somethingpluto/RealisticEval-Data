f
r
o
m
 
c
o
l
l
e
c
t
i
o
n
s
 
i
m
p
o
r
t
 
C
o
u
n
t
e
r






d
e
f
 
m
i
n
_
w
i
n
d
o
w
(
s
:
 
s
t
r
,
 
t
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


 
 
 
 
F
i
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
w
i
n
d
o
w
 
s
u
b
s
t
r
i
n
g
 
i
n
 
`
s
`
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
a
l
l
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
`
t
`
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
 
i
n
p
u
t
 
s
t
r
i
n
g
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
t
h
e
 
s
u
b
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
t
 
(
s
t
r
)
:
 
T
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
 
w
h
o
s
e
 
c
h
a
r
a
c
t
e
r
s
 
m
u
s
t
 
b
e
 
i
n
c
l
u
d
e
d
 
i
n
 
t
h
e
 
s
u
b
s
t
r
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
m
i
n
i
m
u
m
 
w
i
n
d
o
w
 
s
u
b
s
t
r
i
n
g
 
o
f
 
`
s
`
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
a
l
l
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
`
t
`
.
R
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
s
u
c
h
 
s
u
b
s
t
r
i
n
g
 
e
x
i
s
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
s
 
o
r
 
n
o
t
 
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"




 
 
 
 
#
 
C
o
u
n
t
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
f
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
t
.


 
 
 
 
f
r
e
q
 
=
 
C
o
u
n
t
e
r
(
t
)




 
 
 
 
#
 
N
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
t
.


 
 
 
 
d
i
s
t
i
n
c
t
_
c
h
a
r
a
c
t
e
r
s
 
=
 
l
e
n
(
f
r
e
q
)




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
v
a
r
i
a
b
l
e
s
.


 
 
 
 
s
t
a
r
t
 
=
 
0


 
 
 
 
m
i
n
_
l
e
n
g
t
h
 
=
 
f
l
o
a
t
(
"
i
n
f
"
)


 
 
 
 
m
i
n
_
s
u
b
s
t
r
i
n
g
 
=
 
"
"




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
s
t
o
r
e
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
f
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
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
 
w
i
n
d
o
w
.


 
 
 
 
w
i
n
d
o
w
_
f
r
e
q
 
=
 
{
}




 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
a
 
v
a
r
i
a
b
l
e
 
t
o
 
s
t
o
r
e
 
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
 
c
u
r
r
e
n
t
 
w
i
n
d
o
w
.


 
 
 
 
w
i
n
d
o
w
_
l
e
n
g
t
h
 
=
 
0




 
 
 
 
#
 
T
r
a
v
e
r
s
e
 
t
h
r
o
u
g
h
 
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


 
 
 
 
f
o
r
 
e
n
d
,
 
c
h
a
r
 
i
n
 
e
n
u
m
e
r
a
t
e
(
s
)
:




 
 
 
 
 
 
 
 
#
 
I
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
s
 
i
n
 
t
,
 
i
n
c
r
e
m
e
n
t
 
i
t
s
 
f
r
e
q
u
e
n
c
y
 
i
n
 
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
 
w
i
n
d
o
w
.


 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
i
n
 
f
r
e
q
:


 
 
 
 
 
 
 
 
 
 
 
 
w
i
n
d
o
w
_
f
r
e
q
[
c
h
a
r
]
 
=
 
w
i
n
d
o
w
_
f
r
e
q
.
g
e
t
(
c
h
a
r
,
 
0
)
 
+
 
1




 
 
 
 
 
 
 
 
#
 
I
f
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
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
 
c
h
a
r
a
c
t
e
r
 
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
 
f
r
e
q
u
e
n
c
y
 
o
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
 
c
h
a
r
a
c
t
e
r
 
i
n
 
t
,
 
i
n
c
r
e
m
e
n
t
 
t
h
e
 
w
i
n
d
o
w
 
l
e
n
g
t
h
.


 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
i
n
 
f
r
e
q
 
a
n
d
 
w
i
n
d
o
w
_
f
r
e
q
[
c
h
a
r
]
 
=
=
 
f
r
e
q
[
c
h
a
r
]
:


 
 
 
 
 
 
 
 
 
 
 
 
w
i
n
d
o
w
_
l
e
n
g
t
h
 
+
=
 
1




 
 
 
 
 
 
 
 
#
 
W
h
i
l
e
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
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
 
w
i
n
d
o
w
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
o
r
 
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
 
f
r
e
q
u
e
n
c
y
 
o
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
t
,
 
a
n
d
 
t
h
e
 
w
i
n
d
o
w
 
l
e
n
g
t
h
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
o
r
 
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
 
l
e
n
g
t
h
 
o
f
 
t
,
 
d
o
 
t
h
e
 
f
o
l
l
o
w
i
n
g
:


 
 
 
 
 
 
 
 
w
h
i
l
e
 
w
i
n
d
o
w
_
f
r
e
q
.
v
a
l
u
e
s
(
)
.
c
o
u
n
t
(
0
)
 
<
 
d
i
s
t
i
n
c
t
_
c
h
a
r
a
c
t
e
r
s
 
a
n
d
 
w
i
n
d
o
w
_
l
e
n
g
t
h
 
>
=
 
l
e
n
(
t
)
:




 
 
 
 
 
 
 
 
 
 
 
 
#
 
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
 
c
u
r
r
e
n
t
 
w
i
n
d
o
w
 
i
s
 
l
e
s
s
 
t
h
a
n
 
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
 
m
i
n
i
m
u
m
 
s
u
b
s
t
r
i
n
g
 
f
o
u
n
d
 
s
o
 
f
a
r
,
 
u
p
d
a
t
e
 
t
h
e
 
m
i
n
i
m
u
m
 
s
u
b
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
e
n
d
 
-
 
s
t
a
r
t
 
+
 
1
 
<
 
m
i
n
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
i
n
_
l
e
n
g
t
h
 
=
 
e
n
d
 
-
 
s
t
a
r
t
 
+
import unittest


class TestMinWindow(unittest.TestCase):

    def test_basic_case(self):
        """Test with a normal case where the minimum window exists."""
        s = "ADOBECODEBANC"
        t = "ABC"
        expected_output = "BANC"
        self.assertEqual(min_window(s, t), expected_output)

    def test_no_window_exists(self):
        """Test where no window can satisfy the condition."""
        s = "A"
        t = "AA"
        expected_output = ""
        self.assertEqual(min_window(s, t), expected_output)

    def test_empty_string(self):
        """Test with an empty input string s."""
        s = ""
        t = "ABC"
        expected_output = ""
        self.assertEqual(min_window(s, t), expected_output)


    def test_multiple_valid_windows(self):
        """Test with multiple valid windows to ensure the smallest one is returned."""
        s = "AA"
        t = "AA"
        expected_output = "AA"
        self.assertEqual(min_window(s, t), expected_output)

if __name__ == '__main__':
    unittest.main()