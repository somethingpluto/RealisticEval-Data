f
r
o
m
 
d
a
t
e
t
i
m
e
 
i
m
p
o
r
t
 
d
a
t
e






d
e
f
 
c
a
l
c
u
l
a
t
e
_
g
o
o
d
_
f
r
i
d
a
y
(
y
e
a
r
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
a
l
c
u
l
a
t
e
 
t
h
e
 
d
a
t
e
 
o
f
 
G
o
o
d
 
F
r
i
d
a
y
 
i
n
 
a
 
g
i
v
e
n
 
y
e
a
r
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
F
r
i
 
M
a
r
 
2
9
 
2
0
2
4




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
e
a
r
 
(
i
n
t
)
:
 
T
h
e
 
y
e
a
r
 
f
o
r
 
w
h
i
c
h
 
t
o
 
c
a
l
c
u
l
a
t
e
 
G
o
o
d
 
F
r
i
d
a
y
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
 
d
a
t
e
 
o
f
 
G
o
o
d
 
F
r
i
d
a
y
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
y
e
a
r
 
o
f
 
t
h
e
 
p
r
e
v
i
o
u
s
 
c
a
l
c
u
l
a
t
i
o
n


 
 
 
 
p
r
e
v
i
o
u
s
_
y
e
a
r
 
=
 
y
e
a
r
 
-
 
1
 
i
f
 
y
e
a
r
 
%
 
2
 
=
=
 
0
 
e
l
s
e
 
y
e
a
r




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
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
 
d
a
y
s
 
b
e
t
w
e
e
n
 
t
h
e
 
s
t
a
r
t
 
o
f
 
t
h
e
 
p
r
e
v
i
o
u
s
 
y
e
a
r
 
a
n
d


 
 
 
 
#
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
c
u
r
r
e
n
t
 
y
e
a
r


 
 
 
 
d
a
y
s
_
b
e
t
w
e
e
n
 
=
 
(
d
a
t
e
(
p
r
e
v
i
o
u
s
_
y
e
a
r
,
 
1
2
,
 
3
1
)
 
-
 
d
a
t
e
(
y
e
a
r
,
 
1
,
 
1
)
)
.
d
a
y
s




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
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
 
d
a
y
s
 
b
e
t
w
e
e
n
 
t
h
e
 
s
t
a
r
t
 
o
f
 
t
h
e
 
c
u
r
r
e
n
t
 
y
e
a
r
 
a
n
d


 
 
 
 
#
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
n
e
x
t
 
y
e
a
r


 
 
 
 
d
a
y
s
_
t
o
_
n
e
x
t
_
y
e
a
r
 
=
 
(
d
a
t
e
(
y
e
a
r
 
+
 
1
,
 
1
,
 
1
)
 
-
 
d
a
t
e
(
y
e
a
r
,
 
1
2
,
 
3
1
)
)
.
d
a
y
s




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
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
 
d
a
y
s
 
b
e
t
w
e
e
n
 
t
h
e
 
s
t
a
r
t
 
o
f
 
t
h
e
 
p
r
e
v
i
o
u
s
 
y
e
a
r
 
a
n
d


 
 
 
 
#
 
t
h
e
 
G
o
o
d
 
F
r
i
d
a
y


 
 
 
 
d
a
y
s
_
b
e
t
w
e
e
n
_
p
r
e
v
i
o
u
s
_
y
e
a
r
_
a
n
d
_
g
o
o
d
_
f
r
i
d
a
y
 
=
 
(


 
 
 
 
 
 
 
 
d
a
y
s
_
b
e
t
w
e
e
n
 
-
 
d
a
y
s
_
t
o
_
n
e
x
t
_
y
e
a
r
 
+
 
2


 
 
 
 
)




 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
d
a
t
e
 
o
f
 
G
o
o
d
 
F
r
i
d
a
y


 
 
 
 
g
o
o
d
_
f
r
i
d
a
y
 
=
 
d
a
t
e
(
p
r
e
v
i
o
u
s
_
y
e
a
r
,
 
1
,
 
1
)
 
+
 
t
i
m
e
d
e
l
t
a
(


 
 
 
 
 
 
 
 
d
a
y
s
=
d
a
y
s
_
b
e
t
w
e
e
n
_
p
r
e
v
i
o
u
s
_
y
e
a
r
_
a
n
d
_
g
o
o
d
_
f
r
i
d
a
y


 
 
 
 
)




 
 
 
 
#
 
F
o
r
m
a
t
 
t
h
e
 
d
a
t
e
 
o
f
 
G
o
o
d
 
F
r
i
d
a
y


 
 
 
 
r
e
t
u
r
n
 
g
o
o
d
_
f
r
i
d
a
y
.
s
t
r
f
t
i
m
e
(
"
%
a
 
%
b
 
%
d
 
%
Y
"
)






d
e
f
 
c
a
l
c
u
l
a
t
e
_
n
e
w
_
y
e
a
r
s
_
d
a
y
(
y
e
a
r
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
a
l
c
u
l
a
t
e
 
t
h
e
 
d
a
t
e
 
o
f
 
N
e
w
 
Y
e
a
r
'
s
 
D
a
y
 
i
n
 
a
 
g
i
v
e
n
 
y
e
a
r
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
2
0
2
4


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
M
o
n
 
J
a
n
 
 
1
 
2
0
2
4




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
e
a
r
 
(
i
n
t
)
:
 
T
h
e
 
y
e
a
r
 
f
o
r
 
w
h
i
c
h
 
t
o
 
c
a
l
c
u
l
a
t
e
 
N
e
w
 
Y
e
a
r
'
s
 
D
a
y
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
 
d
a
t
e
 
o
f
 
N
e
w
 
Y
e
a
r
'
s
 
D
a
y
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
a
l
c
u
l
a
t
e
 
t
h
e
 
d
a
t
e
 
o
f
 
N
e
w
 
Y
e
a
r
'
s
 
D
a
y


 
 
 
 
n
e
w
_
y
e
a
r
s
_
d
a
y
 
=
 
d
a
t
e
(
y
e
a
r
,
 
1
,
 
1
)




 
 
 
 
#
 
F
o
r
m
a
t
 
t
h
e
 
d
a
t
e
 
o
f
 
N
e
w
 
Y
e
a
r
'
s
 
D
a
y
import unittest


class TestCalculateGoodFriday(unittest.TestCase):

    def test_calculate_good_friday_2024(self):
        result = calculate_good_friday(2024)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Mar 29 2024')

    def test_calculate_good_friday_2021(self):
        result = calculate_good_friday(2021)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 02 2021')

    def test_calculate_good_friday_2000(self):
        result = calculate_good_friday(2000)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 21 2000')

    def test_calculate_good_friday_2019(self):
        result = calculate_good_friday(2019)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 19 2019')

    def test_calculate_good_friday_1999(self):
        result = calculate_good_friday(1999)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 02 1999')

    def test_calculate_good_friday_1981(self):
        result = calculate_good_friday(1981)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 17 1981')

    def test_calculate_good_friday_1954(self):
        result = calculate_good_friday(1954)
        self.assertEqual(result.strftime('%a %b %d %Y'), 'Fri Apr 16 1954')

if __name__ == '__main__':
    unittest.main()