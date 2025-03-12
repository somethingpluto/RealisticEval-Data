d
e
f
 
c
o
m
p
r
e
s
s
_
f
i
l
e
n
a
m
e
(
f
i
l
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
 
=
 
1
8
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


 
 
 
 
C
o
m
p
r
e
s
s
e
s
 
l
o
n
g
 
f
i
l
e
n
a
m
e
s
 
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
 
i
n
 
t
h
e
 
m
i
d
d
l
e
 
w
h
i
l
e
 
p
r
e
s
e
r
v
i
n
g
 
t
h
e
 
f
i
l
e
n
a
m
e
 
e
x
t
e
n
s
i
o
n
,
 
w
h
i
c
h
 
d
e
f
a
u
l
t
s
 
t
o
 
1
8
 
c
h
a
r
a
c
t
e
r
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


 
 
 
 
 
 
 
 
c
o
m
p
r
e
s
s
_
f
i
l
e
n
a
m
e
(
'
v
e
r
y
l
o
n
g
f
i
l
e
n
a
m
e
.
t
x
t
'
,
 
1
0
)
 
o
u
t
p
u
t
:
 
v
e
r
y
l
o
n
g
f
i
*
*
*
.
t
x
t




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
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
 
o
r
i
g
i
n
a
l
 
f
i
l
e
 
n
a
m
e
 
t
o
 
b
e
 
c
o
m
p
r
e
s
s
e
d
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
 
a
l
l
o
w
e
d
 
l
e
n
g
t
h
 
f
o
r
 
t
h
e
 
c
o
m
p
r
e
s
s
e
d
 
f
i
l
e
 
n
a
m
e
.
 
D
e
f
a
u
l
t
s
 
t
o
 
1
8
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
 
c
o
m
p
r
e
s
s
e
d
 
f
i
l
e
 
n
a
m
e
,
 
w
i
t
h
 
t
h
e
 
m
i
d
d
l
e
 
s
e
c
t
i
o
n
 
r
e
p
l
a
c
e
d
 
b
y
 
e
l
l
i
p
s
e
s
 
(
'
.
.
.
'
)
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
r
 
t
h
e
 
o
r
i
g
i
n
a
l
 
f
i
l
e
 
n
a
m
e
 
i
f
 
i
t
 
i
s
 
w
i
t
h
i
n
 
t
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
f
i
l
e
_
n
a
m
e
)
 
<
=
 
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
 
f
i
l
e
_
n
a
m
e


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
e
x
t
e
n
s
i
o
n
 
=
 
o
s
.
p
a
t
h
.
s
p
l
i
t
e
x
t
(
f
i
l
e
_
n
a
m
e
)
[
1
]


 
 
 
 
 
 
 
 
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
n
a
m
e
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
 
+
 
e
x
t
e
n
s
i
o
n






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
s
i
z
e
(
f
i
l
e
_
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
 
f
i
l
e
 
s
i
z
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
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
 
t
o
 
t
h
e
 
f
i
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
i
l
e
 
s
i
z
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
e
_
s
i
z
e
 
=
 
o
s
.
p
a
t
h
.
g
e
t
s
i
z
e
(
f
i
l
e
_
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
s
i
z
e
 
<
 
1
0
2
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
f
i
l
e
_
s
i
z
e
)
 
+
 
"
 
B
"


 
 
 
 
e
l
i
f
 
f
i
l
e
_
s
i
z
e
 
<
 
1
0
2
4
 
*
 
1
0
2
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
r
o
u
n
d
(
f
i
l
e
_
s
i
z
e
 
/
 
1
0
2
4
,
 
2
)
)
 
+
 
"
 
K
B
"


 
 
 
 
e
l
i
f
 
f
i
l
e
_
s
i
z
e
 
<
 
1
0
2
4
 
*
 
1
0
2
4
 
*
 
1
0
2
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
r
o
u
n
d
(
f
i
l
e
_
s
i
z
e
 
/
 
(
1
0
2
4
 
*
 
1
0
2
4
)
,
 
2
)
)
 
+
 
"
 
M
B
"


 
 
 
 
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
 
s
t
r
(
r
o
u
n
d
(
f
i
l
e
_
s
i
z
e
 
/
 
(
1
0
2
4
 
*
 
1
0
2
4
 
*
 
1
0
2
4
)
,
 
2
)
)
 
+
 
"
 
G
B
"






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
d
a
t
e
(
f
i
l
e
_
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
 
f
i
l
e
 
d
a
t
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
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
 
t
o
 
t
h
e
 
f
i
l
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
f
i
l
e
 
d
a
t
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
f
o
r
m
a
t
.


 
 
 
 
"
"
"
import unittest


class TestCompressFilename(unittest.TestCase):
    def test_return_filename_unchanged_if_under_max_length(self):
        self.assertEqual(compress_filename('file.txt', 10), 'file.txt')

    def test_truncate_and_append_if_exceeds_max_length(self):
        self.assertEqual(compress_filename('verylongfilename.txt', 10), 'verylongfi***.txt')

    def test_preserve_file_extension_after_compression(self):
        self.assertEqual(compress_filename('document.pdf', 5), 'docum***.pdf')

    def test_truncate_and_append_if_filename_exceeds(self):
        self.assertEqual(compress_filename('short.mp3', 2), 'sh***.mp3')
if __name__ == '__main__':
    unittest.main()