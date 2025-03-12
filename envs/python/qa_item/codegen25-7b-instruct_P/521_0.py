i
m
p
o
r
t
 
r
e


f
r
o
m
 
c
o
l
l
e
c
t
i
o
n
s
 
i
m
p
o
r
t
 
C
o
u
n
t
e
r


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
,
 
D
i
c
t






d
e
f
 
w
o
r
d
_
f
i
l
t
e
r
_
c
o
u
n
t
e
r
(
t
e
x
t
:
 
s
t
r
,
 
f
i
l
t
e
r
_
w
o
r
d
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
 
D
i
c
t
[
s
t
r
,
 
i
n
t
]
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
 
s
p
e
c
i
f
i
e
d
 
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
 
g
i
v
e
n
 
t
e
x
t
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
f
i
l
t
e
r
s
 
t
h
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
 
t
e
x
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
,


 
 
 
 
c
o
u
n
t
s
 
t
h
e
i
r
 
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
,
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
d
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
t
h
e
 
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


 
 
 
 
o
r
d
e
r
 
t
h
e
y
 
w
e
r
e
 
p
r
o
v
i
d
e
d
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
 
c
o
u
n
t
 
w
o
r
d
s
.


 
 
 
 
 
 
 
 
f
i
l
t
e
r
_
w
o
r
d
s
 
(
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
 
t
o
 
f
i
l
t
e
r
 
a
n
d
 
c
o
u
n
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
i
n
t
]
:
 
A
 
d
i
c
t
i
o
n
a
r
y
 
w
i
t
h
 
t
h
e
 
c
o
u
n
t
 
o
f
 
e
a
c
h
 
f
i
l
t
e
r
 
w
o
r
d
 
i
n
 
t
h
e
 
t
e
x
t
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
a
i
n
t
a
i
n
i
n
g
 
t
h
e
 
o
r
d
e
r
 
f
r
o
m
 
f
i
l
t
e
r
_
w
o
r
d
s
.


 
 
 
 
"
"
"


 
 
 
 
#
 
F
i
l
t
e
r
 
t
h
e
 
t
e
x
t
 
t
o
 
r
e
m
o
v
e
 
a
n
y
 
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
 
c
o
n
v
e
r
t
 
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


 
 
 
 
t
e
x
t
 
=
 
r
e
.
s
u
b
(
r
'
[
^
\
w
\
s
]
'
,
 
'
'
,
 
t
e
x
t
.
l
o
w
e
r
(
)
)




 
 
 
 
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
 
w
o
r
d
s


 
 
 
 
w
o
r
d
s
 
=
 
t
e
x
t
.
s
p
l
i
t
(
)




 
 
 
 
#
 
F
i
l
t
e
r
 
t
h
e
 
w
o
r
d
s
 
b
a
s
e
d
 
o
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t


 
 
 
 
f
i
l
t
e
r
e
d
_
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
 
i
f
 
w
o
r
d
 
i
n
 
f
i
l
t
e
r
_
w
o
r
d
s
]




 
 
 
 
#
 
C
o
u
n
t
 
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
 
e
a
c
h
 
f
i
l
t
e
r
e
d
 
w
o
r
d


 
 
 
 
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
s
 
=
 
C
o
u
n
t
e
r
(
f
i
l
t
e
r
e
d
_
w
o
r
d
s
)




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
d
i
c
t
i
o
n
a
r
y
 
t
o
 
a
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s


 
 
 
 
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
s
_
l
i
s
t
 
=
 
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
s
.
i
t
e
m
s
(
)




 
 
 
 
#
 
S
o
r
t
 
t
h
e
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
 
b
y
 
t
h
e
 
s
e
c
o
n
d
 
e
l
e
m
e
n
t
 
o
f
 
e
a
c
h
 
t
u
p
l
e


 
 
 
 
s
o
r
t
e
d
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
s
_
l
i
s
t
 
=
 
s
o
r
t
e
d
(
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
s
_
l
i
s
t
,
 
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
1
]
,
 
r
e
v
e
r
s
e
=
T
r
u
e
)




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
 
t
o
 
a
 
d
i
c
t
i
o
n
a
r
y


 
 
 
 
s
o
r
t
e
d
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
s
 
=
 
{
w
o
r
d
:
 
c
o
u
n
t
 
f
o
r
 
w
o
r
d
,
 
c
o
u
n
t
 
i
n
 
s
o
r
t
e
d
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
s
_
l
i
s
t
}




 
 
 
 
r
e
t
u
r
n
 
s
o
r
t
e
d
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
s






d
e
f
 
w
o
r
d
_
f
i
l
t
e
r
_
l
i
s
t
(
t
e
x
t
:
 
s
t
r
,
 
f
i
l
t
e
r
_
w
o
r
d
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


 
 
 
 
F
i
l
t
e
r
s
 
t
h
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
 
g
i
v
e
n
 
t
e
x
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
f
i
l
t
e
r
s
 
t
h
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
 
t
e
x
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
p
r
o
v
i
d
e
d
 
l
i
s
t
,


 
 
 
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
l
i
s
t
 
o
f
 
t
h
e
 
r
e
m
a
i
n
i
n
g
 
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
 
f
i
l
t
e
r
 
w
o
r
d
s
.


 
 
 
 
 
 
 
 
f
i
l
t
e
r
_
w
o
r
d
s
 
(
L
i
s
t
import unittest


class TestWordFilterCounter(unittest.TestCase):

    def test_case1(self):
        text = "go to the school.go to the park."
        filter_words = ["go", "to", "the", "school", "park", "play"]
        expected_output = {
            "go": 2,
            "to": 2,
            "the": 2,
            "school": 1,
            "park": 1,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

    def test_case2(self):
        text = "This is a completely different sentence."
        filter_words = ["I'll", "go", "to", "the", "school", "park", "play"]
        expected_output = {
            "I'll": 0,
            "go": 0,
            "to": 0,
            "the": 0,
            "school": 0,
            "park": 0,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

    def test_case3(self):
        text = "I will not go to the school's park."
        filter_words = ["I", "will", "not", "go", "to", "the", "school's", "park"]
        expected_output = {
            "I": 1,
            "will": 1,
            "not": 1,
            "go": 1,
            "to": 1,
            "the": 1,
            "school's": 1,
            "park": 1,
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

if __name__ == '__main__':
    unittest.main()