d
e
f
 
f
o
r
m
a
t
_
b
y
t
e
s
(
b
y
t
e
s
:
 
i
n
t
,
 
o
p
t
i
o
n
s
:
 
d
i
c
t
 
=
 
N
o
n
e
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


 
 
 
 
F
o
r
m
a
t
s
 
a
 
g
i
v
e
n
 
n
u
m
b
e
r
 
o
f
 
b
y
t
e
s
 
i
n
t
o
 
a
 
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
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
,


 
 
 
 
u
s
i
n
g
 
e
i
t
h
e
r
 
t
h
e
 
S
I
 
(
d
e
c
i
m
a
l
)
 
o
r
 
b
i
n
a
r
y
 
(
a
c
c
u
r
a
t
e
)
 
s
i
z
e
 
n
o
t
a
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


 
 
 
 
 
 
 
 
b
y
t
e
s
 
(
i
n
t
)
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
 
b
y
t
e
s
 
t
o
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
o
p
t
i
o
n
s
 
(
d
i
c
t
,
 
o
p
t
i
o
n
a
l
)
:
 
O
p
t
i
o
n
a
l
 
s
e
t
t
i
n
g
s
 
t
o
 
c
u
s
t
o
m
i
z
e
 
t
h
e
 
o
u
t
p
u
t
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
d
e
c
i
m
a
l
s
'
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
d
e
c
i
m
a
l
 
p
l
a
c
e
s
 
t
o
 
i
n
c
l
u
d
e
 
i
n
 
t
h
e
 
r
e
s
u
l
t
.


 
 
 
 
 
 
 
 
 
 
 
 
-
 
'
s
i
z
e
T
y
p
e
'
 
(
s
t
r
)
:
 
S
p
e
c
i
f
i
e
s
 
w
h
e
t
h
e
r
 
t
o
 
u
s
e
 
b
i
n
a
r
y
 
(
"
a
c
c
u
r
a
t
e
"
)
 
o
r


 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
c
i
m
a
l
 
(
"
n
o
r
m
a
l
"
)
 
u
n
i
t
s
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
a
c
c
u
r
a
t
e
"
 
u
s
e
s
 
u
n
i
t
s
 
l
i
k
e
 
K
i
B
,
 
M
i
B
 
(
b
a
s
e
 
1
0
2
4
)
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
n
o
r
m
a
l
"
 
u
s
e
s
 
u
n
i
t
s
 
l
i
k
e
 
K
B
,
 
M
B
 
(
b
a
s
e
 
1
0
0
0
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
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
b
y
t
e
 
s
i
z
e
 
i
n
 
a
 
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


 
 
 
 
i
f
 
o
p
t
i
o
n
s
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
o
p
t
i
o
n
s
 
=
 
{
}




 
 
 
 
d
e
c
i
m
a
l
s
 
=
 
o
p
t
i
o
n
s
.
g
e
t
(
"
d
e
c
i
m
a
l
s
"
,
 
2
)


 
 
 
 
s
i
z
e
_
t
y
p
e
 
=
 
o
p
t
i
o
n
s
.
g
e
t
(
"
s
i
z
e
T
y
p
e
"
,
 
"
n
o
r
m
a
l
"
)




 
 
 
 
i
f
 
s
i
z
e
_
t
y
p
e
 
=
=
 
"
n
o
r
m
a
l
"
:


 
 
 
 
 
 
 
 
b
a
s
e
 
=
 
1
0
0
0


 
 
 
 
 
 
 
 
s
u
f
f
i
x
e
s
 
=
 
[
"
B
"
,
 
"
K
B
"
,
 
"
M
B
"
,
 
"
G
B
"
,
 
"
T
B
"
,
 
"
P
B
"
,
 
"
E
B
"
,
 
"
Z
B
"
,
 
"
Y
B
"
]


 
 
 
 
e
l
i
f
 
s
i
z
e
_
t
y
p
e
 
=
=
 
"
a
c
c
u
r
a
t
e
"
:


 
 
 
 
 
 
 
 
b
a
s
e
 
=
 
1
0
2
4


 
 
 
 
 
 
 
 
s
u
f
f
i
x
e
s
 
=
 
[
"
B
"
,
 
"
K
i
B
"
,
 
"
M
i
B
"
,
 
"
G
i
B
"
,
 
"
T
i
B
"
,
 
"
P
i
B
"
,
 
"
E
i
B
"
,
 
"
Z
i
B
"
,
 
"
Y
i
B
"
]


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
f
"
I
n
v
a
l
i
d
 
s
i
z
e
 
t
y
p
e
:
 
{
s
i
z
e
_
t
y
p
e
}
"
)




 
 
 
 
i
f
 
b
y
t
e
s
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
0
 
{
}
{
}
"
.
f
o
r
m
a
t
(
s
u
f
f
i
x
e
s
[
0
]
,
 
"
B
"
 
i
f
 
d
e
c
i
m
a
l
s
 
>
 
0
 
e
l
s
e
 
"
"
)




 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
a
p
p
r
o
p
r
i
a
t
e
 
s
c
a
l
e
 
(
p
o
w
e
r
 
o
f
 
1
0
2
4
)
 
a
n
d
 
f
o
r
m
a
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


 
 
 
 
#
 
a
p
p
r
o
p
r
i
a
t
e
l
y
.


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
s
u
f
f
i
x
e
s
)
)
:


 
 
 
 
 
 
 
 
u
n
i
t
 
=
 
b
a
s
e
 
*
*
 
(
i
 
+
 
1
)


 
 
 
 
 
 
 
 
i
f
 
b
y
t
e
s
 
<
 
u
n
i
t
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
{
:
.
{
d
e
c
i
m
a
l
s
}
f
}
 
{
}
{
}
"
.
f
o
r
m
a
t
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
y
t
e
s
 
/
 
u
n
i
t
,
 
s
u
f
f
i
x
e
s
[
i
]
,
 
"
B
"
 
i
f
 
d
e
c
i
m
a
l
s
 
>
 
0
 
e
l
s
e
 
"
"
,
 
d
e
c
i
m
a
l
s
=
d
e
c
i
m
a
l
s
import unittest

class TestFormatBytes(unittest.TestCase):

    def test_zero_bytes(self):
        result = format_bytes(0)
        self.assertIn(result, ['0 B', '0 Byte'])

    def test_two_kb(self):
        result = format_bytes(2048)
        self.assertIn(result, ['2 KB', '2.0 KB'])

    def test_two_kib(self):
        result = format_bytes(2048, {'sizeType': 'accurate'})
        self.assertIn(result, ['2 KiB', '2.0 KiB'])

    def test_five_mb(self):
        result = format_bytes(5242880)
        self.assertIn(result, ['5 MB', '5.0 MB'])

    def test_five_mib_with_decimals(self):
        result = format_bytes(5242880, {'decimals': 2, 'sizeType': 'accurate'})
        self.assertEqual(result, '5.00 MiB')
if __name__ == '__main__':
    unittest.main()