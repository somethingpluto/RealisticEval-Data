d
e
f
 
c
o
m
p
r
e
s
s
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
p
u
t
:
 
s
t
r
,
 
m
a
x
_
l
e
n
g
t
h
:
 
i
n
t
 
=
 
1
8
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
m
p
r
e
s
s
e
s
 
a
 
s
t
r
i
n
g
 
t
o
 
e
n
s
u
r
e
 
i
t
s
 
l
e
n
g
t
h
 
d
o
e
s
 
n
o
t
 
e
x
c
e
e
d
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
m
a
x
i
m
u
m
 
l
e
n
g
t
h
.


 
 
 
 
I
f
 
t
h
e
 
s
t
r
i
n
g
 
e
x
c
e
e
d
s
 
t
h
e
 
m
a
x
i
m
u
m
 
l
e
n
g
t
h
,
 
i
t
 
t
r
u
n
c
a
t
e
s
 
t
h
e
 
s
t
r
i
n
g
 
a
n
d
 
a
p
p
e
n
d
s
 
a
n
 
e
l
l
i
p
s
i
s
 
(
"
.
.
.
"
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
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
m
p
r
e
s
s
e
d
.


 
 
 
 
 
 
 
 
m
a
x
_
l
e
n
g
t
h
 
(
i
n
t
,
 
o
p
t
i
o
n
a
l
)
:
 
T
h
e
 
m
a
x
i
m
u
m
 
a
l
l
o
w
e
d
 
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
 
s
t
r
i
n
g
 
(
d
e
f
a
u
l
t
 
i
s
 
1
8
)
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
 
c
o
m
p
r
e
s
s
e
d
 
s
t
r
i
n
g
 
t
h
a
t
 
d
o
e
s
 
n
o
t
 
e
x
c
e
e
d
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
.


 
 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
t
r
u
n
c
a
t
i
o
n
 
o
c
c
u
r
s
,
 
a
n
 
e
l
l
i
p
s
i
s
 
(
"
.
.
.
"
)
 
i
s
 
a
p
p
e
n
d
e
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
l
e
n
(
i
n
p
u
t
)
 
<
=
 
m
a
x
_
l
e
n
g
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
p
u
t


 
 
 
 
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
 
i
n
p
u
t
[
:
m
a
x
_
l
e
n
g
t
h
 
-
 
3
]
 
+
 
"
.
.
.
"






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
s
t
r
i
n
g
(
l
e
n
g
t
h
:
 
i
n
t
 
=
 
8
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
e
n
g
t
h
 
(
i
n
t
,
 
o
p
t
i
o
n
a
l
)
:
 
T
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
 
s
t
r
i
n
g
 
(
d
e
f
a
u
l
t
 
i
s
 
8
)
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
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
 
'
'
.
j
o
i
n
(
r
a
n
d
o
m
.
c
h
o
i
c
e
s
(
s
t
r
i
n
g
.
a
s
c
i
i
_
l
e
t
t
e
r
s
 
+
 
s
t
r
i
n
g
.
d
i
g
i
t
s
,
 
k
=
l
e
n
g
t
h
)
)






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
s
t
r
i
n
g
_
w
i
t
h
_
p
r
e
f
i
x
(
p
r
e
f
i
x
:
 
s
t
r
,
 
l
e
n
g
t
h
:
 
i
n
t
 
=
 
8
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
,
 
p
r
e
f
i
x
e
d
 
w
i
t
h
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
r
e
f
i
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
r
e
f
i
x
 
(
s
t
r
)
:
 
T
h
e
 
p
r
e
f
i
x
 
t
o
 
b
e
 
u
s
e
d
 
i
n
 
t
h
e
 
r
a
n
d
o
m
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
l
e
n
g
t
h
 
(
i
n
t
,
 
o
p
t
i
o
n
a
l
)
:
 
T
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
 
s
t
r
i
n
g
 
(
d
e
f
a
u
l
t
 
i
s
 
8
)
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
,
 
p
r
e
f
i
x
e
d
 
w
i
t
h
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
r
e
f
i
x
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
 
p
r
e
f
i
x
 
+
 
g
e
t
_
r
a
n
d
o
m
_
s
t
r
i
n
g
(
l
e
n
g
t
h
)






d
e
f
 
g
e
t
_
r
a
n
d
o
m
_
s
t
r
i
n
g
_
w
i
t
h
_
s
u
f
f
i
x
(
s
u
f
f
i
x
:
 
s
t
r
,
 
l
e
n
g
t
h
:
 
i
n
t
 
=
 
8
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
n
g
t
h
,
 
s
u
f
f
i
x
e
d
 
w
i
t
h
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
s
u
f
f
i
x
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
u
f
f
i
x
 
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
u
f
f
i
x
 
t
o
 
b
e
 
u
s
e
d
 
i
n
 
t
h
e
 
r
a
n
d
o
m
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
l
e
n
g
t
h
 
(
i
n
t
,
 
o
p
t
i
o
n
a
l
)
:
 
T
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
 
s
t
r
i
n
g
 
(
d
e
f
a
u
l
t
 
i
s
 
8
)
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
 
r
a
n
d
o
m
 
s
t
r
i
n
g
 
o
f
 
t
h
e
import unittest


class TestCompressString(unittest.TestCase):
    def test_short_string(self):
        """ should return the original string if it is shorter than the max length """
        input_str = "Short string"
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

    def test_exact_length_string(self):
        """ should return the original string if it is exactly equal to the max length """
        input_str = "Exactly 18 chars"
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

    def test_truncate_long_string(self):
        """ should truncate the string and append "..." if it exceeds the max length """
        input_str = "This is a long string that needs to be compressed."
        result = compress_string(input_str)
        self.assertEqual(result, "This is a long ...")

    def test_truncate_with_custom_max_length(self):
        """ should truncate the string to maxLength - 3 and append "..." when maxLength is specified """
        input_str = "Another long string that is definitely too long."
        result = compress_string(input_str, 25)
        self.assertEqual(result, "Another long string th...")

    def test_default_max_length(self):
        """ should use default max length of 18 if no maxLength is provided """
        input_str = "This string is way too long."
        result = compress_string(input_str)
        self.assertEqual(result, "This string is ...")

    def test_empty_string(self):
        """ should return the original string if it is empty """
        input_str = ""
        result = compress_string(input_str)
        self.assertEqual(result, input_str)

if __name__ == '__main__':
    unittest.main()