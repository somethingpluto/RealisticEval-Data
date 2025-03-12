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
 
m
o
v
e
_
e
m
o
j
i
s
_
t
o
_
e
n
d
(
t
e
x
t
:
 
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
M
o
v
e
 
t
h
e
 
e
m
o
j
 
e
x
p
r
e
s
s
i
o
n
 
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
 
t
o
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
t
e
x
t




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
c
o
n
t
a
i
n
i
n
g
 
t
e
x
t
 
a
n
d
 
p
o
s
s
i
b
l
y
 
e
m
o
j
i
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
 
m
o
d
i
f
i
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
 
a
l
l
 
e
m
o
j
i
s
 
m
o
v
e
d
 
t
o
 
t
h
e
 
e
n
d
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
(
[
^
\
w
\
s
]
+
)
"
,
 
r
"
\
1
 
"
,
 
t
e
x
t
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
e
m
o
j
i
s
(
t
e
x
t
:
 
s
t
r
)
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
 
a
l
l
 
e
m
o
j
i
s
 
f
r
o
m
 
t
h
e
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
c
o
n
t
a
i
n
i
n
g
 
t
e
x
t
 
a
n
d
 
p
o
s
s
i
b
l
y
 
e
m
o
j
i
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
 
m
o
d
i
f
i
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
 
a
l
l
 
e
m
o
j
i
s
 
r
e
m
o
v
e
d
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
\
s
(
[
^
\
w
\
s
]
+
)
"
,
 
r
"
\
1
"
,
 
t
e
x
t
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
e
m
o
j
i
s
_
a
n
d
_
u
r
l
s
(
t
e
x
t
:
 
s
t
r
)
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
 
a
l
l
 
e
m
o
j
i
s
 
a
n
d
 
u
r
l
s
 
f
r
o
m
 
t
h
e
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
c
o
n
t
a
i
n
i
n
g
 
t
e
x
t
 
a
n
d
 
p
o
s
s
i
b
l
y
 
e
m
o
j
i
s
 
a
n
d
 
u
r
l
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
 
m
o
d
i
f
i
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
 
a
l
l
 
e
m
o
j
i
s
 
a
n
d
 
u
r
l
s
 
r
e
m
o
v
e
d
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
(
[
^
\
w
\
s
]
+
)
"
,
 
r
"
"
,
 
t
e
x
t
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
e
m
o
j
i
s
_
a
n
d
_
u
r
l
s
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
t
e
x
t
:
 
s
t
r
)
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
 
a
l
l
 
e
m
o
j
i
s
,
 
u
r
l
s
 
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
 
t
h
e
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
c
o
n
t
a
i
n
i
n
g
 
t
e
x
t
 
a
n
d
 
p
o
s
s
i
b
l
y
 
e
m
o
j
i
s
,
 
u
r
l
s
 
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
 
m
o
d
i
f
i
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
 
a
l
l
 
e
m
o
j
i
s
,
 
u
r
l
s
 
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
 
r
e
m
o
v
e
d
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
(
[
^
\
w
\
s
]
+
)
"
,
 
r
"
"
,
 
t
e
x
t
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
e
m
o
j
i
s
_
a
n
d
_
u
r
l
s
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
_
a
n
d
_
n
u
m
b
e
r
s
(
t
e
x
t
:
 
s
t
r
)
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
 
a
l
l
 
e
m
o
j
i
s
,
 
u
r
l
s
,
 
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
 
a
n
d
 
n
u
m
b
e
r
s
 
f
r
o
m
 
t
h
e
 
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


 
 
 
 
 
 
 
 
t
e
x
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
 
c
o
n
t
a
i
n
i
n
g
 
t
e
x
t
 
a
n
d
 
p
o
s
s
i
b
l
y
 
e
m
o
j
i
s
,
 
u
r
l
s
,
 
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
 
a
n
d
 
n
u
m
b
e
r
s
.
import unittest


class TestMoveEmojisToEnd(unittest.TestCase):

    def test_no_emojis(self):
        # Case: String with no emojis
        input_text = "This is a test."
        expected_output = "This is a test."
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_all_emojis(self):
        # Case: String with only emojis
        input_text = "😀😃😄😁"
        expected_output = "😀😃😄😁"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_at_start(self):
        # Case: Emojis at the start of the text
        input_text = "😀😃Hello world!"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_at_end(self):
        # Case: Emojis already at the end of the text
        input_text = "Hello world!😀😃"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_in_middle(self):
        # Case: Emojis in the middle of the text
        input_text = "Hello 😀world😃!"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_mixed_characters(self):
        # Case: Text with mixed characters and emojis
        input_text = "Hi! 😀 How are you? 😃"
        expected_output = "Hi!  How are you? 😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()