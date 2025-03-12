c
l
a
s
s
 
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


 
 
 
 
 
 
 
 
"
"
"
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
 
a
n
 
e
m
p
t
y
 
q
u
e
u
e
.
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
i
t
e
m
s
 
=
 
[
]




 
 
 
 
d
e
f
 
e
n
q
u
e
u
e
(
s
e
l
f
,
 
e
l
e
m
e
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
A
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
 
e
n
d
 
o
f
 
t
h
e
 
q
u
e
u
e
.




 
 
 
 
 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
:
 
T
h
e
 
e
l
e
m
e
n
t
 
t
o
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
q
u
e
u
e
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
d
e
q
u
e
u
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
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
 
f
r
o
m
 
t
h
e
 
f
r
o
n
t
 
o
f
 
t
h
e
 
q
u
e
u
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


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
r
e
m
o
v
e
d
 
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
 
f
r
o
n
t
 
o
f
 
t
h
e
 
q
u
e
u
e
,
 
o
r
 
"
U
n
d
e
r
f
l
o
w
"
 
i
f
 
t
h
e
 
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
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
f
r
o
n
t
(
s
e
l
f
)
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
r
o
n
t
 
e
l
e
m
e
n
t
 
o
f
 
t
h
e
 
q
u
e
u
e
 
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
.




 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
f
r
o
n
t
 
e
l
e
m
e
n
t
 
o
f
 
t
h
e
 
q
u
e
u
e
,
 
o
r
 
"
N
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
 
Q
u
e
u
e
"
 
i
f
 
t
h
e
 
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
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
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


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
s
 
i
f
 
t
h
e
 
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
.




 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
T
r
u
e
 
i
f
 
t
h
e
 
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
 
F
a
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
l
e
n
(
s
e
l
f
.
i
t
e
m
s
)
 
=
=
 
0




 
 
 
 
d
e
f
 
p
r
i
n
t
_
q
u
e
u
e
(
s
e
l
f
)
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
 
a
 
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
l
l
 
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
 
i
n
 
t
h
e
 
q
u
e
u
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


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
r
i
n
g
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
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
 
q
u
e
u
e
,
 
s
e
p
a
r
a
t
e
d
 
b
y
 
s
p
a
c
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
 
"
.
j
o
i
n
(
s
t
r
(
i
t
e
m
)
 
f
o
r
 
i
t
e
m
 
i
n
 
s
e
l
f
.
i
t
e
m
s
)






c
l
a
s
s
 
S
t
a
c
k
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


 
 
 
 
 
 
 
 
"
"
"
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
 
a
n
 
e
m
p
t
y
 
s
t
a
c
k
.
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
i
t
e
m
s
 
=
 
[
]




 
 
 
 
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
 
e
l
e
m
e
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
A
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
 
t
o
p
 
o
f
 
t
h
e
 
s
t
a
c
k
.




 
 
 
 
 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
 
 
 
 
e
l
e
m
e
n
t
:
 
T
h
e
 
e
l
e
m
e
n
t
 
t
o
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
t
o
p
 
o
f
 
t
h
e
 
s
t
a
c
k
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
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


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
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
 
a
t
 
t
h
e
 
t
o
p
 
o
f
 
t
h
e
 
s
t
a
c
k
.




 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
r
e
m
o
v
e
d
 
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
 
t
o
p
 
o
f
 
t
h
e
 
s
t
a
c
k
,
 
o
r
 
"
U
n
d
e
r
f
l
o
w
"
 
i
f
 
t
h
e
 
s
t
a
c
k
 
i
s
 
e
m
p
t
y
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
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
 
t
o
p
 
e
l
e
m
e
n
t
 
o
f
 
t
h
e
 
s
t
a
c
k
 
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
.




 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
o
p
 
e
l
e
m
e
n
t
 
o
f
 
t
h
e
 
s
t
a
c
k
,
 
o
r
 
"
N
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
 
S
t
a
c
k
"
 
i
f
 
t
h
e
 
s
t
a
c
k
 
i
s
 
e
m
p
t
y
.


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
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


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
s
 
i
f
 
t
h
e
 
s
t
a
c
k
 
i
s
 
e
m
p
t
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


 
 
 
 
 
 
 
 
 
 
 
 
T
r
u
e
 
i
f
 
t
h
e
 
s
t
a
c
k
 
i
s
 
e
m
p
t
y
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
 
F
a
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self):
        """Initialize an empty queue before each test."""
        self.queue = Queue()

    def test_initialize_empty_queue(self):
        """Test if the queue is initialized empty."""
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_elements(self):
        """Test enqueueing elements into the queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertFalse(self.queue.is_empty())

    def test_dequeue_elements(self):
        """Test dequeueing elements from the queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        dequeued_element = self.queue.dequeue()
        self.assertEqual(dequeued_element, 1)

    def test_front_element(self):
        """Test getting the front element without removing it."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        front_element = self.queue.front()
        self.assertEqual(front_element, 10)

    def test_check_empty_queue(self):
        """Test checking if the queue is empty."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()