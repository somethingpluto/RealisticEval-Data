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
 
f
i
n
d
_
d
u
p
l
i
c
a
t
e
s
_
e
x
c
l
u
d
i
n
g
_
i
p
s
(
i
p
_
l
i
s
t
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
g
n
o
r
e
_
l
i
s
t
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
n
d
 
d
u
p
l
i
c
a
t
e
 
I
P
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
 
I
P
 
l
i
s
t
 
e
x
c
l
u
d
i
n
g
 
s
p
e
c
i
f
i
e
d
 
I
P
s
 
t
o
 
i
g
n
o
r
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
p
_
l
i
s
t
 
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
 
L
i
s
t
 
o
f
 
I
P
 
a
d
d
r
e
s
s
e
s


 
 
 
 
 
 
 
 
i
g
n
o
r
e
_
l
i
s
t
 
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
 
L
i
s
t
 
o
f
 
I
P
 
a
d
d
r
e
s
s
e
s
 
t
o
 
i
g
n
o
r




 
 
 
 
R
e
t
u
r
n
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
:
 
A
 
l
i
s
t
 
o
f
 
d
u
p
l
i
c
a
t
e
 
I
P
s
 
e
x
c
l
u
d
i
n
g
 
t
h
o
s
e
 
i
n
 
t
h
e
 
i
g
n
o
r
e
 
l
i
s
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
r
e
a
t
e
 
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
 
t
o
 
s
t
o
r
e
 
I
P
s
 
a
n
d
 
t
h
e
i
r
 
c
o
u
n
t


 
 
 
 
i
p
_
c
o
u
n
t
 
=
 
{
}




 
 
 
 
#
 
L
o
o
p
 
t
h
r
o
u
g
h
 
e
a
c
h
 
I
P
 
i
n
 
t
h
e
 
l
i
s
t


 
 
 
 
f
o
r
 
i
p
 
i
n
 
i
p
_
l
i
s
t
:


 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
I
P
 
i
s
 
i
n
 
t
h
e
 
i
g
n
o
r
e
 
l
i
s
t


 
 
 
 
 
 
 
 
i
f
 
i
p
 
i
n
 
i
g
n
o
r
e
_
l
i
s
t
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
y
e
s
,
 
s
k
i
p
 
i
t


 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e




 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
I
P
 
i
s
 
a
l
r
e
a
d
y
 
i
n
 
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


 
 
 
 
 
 
 
 
i
f
 
i
p
 
i
n
 
i
p
_
c
o
u
n
t
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
y
e
s
,
 
i
n
c
r
e
m
e
n
t
 
i
t
s
 
c
o
u
n
t


 
 
 
 
 
 
 
 
 
 
 
 
i
p
_
c
o
u
n
t
[
i
p
]
 
+
=
 
1


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
n
o
t
,
 
a
d
d
 
i
t
 
t
o
 
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
 
w
i
t
h
 
a
 
c
o
u
n
t
 
o
f
 
1


 
 
 
 
 
 
 
 
 
 
 
 
i
p
_
c
o
u
n
t
[
i
p
]
 
=
 
1




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
l
i
s
t
 
t
o
 
s
t
o
r
e
 
d
u
p
l
i
c
a
t
e
 
I
P
s


 
 
 
 
d
u
p
l
i
c
a
t
e
_
i
p
s
 
=
 
[
]




 
 
 
 
#
 
L
o
o
p
 
t
h
r
o
u
g
h
 
e
a
c
h
 
I
P
 
i
n
 
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


 
 
 
 
f
o
r
 
i
p
,
 
c
o
u
n
t
 
i
n
 
i
p
_
c
o
u
n
t
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
c
o
u
n
t
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
1


 
 
 
 
 
 
 
 
i
f
 
c
o
u
n
t
 
>
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
y
e
s
,
 
a
d
d
 
t
h
e
 
I
P
 
t
o
 
t
h
e
 
d
u
p
l
i
c
a
t
e
 
l
i
s
t


 
 
 
 
 
 
 
 
 
 
 
 
d
u
p
l
i
c
a
t
e
_
i
p
s
.
a
p
p
e
n
d
(
i
p
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
 
d
u
p
l
i
c
a
t
e
 
I
P
 
l
i
s
t


 
 
 
 
r
e
t
u
r
n
 
d
u
p
l
i
c
a
t
e
_
i
p
s






d
e
f
 
f
i
n
d
_
d
u
p
l
i
c
a
t
e
s
_
i
n
c
l
u
d
i
n
g
_
i
p
s
(
i
p
_
l
i
s
t
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
g
n
o
r
e
_
l
i
s
t
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
n
d
 
d
u
p
l
i
c
a
t
e
 
I
P
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
 
I
P
 
l
i
s
t
 
i
n
c
l
u
d
i
n
g
 
s
p
e
c
i
f
i
e
d
 
I
P
s
 
t
o
 
i
g
n
o
r
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
p
_
l
i
s
t
 
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
 
L
i
s
t
 
o
f
 
I
P
 
a
d
d
r
e
s
s
e
s


 
 
 
 
 
 
 
 
i
g
n
o
r
e
_
l
i
s
t
 
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
 
L
i
s
t
 
o
f
 
I
P
 
a
d
d
r
e
s
s
e
s
 
t
o
 
i
g
n
o
r




 
 
 
 
R
e
t
u
r
n
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
:
 
A
 
l
i
s
t
 
o
f
 
d
u
p
l
i
c
a
t
e
 
I
P
s
 
i
n
c
l
u
d
i
n
g
 
t
h
o
s
e
 
i
n
 
t
h
e
 
i
g
n
o
r
e
 
l
i
s
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
r
e
a
t
e
 
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
 
t
o
 
s
t
o
r
e
 
I
P
s
 
a
n
d
 
t
h
e
i
r
 
c
o
u
n
t


 
 
 
 
i
p
_
c
o
u
n
t
 
=
 
{
}




 
 
 
 
#
 
L
o
o
p
 
t
h
r
o
u
g
h
 
e
a
c
h
 
I
P
 
i
n
 
t
h
e
 
l
i
s
t


 
 
 
 
f
o
r
 
i
p
 
i
n
import unittest


class TestFindDuplicateIPs(unittest.TestCase):

    def test_basic_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])

    def test_ignored_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "192.168.1.2"]
        ignore_list = ["192.168.1.1"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_no_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_mixed_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "10.0.0.1", "192.168.1.2"]
        ignore_list = ["192.168.1.2"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])

    def test_empty_input(self):
        ip_list = []
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_only_ignored_ips(self):
        ip_list = ["192.168.1.1", "192.168.1.1"]
        ignore_list = ["192.168.1.1"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_all_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "192.168.1.1"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])
if __name__ == '__main__':
    unittest.main()