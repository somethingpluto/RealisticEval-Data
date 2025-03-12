d
e
f
 
l
o
o
k
_
a
n
d
_
s
a
y
(
n
u
m
b
e
r
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
t
h
e
 
n
e
x
t
 
s
e
q
u
e
n
c
e
 
i
n
 
t
h
e
 
'
l
o
o
k
-
a
n
d
-
s
a
y
'
 
s
e
q
u
e
n
c
e
 
b
y
 
r
e
a
d
i
n
g
 
o
f
f
 
t
h
e
 
d
i
g
i
t
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
n
u
m
b
e
r
,


 
 
 
 
g
r
o
u
p
i
n
g
 
b
y
 
c
o
n
s
e
c
u
t
i
v
e
 
d
i
g
i
t
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
(
s
t
r
)
:
 
T
h
e
 
c
u
r
r
e
n
t
 
s
e
q
u
e
n
c
e
 
a
s
 
a
 
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
 
n
e
x
t
 
s
e
q
u
e
n
c
e
 
i
n
 
t
h
e
 
'
l
o
o
k
-
a
n
d
-
s
a
y
'
 
s
e
r
i
e
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
s
u
l
t
 
=
 
[
]


 
 
 
 
c
o
u
n
t
 
=
 
1


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
1
,
 
l
e
n
(
n
u
m
b
e
r
)
)
:


 
 
 
 
 
 
 
 
i
f
 
n
u
m
b
e
r
[
i
]
 
=
=
 
n
u
m
b
e
r
[
i
 
-
 
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
s
t
r
(
c
o
u
n
t
)
)


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
n
u
m
b
e
r
[
i
 
-
 
1
]
)


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
=
 
1


 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
s
t
r
(
c
o
u
n
t
)
)


 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
n
u
m
b
e
r
[
-
1
]
)


 
 
 
 
r
e
t
u
r
n
 
'
'
.
j
o
i
n
(
r
e
s
u
l
t
)






d
e
f
 
l
o
o
k
_
a
n
d
_
s
a
y
_
s
e
q
u
e
n
c
e
(
s
t
a
r
t
:
 
s
t
r
,
 
c
o
u
n
t
:
 
i
n
t
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
 
s
e
q
u
e
n
c
e
 
o
f
 
'
l
o
o
k
-
a
n
d
-
s
a
y
'
 
s
e
q
u
e
n
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
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
 
s
t
a
r
t
i
n
g
 
s
e
q
u
e
n
c
e
.


 
 
 
 
 
 
 
 
c
o
u
n
t
 
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
 
s
e
q
u
e
n
c
e
s
 
t
o
 
g
e
n
e
r
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


 
 
 
 
 
 
 
 
l
i
s
t
[
s
t
r
]
:
 
T
h
e
 
g
e
n
e
r
a
t
e
d
 
s
e
q
u
e
n
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
s
u
l
t
 
=
 
[
s
t
a
r
t
]


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
c
o
u
n
t
 
-
 
1
)
:


 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
l
o
o
k
_
a
n
d
_
s
a
y
(
r
e
s
u
l
t
[
-
1
]
)
)


 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t






d
e
f
 
l
o
o
k
_
a
n
d
_
s
a
y
_
s
e
q
u
e
n
c
e
_
u
n
t
i
l
_
r
e
p
e
a
t
(
s
t
a
r
t
:
 
s
t
r
,
 
c
o
u
n
t
:
 
i
n
t
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
 
s
e
q
u
e
n
c
e
 
o
f
 
'
l
o
o
k
-
a
n
d
-
s
a
y
'
 
s
e
q
u
e
n
c
e
s
 
u
n
t
i
l
 
a
 
r
e
p
e
a
t
 
i
s
 
d
e
t
e
c
t
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
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
 
s
t
a
r
t
i
n
g
 
s
e
q
u
e
n
c
e
.


 
 
 
 
 
 
 
 
c
o
u
n
t
 
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
 
s
e
q
u
e
n
c
e
s
 
t
o
 
g
e
n
e
r
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


 
 
 
 
 
 
 
 
l
i
s
t
[
s
t
r
]
:
 
T
h
e
 
g
e
n
e
r
a
t
e
d
 
s
e
q
u
e
n
c
e
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
s
u
l
t
 
=
 
[
s
t
a
r
t
]


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
c
o
u
n
t
 
-
 
1
)
:


 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
a
p
p
e
n
d
(
l
o
o
k
_
a
n
d
_
s
a
y
(
r
e
s
u
l
t
[
-
1
]
)
)


 
 
 
 
 
 
 
 
i
f
 
r
e
s
u
l
t
[
-
1
]
 
=
=
 
r
e
s
u
l
t
[
0
]
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t


 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t






d
e
f
 
l
o
o
k
_
a
n
d
_
s
a
y
_
s
e
q
u
e
n
c
e
_
u
n
t
i
l
_
r
e
p
e
a
t
_
l
e
n
g
t
h
(
s
t
a
r
t
:
 
s
t
r
,
 
c
o
u
n
t
:
 
i
n
t
)
:


 
 
 
 
"
"
"


 
 
 
 
G
e
n
e
r
a
t
e
s
 
a
 
s
e
q
u
e
n
c
e
 
o
f
 
'
l
o
o
k
-
a
n
d
-
s
a
y
'
 
s
e
q
u
e
n
c
e
s
 
u
n
t
i
l
 
a
import unittest

class TestLookAndSay(unittest.TestCase):

    def test_single_digit(self):
        # Test with a single digit to see if it replicates correctly
        self.assertEqual(look_and_say('1'), '11')

    def test_repetitive_digits(self):
        # Test a sequence of the same digits
        self.assertEqual(look_and_say('111'), '31')

    def test_mixed_digits(self):
        # Test a sequence with different digits
        self.assertEqual(look_and_say('1211'), '111221')

    def test_complex_sequence(self):
        # Test a more complex sequence
        self.assertEqual(look_and_say('312211'), '13112221')

if __name__ == '__main__':
    unittest.main()