f
r
o
m
 
c
o
l
l
e
c
t
i
o
n
s
 
i
m
p
o
r
t
 
C
o
u
n
t
e
r


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
 
O
p
t
i
o
n
a
l






d
e
f
 
f
i
n
d
_
m
i
n
_
w
i
n
d
o
w
_
s
u
b
s
t
r
i
n
g
(
s
o
u
r
c
e
:
 
s
t
r
,
 
t
a
r
g
e
t
:
 
s
t
r
)
 
-
>
 
O
p
t
i
o
n
a
l
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
t
h
e
 
s
m
a
l
l
e
s
t
 
w
i
n
d
o
w
 
i
n
 
t
h
e
 
s
o
u
r
c
e
 
s
t
r
i
n
g
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
a
l
l
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
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


 
 
 
 
 
 
 
 
s
o
u
r
c
e
 
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
o
u
r
c
e
 
s
t
r
i
n
g
 
i
n
 
w
h
i
c
h
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
t
h
e
 
w
i
n
d
o
w
.


 
 
 
 
 
 
 
 
t
a
r
g
e
t
 
(
s
t
r
)
:
 
T
h
e
 
t
a
r
g
e
t
 
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
 
t
h
e
 
c
h
a
r
a
c
t
e
r
s
 
t
o
 
b
e
 
m
a
t
c
h
e
d
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
[
s
t
r
]
:
 
T
h
e
 
s
m
a
l
l
e
s
t
 
w
i
n
d
o
w
 
i
n
 
t
h
e
 
s
o
u
r
c
e
 
s
t
r
i
n
g
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
a
l
l
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
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
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
f
 
n
o
 
s
u
c
h
 
w
i
n
d
o
w
 
e
x
i
s
t
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
o
t
 
s
o
u
r
c
e
 
o
r
 
n
o
t
 
t
a
r
g
e
t
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
"




 
 
 
 
#
 
C
r
e
a
t
e
 
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
 
c
h
a
r
a
c
t
e
r
s
 
i
n
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
 
a
n
d
 
t
h
e
i
r
 
f
r
e
q
u
e
n
c
y


 
 
 
 
t
a
r
g
e
t
_
c
h
a
r
_
f
r
e
q
 
=
 
C
o
u
n
t
e
r
(
t
a
r
g
e
t
)




 
 
 
 
#
 
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
 
v
a
r
i
a
b
l
e
s
 
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
 
w
i
n
d
o
w
 
a
n
d
 
t
h
e
 
m
i
n
i
m
u
m
 
w
i
n
d
o
w


 
 
 
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
 
=
 
{
}


 
 
 
 
m
i
n
_
w
i
n
d
o
w
 
=
 
{
}




 
 
 
 
#
 
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
 
v
a
r
i
a
b
l
e
s
 
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
 
o
f
 
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
 
w
i
n
d
o
w


 
 
 
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
_
s
t
a
r
t
 
=
 
0


 
 
 
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
_
e
n
d
 
=
 
0




 
 
 
 
#
 
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
 
v
a
r
i
a
b
l
e
s
 
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
 
t
h
e
 
s
m
a
l
l
e
s
t
 
w
i
n
d
o
w
 
a
n
d
 
i
t
s
 
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


 
 
 
 
s
m
a
l
l
e
s
t
_
w
i
n
d
o
w
 
=
 
"
"


 
 
 
 
s
m
a
l
l
e
s
t
_
w
i
n
d
o
w
_
s
t
a
r
t
 
=
 
0


 
 
 
 
s
m
a
l
l
e
s
t
_
w
i
n
d
o
w
_
e
n
d
 
=
 
0




 
 
 
 
#
 
L
o
o
p
 
t
h
r
o
u
g
h
 
t
h
e
 
s
o
u
r
c
e
 
s
t
r
i
n
g


 
 
 
 
f
o
r
 
i
,
 
c
h
a
r
 
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
s
o
u
r
c
e
)
:


 
 
 
 
 
 
 
 
#
 
I
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
s
 
i
n
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g
,
 
a
d
d
 
i
t
 
t
o
 
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
 
w
i
n
d
o
w


 
 
 
 
 
 
 
 
i
f
 
c
h
a
r
 
i
n
 
t
a
r
g
e
t
_
c
h
a
r
_
f
r
e
q
:


 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
[
c
h
a
r
]
 
=
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
.
g
e
t
(
c
h
a
r
,
 
0
)
 
+
 
1




 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
n
 
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
 
w
i
n
d
o
w
 
m
a
t
c
h
e
s
 
t
h
e
 
f
r
e
q
u
e
n
c
y
 
o
f
 
t
h
e
 
c
h
a
r
a
c
t
e
r
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
#
 
t
a
r
g
e
t
 
s
t
r
i
n
g
,
 
m
o
v
e
 
t
h
e
 
s
t
a
r
t
 
o
f
 
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
 
w
i
n
d
o
w
 
t
o
 
t
h
e
 
r
i
g
h
t


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
[
c
h
a
r
]
 
=
=
 
t
a
r
g
e
t
_
c
h
a
r
_
f
r
e
q
[
c
h
a
r
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
_
s
t
a
r
t
 
=
 
m
a
x
(
c
u
r
r
e
n
t
_
w
i
n
d
o
w
_
s
t
a
r
t
,
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
_
e
n
d
 
+
 
1
)




 
 
 
 
 
 
 
 
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
 
c
u
r
r
e
n
t
 
w
i
n
d
o
w
 
c
o
n
t
a
i
n
s
 
a
l
l
 
c
h
a
r
a
c
t
e
r
s
 
o
f
 
t
h
e
 
t
a
r
g
e
t
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
w
h
i
l
e
 
c
u
r
r
e
n
t
_
w
i
n
d
o
w
 
=
=
 
t
a
r
g
e
t
_
c
h
a
r
_
f
r
e
q
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
I
f
 
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
 
w
i
n
d
o
w
 
i
s
 
s
m
a
l
l
e
r
 
t
h
a
n
 
t
h
e
 
s
m
a
l
l
e
s
t
 
w
i
n
d
o
w
 
f
o
u
n
d
 
s
o
 
f
a
r
,
 
u
p
d
a
t
e
 
t
h
e
 
s
m
a
l
l
e
s
t
 
w
i
n
d
o
w


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
e
n
(
c
u
r
r
e
n
t
_
w
i
n
d
o
w
)
 
<
 
l
e
n
(
m
i
n
_
w
i
n
d
o
w
)
 
o
r
 
n
o
t
 
m
i
n
_
w
i
n
d
o
w
:


import unittest


class TestFindMinWindowSubstring(unittest.TestCase):

    def test_empty_source_string(self):
        # Test with an empty source string
        self.assertEqual(find_min_window_substring("", "abc"), "", "Should return an empty string when source is empty")

    def test_empty_target_string(self):
        # Test with an empty target string
        self.assertEqual(find_min_window_substring("abc", ""), "", "Should return an empty string when target is empty")

    def test_no_valid_window(self):
        # Test when there is no valid window
        self.assertEqual(find_min_window_substring("abcdef", "xyz"), "",
                         "Should return an empty string when no valid window exists")

    def test_exact_match_window(self):
        # Test when the entire source string is the exact match
        self.assertEqual(find_min_window_substring("abcd", "abcd"), "abcd",
                         "Should return the entire string when it is an exact match")

    def test_minimal_valid_window(self):
        # Test with a minimal valid window case
        self.assertEqual(find_min_window_substring("ADOBECODEBANC", "ABC"), "BANC",
                         "Should return 'BANC' as the smallest window containing all characters of 'ABC'")



if __name__ == '__main__':
    unittest.main()