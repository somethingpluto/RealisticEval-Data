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
i
n
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
s
t
r
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


 
 
 
 
S
o
r
t
 
t
h
e
 
i
m
a
g
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
i
r
 
s
c
o
r
e
s
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
r
e
o
r
d
e
r
e
d
 
i
m
a
g
e
 
s
c
o
r
e
,
 
n
a
m
e
,
 
a
n
d
 
I
D
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
i
n
t
]
)
:
 
A
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
]
)
:
 
A
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:
 
{
'
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
'
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
 
'
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
'
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
 
'
r
e
s
u
l
t
I
D
s
'
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
 
s
c
o
r
e
s


 
 
 
 
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
 
z
i
p
(
*
s
o
r
t
e
d
(
z
i
p
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
)
)
)




 
 
 
 
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
'
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
'
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
 
'
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
'
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
 
'
r
e
s
u
l
t
I
D
s
'
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
i
n
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
n
a
m
e
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


 
 
 
 
G
e
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
 
i
m
a
g
e
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
i
n
t
]
)
:
 
A
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
]
)
:
 
A
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
 
(
s
t
r
)
:
 
T
h
e
 
n
a
m
e
 
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
 
t
o
 
g
e
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
 
f
o
r
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
c
o
r
e
s
 
a
n
d
 
I
D
s
 
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
 
i
m
a
g
e
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:
 
{
'
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
'
:
 
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
]
,
 
'
r
e
s
u
l
t
I
D
s
'
:
 
[
i
m
a
g
e
_
i
d
]
}


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
i
n
d
e
x
 
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
 
i
m
a
g
e


 
 
 
 
i
m
a
g
e
_
i
n
d
e
x
 
=
 
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
.
i
n
d
e
x
(
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
)




 
 
 
 
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
c
o
r
e
 
a
n
d
 
I
D
 
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
 
i
m
a
g
e


 
 
 
 
r
e
t
u
r
n
 
{
'
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
'
:
import unittest


class TestReorderData(unittest.TestCase):
    def test_reorder_scores_ascending(self):
        imageScores = [90, 85, 95]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [85, 90, 95])
        self.assertEqual(result.resultNames, ["image2.png", "image1.png", "image3.png"])
        self.assertEqual(result.resultIDs, ["id2", "id1", "id3"])

    def test_scores_already_in_order(self):
        imageScores = [70, 75, 80]
        imageNames = ["imageA.png", "imageB.png", "imageC.png"]
        imageIDs = ["idA", "idB", "idC"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [70, 75, 80])
        self.assertEqual(result.resultNames, ["imageA.png", "imageB.png", "imageC.png"])
        self.assertEqual(result.resultIDs, ["idA", "idB", "idC"])

    def test_single_element(self):
        imageScores = [50]
        imageNames = ["imageSingle.png"]
        imageIDs = ["idSingle"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [50])
        self.assertEqual(result.resultNames, ["imageSingle.png"])
        self.assertEqual(result.resultIDs, ["idSingle"])

    def test_empty_array(self):
        imageScores = []
        imageNames = []
        imageIDs = []
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [])
        self.assertEqual(result.resultNames, [])
        self.assertEqual(result.resultIDs, [])

    def test_duplicate_scores(self):
        imageScores = [88, 88, 92]
        imageNames = ["image1.png", "image2.png", "image3.png"]
        imageIDs = ["id1", "id2", "id3"]
        result = reorderData(imageScores, imageNames, imageIDs)
        self.assertEqual(result.resultScores, [88, 88, 92])
        self.assertEqual(result.resultNames, ["image1.png", "image2.png", "image3.png"])
        self.assertEqual(result.resultIDs, ["id1", "id2", "id3"])
if __name__ == '__main__':
    unittest.main()