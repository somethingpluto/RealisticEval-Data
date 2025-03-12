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
 
T
u
p
l
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
t
o
t
a
l
_
s
e
c
o
n
d
s
(
t
i
m
e
:
 
T
u
p
l
e
[
i
n
t
]
)
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
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s
 
g
i
v
e
n
 
a
 
t
u
p
l
e
 
o
r
 
l
i
s
t
 
o
f
 
t
i
m
e
 
p
e
r
i
o
d
s
 
i
n
 
t
h
e
 
o
r
d
e
r
 
o
f


 
 
 
 
d
a
y
s
,
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
,
 
a
n
d
 
s
e
c
o
n
d
s
.




 
 
 
 
:
p
a
r
a
m
 
t
i
m
e
:
 
t
u
p
l
e
 
o
r
 
l
i
s
t
,
 
w
h
e
r
e


 
 
 
 
 
 
 
 
t
i
m
e
[
0
]
 
-
 
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
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
1
]
 
-
 
n
u
m
b
e
r
 
o
f
 
h
o
u
r
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
2
]
 
-
 
n
u
m
b
e
r
 
o
f
 
m
i
n
u
t
e
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
3
]
 
-
 
n
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s
 
(
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
r
e
t
u
r
n
:
 
i
n
t
,
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s




 
 
 
 
E
x
a
m
p
l
e
s
:


 
 
 
 
 
 
 
 
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
t
o
t
a
l
_
s
e
c
o
n
d
s
(
[
1
,
 
2
,
 
3
,
 
4
]
)
 
r
e
t
u
r
n
s
 
9
3
7
8
4


 
 
 
 
 
 
 
 
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
t
o
t
a
l
_
s
e
c
o
n
d
s
(
[
0
,
 
2
,
 
3
]
)
 
r
e
t
u
r
n
s
 
7
3
8
0


 
 
 
 
"
"
"


 
 
 
 
t
o
t
a
l
_
s
e
c
o
n
d
s
 
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
t
i
m
e
)
)
:


 
 
 
 
 
 
 
 
t
o
t
a
l
_
s
e
c
o
n
d
s
 
+
=
 
t
i
m
e
[
i
]
 
*
 
(
6
0
 
*
*
 
(
l
e
n
(
t
i
m
e
)
 
-
 
i
 
-
 
1
)
)


 
 
 
 
r
e
t
u
r
n
 
t
o
t
a
l
_
s
e
c
o
n
d
s






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
t
i
m
e
_
p
e
r
i
o
d
s
(
t
o
t
a
l
_
s
e
c
o
n
d
s
:
 
i
n
t
)
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
 
t
i
m
e
 
p
e
r
i
o
d
s
 
i
n
 
t
h
e
 
o
r
d
e
r
 
o
f
 
d
a
y
s
,
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
,
 
a
n
d
 
s
e
c
o
n
d
s
.




 
 
 
 
:
p
a
r
a
m
 
t
o
t
a
l
_
s
e
c
o
n
d
s
:
 
i
n
t
,
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s


 
 
 
 
:
r
e
t
u
r
n
:
 
t
u
p
l
e
,
 
w
h
e
r
e


 
 
 
 
 
 
 
 
t
i
m
e
[
0
]
 
-
 
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
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
1
]
 
-
 
n
u
m
b
e
r
 
o
f
 
h
o
u
r
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
2
]
 
-
 
n
u
m
b
e
r
 
o
f
 
m
i
n
u
t
e
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
3
]
 
-
 
n
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
"
"
"


 
 
 
 
t
i
m
e
 
=
 
[
0
,
 
0
,
 
0
,
 
0
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
t
i
m
e
)
)
:


 
 
 
 
 
 
 
 
t
i
m
e
[
i
]
 
=
 
t
o
t
a
l
_
s
e
c
o
n
d
s
 
/
/
 
(
6
0
 
*
*
 
(
l
e
n
(
t
i
m
e
)
 
-
 
i
 
-
 
1
)
)


 
 
 
 
 
 
 
 
t
o
t
a
l
_
s
e
c
o
n
d
s
 
-
=
 
t
i
m
e
[
i
]
 
*
 
(
6
0
 
*
*
 
(
l
e
n
(
t
i
m
e
)
 
-
 
i
 
-
 
1
)
)


 
 
 
 
r
e
t
u
r
n
 
t
u
p
l
e
(
t
i
m
e
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
t
i
m
e
_
d
i
f
f
e
r
e
n
c
e
(
t
i
m
e
1
:
 
T
u
p
l
e
[
i
n
t
]
,
 
t
i
m
e
2
:
 
T
u
p
l
e
[
i
n
t
]
)
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
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
n
 
t
w
o
 
t
i
m
e
 
p
e
r
i
o
d
s
 
i
n
 
t
h
e
 
o
r
d
e
r
 
o
f
 
d
a
y
s
,
 
h
o
u
r
s
,
 
m
i
n
u
t
e
s
,
 
a
n
d
 
s
e
c
o
n
d
s
.




 
 
 
 
:
p
a
r
a
m
 
t
i
m
e
1
:
 
t
u
p
l
e
,
 
w
h
e
r
e


 
 
 
 
 
 
 
 
t
i
m
e
[
0
]
 
-
 
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
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
[
1
]
 
-
 
n
u
m
b
e
r
 
o
f
 
h
o
u
r
s
 
(
o
p
t
i
o
n
a
l
)


 
 
 
 
 
 
 
 
t
i
m
e
import unittest

class TestCalculateTotalSeconds(unittest.TestCase):

    def test_complete_time(self):
        # Test with full values provided for days, hours, minutes, and seconds
        time = [1, 2, 3, 4]  # 1 day, 2 hours, 3 minutes, 4 seconds
        expected = 93784
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_partial_time(self):
        # Test with some values missing (assumed trailing zeros)
        time = [0, 2, 3]  # 0 days, 2 hours, 3 minutes
        expected = 7380
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_seconds_only(self):
        # Test with only seconds provided
        time = [7200]  # 7200 seconds
        expected = 622080000
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)

    def test_no_time(self):
        # Test with no time values provided
        time = []
        expected = 0
        result = calculate_total_seconds(time)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()