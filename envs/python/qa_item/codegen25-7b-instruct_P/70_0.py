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
o
d
e
_
b
l
o
c
k
_
r
e
m
o
v
e
r
(
m
a
r
k
d
o
w
n
_
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


 
 
 
 
e
x
t
r
a
c
t
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
c
o
d
e
 
b
l
o
c
k
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
M
a
r
k
d
o
w
n
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
n
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
)
:
 
T
h
e
 
i
n
p
u
t
 
m
a
r
k
d
o
w
n
 
s
t
r
i
n
g
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
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
 
e
a
c
h
 
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
n
t
e
n
t
 
o
f
 
a
 
c
o
d
e
 
b
l
o
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
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
i
f
 
n
o
 
c
o
d
e
 
b
l
o
c
k
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
l
i
s
t
 
=
 
[
]


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
s
t
a
r
t
_
i
n
d
i
c
e
s
 
=
 
[


 
 
 
 
 
 
 
 
i
 
f
o
r
 
i
,
 
c
 
i
n
 
e
n
u
m
e
r
a
t
e
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
i
f
 
c
 
=
=
 
"
`
"
 
a
n
d
 
i
 
!
=
 
0


 
 
 
 
]


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
e
n
d
_
i
n
d
i
c
e
s
 
=
 
[


 
 
 
 
 
 
 
 
i
 
f
o
r
 
i
,
 
c
 
i
n
 
e
n
u
m
e
r
a
t
e
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
i
f
 
c
 
=
=
 
"
`
"
 
a
n
d
 
i
 
!
=
 
l
e
n
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
-
 
1


 
 
 
 
]


 
 
 
 
i
f
 
l
e
n
(
c
o
d
e
_
b
l
o
c
k
_
s
t
a
r
t
_
i
n
d
i
c
e
s
)
 
=
=
 
l
e
n
(
c
o
d
e
_
b
l
o
c
k
_
e
n
d
_
i
n
d
i
c
e
s
)
:


 
 
 
 
 
 
 
 
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
c
o
d
e
_
b
l
o
c
k
_
s
t
a
r
t
_
i
n
d
i
c
e
s
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
l
i
s
t
.
a
p
p
e
n
d
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
[
c
o
d
e
_
b
l
o
c
k
_
s
t
a
r
t
_
i
n
d
i
c
e
s
[
i
]
 
+
 
1
 
:
 
c
o
d
e
_
b
l
o
c
k
_
e
n
d
_
i
n
d
i
c
e
s
[
i
]
]


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
c
o
d
e
_
b
l
o
c
k
_
l
i
s
t






d
e
f
 
c
o
d
e
_
b
l
o
c
k
_
r
e
m
o
v
e
r
_
w
i
t
h
_
i
n
d
i
c
e
s
(
m
a
r
k
d
o
w
n
_
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


 
 
 
 
e
x
t
r
a
c
t
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
c
o
d
e
 
b
l
o
c
k
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
M
a
r
k
d
o
w
n
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
n
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
)
:
 
T
h
e
 
i
n
p
u
t
 
m
a
r
k
d
o
w
n
 
s
t
r
i
n
g
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
,
 
e
a
c
h
 
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
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
i
n
d
i
c
e
s
 
o
f
 
a
 
c
o
d
e
 
b
l
o
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
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
i
f
 
n
o
 
c
o
d
e
 
b
l
o
c
k
s
 
a
r
e
 
f
o
u
n
d
.


 
 
 
 
"
"
"


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
l
i
s
t
 
=
 
[
]


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
s
t
a
r
t
_
i
n
d
i
c
e
s
 
=
 
[


 
 
 
 
 
 
 
 
i
 
f
o
r
 
i
,
 
c
 
i
n
 
e
n
u
m
e
r
a
t
e
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
i
f
 
c
 
=
=
 
"
`
"
 
a
n
d
 
i
 
!
=
 
0


 
 
 
 
]


 
 
 
 
c
o
d
e
_
b
l
o
c
k
_
e
n
d
_
i
n
d
i
c
e
s
 
=
 
[


 
 
 
 
 
 
 
 
i
 
f
o
r
 
i
,
 
c
 
i
n
 
e
n
u
m
e
r
a
t
e
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
i
f
 
c
 
=
=
 
"
`
"
 
a
n
d
 
i
 
!
=
 
l
e
n
(
m
a
r
k
d
o
w
n
_
s
t
r
i
n
g
)
 
-
 
1


 
 
 
 
]


 
 
 
 
i
f
 
l
e
n
(
import unittest


class TestCodeBlockRemover(unittest.TestCase):

    def test_single_code_block(self):
        markdown = """
        This is a markdown with a code block.

        ```python
        print("Hello, World!")
        ```

        End of markdown.
        """
        expected = ['print("Hello, World!")']
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        markdown = """
        First code block:

        ```python
        print("Hello, World!")
        ```

        Second code block:

        ```javascript
        console.log("Hello, World!");
        ```
        """
        expected = [
            'print("Hello, World!")',
            'console.log("Hello, World!");'
        ]
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_no_code_block(self):
        markdown = """
        This markdown has no code blocks.

        Just some plain text.
        """
        expected = []
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_empty_code_block(self):
        markdown = """
        Here is an empty code block:

        ```python
        ```

        End of markdown.
        """
        expected = ['']
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_malformed_code_block(self):
        markdown = """
        This code block is missing ending:

        ```python
        print("Hello, World!")

        And some more text.
        """
        expected = []
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()