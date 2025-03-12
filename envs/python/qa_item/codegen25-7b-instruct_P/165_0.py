d
e
f
 
b
a
s
e
6
4
_
t
o
_
u
r
l
_
s
a
f
e
(
b
a
s
e
6
4
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
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
U
R
L
-
s
a
f
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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


 
 
 
 
 
 
 
 
b
a
s
e
6
4
 
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
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
U
R
L
-
s
a
f
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
,
 
w
h
i
c
h
 
r
e
p
l
a
c
e
s
 
'
+
'
 
w
i
t
h
 
'
-
'
 
a
n
d
 
'
/
'
 
w
i
t
h
 
'
_
'


 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
m
a
y
 
r
e
m
o
v
e
 
a
n
y
 
t
r
a
i
l
i
n
g
 
'
=
'
 
p
a
d
d
i
n
g
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
 
b
a
s
e
6
4
.
r
e
p
l
a
c
e
(
'
+
'
,
 
'
-
'
)
.
r
e
p
l
a
c
e
(
'
/
'
,
 
'
_
'
)






d
e
f
 
u
r
l
_
s
a
f
e
_
t
o
_
b
a
s
e
6
4
(
u
r
l
_
s
a
f
e
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
 
U
R
L
-
s
a
f
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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


 
 
 
 
 
 
 
 
u
r
l
_
s
a
f
e
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
-
s
a
f
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
,
 
w
h
i
c
h
 
r
e
p
l
a
c
e
s
 
'
-
'
 
w
i
t
h
 
'
+
'
 
a
n
d
 
'
_
'
 
w
i
t
h
 
'
/
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
 
u
r
l
_
s
a
f
e
.
r
e
p
l
a
c
e
(
'
-
'
,
 
'
+
'
)
.
r
e
p
l
a
c
e
(
'
_
'
,
 
'
/
'
)






d
e
f
 
b
a
s
e
6
4
_
t
o
_
b
y
t
e
s
(
b
a
s
e
6
4
:
 
s
t
r
)
 
-
>
 
b
y
t
e
s
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
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
i
n
t
o
 
b
y
t
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
a
s
e
6
4
 
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
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
b
y
t
e
s
:
 
T
h
e
 
b
y
t
e
s
 
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
 
o
f
 
t
h
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
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
 
b
a
s
e
6
4
.
e
n
c
o
d
e
(
'
a
s
c
i
i
'
)






d
e
f
 
b
y
t
e
s
_
t
o
_
b
a
s
e
6
4
(
b
y
t
e
s
_
:
 
b
y
t
e
s
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
 
b
y
t
e
s
 
i
n
t
o
 
a
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
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


 
 
 
 
 
 
 
 
b
y
t
e
s
_
 
(
b
y
t
e
s
)
:
 
T
h
e
 
b
y
t
e
s
 
t
o
 
b
e
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
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
 
b
a
s
e
6
4
.
b
6
4
e
n
c
o
d
e
(
b
y
t
e
s
_
)
.
d
e
c
o
d
e
(
'
a
s
c
i
i
'
)






d
e
f
 
b
a
s
e
6
4
_
t
o
_
h
e
x
(
b
a
s
e
6
4
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
 
s
t
a
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
i
n
t
o
 
a
 
h
e
x
 
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


 
 
 
 
 
 
 
 
b
a
s
e
6
4
 
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
n
d
a
r
d
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
h
e
x
 
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
 
o
f
 
t
h
e
 
B
a
s
e
6
4
 
e
n
c
o
d
e
d
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"
import unittest


class TestBase64ToUrlSafe(unittest.TestCase):

    def test_correct_conversion_to_url_safe_format(self):
        base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "YW55IGNhcm5hbCBwbGVhc3VyZS4-_w")

    def test_empty_string_input(self):
        base64 = ""
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "")

    def test_remove_trailing_equals(self):
        base64 = "dGVzdA=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "dGVzdA")

    def test_no_replacement_needed(self):
        base64 = "dGVzdA"
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "dGVzdA")

    def test_multiple_plus_and_slash(self):
        base64 = "aGVsbG8rL3dvcmxkLw=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "aGVsbG8rL3dvcmxkLw")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            base64_to_url_safe(None)  # Testing with None as input

if __name__ == '__main__':
    unittest.main()