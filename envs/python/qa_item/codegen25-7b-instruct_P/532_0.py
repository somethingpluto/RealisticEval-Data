d
e
f
 
c
o
u
n
t
_
l
e
t
t
e
r
_
c
h
a
n
g
e
s
(
i
n
p
u
t
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
 
l
i
s
t
:


 
 
 
 
"
"
"
C
o
u
n
t
s
 
t
h
e
 
o
c
c
u
r
r
e
n
c
e
s
 
o
f
 
c
o
n
s
e
c
u
t
i
v
e
 
i
d
e
n
t
i
c
a
l
 
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
 
a
n
a
l
y
z
e
 
f
o
r
 
l
e
t
t
e
r
 
c
h
a
n
g
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
c
o
u
n
t
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
i
n
g
 
t
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
 
c
o
n
s
e
c
u
t
i
v
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
d
e
n
t
i
c
a
l
 
l
e
t
t
e
r
s
 
b
e
f
o
r
e
 
a
 
d
i
f
f
e
r
e
n
t
 
l
e
t
t
e
r
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
s
 
=
 
[
]


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
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
l
e
n
(
i
n
p
u
t
_
s
t
r
i
n
g
)
 
-
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
]
 
=
=
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
 
+
 
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t
s






d
e
f
 
c
o
u
n
t
_
l
e
t
t
e
r
_
c
h
a
n
g
e
s
_
v
2
(
i
n
p
u
t
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
 
l
i
s
t
:


 
 
 
 
"
"
"
C
o
u
n
t
s
 
t
h
e
 
o
c
c
u
r
r
e
n
c
e
s
 
o
f
 
c
o
n
s
e
c
u
t
i
v
e
 
i
d
e
n
t
i
c
a
l
 
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
 
a
n
a
l
y
z
e
 
f
o
r
 
l
e
t
t
e
r
 
c
h
a
n
g
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
c
o
u
n
t
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
i
n
g
 
t
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
 
c
o
n
s
e
c
u
t
i
v
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
d
e
n
t
i
c
a
l
 
l
e
t
t
e
r
s
 
b
e
f
o
r
e
 
a
 
d
i
f
f
e
r
e
n
t
 
l
e
t
t
e
r
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
s
 
=
 
[
]


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
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
l
e
n
(
i
n
p
u
t
_
s
t
r
i
n
g
)
 
-
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
]
 
=
=
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
 
+
 
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t
s






d
e
f
 
c
o
u
n
t
_
l
e
t
t
e
r
_
c
h
a
n
g
e
s
_
v
3
(
i
n
p
u
t
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
 
l
i
s
t
:


 
 
 
 
"
"
"
C
o
u
n
t
s
 
t
h
e
 
o
c
c
u
r
r
e
n
c
e
s
 
o
f
 
c
o
n
s
e
c
u
t
i
v
e
 
i
d
e
n
t
i
c
a
l
 
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
 
a
n
a
l
y
z
e
 
f
o
r
 
l
e
t
t
e
r
 
c
h
a
n
g
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
c
o
u
n
t
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
i
n
g
 
t
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
 
c
o
n
s
e
c
u
t
i
v
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
d
e
n
t
i
c
a
l
 
l
e
t
t
e
r
s
 
b
e
f
o
r
e
 
a
 
d
i
f
f
e
r
e
n
t
 
l
e
t
t
e
r
 
i
s
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
u
n
t
s
 
=
 
[
]


 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
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
l
e
n
(
i
n
p
u
t
_
s
t
r
i
n
g
)
 
-
 
1
)
:


 
 
 
 
 
 
 
 
i
f
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
]
 
=
=
 
i
n
p
u
t
_
s
t
r
i
n
g
[
i
 
+
 
1
]
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
 
 
 
 
 
 
 
 
c
o
u
n
t
 
=
 
0


 
 
 
 
c
o
u
n
t
s
.
a
p
p
e
n
d
(
c
o
u
n
t
)


 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t
s






d
e
f
 
c
o
u
n
t
_
l
e
t
t
e
r
_
c
h
a
n
g
e
s
_
v
4
(
i
n
p
u
t
_
s
t
r
i
n
g
:
import unittest


class TestCountLetterChanges(unittest.TestCase):

    def test_count_consecutive_letters_correctly(self):
        result = count_letter_changes("aaabbcdeee")
        self.assertEqual(result, [3, 2, 1, 1, 3])

    def test_single_character_count(self):
        result = count_letter_changes("a")
        self.assertEqual(result, [1])

    def test_no_consecutive_letters(self):
        result = count_letter_changes("abcdef")
        self.assertEqual(result, [1, 1, 1, 1, 1, 1])

    def test_identical_letters(self):
        result = count_letter_changes("rrrrrr")
        self.assertEqual(result, [6])

    def test_long_string_random_letters(self):
        result = count_letter_changes("xxxyyyzzzaaaab")
        self.assertEqual(result, [3, 3, 3, 4, 1])

    def test_numeric_characters(self):
        result = count_letter_changes("1122334455")
        self.assertEqual(result, [2, 2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()