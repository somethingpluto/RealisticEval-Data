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
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
s
t
a
c
k
 
s
t
r
u
c
t
u
r
e
 
b
a
s
e
d
 
o
n
 
a
r
r
a
y
s
.




 
 
 
 
T
h
i
s
 
c
l
a
s
s
 
p
r
o
v
i
d
e
s
 
b
a
s
i
c
 
s
t
a
c
k
 
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
 
i
n
c
l
u
d
i
n
g
 
p
u
s
h
,
 
p
o
p
,
 
p
e
e
k
,
 
a
n
d
 
c
h
e
c
k
i
n
g
 
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


 
 
 
 
T
h
e
 
s
t
a
c
k
 
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
e
d
 
u
s
i
n
g
 
a
 
f
i
x
e
d
-
s
i
z
e
 
a
r
r
a
y
.
 
I
f
 
t
h
e
 
s
t
a
c
k
 
r
e
a
c
h
e
s
 
i
t
s
 
m
a
x
i
m
u
m
 
c
a
p
a
c
i
t
y
,
 
n
o
 
m
o
r
e
 
e
l
e
m
e
n
t
s


 
 
 
 
c
a
n
 
b
e
 
p
u
s
h
e
d
 
o
n
t
o
 
i
t
 
u
n
t
i
l
 
s
p
a
c
e
 
i
s
 
f
r
e
e
d
 
b
y
 
p
o
p
p
i
n
g
 
e
l
e
m
e
n
t
s
.


 
 
 
 
"
"
"




 
 
 
 
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
:
 
f
l
o
a
t
)
:


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
P
u
s
h
e
s
 
a
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
 
o
n
t
o
 
t
h
e
 
s
t
a
c
k
.




 
 
 
 
 
 
 
 
:
p
a
r
a
m
 
v
a
l
u
e
:
 
T
h
e
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
 
t
o
 
b
e
 
p
u
s
h
e
d
 
o
n
t
o
 
t
h
e
 
s
t
a
c
k
.


 
 
 
 
 
 
 
 
:
r
a
i
s
e
s
 
S
t
a
c
k
O
v
e
r
f
l
o
w
E
r
r
o
r
:
 
I
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
 
f
u
l
l
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


 
 
 
 
 
 
 
 
P
o
p
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
f
 
t
h
e
 
s
t
a
c
k
 
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
 
i
t
.




 
 
 
 
 
 
 
 
:
r
e
t
u
r
n
:
 
T
h
e
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
 
t
h
a
t
 
w
a
s
 
p
o
p
p
e
d
 
f
r
o
m
 
t
h
e
 
s
t
a
c
k
.


 
 
 
 
 
 
 
 
:
r
a
i
s
e
s
 
S
t
a
c
k
U
n
d
e
r
f
l
o
w
E
r
r
o
r
:
 
I
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
 
p
e
e
k
(
s
e
l
f
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




 
 
 
 
 
 
 
 
:
r
e
t
u
r
n
:
 
T
h
e
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
n
u
m
b
e
r
 
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


 
 
 
 
 
 
 
 
:
r
a
i
s
e
s
 
S
t
a
c
k
U
n
d
e
r
f
l
o
w
E
r
r
o
r
:
 
I
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
 
-
>
 
b
o
o
l
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
 
w
h
e
t
h
e
r
 
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




 
 
 
 
 
 
 
 
:
r
e
t
u
r
n
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
;
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
 
 
 
 
"
"
"




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
U
n
d
e
r
f
l
o
w
E
r
r
o
r
(
E
x
c
e
p
t
i
o
n
)
:


 
 
 
 
"
"
"


 
 
 
 
E
x
c
e
p
t
i
o
n
 
r
a
i
s
e
d
 
w
h
e
n
 
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
s
 
a
t
t
e
m
p
t
e
d
 
t
o
 
b
e
 
p
o
p
p
e
d
 
f
r
o
m
 
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
"
T
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
O
v
e
r
f
l
o
w
E
r
r
o
r
(
E
x
c
e
p
t
i
o
n
)
:


 
 
 
 
"
"
"


 
 
 
 
E
x
c
e
p
t
i
o
n
 
r
a
i
s
e
d
 
w
h
e
n
 
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
s
 
a
t
t
e
m
p
t
e
d
 
t
o
 
b
e
 
p
u
s
h
e
d
 
o
n
t
o
 
a
 
f
u
l
l
 
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
"
T
h
e
 
s
t
a
c
k
 
i
s
 
f
u
l
l
.
"
)




c
l
a
s
s
 
A
r
r
a
y
S
t
a
c
k
(
S
t
a
c
k
)
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
 
f
l
o
a
t
i
n
g
-
p
o
i
n
t
 
s
t
a
c
k
 
s
t
r
u
c
t
u
r
e
 
b
a
s
e
d
 
o
n
 
a
r
r
a
y
s
.




 
 
 
 
T
h
i
s
 
c
l
a
s
s
 
p
r
o
v
i
d
e
s
 
b
a
s
i
c
 
s
t
a
c
k
 
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
 
i
n
c
l
u
d
i
n
g
 
p
u
s
h
,
 
p
o
p
,
 
p
e
e
k
,
 
a
n
d
 
c
h
e
c
k
i
n
g
 
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


 
 
 
 
T
h
e
 
s
t
a
c
k
 
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
e
d
 
u
s
i
n
g
 
a
 
f
i
x
e
d
-
s
i
z
e
 
a
r
r
a
y
.
 
I
f
 
t
h
e
 
s
t
a
c
k
 
r
e
a
c
h
e
s
 
i
t
s
 
m
a
x
i
m
u
m
 
c
a
p
a
c
i
t
y
,
 
n
o
 
m
o
r
e
 
e
l
e
m
e
n
t
s


 
 
 
 
c
a
n
 
b
e
 
p
u
s
h
e
d
 
o
n
t
o
 
i
t
 
u
n
t
i
l
 
s
p
a
c
e
 
i
s
 
f
r
e
e
d
 
b
y
 
p
o
p
p
i
n
g
 
e
l
e
m
e
n
t
s
.


class Tester(unittest.TestCase):

    def test_stack_operations(self):
        """Test stack_t Test Cases"""
        stack = Stack(10)  # Provide capacity when creating the stack

        # Test Case 1: Pushing and popping a single element
        stack.push(3.14)
        self.assertEqual(stack.pop(), 3.14)
        self.assertTrue(stack.is_empty())  # Change to is_empty

        # Test Case 2: Pushing multiple elements and checking peek
        stack.push(1.23)
        stack.push(4.56)
        self.assertEqual(stack.peek(), 4.56)
        self.assertEqual(stack.pop(), 4.56)
        self.assertEqual(stack.pop(), 1.23)
        self.assertTrue(stack.is_empty())  # Change to is_empty

        # Test Case 3: Pop from an empty stack (should throw an exception)
        with self.assertRaises(StackUnderflowError):
            stack.pop()

        # Test Case 4: Peek on an empty stack (should throw an exception)
        with self.assertRaises(StackUnderflowError):
            stack.peek()

        # Test Case 5: Push elements until stack is full and attempt to push another element
        full_stack = Stack(100)  # Provide capacity when creating the stack
        for i in range(100):
            full_stack.push(float(i) + 0.5)

        with self.assertRaises(StackOverflowError):
            full_stack.push(100.5)

if __name__ == '__main__':
    unittest.main()