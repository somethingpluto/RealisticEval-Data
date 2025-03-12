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
 
D
i
c
t






d
e
f
 
c
h
e
c
k
_
s
e
q
u
e
n
c
e
s
(
f
i
l
e
n
a
m
e
:
s
t
r
)
 
-
>
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
 
m
u
l
t
i
p
l
e
 
s
e
q
u
e
n
c
e
s
 
f
r
o
m
 
t
h
e
 
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
 
i
f
 
e
a
c
h
 
s
e
q
u
e
n
c
e
 
i
s
 
a
 
"
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e
"
.
 
T
h
e
 
d
e
f
i
n
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
 
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e
 
i
s
 
b
a
s
e
d
 
o
n
 
a
 
s
p
e
c
i
f
i
c
 
r
e
c
u
r
s
i
v
e
 
r
e
l
a
t
i
o
n
s
h
i
p
,
 
t
h
a
t
 
i
s
,
 
f
o
r
 
e
v
e
n
 
n
u
m
b
e
r
s
,
 
t
h
e
 
n
e
x
t
 
t
e
r
m
 
i
s
 
h
a
l
f
 
o
f
 
i
t
,
 
f
o
r
 
o
d
d
 
n
u
m
b
e
r
s
,
 
t
h
e
 
n
e
x
t
 
t
e
r
m
 
i
s
 
3
*
n
 
+
 
1
,
 
a
n
d
 
t
h
e
 
s
e
q
u
e
n
c
e
 
t
e
r
m
i
n
a
t
e
s
 
w
h
e
n
 
i
t
 
e
n
c
o
u
n
t
e
r
s
 
1
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
 
(
2
,
 
4
,
 
6
,
 
8
)
 
i
s
 
M
u
n
d
i
 
s
e
q
u
e
n
c
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
n
a
m
e
(
s
t
r
)
:
 
f
i
l
e
 
p
a
t
h




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
D
i
c
t
:
 
s
e
q
u
e
n
c
e
s
 
w
e
a
t
h
e
r
 
i
s
 
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e


 
 
 
 
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
f
i
l
e
n
a
m
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
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


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
[
l
i
n
e
.
s
t
r
i
p
(
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
 
l
i
n
e
s
]


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
[
l
i
n
e
.
s
p
l
i
t
(
'
,
'
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
 
l
i
n
e
s
]


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
[
l
i
s
t
(
m
a
p
(
i
n
t
,
 
l
i
n
e
)
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
 
l
i
n
e
s
]


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
[
l
i
n
e
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
 
i
f
 
l
i
n
e
 
!
=
 
[
]
]


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
{
}


 
 
 
 
 
 
 
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
[
t
u
p
l
e
(
l
i
n
e
)
]
 
=
 
c
h
e
c
k
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
l
i
n
e
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
 
c
h
e
c
k
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
e
q
u
e
n
c
e
:
l
i
s
t
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
i
f
 
t
h
e
 
s
e
q
u
e
n
c
e
 
i
s
 
a
 
"
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e
"
.
 
T
h
e
 
d
e
f
i
n
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
 
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e
 
i
s
 
b
a
s
e
d
 
o
n
 
a
 
s
p
e
c
i
f
i
c
 
r
e
c
u
r
s
i
v
e
 
r
e
l
a
t
i
o
n
s
h
i
p
,
 
t
h
a
t
 
i
s
,
 
f
o
r
 
e
v
e
n
 
n
u
m
b
e
r
s
,
 
t
h
e
 
n
e
x
t
 
t
e
r
m
 
i
s
 
h
a
l
f
 
o
f
 
i
t
,
 
f
o
r
 
o
d
d
 
n
u
m
b
e
r
s
,
 
t
h
e
 
n
e
x
t
 
t
e
r
m
 
i
s
 
3
*
n
 
+
 
1
,
 
a
n
d
 
t
h
e
 
s
e
q
u
e
n
c
e
 
t
e
r
m
i
n
a
t
e
s
 
w
h
e
n
 
i
t
 
e
n
c
o
u
n
t
e
r
s
 
1
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
q
u
e
n
c
e
(
l
i
s
t
)
:
 
s
e
q
u
e
n
c
e




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
b
o
o
l
:
 
w
e
a
t
h
e
r
 
s
e
q
u
e
n
c
e
 
i
s
 
a
 
"
M
u
n
o
d
i
 
s
e
q
u
e
n
c
e
"


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
s
e
q
u
e
n
c
e
)
 
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
 
F
a
l
s
e


 
 
 
 
i
f
 
l
e
n
(
s
e
q
u
e
n
c
e
)
 
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
 
T
r
u
e


 
 
 
 
i
f
 
s
e
q
u
e
n
c
e
[
0
]
 
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
 
F
a
l
s
e


 
 
 
 
i
f
 
s
e
q
u
e
n
c
e
[
0
]
 
%
 
2
 
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
 
c
h
e
c
k
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
e
q
u
e
n
c
e
[
1
:
]
)
 
a
n
d
 
c
h
e
c
k
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
[
s
e
q
u
e
n
c
e
[
0
]
 
/
/
 
2
]
 
+
 
s
e
q
u
e
n
c
e
[
2
:
]
)


 
 
 
 
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
 
c
h
e
c
k
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
e
q
u
e
n
c
e
[
1
:
]
)
 
a
n
d
 
c
h
e
c
k
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
[
3
 
*
 
s
e
q
u
e
n
c
e
[
0
]
 
+
 
1
]
 
+
 
s
e
q
u
e
n
c
e
[
2
:
]
)






d
e
f
 
c
h
e
c
k
_
s
e
q
u
e
n
c
e
s
_
r
e
c
import unittest


class TestCheckSequences(unittest.TestCase):
    def setUp(self):
        """Set up the test cases with sequences."""
        # Create a temporary file with test cases
        self.test_file = 'test_sequences.dat'
        with open(self.test_file, 'w') as f:
            f.write("2,4,6,8\n")    # Munodi sequence (d = 2)
            f.write("1,3,5,7\n")    # Munodi sequence (d = 2)
            f.write("10,20,30\n")   # Munodi sequence (d = 10)
            f.write("1,2,4,8\n")    # Not a Munodi sequence (d changes)
            f.write("5,10,15,20\n") # Munodi sequence (d = 5)

    def test_sequences(self):
        """Test the sequences for Munodi property."""
        expected_results = {
            (2, 4, 6, 8): True,
            (1, 3, 5, 7): True,
            (10, 20, 30): True,
            (1, 2, 4, 8): False,
            (5, 10, 15, 20): True,
        }
        results = check_sequences(self.test_file)
        for seq in expected_results:
            self.assertEqual(results[seq], expected_results[seq])

    def tearDown(self):
        """Clean up the test file after tests."""
        import os
        os.remove(self.test_file)
if __name__ == '__main__':
    unittest.main()