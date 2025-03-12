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
 
c
a
n
C
o
m
p
l
e
t
e
C
i
r
c
u
i
t
(
g
a
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
 
c
o
s
t
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


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
i
f
 
t
h
e
r
e
 
e
x
i
s
t
s
 
a
 
s
t
a
r
t
i
n
g
 
g
a
s
 
s
t
a
t
i
o
n
'
s
 
i
n
d
e
x
 
w
h
e
r
e
 
y
o
u
 
c
a
n
 
t
r
a
v
e
l


 
 
 
 
a
r
o
u
n
d
 
t
h
e
 
c
i
r
c
u
i
t
 
o
n
c
e
 
i
n
 
a
 
c
l
o
c
k
w
i
s
e
 
d
i
r
e
c
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


 
 
 
 
 
 
 
 
g
a
s
 
(
L
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
 
L
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
a
m
o
u
n
t
 
o
f
 
g
a
s
 
a
t
 
e
a
c
h
 
s
t
a
t
i
o
n
.


 
 
 
 
 
 
 
 
c
o
s
t
 
(
L
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
 
L
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
c
o
s
t
 
o
f
 
g
a
s
 
t
o
 
t
r
a
v
e
l
 
f
r
o
m
 
e
a
c
h
 
s
t
a
t
i
o
n
 
t
o
 
t
h
e
 
n
e
x
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
g
a
s
 
s
t
a
t
i
o
n
'
s
 
i
n
d
e
x
 
i
f
 
t
h
e
 
c
i
r
c
u
i
t
 
c
a
n
 
b
e
 
c
o
m
p
l
e
t
e
d
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
 
-
1
.


 
 
 
 
"
"
"


 
 
 
 
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
r
e
 
i
s
 
e
n
o
u
g
h
 
g
a
s
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
c
i
r
c
u
i
t


 
 
 
 
i
f
 
s
u
m
(
g
a
s
)
 
<
 
s
u
m
(
c
o
s
t
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
-
1




 
 
 
 
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
 
a
m
o
u
n
t
 
o
f
 
g
a
s
 
l
e
f
t
 
a
t
 
e
a
c
h
 
s
t
a
t
i
o
n


 
 
 
 
g
a
s
_
l
e
f
t
 
=
 
[
g
a
s
[
i
]
 
-
 
c
o
s
t
[
i
]
 
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
g
a
s
)
)
]




 
 
 
 
#
 
F
i
n
d
 
t
h
e
 
s
t
a
r
t
i
n
g
 
g
a
s
 
s
t
a
t
i
o
n
'
s
 
i
n
d
e
x


 
 
 
 
s
t
a
r
t
_
i
n
d
e
x
 
=
 
0


 
 
 
 
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
g
a
s
_
l
e
f
t
)
)
:


 
 
 
 
 
 
 
 
i
f
 
g
a
s
_
l
e
f
t
[
i
]
 
<
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
r
t
_
i
n
d
e
x
 
=
 
i
 
+
 
1


 
 
 
 
 
 
 
 
e
l
i
f
 
g
a
s
_
l
e
f
t
[
i
]
 
=
=
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
r
t
_
i
n
d
e
x
 
=
 
i


 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k




 
 
 
 
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
i
r
c
u
i
t
 
c
a
n
 
b
e
 
c
o
m
p
l
e
t
e
d
 
i
n
 
a
 
c
l
o
c
k
w
i
s
e
 
d
i
r
e
c
t
i
o
n


 
 
 
 
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
s
t
a
r
t
_
i
n
d
e
x
,
 
s
t
a
r
t
_
i
n
d
e
x
 
+
 
l
e
n
(
g
a
s
)
)
:


 
 
 
 
 
 
 
 
i
f
 
g
a
s
_
l
e
f
t
[
i
 
%
 
l
e
n
(
g
a
s
)
]
 
<
 
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
-
1




 
 
 
 
r
e
t
u
r
n
 
s
t
a
r
t
_
i
n
d
e
x






d
e
f
 
c
a
n
C
o
m
p
l
e
t
e
C
i
r
c
u
i
t
2
(
g
a
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
 
c
o
s
t
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


 
 
 
 
D
e
t
e
r
m
i
n
e
s
 
i
f
 
t
h
e
r
e
 
e
x
i
s
t
s
 
a
 
s
t
a
r
t
i
n
g
 
g
a
s
 
s
t
a
t
i
o
n
'
s
 
i
n
d
e
x
 
w
h
e
r
e
 
y
o
u
 
c
a
n
 
t
r
a
v
e
l


 
 
 
 
a
r
o
u
n
d
 
t
h
e
 
c
i
r
c
u
i
t
 
o
n
c
e
 
i
n
 
a
 
c
l
o
c
k
w
i
s
e
 
d
i
r
e
c
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


 
 
 
 
 
 
 
 
g
a
s
 
(
L
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
 
L
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
a
m
o
u
n
t
 
o
f
 
g
a
s
 
a
t
 
e
a
c
h
 
s
t
a
t
i
o
n
.


 
 
 
 
 
 
 
 
c
o
s
t
 
(
L
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
 
L
i
s
t
 
o
f
 
i
n
t
e
g
e
r
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
i
n
g
 
t
h
e
 
c
o
s
t
 
o
f
 
g
a
s
 
t
o
 
t
r
a
v
e
l
 
f
r
o
m
 
e
a
c
h
 
s
t
a
t
i
o
n
 
t
o
 
t
h
e
 
n
e
x
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
s
t
a
r
t
i
n
g
 
g
a
s
 
s
t
a
t
i
o
n
'
s
 
i
n
d
e
x
 
i
f
 
t
h
e
 
c
i
r
c
u
i
t
 
c
a
n
 
b
e
 
c
o
m
p
l
e
t
e
d
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
 
-
1
.


 
 
 
 
"
"
"


 
 
 
 
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
r
e
 
i
s
 
e
n
o
u
g
h
 
g
a
s
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
e
 
c
i
r
c
u
i
t


 
 
 
 
i
f
 
s
u
m
(
g
a
s
)
 
<
 
s
u
m
(
c
o
s
t
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
-
import unittest


class TestCanCompleteCircuit(unittest.TestCase):

    def test_possible_single_station(self):
        gas = [5]
        cost = [4]
        expected = 0
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_impossible_single_station(self):
        gas = [4]
        cost = [5]
        expected = -1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_two_stations_possible(self):
        gas = [1, 2]
        cost = [2, 1]
        expected = 1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_circular_route_possible(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_circular_route_impossible(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()