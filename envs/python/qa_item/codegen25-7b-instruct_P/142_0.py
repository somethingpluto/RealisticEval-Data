d
e
f
 
c
a
m
e
l
_
c
a
s
e
_
t
o
_
c
a
p
i
t
a
l
i
z
e
d
_
w
i
t
h
_
s
p
a
c
e
s
(
i
n
p
u
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
c
a
m
e
l
C
a
s
e
 
s
t
r
i
n
g
 
t
o
 
a
 
f
o
r
m
a
t
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
c
a
p
i
t
a
l
i
z
e
d
 
a
n
d
 
s
p
a
c
e
s
 
b
e
t
w
e
e
n
 
w
o
r
d
s
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
"
t
h
i
s
I
s
T
e
s
t
"


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
"
T
h
i
s
 
i
s
 
t
e
s
t
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
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
 
c
a
m
e
l
C
a
s
e
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
o
n
v
e
r
t
e
d
 
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
 
s
p
a
c
e
s
 
a
n
d
 
i
n
i
t
i
a
l
 
c
a
p
i
t
a
l
i
z
a
t
i
o
n
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
w
o
r
d
.
c
a
p
i
t
a
l
i
z
e
(
)
 
f
o
r
 
w
o
r
d
 
i
n
 
i
n
p
u
t
.
s
p
l
i
t
(
"
_
"
)
)






d
e
f
 
c
a
m
e
l
_
c
a
s
e
_
t
o
_
s
n
a
k
e
_
c
a
s
e
(
i
n
p
u
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
c
a
m
e
l
C
a
s
e
 
s
t
r
i
n
g
 
t
o
 
a
 
f
o
r
m
a
t
 
w
i
t
h
 
u
n
d
e
r
s
c
o
r
e
s
 
b
e
t
w
e
e
n
 
w
o
r
d
s
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
"
t
h
i
s
I
s
T
e
s
t
"


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
"
t
h
i
s
_
i
s
_
t
e
s
t
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
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
 
c
a
m
e
l
C
a
s
e
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
o
n
v
e
r
t
e
d
 
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
 
u
n
d
e
r
s
c
o
r
e
s
 
b
e
t
w
e
e
n
 
w
o
r
d
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
f
"
_
{
w
o
r
d
.
l
o
w
e
r
(
)
}
"
 
i
f
 
w
o
r
d
.
i
s
u
p
p
e
r
(
)
 
e
l
s
e
 
w
o
r
d
 
f
o
r
 
w
o
r
d
 
i
n
 
i
n
p
u
t
)






d
e
f
 
s
n
a
k
e
_
c
a
s
e
_
t
o
_
c
a
m
e
l
_
c
a
s
e
(
i
n
p
u
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
s
n
a
k
e
_
c
a
s
e
 
s
t
r
i
n
g
 
t
o
 
a
 
f
o
r
m
a
t
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
c
a
p
i
t
a
l
i
z
e
d
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
"
t
h
i
s
_
i
s
_
t
e
s
t
"


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
"
T
h
i
s
I
s
T
e
s
t
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
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
 
s
n
a
k
e
_
c
a
s
e
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
o
n
v
e
r
t
e
d
 
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
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
c
a
p
i
t
a
l
i
z
e
d
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
w
o
r
d
.
c
a
p
i
t
a
l
i
z
e
(
)
 
f
o
r
 
w
o
r
d
 
i
n
 
i
n
p
u
t
.
s
p
l
i
t
(
"
_
"
)
)






d
e
f
 
s
n
a
k
e
_
c
a
s
e
_
t
o
_
c
a
p
i
t
a
l
i
z
e
d
_
w
i
t
h
_
s
p
a
c
e
s
(
i
n
p
u
t
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
s
n
a
k
e
_
c
a
s
e
 
s
t
r
i
n
g
 
t
o
 
a
 
f
o
r
m
a
t
 
w
i
t
h
 
t
h
e
 
f
i
r
s
t
 
l
e
t
t
e
r
 
c
a
p
i
t
a
l
i
z
e
d
 
a
n
d
 
s
p
a
c
e
s
 
b
e
t
w
e
e
n
 
w
o
r
d
s
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
"
t
h
i
s
_
i
s
_
t
e
s
t
"


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
"
T
h
i
s
 
i
s
 
t
e
s
t
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
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
 
s
n
a
k
e
_
c
a
s
e
 
s
t
r
i
n
g
 
t
o
 
b
e
 
c
o
n
v
e
r
t
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


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
c
o
n
v
e
r
t
e
d
 
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
 
s
p
a
c
e
s
 
a
n
d
 
i
n
i
t
i
a
l
 
c
a
p
i
t
a
l
i
z
a
t
i
o
n
import unittest


class TestCamelCaseConversion(unittest.TestCase):

    def test_simple_camel_case(self):
        input = "thisIsTest"
        expected_output = "This is test"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_single_word_lowercase(self):
        input = "example"
        expected_output = "Example"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_multiple_uppercase_letters(self):
        input = "thisIsAnExampleString"
        expected_output = "This is an example string"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_single_uppercase_letter(self):
        input = "aSingleUppercaseLetterX"
        expected_output = "A single uppercase letter x"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)

    def test_already_capitalized_string(self):
        input = "AlreadyCapitalized"
        expected_output = "Already capitalized"
        self.assertEqual(camel_case_to_capitalized_with_spaces(input), expected_output)
if __name__ == '__main__':
    unittest.main()