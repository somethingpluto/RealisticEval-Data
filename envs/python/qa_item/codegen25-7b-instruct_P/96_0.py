d
e
f
 
i
n
s
e
r
t
_
c
l
e
f
(
a
b
c
:
 
s
t
r
,
 
c
l
e
f
:
 
s
t
r
 
=
 
"
b
a
s
s
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


 
 
 
 
M
o
d
i
f
y
 
t
h
e
 
A
B
C
 
s
t
r
i
n
g
 
b
y
 
i
n
s
e
r
t
i
n
g
 
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
l
e
f
 
(
e
.
g
.
,
 
"
c
l
e
f
=
b
a
s
s
"
)


 
 
 
 
a
f
t
e
r
 
t
h
e
 
t
o
n
e
 
l
i
n
e
 
(
K
:
)
,
 
o
r
 
"
b
a
s
s
"
 
i
f
 
n
o
 
c
l
e
f
 
i
s
 
s
p
e
c
i
f
i
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
b
c
 
(
s
t
r
)
:
 
T
h
e
 
A
B
C
 
n
o
t
a
t
i
o
n
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
c
l
e
f
 
(
s
t
r
)
:
 
T
h
e
 
c
l
e
f
 
t
o
 
s
e
t
 
(
d
e
f
a
u
l
t
 
i
s
 
"
b
a
s
s
"
)
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
 
u
p
d
a
t
e
d
 
A
B
C
 
n
o
t
a
t
i
o
n
 
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
 
t
h
e
 
n
e
w
 
c
l
e
f
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
c
l
e
f
 
=
=
 
"
b
a
s
s
"
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
b
c


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
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
K
:
"
,
 
f
"
K
:
{
c
l
e
f
}
\
n
K
:
"
,
 
a
b
c
)






d
e
f
 
i
n
s
e
r
t
_
k
e
y
(
a
b
c
:
 
s
t
r
,
 
k
e
y
:
 
s
t
r
 
=
 
"
C
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


 
 
 
 
M
o
d
i
f
y
 
t
h
e
 
A
B
C
 
s
t
r
i
n
g
 
b
y
 
i
n
s
e
r
t
i
n
g
 
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
 
k
e
y
 
(
e
.
g
.
,
 
"
k
e
y
=
C
"
)


 
 
 
 
a
f
t
e
r
 
t
h
e
 
t
o
n
e
 
l
i
n
e
 
(
K
:
)
,
 
o
r
 
"
C
"
 
i
f
 
n
o
 
k
e
y
 
i
s
 
s
p
e
c
i
f
i
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
b
c
 
(
s
t
r
)
:
 
T
h
e
 
A
B
C
 
n
o
t
a
t
i
o
n
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
k
e
y
 
(
s
t
r
)
:
 
T
h
e
 
k
e
y
 
t
o
 
s
e
t
 
(
d
e
f
a
u
l
t
 
i
s
 
"
C
"
)
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
 
u
p
d
a
t
e
d
 
A
B
C
 
n
o
t
a
t
i
o
n
 
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
 
t
h
e
 
n
e
w
 
k
e
y
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
k
e
y
 
=
=
 
"
C
"
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
b
c


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
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
K
:
"
,
 
f
"
K
:
{
k
e
y
}
\
n
K
:
"
,
 
a
b
c
)






d
e
f
 
i
n
s
e
r
t
_
t
i
m
e
(
a
b
c
:
 
s
t
r
,
 
t
i
m
e
:
 
s
t
r
 
=
 
"
4
/
4
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


 
 
 
 
M
o
d
i
f
y
 
t
h
e
 
A
B
C
 
s
t
r
i
n
g
 
b
y
 
i
n
s
e
r
t
i
n
g
 
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
 
t
i
m
e
 
s
i
g
n
a
t
u
r
e


 
 
 
 
(
e
.
g
.
,
 
"
t
i
m
e
=
4
/
4
"
)
 
a
f
t
e
r
 
t
h
e
 
t
o
n
e
 
l
i
n
e
 
(
K
:
)
,
 
o
r
 
"
4
/
4
"
 
i
f
 
n
o
 
t
i
m
e


 
 
 
 
s
i
g
n
a
t
u
r
e
 
i
s
 
s
p
e
c
i
f
i
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
b
c
 
(
s
t
r
)
:
 
T
h
e
 
A
B
C
 
n
o
t
a
t
i
o
n
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
t
i
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
 
t
i
m
e
 
s
i
g
n
a
t
u
r
e
 
t
o
 
s
e
t
 
(
d
e
f
a
u
l
t
 
i
s
 
"
4
/
4
"
)
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
 
u
p
d
a
t
e
d
 
A
B
C
 
n
o
t
a
t
i
o
n
 
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
 
t
h
e
 
n
e
w
 
t
i
m
e
 
s
i
g
n
a
t
u
r
e
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
t
i
m
e
 
=
=
 
"
4
/
4
"
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
b
c


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
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
K
:
"
,
 
f
"
K
:
{
t
i
m
e
}
\
n
K
:
"
,
 
a
b
c
)






import unittest


class TestChangedClef(unittest.TestCase):

    def test_default_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = insert_clef(abc)
        expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_specific_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = insert_clef(abc, "treble")
        expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_no_newline_after_key_signature(self):
        abc = "X:1\nT:Test Tune\nK:C"
        result = insert_clef(abc, "alto")
        expected = "X:1\nT:Test Tune\nK:C clef=alto"
        self.assertEqual(result, expected)

    def test_no_key_signature_found(self):
        abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n"
        result = insert_clef(abc, "tenor")
        self.assertEqual(result, abc)  # Expect the original string to be returned unchanged

    def test_multiple_key_signatures(self):
        abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n"
        result = insert_clef(abc, "baritone")
        expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()