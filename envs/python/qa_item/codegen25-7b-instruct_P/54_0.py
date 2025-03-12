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
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
(
s
t
r
i
n
g
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


 
 
 
 
p
r
o
c
e
s
s
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
,
 
r
e
m
o
v
i
n
g
 
t
h
e
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
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
r
i
n
g


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
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
 
T
h
e
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
 
t
o
 
p
r
o
c
e
s
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


 
 
 
 
 
 
 
 
A
 
n
e
w
 
l
i
s
t
 
w
i
t
h
 
a
l
l
 
i
n
s
t
a
n
c
e
s
 
o
f
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
r
e
m
o
v
e
d
 
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
r
i
n
g
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
 
[
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
`
`
"
,
 
"
"
)
 
f
o
r
 
s
t
r
i
n
g
 
i
n
 
s
t
r
i
n
g
_
l
i
s
t
]






d
e
f
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
(
s
t
r
i
n
g
:
 
s
t
r
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


 
 
 
 
p
r
o
c
e
s
s
 
a
 
s
t
r
i
n
g
,
 
r
e
m
o
v
i
n
g
 
t
h
e
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
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
r
i
n
g


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
(
s
t
r
)
:
 
T
h
e
 
s
t
r
i
n
g
 
t
o
 
p
r
o
c
e
s
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


 
 
 
 
 
 
 
 
A
 
n
e
w
 
s
t
r
i
n
g
 
w
i
t
h
 
a
l
l
 
i
n
s
t
a
n
c
e
s
 
o
f
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
r
e
m
o
v
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
r
i
n
g
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
 
s
t
r
i
n
g
.
r
e
p
l
a
c
e
(
"
`
`
"
,
 
"
"
)






d
e
f
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
_
l
i
s
t
(
s
t
r
i
n
g
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


 
 
 
 
p
r
o
c
e
s
s
 
a
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
,
 
r
e
m
o
v
i
n
g
 
t
h
e
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
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
r
i
n
g


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
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
 
T
h
e
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
 
t
o
 
p
r
o
c
e
s
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


 
 
 
 
 
 
 
 
A
 
n
e
w
 
l
i
s
t
 
w
i
t
h
 
a
l
l
 
i
n
s
t
a
n
c
e
s
 
o
f
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
r
e
m
o
v
e
d
 
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
r
i
n
g
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
 
[
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
(
s
t
r
i
n
g
)
 
f
o
r
 
s
t
r
i
n
g
 
i
n
 
s
t
r
i
n
g
_
l
i
s
t
]






d
e
f
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
_
l
i
s
t
_
i
n
_
d
i
c
t
(
s
t
r
i
n
g
_
d
i
c
t
:
 
d
i
c
t
)
 
-
>
 
d
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
p
r
o
c
e
s
s
 
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
 
o
f
 
s
t
r
i
n
g
s
,
 
r
e
m
o
v
i
n
g
 
t
h
e
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
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
r
i
n
g


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
r
i
n
g
_
d
i
c
t
 
(
d
i
c
t
)
:
 
T
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
 
o
f
 
s
t
r
i
n
g
s
 
t
o
 
p
r
o
c
e
s
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


 
 
 
 
 
 
 
 
A
 
n
e
w
 
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
l
l
 
i
n
s
t
a
n
c
e
s
 
o
f
 
t
h
r
e
e
 
c
o
n
s
e
c
u
t
i
v
e
 
b
a
c
k
t
i
c
k
s
 
r
e
m
o
v
e
d
 
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
r
i
n
g
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
 
{
k
e
y
:
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
(
v
a
l
u
e
)
 
f
o
r
 
k
e
y
,
 
v
a
l
u
e
 
i
n
 
s
t
r
i
n
g
_
d
i
c
t
.
i
t
e
m
s
(
)
}






d
e
f
 
r
e
m
o
v
e
_
t
r
i
p
l
e
_
b
a
c
k
t
i
c
k
s
_
f
r
o
m
_
s
t
r
i
n
g
_
l
i
s
t
_
i
n
_
d
i
c
t
_
o
f
_
l
i
s
t
s
(
s
t
r
i
n
g
_
d
i
c
t
_
o
f
_
l
i
s
t
s
:
 
d
i
c
t
)
 
-
>
 
d
i
c
t
:


 
 
 
import unittest

class TestRemoveTripleBackticks(unittest.TestCase):

    def test_remove_triple_backticks_basic(self):
        # Test basic functionality
        input_strings = ['Here is ```code``` example', 'Another ```example``` here', 'No backticks here']
        expected_output = ['Here is code example', 'Another example here', 'No backticks here']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_strings_with_multiple_instances(self):
        # Test strings containing multiple instances of triple backticks
        input_strings = ['Multiple ```backticks``` in ```one``` string']
        expected_output = ['Multiple backticks in one string']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_empty_strings(self):
        # Test with empty strings
        input_strings = ['']
        expected_output = ['']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_no_triple_backticks(self):
        # Test strings that do not contain triple backticks
        input_strings = ['Just a normal string', 'Another normal string']
        expected_output = ['Just a normal string', 'Another normal string']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_edge_cases(self):
        # Test edge cases like strings made entirely of triple backticks
        input_strings = ['```', '```more```', 'text``````']
        expected_output = ['', 'more', 'text']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)
if __name__ == '__main__':
    unittest.main()