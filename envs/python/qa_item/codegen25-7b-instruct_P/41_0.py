c
l
a
s
s
 
B
l
o
o
m
F
i
l
t
e
r
:


 
 
 
 
"
"
"


 
 
 
 
I
m
p
l
e
m
e
n
t
 
a
 
b
l
o
o
m
 
f
i
l
t
e
r
 
c
l
a
s
s
 
w
i
t
h
 
a
n
 
a
d
d
 
m
e
t
h
o
d
 
t
h
a
t
 
a
d
d
s
 
a
n
 
e
l
e
m
e
n
t
 
t
o
 
t
h
e
 
B
l
o
o
m
 
f
i
l
t
e
r
.
C
a
l
l
e
r
s
 
c
a
n
 
c
h
e
c
k
 
f
o
r
 
t
h
e
 
p
r
e
s
e
n
c
e
 
o
f
 
a
n
 
e
l
e
m
e
n
t
 
d
i
r
e
c
t
l
y
 
u
s
i
n
g
 
t
h
e
 
i
n
 
k
e
y
w
o
r
d


 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
s
i
z
e
,
 
h
a
s
h
_
c
o
u
n
t
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
a
d
d
(
s
e
l
f
,
 
i
t
e
m
)
:


 
 
 
 
 
 
 
 
#
 
A
d
d
 
a
n
 
i
t
e
m
 
t
o
 
t
h
e
 
b
l
o
o
m
 
f
i
l
t
e
r


 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 


 
 
 
 
d
e
f
 
_
_
c
o
n
t
a
i
n
s
_
_
(
s
e
l
f
,
 
i
t
e
m
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
 
a
n
 
i
t
e
m
 
i
s
 
i
n
 
t
h
e
 
b
l
o
o
m
 
f
i
l
t
e
r


 
 
 
 
 
 
 
 
p
a
s
s




c
l
a
s
s
 
B
l
o
o
m
F
i
l
t
e
r
T
e
s
t
s
(
u
n
i
t
t
e
s
t
.
T
e
s
t
C
a
s
e
)
:


 
 
 
 
d
e
f
 
t
e
s
t
_
b
l
o
o
m
_
f
i
l
t
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
b
f
 
=
 
B
l
o
o
m
F
i
l
t
e
r
(
1
0
0
0
,
 
3
)


 
 
 
 
 
 
 
 
b
f
.
a
d
d
(
"
h
e
l
l
o
"
)


 
 
 
 
 
 
 
 
b
f
.
a
d
d
(
"
w
o
r
l
d
"
)


 
 
 
 
 
 
 
 
s
e
l
f
.
a
s
s
e
r
t
T
r
u
e
(
"
h
e
l
l
o
"
 
i
n
 
b
f
)


 
 
 
 
 
 
 
 
s
e
l
f
.
a
s
s
e
r
t
T
r
u
e
(
"
w
o
r
l
d
"
 
i
n
 
b
f
)


 
 
 
 
 
 
 
 
s
e
l
f
.
a
s
s
e
r
t
F
a
l
s
e
(
"
f
o
o
"
 
i
n
 
b
f
)


 
 
 
 
 
 
 
 
s
e
l
f
.
a
s
s
e
r
t
F
a
l
s
e
(
"
b
a
r
"
 
i
n
 
b
f
)




i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
"
_
_
m
a
i
n
_
_
"
:


 
 
 
 
u
n
i
t
t
e
s
t
.
m
a
i
n
(
)


`
`
`




I
n
 
t
h
i
s
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
,
 
w
e
 
u
s
e
 
a
 
h
a
s
h
 
f
u
n
c
t
i
o
n
 
t
h
a
t
 
t
a
k
e
s
 
a
 
s
t
r
i
n
g
 
a
s
 
i
n
p
u
t
 
a
n
d
 
r
e
t
u
r
n
s
 
a
n
 
i
n
t
e
g
e
r
 
a
s
 
o
u
t
p
u
t
.
 
W
e
 
u
s
e
 
a
 
l
i
s
t
 
o
f
 
s
u
c
h
 
h
a
s
h
 
f
u
n
c
t
i
o
n
s
 
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
 
t
h
e
 
h
a
s
h
 
v
a
l
u
e
s
 
f
o
r
 
a
n
 
i
t
e
m
.
 
W
e
 
a
l
s
o
 
u
s
e
 
a
 
b
i
t
 
a
r
r
a
y
 
o
f
 
s
i
z
e
 
`
s
i
z
e
`
 
t
o
 
k
e
e
p
 
t
r
a
c
k
 
o
f
 
w
h
e
t
h
e
r
 
a
n
 
i
t
e
m
 
i
s
 
p
r
e
s
e
n
t
 
i
n
 
t
h
e
 
f
i
l
t
e
r
 
o
r
 
n
o
t
.
 
W
e
 
p
e
r
f
o
r
m
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
o
p
e
r
a
t
i
o
n
s
:




1
.
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
b
i
t
 
a
r
r
a
y
 
t
o
 
a
l
l
 
z
e
r
o
s
.


2
.
 
F
o
r
 
e
a
c
h
 
h
a
s
h
 
f
u
n
c
t
i
o
n
,
 
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
 
h
a
s
h
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
i
t
e
m
 
a
n
d
 
s
e
t
 
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
 
b
i
t
 
i
n
 
t
h
e
 
b
i
t
 
a
r
r
a
y
 
t
o
 
1
.


3
.
 
R
e
t
u
r
n
 
t
h
e
 
b
i
t
 
a
r
r
a
y
.




W
e
 
c
a
n
 
u
s
e
 
t
h
i
s
 
b
i
t
 
a
r
r
a
y
 
t
o
 
c
h
e
c
k
 
w
h
e
t
h
e
r
 
a
n
 
i
t
e
m
 
i
s
 
p
r
e
s
e
n
t
 
i
n
 
t
h
e
 
f
i
l
t
e
r
 
b
y
 
p
e
r
f
o
r
m
i
n
g
 
a
 
b
i
t
w
i
s
e
 
A
N
D
 
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
 
b
i
t
 
a
r
r
a
y
 
a
n
d
 
a
 
m
a
s
k
 
o
f
 
a
l
l
 
o
n
e
s
.
 
I
f
 
t
h
e
 
r
e
s
u
l
t
 
i
s
 
a
l
l
 
o
n
e
s
,
 
t
h
e
n
 
t
h
e
 
i
t
e
m
 
i
s
 
d
e
f
i
n
i
t
e
l
y
 
p
r
e
s
e
n
t
 
i
n
 
t
h
e
 
f
i
l
t
e
r
.




T
o
 
c
h
e
c
k
 
f
o
r
 
t
h
e
 
p
r
e
s
e
n
c
e
 
o
f
 
a
n
 
e
l
e
m
e
n
t
 
u
s
i
n
g
 
t
h
e
 
`
_
_
c
o
n
t
a
i
n
s
_
_
`
 
m
e
t
h
o
d
,
 
w
e
 
f
i
r
s
t
 
c
h
e
c
k
 
i
f
 
t
h
e
 
e
l
e
m
e
n
t
 
i
s
 
i
n
 
t
h
e
 
f
i
l
t
e
r
 
b
y
 
c
a
l
l
i
n
g
 
t
h
e
 
`
_
_
c
o
n
t
a
i
n
s
_
_
`
 
m
e
t
h
o
d
.
 
I
f
 
t
h
e
 
e
l
e
m
e
n
t
 
i
s
 
n
o
t
 
f
o
u
n
d
,
 
w
e
 
r
e
t
u
r
n
 
`
F
a
l
s
e
`
.
 
I
f
 
t
h
e
 
e
l
e
m
e
n
t
 
i
s
 
f
o
u
n
d
,
 
w
e
 
i
n
i
t
i
a
l
i
z
e
 
a
 
t
e
m
p
o
r
a
r
y
 
f
i
l
t
e
r
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
s
i
z
e
 
a
n
d
 
h
a
s
h
 
f
u
n
c
t
i
o
n
s
 
a
s
 
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
t
e
r
.
 
W
e
 
t
h
e
n
 
s
e
t
 
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
 
b
i
t
s
 
i
n
 
t
h
e
 
t
e
m
p
o
r
a
r
y
 
f
i
l
t
e
r
 
t
o
 
1
 
f
o
r
 
e
a
c
h
 
h
a
s
h
 
f
u
n
c
t
i
o
n
import unittest


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        # Initialize BloomFilter with reasonable size and hash count for testing
        self.bf = BloomFilter(1000, 5)

    def test_add_and_check_presence(self):
        # Test that added elements are reported as present
        test_item = "hello world"
        self.bf.add(test_item)
        self.assertIn(test_item, self.bf)

    def test_check_absence(self):
        # Test that an unadded element is not present
        self.assertNotIn("random item", self.bf)

    def test_false_positives(self):
        # Adding some elements and check for a false positive
        items_to_add = ["item1", "item2", "item3"]
        for item in items_to_add:
            self.bf.add(item)
        # Check for an item not added, expecting a very low chance of false positive due to size and hash count
        self.assertNotIn("item4", self.bf)

    def test_collision_handling(self):
        # Test how the Bloom filter handles hash collisions by adding similar items
        self.bf.add("item123")
        self.bf.add("item124")
        self.assertIn("item123", self.bf)
        self.assertIn("item124", self.bf)

    def test_empty_bloom_filter(self):
        # Ensure that an empty Bloom Filter reports no items
        self.assertNotIn("anything", self.bf)
if __name__ == '__main__':
    unittest.main()