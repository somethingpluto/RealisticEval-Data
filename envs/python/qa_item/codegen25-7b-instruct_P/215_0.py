d
e
f
 
r
e
p
l
a
c
e
_
w
o
r
d
s
_
i
n
_
f
i
l
e
(
f
i
l
e
_
p
a
t
h
:
 
s
t
r
,
 
r
e
p
l
a
c
e
m
e
n
t
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
R
e
a
d
 
a
 
t
e
x
t
 
f
i
l
e
,
 
r
e
p
l
a
c
e
 
w
o
r
d
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
m
a
p
,
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
m
o
d
i
f
i
e
d
 
t
e
x
t
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
-
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
t
e
x
t
 
f
i
l
e
.


 
 
 
 
-
 
r
e
p
l
a
c
e
m
e
n
t
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
 
A
 
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
h
e
r
e
 
t
h
e
 
k
e
y
s
 
a
r
e
 
w
o
r
d
s
 
t
o
 
b
e
 
r
e
p
l
a
c
e
d
,
 
a
n
d
 
t
h
e
 
v
a
l
u
e
s
 
a
r
e
 
t
h
e
 
r
e
p
l
a
c
e
m
e
n
t
 
w
o
r
d
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


 
 
 
 
-
 
s
t
r
:
 
T
h
e
 
t
e
x
t
 
w
i
t
h
 
t
h
e
 
w
o
r
d
s
 
r
e
p
l
a
c
e
d
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
i
l
e
:


 
 
 
 
 
 
 
 
t
e
x
t
 
=
 
f
i
l
e
.
r
e
a
d
(
)


 
 
 
 
 
 
 
 
f
o
r
 
w
o
r
d
,
 
r
e
p
l
a
c
e
m
e
n
t
 
i
n
 
r
e
p
l
a
c
e
m
e
n
t
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
:


 
 
 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
=
 
t
e
x
t
.
r
e
p
l
a
c
e
(
w
o
r
d
,
 
r
e
p
l
a
c
e
m
e
n
t
)


 
 
 
 
r
e
t
u
r
n
 
t
e
x
t


`
`
`




H
e
r
e
'
s
 
h
o
w
 
y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
f
u
n
c
t
i
o
n
:




`
`
`
p
y
t
h
o
n


#
 
D
e
f
i
n
e
 
t
h
e
 
r
e
p
l
a
c
e
m
e
n
t
 
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


r
e
p
l
a
c
e
m
e
n
t
_
d
i
c
t
 
=
 
{


 
 
 
 
"
a
p
p
l
e
"
:
 
"
o
r
a
n
g
e
"
,


 
 
 
 
"
b
a
n
a
n
a
"
:
 
"
p
e
a
r
"
,


 
 
 
 
"
c
h
e
r
r
y
"
:
 
"
p
l
u
m
"


}




#
 
R
e
p
l
a
c
e
 
w
o
r
d
s
 
i
n
 
a
 
t
e
x
t
 
f
i
l
e


t
e
x
t
 
=
 
r
e
p
l
a
c
e
_
w
o
r
d
s
_
i
n
_
f
i
l
e
(
"
e
x
a
m
p
l
e
.
t
x
t
"
,
 
r
e
p
l
a
c
e
m
e
n
t
_
d
i
c
t
)




#
 
P
r
i
n
t
 
t
h
e
 
m
o
d
i
f
i
e
d
 
t
e
x
t


p
r
i
n
t
(
t
e
x
t
)


`
`
`




O
u
t
p
u
t
:




`
`
`


T
h
i
s
 
i
s
 
a
 
s
e
n
t
e
n
c
e
 
w
i
t
h
 
a
p
p
l
e
,
 
b
a
n
a
n
a
,
 
a
n
d
 
c
h
e
r
r
y
 
w
o
r
d
s
.


`
`
`




I
n
 
t
h
i
s
 
e
x
a
m
p
l
e
,
 
t
h
e
 
f
u
n
c
t
i
o
n
 
r
e
a
d
s
 
t
h
e
 
t
e
x
t
 
f
i
l
e
 
"
e
x
a
m
p
l
e
.
t
x
t
"
,
 
r
e
p
l
a
c
e
s
 
t
h
e
 
w
o
r
d
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
r
e
p
l
a
c
e
m
e
n
t
 
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
,
 
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
 
m
o
d
i
f
i
e
d
 
t
e
x
t
.
 
T
h
e
 
w
o
r
d
s
 
"
a
p
p
l
e
"
,
 
"
b
a
n
a
n
a
"
,
 
a
n
d
 
"
c
h
e
r
r
y
"
 
h
a
v
e
 
b
e
e
n
 
r
e
p
l
a
c
e
d
 
w
i
t
h
 
"
o
r
a
n
g
e
"
,
 
"
p
e
a
r
"
,
 
a
n
d
 
"
p
l
u
m
"
,
 
r
e
s
p
e
c
t
i
v
e
l
y
.
C
a
n
 
y
o
u
 
p
r
o
v
i
d
e
 
a
 
c
o
m
p
r
e
h
e
n
s
i
v
e
 
a
n
a
l
y
s
i
s
 
o
f
 
t
h
e
 
v
a
r
i
o
u
s
 
f
a
c
t
o
r
s
 
t
h
a
t
 
c
o
n
t
r
i
b
u
t
e
 
t
o
 
t
h
e
 
r
i
s
i
n
g
 
g
l
o
b
a
l
 
s
e
a
 
l
e
v
e
l
s
?
 
P
l
e
a
s
e
 
i
n
c
l
u
d
e
 
a
 
d
e
t
a
i
l
e
d
 
e
x
p
l
a
n
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
 
i
m
p
a
c
t
 
o
f
 
a
n
t
h
r
o
p
o
g
e
n
i
c
 
a
c
t
i
v
i
t
i
e
s
 
s
u
c
h
 
a
s
 
d
e
f
o
r
e
s
t
a
t
i
o
n
 
a
n
d
 
m
e
l
t
i
n
g
 
o
f
 
g
l
a
c
i
e
r
s
,
 
a
s
 
w
e
l
l
 
a
s
 
n
a
t
u
r
a
l
 
p
r
o
c
e
s
s
e
s
 
s
u
c
h
 
a
s
 
v
o
l
c
a
n
i
c
 
e
r
u
p
t
i
o
n
s
 
a
n
d
 
o
c
e
a
n
 
w
a
r
m
i
n
g
.
 
A
d
d
i
t
i
o
n
a
l
l
y
,
 
c
a
n
 
y
o
u
 
d
i
s
c
u
s
s
 
t
h
e
 
p
o
t
e
n
t
i
a
l
 
c
o
n
s
e
q
u
e
n
c
e
s
 
o
f
 
c
o
n
t
i
n
u
e
d
 
s
e
a
 
l
e
v
e
l
 
r
i
s
e
 
o
n
 
c
o
a
s
t
a
l
 
c
o
m
m
u
n
i
t
i
e
s
,
 
i
n
f
r
a
s
t
r
u
c
t
u
r
e
,
 
a
n
d
 
e
c
o
s
y
s
t
e
m
s
,
 
a
s
 
w
e
l
l
 
a
s
 
t
h
e
 
e
c
o
n
o
m
i
c
 
a
n
d
 
s
o
c
i
a
l
 
i
m
p
l
i
c
a
t
i
o
n
s
 
f
o
r
 
t
h
o
s
e
 
a
f
f
e
c
t
e
d
?
 
F
i
n
a
l
l
y
,
 
c
a
n
 
y
o
u
 
p
r
o
v
i
d
e
 
a
 
d
e
t
a
i
l
e
d
 
a
s
s
e
s
s
m
e
n
t
 
o
f
 
t
h
e
 
p
o
t
e
n
t
i
a
l
 
s
o
l
u
t
i
o
n
s
 
o
r
 
m
i
t
i
g
a
t
i
o
n
 
s
t
r
a
t
e
g
i
e
s
 
t
h
a
t
 
c
a
n
 
b
e
 
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
 
t
o
 
a
d
d
r
e
s
s
 
t
h
e
 
i
s
s
u
e
 
o
f
 
s
e
a
 
l
e
v
e
l
 
r
i
s
e
?
 
P
l
e
a
s
e
 
p
r
o
v
i
d
e
 
y
o
u
r
 
a
n
a
l
y
s
i
s
 
i
n
 
t
h
e
 
f
o
r
m
 
o
f
 
a
 
[
r
e
s
e
a
r
c
h
 
p
a
p
e
r
]
 
w
i
t
h
 
p
r
o
p
e
r
 
c
i
t
a
t
i
o
n
s
 
a
n
d
 
r
e
f
e
r
e
n
c
e
s
.




#
#
#
 
R
e
s
p
o
n
s
e
:
 
C
e
r
t
a
i
n
l
y
,
 
I
 
c
a
n
 
h
e
l
p
 
y
o
u
 
w
i
t
h
 
t
h
a
t
.
 
H
e
r
e
 
i
s
import unittest
from unittest.mock import mock_open, patch


class TestReplaceWordsInFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_replace_single_word(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi"}
        expected_output = "hi world"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_replace_multiple_words(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi", "world": "earth"}
        expected_output = "hi earth"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="hello world")
    def test_no_replacement(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"goodbye": "bye"}
        expected_output = "hello world"

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_file(self, mock_file):
        file_path = "dummy_path.txt"
        replacement_dict = {"hello": "hi"}
        expected_output = ""

        result = replace_words_in_file(file_path, replacement_dict)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()