d
e
f
 
r
e
m
o
v
e
_
p
a
r
t
s
_
o
f
_
s
t
r
i
n
g
(
*
s
t
r
i
n
g
s
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
m
o
v
e
 
t
h
e
 
p
a
r
t
 
b
e
f
o
r
e
 
t
h
e
 
f
i
r
s
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
 
a
n
d
 
t
h
e
 
f
i
r
s
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
 
f
r
o
m
 
t
h
e
 
s
t
r
i
n
g




 
 
 
 
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
 
1
2
3
4
A
b
C
d
e
5
6
7
8


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
A
b
C
d
e
5
6
7
8


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
*
s
t
r
i
n
g
s
:
 
A
c
c
e
p
t
s
 
o
n
e
 
o
r
 
m
o
r
e
 
s
t
r
i
n
g
s
 
a
s
 
v
a
r
i
a
b
l
e
 
a
r
g
u
m
e
n
t
s


 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
s
t
r
i
n
g
 
i
n
 
s
t
r
i
n
g
s
:


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
.
s
t
r
i
p
(
)


 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
s
t
r
i
n
g
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
0
]
.
i
s
u
p
p
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
1
:
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
0
]
.
i
s
l
o
w
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
1
:
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
-
1
]
.
i
s
u
p
p
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
:
-
1
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
-
1
]
.
i
s
l
o
w
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
:
-
1
]


 
 
 
 
 
 
 
 
y
i
e
l
d
 
s
t
r
i
n
g






d
e
f
 
r
e
m
o
v
e
_
p
a
r
t
s
_
o
f
_
s
t
r
i
n
g
_
i
n
_
l
i
s
t
(
s
t
r
i
n
g
s
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
m
o
v
e
 
t
h
e
 
p
a
r
t
 
b
e
f
o
r
e
 
t
h
e
 
f
i
r
s
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
 
a
n
d
 
t
h
e
 
f
i
r
s
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
 
f
r
o
m
 
t
h
e
 
s
t
r
i
n
g




 
 
 
 
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
 
[
'
1
2
3
4
A
b
C
d
e
5
6
7
8
'
,
 
'
A
b
C
d
e
5
6
7
8
'
]


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
[
'
A
b
C
d
e
5
6
7
8
'
,
 
'
A
b
C
d
e
5
6
7
8
'
]


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
s
:
 
A
c
c
e
p
t
s
 
o
n
e
 
o
r
 
m
o
r
e
 
s
t
r
i
n
g
s
 
a
s
 
v
a
r
i
a
b
l
e
 
a
r
g
u
m
e
n
t
s


 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
f
o
r
 
s
t
r
i
n
g
 
i
n
 
s
t
r
i
n
g
s
:


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
.
s
t
r
i
p
(
)


 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
s
t
r
i
n
g
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
0
]
.
i
s
u
p
p
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
1
:
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
0
]
.
i
s
l
o
w
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
1
:
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
-
1
]
.
i
s
u
p
p
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
:
-
1
]


 
 
 
 
 
 
 
 
i
f
 
s
t
r
i
n
g
[
-
1
]
.
i
s
l
o
w
e
r
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
=
 
s
t
r
i
n
g
[
:
-
1
]


 
 
 
 
 
 
 
 
y
i
e
l
d
 
s
t
r
i
n
g






d
e
f
 
r
e
m
o
v
e
_
p
a
r
t
s
_
o
f
_
s
t
r
i
n
g
_
i
n
_
d
i
c
t
(
s
t
r
i
n
g
s
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
m
o
v
e
 
t
h
e
 
p
a
r
t
 
b
e
f
o
r
e
 
t
h
e
 
f
i
r
s
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
 
a
n
d
 
t
h
e
 
f
i
r
s
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
 
f
r
o
m
 
t
h
e
 
s
t
r
i
n
g




 
 
 
 
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
 
{
'
1
2
3
4
A
b
C
d
e
5
6
7
8
'
:
 
'
A
b
C
d
e
5
6
7
8
'
}


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
{
'
A
b
C
d
e
5
6
7
8
'
:
 
'
A
b
C
d
e
import unittest


class TestRemovePartsOfString(unittest.TestCase):

    def test_case_3(self):
        # Test with a string that has no uppercase letters
        result = remove_parts_of_string("abcdefg")
        self.assertEqual(result, ["abcdefg"])

    def test_case_4(self):
        # Test with a string that has no lowercase letters
        result = remove_parts_of_string("ABCDEFG")
        self.assertEqual(result, ["ABCDEFG"])

    def test_case_5(self):
        # Test with a string that has mixed cases
        result = remove_parts_of_string("1234AbCde5678")
        self.assertEqual(result, ["AbCde5678"])

    def test_case_6(self):
        # Test with an empty string
        result = remove_parts_of_string("")
        self.assertEqual(result, [""])

    def test_case_7(self):
        # Test with a string that has only one uppercase letter
        result = remove_parts_of_string("X")
        self.assertEqual(result, ["X"])

    def test_case_8(self):
        # Test with a string that has only one lowercase letter
        result = remove_parts_of_string("y")
        self.assertEqual(result, ["y"])

if __name__ == '__main__':
    unittest.main()