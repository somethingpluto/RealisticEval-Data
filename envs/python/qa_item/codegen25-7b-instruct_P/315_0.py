d
e
f
 
g
e
t
_
f
i
l
e
_
i
d
_
f
r
o
m
_
u
r
l
(
u
r
l
:
 
s
t
r
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
E
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
I
D
 
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
 
U
R
L
 
q
u
e
r
y
 
a
r
g
s
.




 
 
 
 
I
f
 
n
o
t
 
f
o
u
n
d
,
 
r
e
t
u
r
n
 
N
o
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
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
h
e
 
f
i
l
e
 
I
D
 
i
s
 
t
o
 
b
e
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
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
i
l
e
 
I
D
 
i
f
 
p
r
e
s
e
n
t
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
 
i
f
 
t
h
e
 
U
R
L
 
d
o
e
s
 
n
o
t
 
c
o
n
f
o
r
m
 
t
o
 
t
h
e
 
e
x
p
e
c
t
e
d
 
f
o
r
m
a
t
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
"
h
t
t
p
s
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
d
o
w
n
l
o
a
d
?
f
i
l
e
I
d
=
1
2
3
4
5
"


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
2
3
4
5
"


 
 
 
 
"
"
"


 
 
 
 
p
a
r
s
e
d
_
u
r
l
 
=
 
u
r
l
p
a
r
s
e
(
u
r
l
)


 
 
 
 
q
u
e
r
y
_
a
r
g
s
 
=
 
p
a
r
s
e
_
q
s
(
p
a
r
s
e
d
_
u
r
l
.
q
u
e
r
y
)


 
 
 
 
f
i
l
e
_
i
d
 
=
 
q
u
e
r
y
_
a
r
g
s
.
g
e
t
(
"
f
i
l
e
I
d
"
)


 
 
 
 
i
f
 
f
i
l
e
_
i
d
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
_
i
d
[
0
]


 
 
 
 
r
e
t
u
r
n
 
N
o
n
e






d
e
f
 
g
e
t
_
f
i
l
e
_
i
d
_
f
r
o
m
_
p
a
t
h
(
p
a
t
h
:
 
s
t
r
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
E
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
I
D
 
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
 
p
a
t
h
.




 
 
 
 
I
f
 
n
o
t
 
f
o
u
n
d
,
 
r
e
t
u
r
n
 
N
o
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
t
h
 
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
a
t
h
 
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
h
e
 
f
i
l
e
 
I
D
 
i
s
 
t
o
 
b
e
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
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
i
l
e
 
I
D
 
i
f
 
p
r
e
s
e
n
t
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
 
i
f
 
t
h
e
 
p
a
t
h
 
d
o
e
s
 
n
o
t
 
c
o
n
f
o
r
m
 
t
o
 
t
h
e
 
e
x
p
e
c
t
e
d
 
f
o
r
m
a
t
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
"
/
d
o
w
n
l
o
a
d
?
f
i
l
e
I
d
=
1
2
3
4
5
"


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
2
3
4
5
"


 
 
 
 
"
"
"


 
 
 
 
f
i
l
e
_
i
d
 
=
 
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
?
f
i
l
e
I
d
=
(
\
d
+
)
"
,
 
p
a
t
h
)


 
 
 
 
i
f
 
f
i
l
e
_
i
d
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
_
i
d
.
g
r
o
u
p
(
1
)


 
 
 
 
r
e
t
u
r
n
 
N
o
n
e






d
e
f
 
g
e
t
_
f
i
l
e
_
i
d
_
f
r
o
m
_
p
a
t
h
_
o
r
_
u
r
l
(
p
a
t
h
_
o
r
_
u
r
l
:
 
s
t
r
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
E
x
t
r
a
c
t
 
t
h
e
 
f
i
l
e
 
I
D
 
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
 
p
a
t
h
 
o
r
 
U
R
L
.




 
 
 
 
I
f
 
n
o
t
 
f
o
u
n
d
,
 
r
e
t
u
r
n
 
N
o
n
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
t
h
_
o
r
_
u
r
l
 
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
a
t
h
 
o
r
 
U
R
L
 
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
h
e
 
f
i
l
e
 
I
D
 
i
s
 
t
o
 
b
e
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
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
i
l
e
 
I
D
 
i
f
 
p
r
e
s
e
n
t
,
 
o
t
h
e
r
w
i
s
e
 
N
o
n
e
 
i
f
 
t
h
e
 
p
a
t
h
 
o
r
 
U
R
L
 
d
o
e
s
 
n
o
t
 
c
o
n
f
o
r
m
 
t
o
 
t
h
e
 
e
x
p
e
c
t
e
d
 
f
o
r
m
a
t
.




 
 
 
 
E
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
"
/
d
o
w
n
l
o
a
d
?
f
i
l
e
I
d
=
1
2
3
4
5
"


 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
2
3
4
5
"




 
 
 
 
 
 
 
 
I
n
p
u
t
:
 
"
h
t
t
p
s
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
d
o
w
n
l
o
a
d
?
f
i
l
e
I
d
=
1
2
3
4
5
"
import unittest


class TestGetFileIdFromUrl(unittest.TestCase):
    def test_valid_url_with_fileId(self):
        url = 'https://example.com/download?fileId=12345'
        self.assertEqual(get_file_id_from_url(url), '12345')

    def test_missing_fileId_parameter(self):
        url = 'https://example.com/download'
        self.assertIsNone(get_file_id_from_url(url))

    def test_empty_fileId_parameter(self):
        url = 'https://example.com/download?fileId='
        self.assertIsNone(get_file_id_from_url(url))

    def test_malformed_url(self):
        url = 'https://example.com/download?fileId=12345&otherParam'
        self.assertEqual(get_file_id_from_url(url), '12345')  # Adjust based on the actual implementation

if __name__ == '__main__':
    unittest.main()