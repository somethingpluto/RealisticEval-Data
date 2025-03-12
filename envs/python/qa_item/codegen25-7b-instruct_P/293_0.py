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
 
U
n
i
o
n






d
e
f
 
r
e
o
r
d
e
r
_
d
a
t
a
(
i
m
a
g
e
_
s
c
o
r
e
s
:
 
L
i
s
t
[
f
l
o
a
t
]
,
 
i
m
a
g
e
_
n
a
m
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
,
 
i
m
a
g
e
_
i
d
s
:
 
L
i
s
t
[
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
]
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
o
r
d
e
r
s
 
i
m
a
g
e
 
q
u
e
s
t
i
o
n
s
 
b
a
s
e
d
 
o
n
 
s
c
o
r
e
s
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
m
a
g
e
_
s
c
o
r
e
s
 
(
l
i
s
t
[
f
l
o
a
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
n
u
m
e
r
i
c
a
l
 
s
c
o
r
e
s
 
f
o
r
 
t
h
e
 
i
m
a
g
e
s
.


 
 
 
 
 
 
 
 
i
m
a
g
e
_
n
a
m
e
s
 
(
l
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
n
 
a
r
r
a
y
 
o
f
 
i
m
a
g
e
 
n
a
m
e
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
c
o
r
e
s
.


 
 
 
 
 
 
 
 
i
m
a
g
e
_
i
d
s
 
(
l
i
s
t
[
s
t
r
 
|
 
f
l
o
a
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
i
m
a
g
e
 
I
D
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
c
o
r
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


 
 
 
 
 
 
 
 
d
i
c
t
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
h
e
 
s
o
r
t
e
d
 
s
c
o
r
e
s
,
 
n
a
m
e
s
,
 
a
n
d
 
I
D
s
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
e
s
u
l
t
S
c
o
r
e
s
 
(
l
i
s
t
[
f
l
o
a
t
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
 
s
o
r
t
e
d
 
n
u
m
e
r
i
c
a
l
 
s
c
o
r
e
s
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
e
s
u
l
t
N
a
m
e
s
 
(
l
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
 
s
o
r
t
e
d
 
i
m
a
g
e
 
n
a
m
e
s
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
r
e
s
u
l
t
I
D
s
 
(
l
i
s
t
[
s
t
r
 
|
 
f
l
o
a
t
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
 
s
o
r
t
e
d
 
i
m
a
g
e
 
I
D
s
.


 
 
 
 
"
"
"


 
 
 
 
#
 
S
o
r
t
 
t
h
e
 
s
c
o
r
e
s
 
a
n
d
 
n
a
m
e
s
 
i
n
 
a
s
c
e
n
d
i
n
g
 
o
r
d
e
r


 
 
 
 
s
o
r
t
e
d
_
s
c
o
r
e
s
 
=
 
s
o
r
t
e
d
(
i
m
a
g
e
_
s
c
o
r
e
s
)


 
 
 
 
s
o
r
t
e
d
_
n
a
m
e
s
 
=
 
[
i
m
a
g
e
_
n
a
m
e
s
[
i
m
a
g
e
_
s
c
o
r
e
s
.
i
n
d
e
x
(
s
c
o
r
e
)
]
 
f
o
r
 
s
c
o
r
e
 
i
n
 
s
o
r
t
e
d
_
s
c
o
r
e
s
]


 
 
 
 
s
o
r
t
e
d
_
i
d
s
 
=
 
[
i
m
a
g
e
_
i
d
s
[
i
m
a
g
e
_
s
c
o
r
e
s
.
i
n
d
e
x
(
s
c
o
r
e
)
]
 
f
o
r
 
s
c
o
r
e
 
i
n
 
s
o
r
t
e
d
_
s
c
o
r
e
s
]




 
 
 
 
#
 
R
e
t
u
r
n
 
t
h
e
 
s
o
r
t
e
d
 
s
c
o
r
e
s
,
 
n
a
m
e
s
,
 
a
n
d
 
I
D
s


 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
"
r
e
s
u
l
t
S
c
o
r
e
s
"
:
 
s
o
r
t
e
d
_
s
c
o
r
e
s
,


 
 
 
 
 
 
 
 
"
r
e
s
u
l
t
N
a
m
e
s
"
:
 
s
o
r
t
e
d
_
n
a
m
e
s
,


 
 
 
 
 
 
 
 
"
r
e
s
u
l
t
I
D
s
"
:
 
s
o
r
t
e
d
_
i
d
s


 
 
 
 
}






d
e
f
 
g
e
t
_
i
m
a
g
e
_
s
c
o
r
e
s
(
i
m
a
g
e
_
s
c
o
r
e
s
:
 
L
i
s
t
[
f
l
o
a
t
]
,
 
i
m
a
g
e
_
n
a
m
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
,
 
i
m
a
g
e
_
i
d
s
:
 
L
i
s
t
[
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
_
i
d
:
 
U
n
i
o
n
[
s
t
r
,
f
l
o
a
t
]
,
 
q
u
e
s
t
i
o
n
_
t
e
x
t
:
 
s
t
r
,
 
a
n
s
w
e
r
:
 
s
t
r
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
s
c
o
r
e
s
 
o
f
 
t
h
e
 
i
m
a
g
e
s
 
t
h
a
t
 
c
o
n
t
a
i
n
 
t
h
e
 
a
n
s
w
e
r
 
t
o
 
t
h
e
 
q
u
e
s
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
m
a
g
e
_
s
c
o
r
e
s
 
(
l
i
s
t
[
f
l
o
a
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
n
u
m
e
r
i
c
a
l
 
s
c
o
r
e
s
 
f
o
r
 
t
h
e
 
i
m
a
g
e
s
.


 
 
 
 
 
 
 
 
i
m
a
g
e
_
n
a
m
e
s
 
(
l
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
n
 
a
r
r
a
y
 
o
f
 
i
m
a
g
e
 
n
a
m
e
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
c
o
r
e
s
.


 
 
 
 
 
 
 
 
i
m
a
g
e
_
i
d
s
 
(
l
i
s
t
[
s
t
r
 
|
 
f
l
o
a
t
]
)
:
 
A
n
 
a
r
r
a
y
 
o
f
 
i
m
a
g
e
 
I
D
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
c
o
r
e
s
.


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
_
i
d
 
(
s
t
r
 
|
 
f
l
o
a
t
)
:
 
T
h
e
 
I
D
 
o
f
 
t
h
e
import unittest

class TestReorderData(unittest.TestCase):
    
    def test_sorts_question_correctly_for_basic_inputs(self):
        scores = [3, 1, 2]
        names = ['Image3', 'Image1', 'Image2']
        ids = [103, 101, 102]
        expected = {
            'resultScores': [1, 2, 3],
            'resultNames': ['Image1', 'Image2', 'Image3'],
            'resultIDs': [101, 102, 103]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_sorts_question_correctly_with_mixed_scores(self):
        scores = [5, 1, 3, 5, 2]
        names = ['Image5', 'Image1', 'Image3', 'Image6', 'Image2']
        ids = [105, 101, 103, 106, 102]
        expected = {
            'resultScores': [1, 2, 3, 5, 5],
            'resultNames': ['Image1', 'Image2', 'Image3', 'Image5', 'Image6'],
            'resultIDs': [101, 102, 103, 105, 106]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_handles_duplicate_scores(self):
        scores = [2, 2, 1]
        names = ['Image2', 'Image3', 'Image1']
        ids = [102, 103, 101]
        expected = {
            'resultScores': [1, 2, 2],
            'resultNames': ['Image1', 'Image2', 'Image3'],
            'resultIDs': [101, 102, 103]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_handles_empty_arrays(self):
        scores = []
        names = []
        ids = []
        expected = {
            'resultScores': [],
            'resultNames': [],
            'resultIDs': []
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

if __name__ == '__main__':
    unittest.main()