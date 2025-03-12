d
e
f
 
i
s
_
h
a
v
a
_
p
h
o
n
e
_
n
u
m
b
e
r
(
s
:
 
s
t
r
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


 
 
 
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
t
h
e
 
s
t
r
i
n
g
 
c
o
n
t
a
i
n
s
 
a
 
p
h
o
n
e
 
n
u
m
b
e
r
;
 
a
 
p
o
s
s
i
b
l
e
 
f
o
r
m
a
t
 
f
o
r
 
a
 
p
h
o
n
e
 
n
u
m
b
e
r
 
i
s
 
+
1
-
8
0
0
-
5
5
5
-
1
2
3
4
,
 
5
5
5
-
5
5
5
-
1
2
3
4
,
 
5
5
5
 
5
5
5
 
1
2
3
4


 
 
 
 
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
 
i
n
p
u
t
 
s
t
r
 
m
a
y
b
e
 
c
o
n
t
a
i
n
 
p
h
o
n
e
 
n
u
m
b
e
r




 
 
 
 
R
e
t
u
r
n
s
:
 
w
e
a
t
h
e
r
 
t
h
i
s
 
s
t
r
 
c
o
n
t
a
i
n
 
p
h
o
n
e
 
n
u
m
b
e
r




 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
s
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
+
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
(
'
1
-
8
0
0
-
5
5
5
-
5
5
5
5
5
5
5
5
5
5
5
5
5
'
)
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
 
n
o
t
 
s
.
s
t
a
r
t
s
w
i
t
h
import re
import unittest


class TestPhoneNumberDetection(unittest.TestCase):
    def test_with_international_prefix(self):
        self.assertTrue(is_hava_phone_number("+1-800-555-1234"), "Should detect international prefix")

    def test_with_standard_dashes(self):
        self.assertTrue(is_hava_phone_number("800-555-1234"), "Should detect standard format with dashes")

    def test_with_spaces(self):
        self.assertTrue(is_hava_phone_number("800 555 1234"), "Should detect standard format with spaces")

    def test_without_phone_number(self):
        self.assertFalse(is_hava_phone_number("Hello, world!"), "Should not detect any phone number")

    def test_with_text_containing_numbers(self):
        self.assertTrue(is_hava_phone_number("Call me at 800-555-1234 today!"), "Should detect phone number in text")
if __name__ == '__main__':
    unittest.main()