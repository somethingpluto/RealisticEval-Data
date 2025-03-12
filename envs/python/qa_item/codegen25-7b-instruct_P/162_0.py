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
 
b
o
o
l
_
a
r
r
a
y
_
t
o
_
b
i
n
a
r
y
_
s
t
r
i
n
g
(
b
o
o
l
_
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
[
b
o
o
l
]
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


 
 
 
 
C
o
n
v
e
r
t
s
 
t
h
e
 
a
r
r
a
y
 
o
f
 
B
o
o
l
e
a
n
 
v
a
l
u
e
s
 
t
o
 
a
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
,


 
 
 
 
w
h
i
c
h
 
c
o
n
v
e
r
t
s
 
t
o
 
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
 
'
1
'
 
i
f
 
t
h
e
 
B
o
o
l
e
a
n
 
v
a
l
u
e
 
i
s
 
t
r
u
e
.


 
 
 
 
O
t
h
e
r
w
i
s
e
,
 
i
t
 
i
s
 
c
o
n
v
e
r
t
e
d
 
t
o
 
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
 
'
0
'
,
 
a
n
d
 
t
h
e
 
f
i
n
a
l
 
s
t
r
i
n
g
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
o
o
l
_
a
r
r
a
y
 
(
l
i
s
t
[
b
o
o
l
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
b
o
o
l
e
a
n
 
v
a
l
u
e
s
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
 
A
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
w
h
e
r
e
 
'
1
'
 
r
e
p
r
e
s
e
n
t
s
 
t
r
u
e
 
a
n
d
 
'
0
'
 
r
e
p
r
e
s
e
n
t
s
 
f
a
l
s
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
 
"
"
.
j
o
i
n
(
[
"
1
"
 
i
f
 
b
 
e
l
s
e
 
"
0
"
 
f
o
r
 
b
 
i
n
 
b
o
o
l
_
a
r
r
a
y
]
)






d
e
f
 
b
i
n
a
r
y
_
s
t
r
i
n
g
_
t
o
_
b
o
o
l
_
a
r
r
a
y
(
b
i
n
a
r
y
_
s
t
r
i
n
g
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
b
o
o
l
]
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
a
 
l
i
s
t
 
o
f
 
B
o
o
l
e
a
n
 
v
a
l
u
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
A
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
w
h
e
r
e
 
'
1
'
 
r
e
p
r
e
s
e
n
t
s
 
t
r
u
e
 
a
n
d
 
'
0
'
 
r
e
p
r
e
s
e
n
t
s
 
f
a
l
s
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
b
o
o
l
]
:
 
A
 
l
i
s
t
 
o
f
 
B
o
o
l
e
a
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
 
[
b
o
o
l
(
i
n
t
(
b
)
)
 
f
o
r
 
b
 
i
n
 
b
i
n
a
r
y
_
s
t
r
i
n
g
]






d
e
f
 
b
i
n
a
r
y
_
s
t
r
i
n
g
_
t
o
_
i
n
t
(
b
i
n
a
r
y
_
s
t
r
i
n
g
:
 
s
t
r
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
a
n
 
i
n
t
e
g
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
n
a
r
y
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
A
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
w
h
e
r
e
 
'
1
'
 
r
e
p
r
e
s
e
n
t
s
 
t
r
u
e
 
a
n
d
 
'
0
'
 
r
e
p
r
e
s
e
n
t
s
 
f
a
l
s
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
 
A
n
 
i
n
t
e
g
e
r
 
w
h
e
r
e
 
'
1
'
 
r
e
p
r
e
s
e
n
t
s
 
t
r
u
e
 
a
n
d
 
'
0
'
 
r
e
p
r
e
s
e
n
t
s
 
f
a
l
s
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
 
i
n
t
(
b
i
n
a
r
y
_
s
t
r
i
n
g
,
 
2
)






d
e
f
 
i
n
t
_
t
o
_
b
i
n
a
r
y
_
s
t
r
i
n
g
(
i
n
t
e
g
e
r
:
 
i
n
t
,
 
n
u
m
_
b
i
t
s
:
 
i
n
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
n
 
i
n
t
e
g
e
r
 
t
o
 
a
 
b
i
n
a
r
y
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
t
e
g
e
r
 
(
i
n
t
)
:
 
A
n
 
i
n
t
e
g
e
r
.


 
 
 
 
 
 
 
 
n
u
m
_
b
i
t
s
 
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
 
b
i
t
s
 
t
o
 
u
s
e
 
i
n
 
t
h
e
 
b
i
n
a
r
y
 
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
 
A
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
w
h
e
r
e
 
'
1
'
 
r
e
p
r
e
s
e
n
t
s
 
t
r
u
e
 
a
n
d
 
'
0
'
 
r
e
p
r
e
s
e
n
t
s
 
f
a
l
s
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
 
f
o
r
m
a
t
(
i
n
t
e
g
e
r
,
 
f
"
0
{
n
u
m
_
b
i
t
s
}
b
"
)






d
e
f
 
b
i
n
a
r
y
_
s
t
r
i
n
g
_
t
o
_
h
e
x
(
b
i
n
a
r
y
_
s
t
r
i
n
g
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
b
i
n
a
r
y
 
s
t
r
i
n
g
 
t
o
 
a
 
h
e
x
a
d
e
c
i
m
a
l
import unittest


class TestBoolArrayToBinaryString(unittest.TestCase):

    def test_converts_all_true_values(self):
        bool_array = [True, True, True]
        expected = '111'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_all_false_values(self):
        bool_array = [False, False, False]
        expected = '000'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_mixed_true_and_false_values(self):
        bool_array = [True, False, True, False]
        expected = '1010'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_empty_array(self):
        bool_array = []
        expected = ''
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_single_boolean_value(self):
        bool_array = [True]
        expected = '1'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

if __name__ == '__main__':
    unittest.main()