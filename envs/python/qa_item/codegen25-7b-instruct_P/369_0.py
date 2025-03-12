d
e
f
 
e
i
g
h
t
_
q
u
e
e
n
s
(
)
:


 
 
 
 
"
"
"


 
 
 
 
s
o
l
v
e
 
t
h
e
 
E
i
g
h
t
 
Q
u
e
e
n
s
 
p
r
o
b
l
e
m
,
 
i
f
 
a
 
s
o
l
u
t
i
o
n
 
i
s
 
f
o
u
n
d
,
 
i
t
 
w
i
l
l
 
p
r
i
n
t
 
o
u
t
 
t
h
e
 
c
o
n
f
i
g
u
r
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
 
c
h
e
s
s
b
o
a
r
d
.
 
I
f
 
a
l
l
 
q
u
e
e
n
s
 
c
a
n
n
o
t
 
b
e
 
p
l
a
c
e
d
,
 
p
r
i
n
t
 
"
N
o
 
s
o
l
u
t
i
o
n
"


 
 
 
 
p
r
i
n
t
 
e
x
a
m
p
l
e
 
a
s
 
b
e
l
o
w
:


 
 
 
 
.
 
.
 
Q
 
.
 
.
 
.
 
.
 
.


 
 
 
 
.
 
.
 
.
 
.
 
Q
 
.
 
.
 
.


 
 
 
 
.
 
Q
 
.
 
.
 
.
 
.
 
.
 
.


 
 
 
 
.
 
.
 
.
 
.
 
.
 
.
 
.
 
Q


 
 
 
 
.
 
.
 
.
 
.
 
.
 
Q
 
.
 
.


 
 
 
 
.
 
.
 
.
 
Q
 
.
 
.
 
.
 
.


 
 
 
 
.
 
.
 
.
 
.
 
.
 
.
 
Q
 
.


 
 
 
 
Q
 
.
 
.
 
.
 
.
 
.
 
.
 
.


 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
b
o
a
r
d
 
=
 
[
[
'
.
'
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
8
)
]
 
f
o
r
 
_
 
i
n
 
r
a
n
g
e
(
8
)
]


 
 
 
 
i
f
 
n
o
t
 
e
i
g
h
t
_
q
u
e
e
n
s
_
h
e
l
p
e
r
(
b
o
a
r
d
,
 
0
)
:


 
 
 
 
 
 
 
 
p
r
i
n
t
(
"
N
o
 
s
o
l
u
t
i
o
n
"
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
b
o
a
r
d
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
'
 
'
.
j
o
i
n
(
r
o
w
)
)






d
e
f
 
e
i
g
h
t
_
q
u
e
e
n
s
_
h
e
l
p
e
r
(
b
o
a
r
d
,
 
r
o
w
)
:


 
 
 
 
"
"
"


 
 
 
 
h
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
 
f
o
r
 
e
i
g
h
t
 
q
u
e
e
n
s
 
p
r
o
b
l
e
m


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
o
a
r
d
:
 
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
 
b
o
a
r
d


 
 
 
 
 
 
 
 
r
o
w
:
 
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
 
r
o
w




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
b
o
a
r
d
)


 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
r
a
n
g
e
(
n
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
_
v
a
l
i
d
(
b
o
a
r
d
,
 
r
o
w
,
 
c
o
l
)
:


 
 
 
 
 
 
 
 
 
 
 
 
b
o
a
r
d
[
r
o
w
]
[
c
o
l
]
 
=
 
'
Q
'


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
r
o
w
 
=
=
 
n
 
-
 
1
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
e
i
g
h
t
_
q
u
e
e
n
s
_
h
e
l
p
e
r
(
b
o
a
r
d
,
 
r
o
w
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
o
a
r
d
[
r
o
w
]
[
c
o
l
]
 
=
 
'
.
'


 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e






d
e
f
 
i
s
_
v
a
l
i
d
(
b
o
a
r
d
,
 
r
o
w
,
 
c
o
l
)
:


 
 
 
 
"
"
"


 
 
 
 
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
 
p
o
s
i
t
i
o
n
 
i
s
 
v
a
l
i
d


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
o
a
r
d
:
 
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
 
b
o
a
r
d


 
 
 
 
 
 
 
 
r
o
w
:
 
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
 
r
o
w


 
 
 
 
 
 
 
 
c
o
l
:
 
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
 
c
o
l




 
 
 
 
R
e
t
u
r
n
s
:




 
 
 
 
"
"
"


 
 
 
 
n
 
=
 
l
e
n
(
b
o
a
r
d
)


 
 
 
 
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
n
)
:


 
 
 
 
 
 
 
 
i
f
 
b
o
a
r
d
[
i
]
[
c
o
l
]
 
=
=
 
'
Q
'
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
 
 
 
 
i
f
 
i
 
+
 
b
o
a
r
d
[
i
]
[
c
o
l
]
 
=
=
 
r
o
w
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
 
 
 
 
i
f
 
i
 
-
 
b
o
a
r
d
[
i
]
[
c
o
l
]
 
=
=
 
r
o
w
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e


 
 
 
 
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
n
)
:


 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
n
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
i
 
-
 
j
 
=
=
 
r
o
w
 
-
 
c
o
l
 
a
n
d
 
b
o
a
r
d
import unittest
from unittest.mock import patch
from io import StringIO


class TestEightQueens(unittest.TestCase):
    def setUp(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]

    def test_solution_exists(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            eight_queens()
            self.assertTrue("Q" in fake_out.getvalue(), "The board should contain at least one queen.")

    def test_correct_number_of_queens(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            eight_queens()
            output = fake_out.getvalue().strip().split('\n\n')  # Split the output into blocks for each board
            for board in output:
                # Count number of 'Q's in each board
                num_queens = board.count('Q')
                self.assertEqual(num_queens, 8, "Each board should contain exactly 8 queens.")

    def test_no_solution_scenario(self):
        # As the Eight Queens always has a solution for an 8x8 board,
        # to test the 'No solution' output we need a scenario where no solution exists.
        # We will manipulate the board to a smaller size where no solution is possible.
        # Here we consider a 3x3 board for simplicity.
        def no_solution_queens():
            board = [['.' for _ in range(3)] for _ in range(3)]
            if not solve_queens(board, 0):
                print("No solution")

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            no_solution_queens()
            self.assertIn("No solution", fake_out.getvalue(), "Should print 'No solution' when no solution exists.")

if __name__ == '__main__':
    unittest.main()