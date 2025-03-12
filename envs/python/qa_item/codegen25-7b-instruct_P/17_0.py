d
e
f
 
h
a
v
e
r
s
i
n
e
_
d
i
s
t
a
n
c
e
(
l
a
t
1
:
 
f
l
o
a
t
,
 
l
o
n
1
:
 
f
l
o
a
t
,
 
l
a
t
2
:
 
f
l
o
a
t
,
 
l
o
n
2
:
 
f
l
o
a
t
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
"
"
"


 
 
 
 
c
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
s
t
a
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
 
p
o
i
n
t
s
 
o
n
 
t
h
e
 
e
a
r
t
h
 
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
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
a
t
1
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
p
o
i
n
t
 
i
n
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
1
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
f
i
r
s
t
 
p
o
i
n
t
 
i
n
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
a
t
2
 
(
f
l
o
a
t
)
:
 
L
a
t
i
t
u
d
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
 
i
n
 
d
e
g
r
e
e
s
.


 
 
 
 
 
 
 
 
l
o
n
2
 
(
f
l
o
a
t
)
:
 
L
o
n
g
i
t
u
d
e
 
o
f
 
t
h
e
 
s
e
c
o
n
d
 
p
o
i
n
t
 
i
n
 
d
e
g
r
e
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


 
 
 
 
 
 
 
 
D
i
s
t
a
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
h
e
 
t
w
o
 
p
o
i
n
t
s
 
i
n
 
k
i
l
o
m
e
t
e
r
s
.


 
 
 
 
"
"
"


 
 
 
 
#
 
c
o
n
v
e
r
t
 
d
e
c
i
m
a
l
 
d
e
g
r
e
e
s
 
t
o
 
r
a
d
i
a
n
s


 
 
 
 
l
o
n
1
,
 
l
a
t
1
,
 
l
o
n
2
,
 
l
a
t
2
 
=
 
m
a
p
(
r
a
d
i
a
n
s
,
 
[
l
o
n
1
,
 
l
a
t
1
,
 
l
o
n
2
,
 
l
a
t
2
]
)




 
 
 
 
#
 
h
a
v
e
r
s
i
n
e
 
f
o
r
m
u
l
a


 
 
 
 
d
l
o
n
 
=
 
l
o
n
2
 
-
 
l
o
n
1


 
 
 
 
d
l
a
t
 
=
 
l
a
t
2
 
-
 
l
a
t
1


 
 
 
 
a
 
=
 
s
i
n
(
d
l
a
t
 
/
 
2
)
 
*
*
 
2
 
+
 
c
o
s
(
l
a
t
1
)
 
*
 
c
o
s
(
l
a
t
2
)
 
*
 
s
i
n
(
d
l
o
n
 
/
 
2
)
 
*
*
 
2


 
 
 
 
c
 
=
 
2
 
*
 
a
s
i
n
(
s
q
r
t
(
a
)
)


 
 
 
 
r
 
=
 
6
3
7
1
 
 
#
 
R
a
d
i
u
s
 
o
f
 
e
a
r
t
h
 
i
n
 
k
i
l
o
m
e
t
e
r
s
.
 
U
s
e
 
3
9
5
6
 
f
o
r
 
m
i
l
e
s


 
 
 
 
r
e
t
u
r
n
 
c
 
*
 
r






d
e
f
 
g
e
t
_
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
(


 
 
 
 
l
o
c
a
t
i
o
n
s
:
 
L
i
s
t
[
L
o
c
a
t
i
o
n
]
,


 
 
 
 
a
p
i
_
k
e
y
:
 
s
t
r
,


 
 
 
 
l
a
n
g
u
a
g
e
:
 
s
t
r
 
=
 
"
e
n
"
,


 
 
 
 
u
n
i
t
s
:
 
s
t
r
 
=
 
"
m
e
t
r
i
c
"
,


)
 
-
>
 
L
i
s
t
[
L
i
s
t
[
f
l
o
a
t
]
]
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
 
d
i
s
t
a
n
c
e
 
m
a
t
r
i
x
 
b
e
t
w
e
e
n
 
a
l
l
 
l
o
c
a
t
i
o
n
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
c
a
t
i
o
n
s
 
(
L
i
s
t
[
L
o
c
a
t
i
o
n
]
)
:
 
L
i
s
t
 
o
f
 
l
o
c
a
t
i
o
n
s
.


 
 
 
 
 
 
 
 
a
p
i
_
k
e
y
 
(
s
t
r
)
:
 
G
o
o
g
l
e
 
M
a
p
s
 
A
P
I
 
k
e
y
.


 
 
 
 
 
 
 
 
l
a
n
g
u
a
g
e
 
(
s
t
r
)
:
 
L
a
n
g
u
a
g
e
 
o
f
 
t
h
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
s
.


 
 
 
 
 
 
 
 
u
n
i
t
s
 
(
s
t
r
)
:
 
U
n
i
t
s
 
o
f
 
t
h
e
 
d
i
s
t
a
n
c
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


 
 
 
 
 
 
 
 
D
i
s
t
a
n
c
e
 
m
a
t
r
i
x
 
b
e
t
w
e
e
n
 
a
l
l
 
l
o
c
a
t
i
o
n
s
.


 
 
 
 
"
"
"


 
 
 
 
o
r
i
g
i
n
s
 
=
 
[
l
o
c
a
t
i
o
n
.
c
o
o
r
d
i
n
a
t
e
s
 
f
o
r
 
l
o
c
a
t
i
o
n
 
i
n
 
l
o
c
a
t
i
o
n
s
]


 
 
 
 
d
e
s
t
i
n
a
t
i
o
n
s
 
=
 
[
l
o
c
a
t
i
o
n
.
c
o
o
r
d
i
n
a
t
e
s
 
f
o
r
 
l
o
c
a
t
i
o
n
 
i
n
 
l
o
c
a
t
i
o
n
s
]


 
 
 
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
 
=
 
[
]


 
 
 
 
f
o
r
 
o
r
i
g
i
n
,
 
d
e
s
t
i
n
a
t
i
o
n
 
i
n
 
z
i
p
(
o
r
i
g
i
n
s
,
 
d
e
s
t
i
n
a
t
i
o
n
s
)
:


 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
 
=
 
h
a
v
e
r
s
i
n
e
_
d
i
s
t
a
n
c
e
(
*
o
r
i
g
i
n
,
 
*
d
e
s
t
i
n
a
t
i
o
n
)


 
 
 
 
 
 
 
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x
.
a
p
p
e
n
d
(
d
i
s
t
a
n
c
e
)


 
 
 
 
r
e
t
u
r
n
 
d
i
s
t
a
n
c
e
_
m
a
t
r
i
x






d
e
f
 
g
e
t
    import unittest


    class TestHaversineDistance(unittest.TestCase):

        def test_same_point(self):
            # Same point should return a distance of 0
            lat, lon = 52.2296756, 21.0122287
            result = haversine_distance(lat, lon, lat, lon)
            self.assertAlmostEqual(result, 0.0, places=6)

        def test_small_distance(self):
            # Points that are very close together (few meters apart)
            lat1, lon1 = 52.2296756, 21.0122287  # Warsaw, Poland
            lat2, lon2 = 52.2296756, 21.0122297  # Very close to the previous point
            result = haversine_distance(lat1, lon1, lat2, lon2)
            self.assertAlmostEqual(result, 0.0001, places=4)  # Expected small distance

        def test_large_distance(self):
            # Points that are far apart
            lat1, lon1 = 52.2296756, 21.0122287  # Warsaw, Poland
            lat2, lon2 = 41.8919300, 12.5113300  # Rome, Italy
            result = haversine_distance(lat1, lon1, lat2, lon2)
            self.assertAlmostEqual(result, 1315.514, places=2)  # Approx distance in km

        def test_equator_distance(self):
            # Points on the equator
            lat1, lon1 = 0.0, 0.0  # Gulf of Guinea (Equator and Prime Meridian intersection)
            lat2, lon2 = 0.0, 90.0  # On the Equator, 90 degrees east
            result = haversine_distance(lat1, lon1, lat2, lon2)
            self.assertAlmostEqual(result, 10007.54, places=2)  # Approx quarter of Earth's circumference

        def test_pole_to_pole(self):
            # Distance from North Pole to South Pole
            lat1, lon1 = 90.0, 0.0  # North Pole
            lat2, lon2 = -90.0, 0.0  # South Pole
            result = haversine_distance(lat1, lon1, lat2, lon2)
            self.assertAlmostEqual(result, 20015.09, places=2)  # Approx half of Earth's circumference

if __name__ == '__main__':
    unittest.main()