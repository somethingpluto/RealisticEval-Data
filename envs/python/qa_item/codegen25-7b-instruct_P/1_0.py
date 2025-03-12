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
 
U
n
i
o
n






d
e
f
 
n
u
m
e
r
i
c
a
l
_
s
t
r
_
c
o
n
v
e
r
t
(
v
a
l
u
e
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
t
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
,
 
f
i
r
s
t
 
s
e
e
 
i
f
 
i
t
 
i
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
,
 
i
f
 
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
 
a
n
 
i
n
t
e
g
e
r
,
 
i
f
 
i
t
 
i
s
 
n
o
t
,
 
s
e
e
 
i
f
 
i
t
 
i
s
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
y
e
s
,
 
c
o
n
v
e
r
t
 
t
o
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
n
e
i
t
h
e
r
,
 
r
e
t
u
r
n
 
t
h
e
 
o
r
i
g
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
s
t
r
)
:
 
i
n
p
u
t
 
v
a
l
u
e
 
s
t
r


 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:
 
c
o
n
v
e
r
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
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
v
a
l
u
e
)


 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
l
o
a
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
V
a
l
u
e
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e






d
e
f
 
g
e
t
_
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
(
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
t
h
e
 
i
n
p
u
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
,
 
f
i
r
s
t
 
s
e
e
 
i
f
 
i
t
 
i
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
,
 
i
f
 
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
 
a
n
 
i
n
t
e
g
e
r
,
 
i
f
 
i
t
 
i
s
 
n
o
t
,
 
s
e
e
 
i
f
 
i
t
 
i
s
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
y
e
s
,
 
c
o
n
v
e
r
t
 
t
o
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
n
e
i
t
h
e
r
,
 
r
e
t
u
r
n
 
t
h
e
 
o
r
i
g
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
(
s
t
r
)
:
 
i
n
p
u
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:
 
c
o
n
v
e
r
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
n
u
m
e
r
i
c
a
l
_
s
t
r
_
c
o
n
v
e
r
t
(
m
o
d
e
l
_
a
n
s
w
e
r
_
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
 
g
e
t
_
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
_
w
i
t
h
_
u
n
i
t
(
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
t
h
e
 
i
n
p
u
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
,
 
f
i
r
s
t
 
s
e
e
 
i
f
 
i
t
 
i
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
,
 
i
f
 
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
 
a
n
 
i
n
t
e
g
e
r
,
 
i
f
 
i
t
 
i
s
 
n
o
t
,
 
s
e
e
 
i
f
 
i
t
 
i
s
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
y
e
s
,
 
c
o
n
v
e
r
t
 
t
o
 
a
 
f
l
o
a
t
i
n
g
 
p
o
i
n
t
 
n
u
m
b
e
r
,
 
i
f
 
n
e
i
t
h
e
r
,
 
r
e
t
u
r
n
 
t
h
e
 
o
r
i
g
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
 
(
s
t
r
)
:
 
i
n
p
u
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:
 
c
o
n
v
e
r
t
 
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
n
u
m
e
r
i
c
a
l
_
s
t
r
_
c
o
n
v
e
r
t
(
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
.
s
p
l
i
t
(
"
 
"
)
[
0
]
)






d
e
f
 
g
e
t
_
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
_
w
i
t
h
_
u
n
i
t
_
a
n
d
_
u
n
i
t
_
t
y
p
e
(
m
o
d
e
l
_
a
n
s
w
e
r
_
r
e
s
u
l
t
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
i
n
t
,
 
f
l
o
a
t
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
t
h
e
import unittest


class TestSmartConvert(unittest.TestCase):
    def test_convert_integer(self):
        self.assertEqual(numerical_str_convert("123"), 123, "Should convert to integer")

    def test_convert_float(self):
        self.assertEqual(numerical_str_convert("123.45"), 123.45, "Should convert to float")

    def test_convert_non_numeric_string(self):
        self.assertEqual(numerical_str_convert("abc"), "abc", "Should remain a string")

    def test_convert_negative_integer(self):
        self.assertEqual(numerical_str_convert("-456"), -456, "Should convert to negative integer")

    def test_convert_negative_float(self):
        self.assertEqual(numerical_str_convert("-456.78"), -456.78, "Should convert to negative float")

if __name__ == '__main__':
    unittest.main()