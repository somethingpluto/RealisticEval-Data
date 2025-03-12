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
u
n
c
t
u
a
t
i
o
n
(
s
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


 
 
 
 
R
e
m
o
v
e
s
 
a
l
l
 
p
u
n
c
t
u
a
t
i
o
n
 
f
r
o
m
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
,
 
c
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
 
s
t
r
i
n
g
 
t
o
 
l
o
w
e
r
c
a
s
e
,


 
 
 
 
a
n
d
 
t
r
i
m
s
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
b
o
t
h
 
e
n
d
s
.




 
 
 
 
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
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
r
e
m
o
v
e
 
p
u
n
c
t
u
a
t
i
o
n
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
 
c
l
e
a
n
e
d
 
a
n
d
 
f
o
r
m
a
t
t
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
 
s
.
t
r
a
n
s
l
a
t
e
(
s
t
r
.
m
a
k
e
t
r
a
n
s
(
"
"
,
 
"
"
,
 
s
t
r
i
n
g
.
p
u
n
c
t
u
a
t
i
o
n
)
)
.
l
o
w
e
r
(
)
.
s
t
r
i
p
(
)






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
s
t
o
p
w
o
r
d
s
(
s
:
 
s
t
r
,
 
l
a
n
g
u
a
g
e
:
 
s
t
r
 
=
 
"
e
n
g
l
i
s
h
"
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


 
 
 
 
R
e
m
o
v
e
s
 
a
l
l
 
s
t
o
p
w
o
r
d
s
 
f
r
o
m
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
,
 
c
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
 
s
t
r
i
n
g
 
t
o
 
l
o
w
e
r
c
a
s
e
,


 
 
 
 
a
n
d
 
t
r
i
m
s
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
b
o
t
h
 
e
n
d
s
.




 
 
 
 
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
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
r
e
m
o
v
e
 
s
t
o
p
w
o
r
d
s
.


 
 
 
 
 
 
 
 
l
a
n
g
u
a
g
e
 
(
s
t
r
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
a
n
g
u
a
g
e
 
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
.
 
D
e
f
a
u
l
t
s
 
t
o
 
"
e
n
g
l
i
s
h
"
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
 
c
l
e
a
n
e
d
 
a
n
d
 
f
o
r
m
a
t
t
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
 
"
 
"
.
j
o
i
n
(


 
 
 
 
 
 
 
 
[


 
 
 
 
 
 
 
 
 
 
 
 
w
o
r
d


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
w
o
r
d
 
i
n
 
s
.
s
p
l
i
t
(
)


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
w
o
r
d
 
n
o
t
 
i
n
 
s
t
o
p
w
o
r
d
s
.
w
o
r
d
s
(
l
a
n
g
u
a
g
e
)


 
 
 
 
 
 
 
 
]


 
 
 
 
)
.
l
o
w
e
r
(
)
.
s
t
r
i
p
(
)






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
w
h
i
t
e
s
p
a
c
e
(
s
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


 
 
 
 
R
e
m
o
v
e
s
 
a
l
l
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
,
 
c
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
 
s
t
r
i
n
g
 
t
o
 
l
o
w
e
r
c
a
s
e
,


 
 
 
 
a
n
d
 
t
r
i
m
s
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
b
o
t
h
 
e
n
d
s
.




 
 
 
 
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
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
r
e
m
o
v
e
 
w
h
i
t
e
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
l
e
a
n
e
d
 
a
n
d
 
f
o
r
m
a
t
t
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
 
"
 
"
.
j
o
i
n
(
s
.
s
p
l
i
t
(
)
)
.
l
o
w
e
r
(
)
.
s
t
r
i
p
(
)






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
u
r
l
s
(
s
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


 
 
 
 
R
e
m
o
v
e
s
 
a
l
l
 
U
R
L
s
 
f
r
o
m
 
a
 
g
i
v
e
n
 
s
t
r
i
n
g
,
 
c
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
 
s
t
r
i
n
g
 
t
o
 
l
o
w
e
r
c
a
s
e
,


 
 
 
 
a
n
d
 
t
r
i
m
s
 
w
h
i
t
e
s
p
a
c
e
 
f
r
o
m
 
b
o
t
h
 
e
n
d
s
.




 
 
 
 
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
 
T
h
e
 
s
t
r
i
n
g
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
r
e
m
o
v
e
 
U
R
L
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
 
T
h
e
 
c
l
e
a
n
e
d
 
a
n
d
 
f
o
r
m
a
t
t
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
 
r
e
.
s
u
b
(
r
"
h
t
t
p
\
S
+
"
,
 
"
"
,
 
s
.
l
o
w
e
r
(
)
.
s
t
r
i
p
(
)
)






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
w
h
i
t
e
s
p
a
c
e
_
a
n
d
_
p
u
n
c
t
u
a
t
i
o
n
(
s
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


 
 
 
 
R
e
m
o
v
e
s
 
a
l
l
 
w
h
i
t
e
s
p
a
c
e
 
a
n
d
 
p
u
n
c
t
u
a
t
i
o
n
 
f
r
o
m
import unittest
import re

class TestRemovePunctuation(unittest.TestCase):

    def test_removes_punctuation_from_simple_sentence(self):
        input_string = "Hello, world!"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_handles_string_with_no_punctuation(self):
        input_string = "Hello world"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_converts_mixed_case_letters_to_lowercase(self):
        input_string = "HeLLo WoRLd!"
        expected = "hello world"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_removes_a_variety_of_punctuation(self):
        input_string = "Life, in a nutshell: eat, sleep, code!"
        expected = "life in a nutshell eat sleep code"
        self.assertEqual(remove_punctuation(input_string), expected)

    def test_trims_whitespace_from_ends(self):
        input_string = "   What a wonderful world!   "
        expected = "what a wonderful world"
        self.assertEqual(remove_punctuation(input_string), expected)
if __name__ == '__main__':
    unittest.main()