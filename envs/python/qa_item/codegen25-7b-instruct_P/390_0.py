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
 
L
i
s
t






d
e
f
 
s
p
l
i
t
_
i
n
t
o
_
s
e
n
t
e
n
c
e
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
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
S
p
l
i
t
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
 
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
 
s
e
n
t
e
n
c
e
s
.




 
 
 
 
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
 
t
e
x
t
 
t
o
 
b
e
 
s
p
l
i
t
 
i
n
t
o
 
s
e
n
t
e
n
c
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
 
s
e
n
t
e
n
c
e
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
,
 
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
 
s
t
r
i
p
p
e
d
 
o
f
 
l
e
a
d
i
n
g
/
t
r
a
i
l
i
n
g
 
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


 
 
 
 
"
"
"


 
 
 
 
#
 
S
p
l
i
t
 
t
h
e
 
t
e
x
t
 
i
n
t
o
 
s
e
n
t
e
n
c
e
s
 
u
s
i
n
g
 
t
h
e
 
N
L
T
K
 
s
e
n
t
e
n
c
e
 
t
o
k
e
n
i
z
e
r


 
 
 
 
s
e
n
t
e
n
c
e
s
 
=
 
n
l
t
k
.
s
e
n
t
_
t
o
k
e
n
i
z
e
(
t
e
x
t
)




 
 
 
 
#
 
C
l
e
a
n
 
a
n
d
 
s
t
r
i
p
 
e
a
c
h
 
s
e
n
t
e
n
c
e
 
o
f
 
l
e
a
d
i
n
g
/
t
r
a
i
l
i
n
g
 
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


 
 
 
 
s
e
n
t
e
n
c
e
s
 
=
 
[
s
e
n
t
e
n
c
e
.
s
t
r
i
p
(
)
 
f
o
r
 
s
e
n
t
e
n
c
e
 
i
n
 
s
e
n
t
e
n
c
e
s
]




 
 
 
 
r
e
t
u
r
n
 
s
e
n
t
e
n
c
e
s






d
e
f
 
s
p
l
i
t
_
i
n
t
o
_
w
o
r
d
s
(
s
e
n
t
e
n
c
e
:
s
t
r
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
S
p
l
i
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
e
n
t
e
n
c
e
 
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
 
w
o
r
d
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
n
t
e
n
c
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
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
 
t
o
 
b
e
 
s
p
l
i
t
 
i
n
t
o
 
w
o
r
d
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
 
w
o
r
d
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
,
 
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
 
s
t
r
i
p
p
e
d
 
o
f
 
l
e
a
d
i
n
g
/
t
r
a
i
l
i
n
g
 
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


 
 
 
 
"
"
"


 
 
 
 
#
 
S
p
l
i
t
 
t
h
e
 
s
e
n
t
e
n
c
e
 
i
n
t
o
 
w
o
r
d
s
 
u
s
i
n
g
 
t
h
e
 
N
L
T
K
 
w
o
r
d
 
t
o
k
e
n
i
z
e
r


 
 
 
 
w
o
r
d
s
 
=
 
n
l
t
k
.
w
o
r
d
_
t
o
k
e
n
i
z
e
(
s
e
n
t
e
n
c
e
)




 
 
 
 
#
 
C
l
e
a
n
 
a
n
d
 
s
t
r
i
p
 
e
a
c
h
 
w
o
r
d
 
o
f
 
l
e
a
d
i
n
g
/
t
r
a
i
l
i
n
g
 
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


 
 
 
 
w
o
r
d
s
 
=
 
[
w
o
r
d
.
s
t
r
i
p
(
)
 
f
o
r
 
w
o
r
d
 
i
n
 
w
o
r
d
s
]




 
 
 
 
r
e
t
u
r
n
 
w
o
r
d
s






d
e
f
 
g
e
t
_
w
o
r
d
_
c
o
u
n
t
(
s
e
n
t
e
n
c
e
:
s
t
r
)
 
-
>
 
i
n
t
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
 
n
u
m
b
e
r
 
o
f
 
w
o
r
d
s
 
i
n
 
t
h
e
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
n
t
e
n
c
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
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
 
t
o
 
b
e
 
c
o
u
n
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
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
 
w
o
r
d
s
 
i
n
 
t
h
e
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
.


 
 
 
 
"
"
"


 
 
 
 
#
 
S
p
l
i
t
 
t
h
e
 
s
e
n
t
e
n
c
e
 
i
n
t
o
 
w
o
r
d
s
 
u
s
i
n
g
 
t
h
e
 
N
L
T
K
 
w
o
r
d
 
t
o
k
e
n
i
z
e
r


 
 
 
 
w
o
r
d
s
 
=
 
n
l
t
k
.
w
o
r
d
_
t
o
k
e
n
i
z
e
(
s
e
n
t
e
n
c
e
)




 
 
 
 
#
 
C
o
u
n
t
 
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
 
w
o
r
d
s
 
i
n
 
t
h
e
 
s
e
n
t
e
n
c
e


 
 
 
 
w
o
r
d
_
c
o
u
n
t
 
=
 
l
e
n
(
w
o
r
d
s
)




 
 
 
 
r
e
t
u
r
n
 
w
o
r
d
_
c
o
u
n
t






d
e
f
 
g
e
t
_
u
n
i
q
u
e
_
w
o
r
d
s
(
s
e
n
t
e
n
c
e
s
:
L
i
s
t
[
s
t
r
]
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
a
 
l
i
s
t
 
o
f
 
u
n
i
q
u
e
 
w
o
r
d
s
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
l
i
s
t
 
o
f
 
s
e
n
t
e
n
c
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
e
n
t
e
n
c
e
s
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
s
e
n
t
e
n
c
e
s
 
t
o
 
b
e
 
s
e
a
r
c
h
e
d
 
f
o
r
 
u
n
i
q
u
e
 
w
o
r
d
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
 
u
n
i
q
u
e
 
w
o
r
d
s
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
s
e
n
t
e
n
c
e
s
.


import unittest


class TestSplitIntoSentences(unittest.TestCase):

    def test_basic_splitting(self):
        # Test splitting a basic text with clear punctuation
        text = "Hello world! How are you? I am fine."
        expected = ["Hello world!", "How are you?", "I am fine."]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_complex_punctuation(self):
        # Test splitting text that includes quotes and commas
        text = 'He said, This is amazing! Then he left.'
        expected = ['He said, This is amazing!', "Then he left."]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_with_no_punctuation(self):
        # Test text that has no punctuation marks
        text = "Hello world how are you"
        expected = ["Hello world how are you"]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        # Test empty string input
        text = ""
        expected = []
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()