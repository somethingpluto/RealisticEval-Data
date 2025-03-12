d
e
f
 
t
r
u
n
c
a
t
e
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
r
e
p
l
a
c
e
m
e
n
t
(
s
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


 
 
 
 
T
r
u
n
c
a
t
e
 
a
 
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
 
r
e
p
l
a
c
i
n
g
 
t
h
e
 
e
x
c
e
s
s
 
p
a
r
t
 
w
i
t
h
 
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
 
t
o
 
t
r
u
n
c
a
t
e
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
 
r
e
s
u
l
t
i
n
g
 
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
 
T
h
e
 
t
r
u
n
c
a
t
e
d
 
s
t
r
i
n
g
 
w
i
t
h
 
e
l
l
i
p
s
i
s
 
i
f
 
a
p
p
l
i
c
a
b
l
e
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
s
)
 
>
 
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
 
s
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


 
 
 
 
r
e
t
u
r
n
 
s






d
e
f
 
t
r
u
n
c
a
t
e
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
r
e
p
l
a
c
e
m
e
n
t
_
t
o
_
f
i
t
_
i
n
t
o
_
c
e
l
l
(


 
 
 
 
s
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
,
 
c
e
l
l
_
w
i
d
t
h
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


 
 
 
 
T
r
u
n
c
a
t
e
 
a
 
s
t
r
i
n
g
 
t
o
 
f
i
t
 
i
n
t
o
 
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
 
c
e
l
l
 
w
i
d
t
h
,
 
r
e
p
l
a
c
i
n
g
 
t
h
e
 
e
x
c
e
s
s
 
p
a
r
t
 
w
i
t
h
 
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
 
t
o
 
t
r
u
n
c
a
t
e
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
 
r
e
s
u
l
t
i
n
g
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
c
e
l
l
_
w
i
d
t
h
 
(
i
n
t
)
:
 
T
h
e
 
w
i
d
t
h
 
o
f
 
t
h
e
 
c
e
l
l
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
 
t
r
u
n
c
a
t
e
d
 
s
t
r
i
n
g
 
w
i
t
h
 
e
l
l
i
p
s
i
s
 
i
f
 
a
p
p
l
i
c
a
b
l
e
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
s
)
 
>
 
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
 
t
r
u
n
c
a
t
e
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
r
e
p
l
a
c
e
m
e
n
t
(
s
,
 
c
e
l
l
_
w
i
d
t
h
)


 
 
 
 
r
e
t
u
r
n
 
s






d
e
f
 
g
e
t
_
t
e
r
m
i
n
a
l
_
s
i
z
e
(
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
t
h
e
 
s
i
z
e
 
o
f
 
t
h
e
 
t
e
r
m
i
n
a
l
.




 
 
 
 
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
i
n
t
,
 
i
n
t
]
:
 
T
h
e
 
w
i
d
t
h
 
a
n
d
 
h
e
i
g
h
t
 
o
f
 
t
h
e
 
t
e
r
m
i
n
a
l
.


 
 
 
 
"
"
"


 
 
 
 
c
o
l
u
m
n
s
,
 
l
i
n
e
s
 
=
 
s
h
u
t
i
l
.
g
e
t
_
t
e
r
m
i
n
a
l
_
s
i
z
e
(
)


 
 
 
 
r
e
t
u
r
n
 
c
o
l
u
m
n
s
,
 
l
i
n
e
s






d
e
f
 
g
e
t
_
t
e
r
m
i
n
a
l
_
s
i
z
e
_
o
r
_
d
e
f
a
u
l
t
(
d
e
f
a
u
l
t
:
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
)
 
-
>
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
t
h
e
 
s
i
z
e
 
o
f
 
t
h
e
 
t
e
r
m
i
n
a
l
 
o
r
 
t
h
e
 
d
e
f
a
u
l
t
 
s
i
z
e
 
i
f
 
t
h
e
 
t
e
r
m
i
n
a
l
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
 
(
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
)
:
 
T
h
e
 
d
e
f
a
u
l
t
 
s
i
z
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


 
 
 
 
 
 
 
 
T
u
p
l
e
[
i
n
t
,
 
i
n
t
]
:
 
T
h
e
 
w
i
d
t
h
 
a
n
d
 
h
e
i
g
h
t
 
o
f
 
t
h
e
 
t
e
r
m
i
n
a
l
 
o
r
 
t
h
e
 
d
e
f
a
u
l
t
 
s
i
z
e
.


 
 
 
 
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
 
g
e
t
_
t
e
r
m
i
n
a
l
_
s
i
z
e
(
)


 
 
 
 
e
x
c
e
p
t
 
O
S
E
r
r
o
r
:


 
 
 
 
 
 
 
import unittest


class TestTruncateStringWithReplacement(unittest.TestCase):

    def test_should_return_original_string_if_shorter_than_max_length(self):
        result = truncate_string_with_replacement('Hello World', 20)
        self.assertEqual(result, 'Hello World')

    def test_should_truncate_string_and_replace_excess_with_ellipsis(self):
        result = truncate_string_with_replacement('This is a long string that needs to be truncated.', 20)
        self.assertEqual(result, 'This is a long str...')

    def test_should_truncate_string_at_max_length_and_add_ellipsis(self):
        result = truncate_string_with_replacement('Short string', 10)
        self.assertEqual(result, 'Short str...')

    def test_should_handle_empty_string_correctly(self):
        result = truncate_string_with_replacement('', 10)
        self.assertEqual(result, '')

    def test_should_return_original_string_when_max_length_equals_string_length(self):
        result = truncate_string_with_replacement('Exact length', 12)
        self.assertEqual(result, 'Exact length')

    def test_should_replace_excess_with_ellipsis_in_string_with_special_characters(self):
        result = truncate_string_with_replacement('This string has special characters: !@#$%^&*()', 30)
        self.assertEqual(result, 'This string has special c...')

    def test_should_return_ellipsis_only_when_max_length_is_0(self):
        result = truncate_string_with_replacement('Hello, world!', 0)
        self.assertEqual(result, '...')

if __name__ == '__main__':
    unittest.main()