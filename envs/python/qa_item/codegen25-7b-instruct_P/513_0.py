i
m
p
o
r
t
 
r
e






d
e
f
 
i
s
_
p
h
r
a
s
e
_
i
n
_
s
t
r
i
n
g
_
i
g
n
o
r
e
_
c
a
s
e
(
p
h
r
a
s
e
:
 
s
t
r
,
 
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
 
g
i
v
e
n
 
p
h
r
a
s
e
 
e
x
i
s
t
s
 
i
n
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
,
 
i
g
n
o
r
i
n
g
 
c
a
s
e
 
a
n
d
 
a
l
l
o
w
i
n
g
 
f
o
r
 
v
a
r
i
a
t
i
o
n
s
 
i
n
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
h
r
a
s
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
 
p
h
r
a
s
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
i
n
 
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
 
T
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
t
h
e
 
p
h
r
a
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
p
h
r
a
s
e
 
i
s
 
f
o
u
n
d
 
a
s
 
a
 
w
h
o
l
e
 
w
o
r
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
p
h
r
a
s
e
 
=
 
p
h
r
a
s
e
.
s
t
r
i
p
(
)


 
 
 
 
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
e
a
r
c
h
(
r
"
\
b
"
 
+
 
r
e
.
e
s
c
a
p
e
(
p
h
r
a
s
e
)
 
+
 
r
"
\
b
"
,
 
s
t
r
i
n
g
,
 
r
e
.
I
G
N
O
R
E
C
A
S
E
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
i
s
_
p
h
r
a
s
e
_
i
n
_
s
t
r
i
n
g
(
p
h
r
a
s
e
:
 
s
t
r
,
 
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
 
g
i
v
e
n
 
p
h
r
a
s
e
 
e
x
i
s
t
s
 
i
n
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
,
 
a
l
l
o
w
i
n
g
 
f
o
r
 
v
a
r
i
a
t
i
o
n
s
 
i
n
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
h
r
a
s
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
 
p
h
r
a
s
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
i
n
 
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
 
T
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
t
h
e
 
p
h
r
a
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
p
h
r
a
s
e
 
i
s
 
f
o
u
n
d
 
a
s
 
a
 
w
h
o
l
e
 
w
o
r
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
p
h
r
a
s
e
 
=
 
p
h
r
a
s
e
.
s
t
r
i
p
(
)


 
 
 
 
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
e
a
r
c
h
(
r
"
\
b
"
 
+
 
r
e
.
e
s
c
a
p
e
(
p
h
r
a
s
e
)
 
+
 
r
"
\
b
"
,
 
s
t
r
i
n
g
)
 
i
s
 
n
o
t
 
N
o
n
e






d
e
f
 
i
s
_
p
h
r
a
s
e
_
i
n
_
s
t
r
i
n
g
_
s
t
r
i
c
t
(
p
h
r
a
s
e
:
 
s
t
r
,
 
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
 
g
i
v
e
n
 
p
h
r
a
s
e
 
e
x
i
s
t
s
 
i
n
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
,
 
s
t
r
i
c
t
l
y
 
c
h
e
c
k
i
n
g
 
f
o
r
 
t
h
e
 
p
h
r
a
s
e
 
a
s
 
a
 
w
h
o
l
e
 
w
o
r
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
h
r
a
s
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
 
p
h
r
a
s
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
i
n
 
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
 
T
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
t
h
e
 
p
h
r
a
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
p
h
r
a
s
e
 
i
s
 
f
o
u
n
d
 
a
s
 
a
 
w
h
o
l
e
 
w
o
r
d
 
i
n
 
t
h
e
 
s
t
r
i
n
g
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
"
"
"


 
 
 
 
p
h
r
a
s
e
 
=
 
p
h
r
a
s
e
.
s
t
r
i
p
(
)


 
 
 
 
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
e
a
r
c
h
(
r
"
\
b
"
 
+
 
r
e
.
e
s
c
a
p
e
(
p
h
r
a
s
e
)
 
+
 
r
"
\
b
"
,
 
s
t
r
i
n
g
)
 
i
s
 
n
o
t
 
N
o
n
e
 
a
n
d
 
p
h
r
a
s
e
 
=
=
 
s
t
r
i
n
g






d
e
f
 
i
s
_
p
h
r
a
s
e
_
i
n
_
s
t
r
i
n
g
_
s
t
r
i
c
t
_
i
g
n
o
r
e
_
c
a
s
e
(
import unittest


class TestIsPhraseInStringIgnoreCase(unittest.TestCase):

    def test_exact_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("hello world", "Hello World"))


    def test_partial_word_match_case_insensitive(self):
        self.assertTrue(is_phrase_in_string_ignore_case("Hello", "saying Hello there"))

    def test_different_cases(self):
        self.assertTrue(is_phrase_in_string_ignore_case("HELLO", "hello there!"))
        self.assertTrue(is_phrase_in_string_ignore_case("world", "WORLD is great"))

    def test_non_existent_phrase(self):
        self.assertFalse(is_phrase_in_string_ignore_case("goodbye", "Hello world"))
        self.assertFalse(is_phrase_in_string_ignore_case("hello", "goodbye world"))


if __name__ == '__main__':
    unittest.main()