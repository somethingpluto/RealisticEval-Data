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
 
g
e
t
_
a
l
l
_
a
l
p
h
a
b
e
t
s
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
l
e
n
g
t
h
 
5
2
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
l
o
w
e
r
c
a
s
e
 
a
n
d
 
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
l
p
h
a
b
e
t
i
c
a
l
 
o
r
d
e
r
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
 
A
 
l
i
s
t
 
o
f
 
a
l
p
h
a
b
e
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
s
 
f
r
o
m
 
'
a
'
 
t
o
 
'
z
'
 
a
n
d
 
'
A
'
 
t
o
 
'
Z
'
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
 
[
c
h
r
(
i
)
 
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
o
r
d
(
'
a
'
)
,
 
o
r
d
(
'
z
'
)
 
+
 
1
)
]
 
+
 
[
c
h
r
(
i
)
 
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
o
r
d
(
'
A
'
)
,
 
o
r
d
(
'
Z
'
)
 
+
 
1
)
]






d
e
f
 
g
e
t
_
a
l
l
_
n
u
m
b
e
r
s
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
n
u
m
b
e
r
s
 
f
r
o
m
 
0
 
t
o
 
9
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
 
A
 
l
i
s
t
 
o
f
 
a
l
l
 
n
u
m
b
e
r
s
 
f
r
o
m
 
0
 
t
o
 
9
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
 
[
s
t
r
(
i
)
 
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
0
)
]






d
e
f
 
g
e
t
_
a
l
l
_
s
y
m
b
o
l
s
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
s
y
m
b
o
l
s
 
f
r
o
m
 
!
 
t
o
 
~
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
 
A
 
l
i
s
t
 
o
f
 
a
l
l
 
s
y
m
b
o
l
s
 
f
r
o
m
 
!
 
t
o
 
~
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
 
[
c
h
r
(
i
)
 
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
3
3
,
 
1
2
6
 
+
 
1
)
]






d
e
f
 
g
e
t
_
a
l
l
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
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
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
 
A
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
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
 
g
e
t
_
a
l
l
_
a
l
p
h
a
b
e
t
s
(
)
 
+
 
g
e
t
_
a
l
l
_
n
u
m
b
e
r
s
(
)
 
+
 
g
e
t
_
a
l
l
_
s
y
m
b
o
l
s
(
)






d
e
f
 
g
e
t
_
a
l
l
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
_
e
x
c
e
p
t
_
s
p
a
c
e
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
 
e
x
c
e
p
t
 
s
p
a
c
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
 
A
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
 
e
x
c
e
p
t
 
s
p
a
c
e
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
 
g
e
t
_
a
l
l
_
a
l
p
h
a
b
e
t
s
(
)
 
+
 
g
e
t
_
a
l
l
_
n
u
m
b
e
r
s
(
)
 
+
 
g
e
t
_
a
l
l
_
s
y
m
b
o
l
s
(
)
 
+
 
[
'
 
'
]






d
e
f
 
g
e
t
_
a
l
l
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
_
e
x
c
e
p
t
_
n
e
w
l
i
n
e
(
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
P
r
o
d
u
c
e
s
 
a
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
 
e
x
c
e
p
t
 
n
e
w
l
i
n
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
 
A
 
l
i
s
t
 
o
f
 
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
 
f
r
o
m
 
!
 
t
o
 
~
 
e
x
c
e
p
t
import unittest


class TestGetAllAlphabets(unittest.TestCase):

    def test_return_length(self):
        result = get_all_alphabets()
        self.assertEqual(len(result), 52)

    def test_lowercase_alphabets(self):
        result = get_all_alphabets()
        lowercase_alphabets = result[:26]
        self.assertEqual(lowercase_alphabets, [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ])

    def test_uppercase_alphabets(self):
        result = get_all_alphabets()
        uppercase_alphabets = result[26:]
        self.assertEqual(uppercase_alphabets, [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])

    def test_first_element(self):
        result = get_all_alphabets()
        self.assertEqual(result[0], 'a')

    def test_last_element(self):
        result = get_all_alphabets()
        self.assertEqual(result[-1], 'Z')

if __name__ == '__main__':
    unittest.main()