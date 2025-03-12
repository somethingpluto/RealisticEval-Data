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
 
T
u
p
l
e






d
e
f
 
a
l
i
g
n
_
l
i
n
e
s
_
l
e
f
t
(
s
t
r
1
:
 
s
t
r
,
 
s
t
r
2
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
A
l
i
g
n
 
t
w
o
 
l
i
n
e
s
 
o
f
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
l
e
f
t
,
 
s
u
p
p
l
e
m
e
n
t
i
n
g
 
w
i
t
h
 
S
p
a
c
e
s
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
e
n
o
u
g
h




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
1
 
(
s
t
r
)
:
 
s
t
r
1


 
 
 
 
 
 
 
 
s
t
r
2
 
(
s
t
r
)
:
 
s
t
r
2




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
s
t
r
]
:
 
a
l
i
g
n
e
d
 
s
t
r
1
 
a
l
i
g
n
e
d
 
s
t
r
2


 
 
 
 
"
"
"


 
 
 
 
m
a
x
_
l
e
n
 
=
 
m
a
x
(
l
e
n
(
s
t
r
1
)
,
 
l
e
n
(
s
t
r
2
)
)


 
 
 
 
r
e
t
u
r
n
 
s
t
r
1
.
l
j
u
s
t
(
m
a
x
_
l
e
n
)
,
 
s
t
r
2
.
l
j
u
s
t
(
m
a
x
_
l
e
n
)






d
e
f
 
a
l
i
g
n
_
l
i
n
e
s
_
r
i
g
h
t
(
s
t
r
1
:
 
s
t
r
,
 
s
t
r
2
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
A
l
i
g
n
 
t
w
o
 
l
i
n
e
s
 
o
f
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
r
i
g
h
t
,
 
s
u
p
p
l
e
m
e
n
t
i
n
g
 
w
i
t
h
 
S
p
a
c
e
s
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
e
n
o
u
g
h




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
1
 
(
s
t
r
)
:
 
s
t
r
1


 
 
 
 
 
 
 
 
s
t
r
2
 
(
s
t
r
)
:
 
s
t
r
2




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
s
t
r
]
:
 
a
l
i
g
n
e
d
 
s
t
r
1
 
a
l
i
g
n
e
d
 
s
t
r
2


 
 
 
 
"
"
"


 
 
 
 
m
a
x
_
l
e
n
 
=
 
m
a
x
(
l
e
n
(
s
t
r
1
)
,
 
l
e
n
(
s
t
r
2
)
)


 
 
 
 
r
e
t
u
r
n
 
s
t
r
1
.
r
j
u
s
t
(
m
a
x
_
l
e
n
)
,
 
s
t
r
2
.
r
j
u
s
t
(
m
a
x
_
l
e
n
)






d
e
f
 
a
l
i
g
n
_
l
i
n
e
s
_
c
e
n
t
e
r
(
s
t
r
1
:
 
s
t
r
,
 
s
t
r
2
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
A
l
i
g
n
 
t
w
o
 
l
i
n
e
s
 
o
f
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
c
e
n
t
e
r
,
 
s
u
p
p
l
e
m
e
n
t
i
n
g
 
w
i
t
h
 
S
p
a
c
e
s
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
e
n
o
u
g
h




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
1
 
(
s
t
r
)
:
 
s
t
r
1


 
 
 
 
 
 
 
 
s
t
r
2
 
(
s
t
r
)
:
 
s
t
r
2




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
s
t
r
]
:
 
a
l
i
g
n
e
d
 
s
t
r
1
 
a
l
i
g
n
e
d
 
s
t
r
2


 
 
 
 
"
"
"


 
 
 
 
m
a
x
_
l
e
n
 
=
 
m
a
x
(
l
e
n
(
s
t
r
1
)
,
 
l
e
n
(
s
t
r
2
)
)


 
 
 
 
r
e
t
u
r
n
 
s
t
r
1
.
c
e
n
t
e
r
(
m
a
x
_
l
e
n
)
,
 
s
t
r
2
.
c
e
n
t
e
r
(
m
a
x
_
l
e
n
)






d
e
f
 
a
l
i
g
n
_
l
i
n
e
s
_
d
e
c
i
m
a
l
(
s
t
r
1
:
 
s
t
r
,
 
s
t
r
2
:
 
s
t
r
)
 
-
>
 
T
u
p
l
e
[
s
t
r
,
 
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
A
l
i
g
n
 
t
w
o
 
l
i
n
e
s
 
o
f
 
s
t
r
i
n
g
 
t
o
 
t
h
e
 
d
e
c
i
m
a
l
,
 
s
u
p
p
l
e
m
e
n
t
i
n
g
 
w
i
t
h
 
S
p
a
c
e
s
 
i
f
 
t
h
e
 
l
e
n
g
t
h
 
i
s
 
n
o
t
 
e
n
o
u
g
h




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
1
 
(
s
t
r
)
:
 
s
t
r
1


 
 
 
 
 
 
 
 
s
t
r
2
 
(
s
t
r
)
:
 
s
t
r
2




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
T
u
p
l
e
[
s
t
r
,
s
t
r
]
:
 
a
l
i
g
n
e
d
 
s
t
r
1
 
a
l
i
g
n
e
d
 
s
t
r
2
import unittest


class TestAlignLinesLeft(unittest.TestCase):

    def test_equal_length_strings(self):
        str1 = "Hello"
        str2 = "World"
        expected_str1 = "Hello"
        expected_str2 = "World"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_first_string_longer(self):
        str1 = "Hello, World!"
        str2 = "Hi"
        expected_str1 = "Hello, World!"
        expected_str2 = "Hi           "  # 14 spaces after "Hi"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_second_string_longer(self):
        str1 = "Hey"
        str2 = "Goodbye, friend!"
        expected_str1 = "Hey             "  # 15 spaces after "Hey"
        expected_str2 = "Goodbye, friend!"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_empty_first_string(self):
        str1 = ""
        str2 = "World"
        expected_str1 = "     "  # 5 spaces
        expected_str2 = "World"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_empty_second_string(self):
        str1 = "Hello"
        str2 = ""
        expected_str1 = "Hello"
        expected_str2 = "     "  # 5 spaces
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_both_strings_empty(self):
        str1 = ""
        str2 = ""
        expected_str1 = ""
        expected_str2 = ""
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_strings_with_spaces(self):
        str1 = "Hello "
        str2 = "World  "
        expected_str1 = "Hello  "
        expected_str2 = "World  "
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)
if __name__ == '__main__':
    unittest.main()