c
l
a
s
s
 
P
r
i
o
r
i
t
y
Q
u
e
u
e
:


 
 
 
 
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
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
h
e
a
p
 
=
 
[
]
 
 
#
 
T
h
i
s
 
w
i
l
l
 
s
t
o
r
e
 
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
s
 
o
f
 
t
h
e
 
h
e
a
p




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
p
a
r
e
n
t


 
 
 
 
d
e
f
 
p
a
r
e
n
t
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
l
e
f
t
 
c
h
i
l
d


 
 
 
 
d
e
f
 
l
e
f
t
_
c
h
i
l
d
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
r
i
g
h
t
 
c
h
i
l
d


 
 
 
 
d
e
f
 
r
i
g
h
t
_
c
h
i
l
d
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
s
w
a
p
 
t
w
o
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
h
e
a
p


 
 
 
 
d
e
f
 
s
w
a
p
(
s
e
l
f
,
 
a
,
 
b
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
H
e
a
p
i
f
y
 
u
p
 
t
o
 
m
a
i
n
t
a
i
n
 
t
h
e
 
m
a
x
-
h
e
a
p
 
p
r
o
p
e
r
t
y
 
a
f
t
e
r
 
i
n
s
e
r
t
i
o
n


 
 
 
 
d
e
f
 
h
e
a
p
i
f
y
_
u
p
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
H
e
a
p
i
f
y
 
d
o
w
n
 
t
o
 
m
a
i
n
t
a
i
n
 
t
h
e
 
m
a
x
-
h
e
a
p
 
p
r
o
p
e
r
t
y
 
a
f
t
e
r
 
d
e
l
e
t
i
o
n


 
 
 
 
d
e
f
 
h
e
a
p
i
f
y
_
d
o
w
n
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
I
n
s
e
r
t
 
a
n
 
e
l
e
m
e
n
t
 
i
n
t
o
 
t
h
e
 
p
r
i
o
r
i
t
y
 
q
u
e
u
e


 
 
 
 
d
e
f
 
p
u
s
h
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
R
e
m
o
v
e
 
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
 
e
l
e
m
e
n
t
 
f
r
o
m
 
t
h
e
 
p
r
i
o
r
i
t
y
 
q
u
e
u
e


 
 
 
 
d
e
f
 
p
o
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
G
e
t
 
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
 
e
l
e
m
e
n
t
 
w
i
t
h
o
u
t
 
r
e
m
o
v
i
n
g
 
i
t


 
 
 
 
d
e
f
 
t
o
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
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
 
p
r
i
o
r
i
t
y
 
q
u
e
u
e
 
i
s
 
e
m
p
t
y


 
 
 
 
d
e
f
 
i
s
_
e
m
p
t
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
#
 
G
e
t
 
t
h
e
 
s
i
z
e
 
o
f
 
t
h
e
 
p
r
i
o
r
i
t
y
 
q
u
e
u
e


 
 
 
 
d
e
f
 
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
p
a
s
s






c
l
a
s
s
 
M
a
x
H
e
a
p
(
P
r
i
o
r
i
t
y
Q
u
e
u
e
)
:


 
 
 
 
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
)
:


 
 
 
 
 
 
 
 
s
u
p
e
r
(
)
.
_
_
i
n
i
t
_
_
(
)




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
p
a
r
e
n
t


 
 
 
 
d
e
f
 
p
a
r
e
n
t
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
(
i
n
d
e
x
 
-
 
1
)
 
/
/
 
2




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
l
e
f
t
 
c
h
i
l
d


 
 
 
 
d
e
f
 
l
e
f
t
_
c
h
i
l
d
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
2
 
*
 
i
n
d
e
x
 
+
 
1




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
g
e
t
 
t
h
e
 
i
n
d
e
x
 
o
f
 
t
h
e
 
r
i
g
h
t
 
c
h
i
l
d


 
 
 
 
d
e
f
 
r
i
g
h
t
_
c
h
i
l
d
(
s
e
l
f
,
 
i
n
d
e
x
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
2
 
*
 
i
n
d
e
x
 
+
 
2




 
 
 
 
#
 
H
e
l
p
e
r
 
f
u
n
c
t
i
o
n
 
t
o
 
s
w
a
p
 
t
w
o
 
e
l
e
m
e
n
t
s
 
i
n
 
t
h
e
 
h
e
a
p


 
 
 
 
d
e
f
 
s
w
a
p
(
s
e
l
f
,
 
a
,
 
b
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
h
e
a
p
[
a
]
,
 
s
e
l
f
.
h
e
a
p
[
b
]
 
=
 
s
e
l
f
.
h
e
a
p
[
b
]
,
 
s
e
l
f
.
h
e
a
p
[
a
]




 
 
 
 
#
 
H
e
a
p
i
f
y
 
u
p
 
t
o
 
m
a
i
n
t
a
i
n
 
t
h
e
 
m
a
x
-
h
e
a
p
 
p
r
o
p
e
r
t
y
 
a
f
t
e
r
 
i
n
s
e
r
t
i
o
n


 
 
 
 
d
e
f
 
h
e
a
p
i
f
y
_
import unittest

class Tester(unittest.TestCase):
    
    def setUp(self):
        """ Set up a new PriorityQueue instance for each test """
        self.pq = PriorityQueue()
    
    def test_insert_and_access_maximum_element(self):
        """ Test case: Insert and access maximum element """
        self.pq.push(10)
        self.pq.push(20)
        self.pq.push(5)
        self.pq.push(30)
        self.pq.push(15)
        self.assertEqual(self.pq.top(), 30)  # Ensure the max element is 30
    
    def test_remove_maximum_element(self):
        """ Test case: Remove maximum element """
        self.pq.push(10)
        self.pq.push(20)
        self.pq.push(5)
        self.pq.push(30)
        self.pq.pop()  # Remove 30
        self.assertEqual(self.pq.top(), 20)  # Now the max should be 20
        self.pq.pop()  # Remove 20
        self.assertEqual(self.pq.top(), 10)  # Now the max should be 10
    
    def test_check_empty_queue(self):
        """ Test case: Check if the queue is empty """
        self.assertTrue(self.pq.isEmpty())  # Initially empty
        self.pq.push(10)
        self.assertFalse(self.pq.isEmpty())  # Now not empty
        self.pq.pop()
        self.assertTrue(self.pq.isEmpty())  # Back to empty
    
    def test_pop_from_empty_queue(self):
        """ Test case: Pop from empty queue (should raise exception) """
        with self.assertRaises(RuntimeError):
            self.pq.pop()  # Should raise an error
    
    def test_access_top_of_empty_queue(self):
        """ Test case: Access top of empty queue (should raise exception) """
        with self.assertRaises(RuntimeError):
            self.pq.top()  # Should raise an error
    
    def test_maintain_max_heap_property(self):
        """ Test case: Maintain max-heap property """
        self.pq.push(3)
        self.pq.push(1)
        self.pq.push(4)
        self.pq.push(2)
        self.assertEqual(self.pq.top(), 4)  # Ensure max is 4
        self.pq.pop()  # Remove 4
        self.assertEqual(self.pq.top(), 3)  # Now max is 3
        self.pq.push(5)  # Add 5
        self.assertEqual(self.pq.top(), 5)  # Ensure max is now 5

if __name__ == '__main__':
    unittest.main()