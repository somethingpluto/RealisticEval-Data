d
e
f
 
b
y
t
e
s
_
t
o
_
s
i
z
e
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
n
v
e
r
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
 
B
y
t
e
s
 
i
n
t
o
 
a
 
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


 
 
 
 
w
i
t
h
 
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
 
u
n
i
t
s
 
(
B
y
t
e
s
,
 
K
B
,
 
M
B
,
 
G
B
,
 
o
r
 
T
B
)
 
a
n
d
 
k
e
e
p
s
 
t
w
o
 
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
 
b
e
 
c
o
n
v
e
r
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
 
s
i
z
e
 
i
n
 
B
y
t
e
s
,
 
K
B
,
 
M
B
,
 
G
B
,
 
o
r
 
T
B
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
b
y
t
e
s
 
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
 
f
"
{
b
y
t
e
s
:
.
2
f
}
 
B
"


 
 
 
 
e
l
i
f
 
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
b
y
t
e
s
 
/
 
1
0
2
4
:
.
2
f
}
 
K
B
"


 
 
 
 
e
l
i
f
 
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
3
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
b
y
t
e
s
 
/
 
(
1
0
2
4
 
*
*
 
2
)
:
.
2
f
}
 
M
B
"


 
 
 
 
e
l
i
f
 
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
b
y
t
e
s
 
/
 
(
1
0
2
4
 
*
*
 
3
)
:
.
2
f
}
 
G
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
 
f
"
{
b
y
t
e
s
 
/
 
(
1
0
2
4
 
*
*
 
4
)
:
.
2
f
}
 
T
B
"






d
e
f
 
s
i
z
e
_
t
o
_
b
y
t
e
s
(
s
i
z
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
g
i
v
e
n
 
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
 
a
 
s
i
z
e
 
(
B
y
t
e
s
,
 
K
B
,
 
M
B
,
 
G
B
,
 
o
r
 
T
B
)


 
 
 
 
i
n
t
o
 
t
h
e
 
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
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
i
z
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
 
s
i
z
e
 
t
o
 
b
e
 
c
o
n
v
e
r
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
 
b
y
t
e
s
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
h
e
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
s
i
z
e
.
e
n
d
s
w
i
t
h
(
"
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
s
i
z
e
[
:
-
1
]
)


 
 
 
 
e
l
i
f
 
s
i
z
e
.
e
n
d
s
w
i
t
h
(
"
K
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
[
:
-
2
]
)
 
*
 
1
0
2
4
)


 
 
 
 
e
l
i
f
 
s
i
z
e
.
e
n
d
s
w
i
t
h
(
"
M
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
[
:
-
2
]
)
 
*
 
1
0
2
4
 
*
*
 
2
)


 
 
 
 
e
l
i
f
 
s
i
z
e
.
e
n
d
s
w
i
t
h
(
"
G
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
[
:
-
2
]
)
 
*
 
1
0
2
4
 
*
*
 
3
)


 
 
 
 
e
l
i
f
 
s
i
z
e
.
e
n
d
s
w
i
t
h
(
"
T
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
[
:
-
2
]
)
 
*
 
1
0
2
4
 
*
*
 
4
)


 
 
 
 
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
 
s
t
r
i
n
g
:
 
{
s
i
z
e
}
"
)






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
 
s
i
z
e
 
o
f
import unittest


class TestBytesToSize(unittest.TestCase):
    def test_convert_bytes_to_kb(self):
        self.assertEqual(bytes_to_size(1024), '1.00 KB')
        self.assertEqual(bytes_to_size(2048), '2.00 KB')

    def test_convert_bytes_to_mb(self):
        self.assertEqual(bytes_to_size(1048576), '1.00 MB')
        self.assertEqual(bytes_to_size(2097152), '2.00 MB')

    def test_convert_bytes_to_gb(self):
        self.assertEqual(bytes_to_size(1073741824), '1.00 GB')
        self.assertEqual(bytes_to_size(2147483648), '2.00 GB')

    def test_convert_bytes_to_tb(self):
        self.assertEqual(bytes_to_size(1099511627776), '1.00 TB')
        self.assertEqual(bytes_to_size(2199023255552), '2.00 TB')

if __name__ == '__main__':
    unittest.main()