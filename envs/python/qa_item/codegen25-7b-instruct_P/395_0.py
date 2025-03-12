d
e
f
 
s
u
m
_
c
a
l
i
b
r
a
t
i
o
n
_
v
a
l
u
e
s
(
c
a
l
i
b
r
a
t
i
o
n
_
d
o
c
u
m
e
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
u
m
s
 
u
p
 
c
a
l
i
b
r
a
t
i
o
n
 
v
a
l
u
e
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
d
o
c
u
m
e
n
t
.


 
 
 
 
E
a
c
h
 
c
a
l
i
b
r
a
t
i
o
n
 
v
a
l
u
e
 
i
s
 
f
o
r
m
e
d
 
b
y
 
c
o
m
b
i
n
i
n
g
 
t
h
e
 
f
i
r
s
t
 
a
n
d
 
l
a
s
t
 
d
i
g
i
t
s
 
o
f
 
n
u
m
b
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
o
 
a
 
t
w
o
-
d
i
g
i
t
 
n
u
m
b
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
a
l
i
b
r
a
t
i
o
n
_
d
o
c
u
m
e
n
t
 
(
i
t
e
r
a
b
l
e
)
:
 
A
n
 
i
t
e
r
a
b
l
e
 
o
f
 
s
t
r
i
n
g
s
,
 
e
a
c
h
 
r
e
p
r
e
s
e
n
t
i
n
g
 
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
 
s
u
m
 
o
f
 
a
l
l
 
c
a
l
i
b
r
a
t
i
o
n
 
v
a
l
u
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
 
s
u
m
(
i
n
t
(
l
i
n
e
[
0
]
 
+
 
l
i
n
e
[
-
1
]
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
 
c
a
l
i
b
r
a
t
i
o
n
_
d
o
c
u
m
e
n
t
)






d
e
f
 
m
a
i
n
(
)
:


 
 
 
 
"
"
"


 
 
 
 
M
a
i
n
 
e
n
t
r
y
 
p
o
i
n
t
 
f
o
r
 
t
h
e
 
s
c
r
i
p
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
R
e
a
d
 
t
h
e
 
i
n
p
u
t
 
f
i
l
e


 
 
 
 
w
i
t
h
 
o
p
e
n
(
I
N
P
U
T
_
F
I
L
E
,
 
'
r
'
)
 
a
s
 
i
n
p
u
t
_
f
i
l
e
:


 
 
 
 
 
 
 
 
d
o
c
u
m
e
n
t
 
=
 
i
n
p
u
t
_
f
i
l
e
.
r
e
a
d
l
i
n
e
s
(
)




 
 
 
 
#
 
E
x
t
r
a
c
t
 
t
h
e
 
c
a
l
i
b
r
a
t
i
o
n
 
v
a
l
u
e
s


 
 
 
 
c
a
l
i
b
r
a
t
i
o
n
_
v
a
l
u
e
s
 
=
 
e
x
t
r
a
c
t
_
c
a
l
i
b
r
a
t
i
o
n
_
v
a
l
u
e
s
(
d
o
c
u
m
e
n
t
)




 
 
 
 
#
 
P
r
i
n
t
 
t
h
e
 
r
e
s
u
l
t


 
 
 
 
p
r
i
n
t
(
s
u
m
_
c
a
l
i
b
r
a
t
i
o
n
_
v
a
l
u
e
s
(
c
a
l
i
b
r
a
t
i
o
n
_
v
a
l
u
e
s
)
)






i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
'
_
_
m
a
i
n
_
_
'
:


 
 
 
 
m
a
i
n
(
)


import unittest

class TestSumCalibrationValues(unittest.TestCase):

    def test_basic_calculations(self):
        # Test with a simple input where lines contain at least two digits
        document = [
            "Reading 1234 calibration",
            "Measure 5678 complete",
            "End of data 91011"
        ]
        self.assertEqual(sum_calibration_values(document), 163)

    def test_no_digits(self):
        # Test lines with no digits
        document = [
            "No numbers here",
            "Still no numbers"
        ]
        self.assertEqual(sum_calibration_values(document), 0)

    def test_empty_lines(self):
        # Test with empty lines or lines with spaces
        document = [
            "",
            "   "
        ]
        self.assertEqual(sum_calibration_values(document), 0)

    def test_mixed_content(self):
        # Test with a mixture of valid and invalid lines
        document = [
            "Good line 1524 end",
            "Bad line",
            "Another good line 7681"
        ]
        self.assertEqual(sum_calibration_values(document), 85)
if __name__ == '__main__':
    unittest.main()