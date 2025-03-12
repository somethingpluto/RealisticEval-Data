c
l
a
s
s
 
T
r
i
e
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
 
t
r
e
e
 
f
o
r
 
f
a
s
t
 
s
t
r
i
n
g
 
r
e
t
r
i
e
v
a
l
 
a
n
d
 
s
t
o
r
a
g
e


 
 
 
 
"
"
"




 
 
 
 
d
e
f
 
i
n
s
e
r
t
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
s
e
a
r
c
h
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
d
e
f
 
s
t
a
r
t
s
_
w
i
t
h
(
s
e
l
f
,
 
p
r
e
f
i
x
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
 
T
r
i
e
N
o
d
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
c
h
i
l
d
r
e
n
 
=
 
{
}


 
 
 
 
 
 
 
 
s
e
l
f
.
i
s
_
w
o
r
d
 
=
 
F
a
l
s
e






c
l
a
s
s
 
T
r
i
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
r
o
o
t
 
=
 
T
r
i
e
N
o
d
e
(
)




 
 
 
 
d
e
f
 
i
n
s
e
r
t
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
w
o
r
d
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]
 
=
 
T
r
i
e
N
o
d
e
(
)


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
.
i
s
_
w
o
r
d
 
=
 
T
r
u
e




 
 
 
 
d
e
f
 
s
e
a
r
c
h
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
w
o
r
d
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
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


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
u
r
r
e
n
t
.
i
s
_
w
o
r
d




 
 
 
 
d
e
f
 
s
t
a
r
t
s
_
w
i
t
h
(
s
e
l
f
,
 
p
r
e
f
i
x
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
p
r
e
f
i
x
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
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


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]


 
 
 
 
 
 
 
 
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






c
l
a
s
s
 
T
r
i
e
N
o
d
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
c
h
i
l
d
r
e
n
 
=
 
{
}


 
 
 
 
 
 
 
 
s
e
l
f
.
i
s
_
w
o
r
d
 
=
 
F
a
l
s
e






c
l
a
s
s
 
T
r
i
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
r
o
o
t
 
=
 
T
r
i
e
N
o
d
e
(
)




 
 
 
 
d
e
f
 
i
n
s
e
r
t
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
w
o
r
d
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]
 
=
 
T
r
i
e
N
o
d
e
(
)


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
.
i
s
_
w
o
r
d
 
=
 
T
r
u
e




 
 
 
 
d
e
f
 
s
e
a
r
c
h
(
s
e
l
f
,
 
w
o
r
d
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
w
o
r
d
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
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


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
[
c
h
a
r
]


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
u
r
r
e
n
t
.
i
s
_
w
o
r
d




 
 
 
 
d
e
f
 
s
t
a
r
t
s
_
w
i
t
h
(
s
e
l
f
,
 
p
r
e
f
i
x
)
:


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
s
e
l
f
.
r
o
o
t


 
 
 
 
 
 
 
 
f
o
r
 
c
h
a
r
 
i
n
 
p
r
e
f
i
x
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
n
o
t
 
i
n
 
c
u
r
r
e
n
t
.
c
h
i
l
d
r
e
n
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


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
=
 
c
u
r
r
e
n
t
.
import unittest


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.trie.insert("banana")
        self.trie.insert("carrot")
        self.trie.insert("car")
        self.trie.insert("care")
        self.trie.insert("")
        self.trie.insert("Hello")
        self.trie.insert("hello")

    def test_basic_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apricot"))

    def test_unsuccessful_search(self):
        self.assertFalse(self.trie.search("bandana"))

    def test_prefix_search(self):
        self.assertTrue(self.trie.starts_with("car"))
        self.assertTrue(self.trie.starts_with("care"))
        self.assertFalse(self.trie.starts_with("cat"))

    def test_empty_string(self):
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))

    def test_case_sensitivity(self):
        self.assertTrue(self.trie.search("Hello"))
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.search("HELLO"))

if __name__ == '__main__':
    unittest.main()