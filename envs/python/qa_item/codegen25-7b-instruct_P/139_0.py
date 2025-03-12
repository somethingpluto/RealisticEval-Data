d
e
f
 
p
a
r
s
e
_
c
a
t
e
g
o
r
i
e
s
_
f
r
o
m
_
s
u
m
m
a
r
y
(
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t
:
 
s
t
r
 
=
 
'
'
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


 
 
 
 
E
x
t
r
a
c
t
s
 
c
a
t
e
g
o
r
i
e
s
 
f
r
o
m
 
a
 
s
u
m
m
a
r
i
z
e
d
 
o
u
t
p
u
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
 
c
l
e
a
n
e
d
 
s
u
m
m
a
r
y
 
a
n
d
 
c
a
t
e
g
o
r
i
e
s
.




 
 
 
 
T
h
e
 
c
a
t
e
g
o
r
i
e
s
 
a
r
e
 
e
x
p
e
c
t
e
d
 
t
o
 
b
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
"
C
a
t
e
g
o
r
i
e
s
:
 
[
c
a
t
e
g
o
r
y
1
,
 
c
a
t
e
g
o
r
y
2
,
 
.
.
.
]
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
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
 
s
u
m
m
a
r
y
 
t
e
x
t
 
p
o
t
e
n
t
i
a
l
l
y
 
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
 
c
a
t
e
g
o
r
i
z
e
d
 
q
u
e
s
t
i
o
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
d
i
c
t
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
l
e
a
n
e
d
 
s
u
m
m
a
r
y
 
t
e
x
t
 
a
n
d
 
a
 
l
i
s
t
 
o
f
 
c
a
t
e
g
o
r
i
e
s
.


 
 
 
 
"
"
"


 
 
 
 
c
a
t
e
g
o
r
i
e
s
 
=
 
[
]


 
 
 
 
s
u
m
m
a
r
y
 
=
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t


 
 
 
 
i
f
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t
:


 
 
 
 
 
 
 
 
m
a
t
c
h
 
=
 
r
e
.
s
e
a
r
c
h
(
r
'
C
a
t
e
g
o
r
i
e
s
:
 
(
.
*
)
'
,
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t
)


 
 
 
 
 
 
 
 
i
f
 
m
a
t
c
h
:


 
 
 
 
 
 
 
 
 
 
 
 
c
a
t
e
g
o
r
i
e
s
 
=
 
m
a
t
c
h
.
g
r
o
u
p
(
1
)
.
s
p
l
i
t
(
'
,
'
)


 
 
 
 
 
 
 
 
 
 
 
 
s
u
m
m
a
r
y
 
=
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t
[
:
m
a
t
c
h
.
s
t
a
r
t
(
)
]
 
+
 
s
u
m
m
a
r
i
z
e
d
_
o
u
t
p
u
t
[
m
a
t
c
h
.
e
n
d
(
)
:
]


 
 
 
 
r
e
t
u
r
n
 
{
'
s
u
m
m
a
r
y
'
:
 
s
u
m
m
a
r
y
,
 
'
c
a
t
e
g
o
r
i
e
s
'
:
 
c
a
t
e
g
o
r
i
e
s
}






d
e
f
 
p
a
r
s
e
_
c
a
t
e
g
o
r
i
e
s
_
f
r
o
m
_
q
u
e
s
t
i
o
n
(
q
u
e
s
t
i
o
n
:
 
s
t
r
 
=
 
'
'
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


 
 
 
 
E
x
t
r
a
c
t
s
 
c
a
t
e
g
o
r
i
e
s
 
f
r
o
m
 
a
 
q
u
e
s
t
i
o
n
 
s
t
r
i
n
g
 
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
 
c
l
e
a
n
e
d
 
q
u
e
s
t
i
o
n
 
a
n
d
 
c
a
t
e
g
o
r
i
e
s
.




 
 
 
 
T
h
e
 
c
a
t
e
g
o
r
i
e
s
 
a
r
e
 
e
x
p
e
c
t
e
d
 
t
o
 
b
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
"
C
a
t
e
g
o
r
y
:
 
[
c
a
t
e
g
o
r
y
1
,
 
c
a
t
e
g
o
r
y
2
,
 
.
.
.
]
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
(
s
t
r
)
:
 
T
h
e
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
p
o
t
e
n
t
i
a
l
l
y
 
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
 
c
a
t
e
g
o
r
i
z
e
d
 
q
u
e
s
t
i
o
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
d
i
c
t
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
l
e
a
n
e
d
 
q
u
e
s
t
i
o
n
 
t
e
x
t
 
a
n
d
 
a
 
l
i
s
t
 
o
f
 
c
a
t
e
g
o
r
i
e
s
.


 
 
 
 
"
"
"


 
 
 
 
c
a
t
e
g
o
r
i
e
s
 
=
 
[
]


 
 
 
 
i
f
 
q
u
e
s
t
i
o
n
:


 
 
 
 
 
 
 
 
m
a
t
c
h
 
=
 
r
e
.
s
e
a
r
c
h
(
r
'
C
a
t
e
g
o
r
y
:
 
(
.
*
)
'
,
 
q
u
e
s
t
i
o
n
)


 
 
 
 
 
 
 
 
i
f
 
m
a
t
c
h
:


 
 
 
 
 
 
 
 
 
 
 
 
c
a
t
e
g
o
r
i
e
s
 
=
 
m
a
t
c
h
.
g
r
o
u
p
(
1
)
.
s
p
l
i
t
(
'
,
'
)


 
 
 
 
 
 
 
 
 
 
 
 
q
u
e
s
t
i
o
n
 
=
 
q
u
e
s
t
i
o
n
[
:
m
a
t
c
h
.
s
t
a
r
t
(
)
]
 
+
 
q
u
e
s
t
i
o
n
[
m
a
t
c
h
.
e
n
d
(
)
:
]


 
 
 
 
r
e
t
u
r
n
 
{
'
q
u
e
s
t
i
o
n
'
:
 
q
u
e
s
t
i
o
n
,
 
'
c
a
t
e
g
o
r
i
e
s
'
:
 
c
a
t
e
g
o
r
i
e
s
}






d
e
f
 
p
a
r
s
e
_
c
a
t
e
g
o
r
i
e
s
_
f
r
o
m
_
a
n
s
w
e
r
(
a
n
s
w
e
r
:
 
s
t
r
 
=
 
'
'
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


 
 
 
 
E
x
t
r
a
c
t
s
 
c
a
t
e
g
o
r
i
e
s
 
f
r
o
m
 
a
n
 
a
n
s
w
e
r
 
s
t
r
i
n
g
 
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
 
c
l
e
a
n
e
d
 
a
n
s
w
e
r
 
a
n
d
 
c
a
t
e
g
o
r
i
e
s
.




 
 
 
 
T
h
e
 
c
a
t
e
g
o
r
i
e
s
 
a
r
e
 
e
x
p
e
c
t
e
d
 
t
o
 
b
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
"
C
a
t
e
g
o
r
y
:
 
[
c
a
t
e
g
o
r
y
1
,
 
c
a
t
e
g
o
r
y
2
,
 
.
.
.
]
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
a
n
s
w
e
r
 
(
s
t
r
)
:
 
T
h
e
 
a
n
s
w
e
r
 
t
e
x
t
 
p
o
t
e
n
t
i
a
l
l
y
 
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
 
c
a
t
e
g
o
r
i
z
e
d
 
a
n
s
w
e
r
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
d
i
c
t
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
l
e
a
n
e
d
 
a
n
s
w
e
r
 
t
e
x
t
 
a
n
d
 
a
 
l
i
s
t
 
o
f
 
c
a
t
e
g
o
r
i
e
s
.


 
 
 
 
"
"
"


 
 
 
import unittest

class TestParseCategoriesFromSummary(unittest.TestCase):
    def test_extracts_categories_and_cleans_the_summary_correctly(self):
        input_data = "This is a summary. Categories: [Technology, Health]"
        expected = {
            'summary': "This is a summary.",
            'categories': ["Technology", "Health"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_returns_empty_categories_and_original_summary_when_no_categories_are_present(self):
        input_data = "This is a summary without categories."
        expected = {
            'summary': "This is a summary without categories.",
            'categories': []
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_ignores_case_of_the_category_prefix(self):
        input_data = "Summary text. categories: [Education, Science]"
        expected = {
            'summary': "Summary text.",
            'categories': ["Education", "Science"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_handles_extra_spaces_and_malformed_category_strings_correctly(self):
        input_data = "Details follow. Categories: [ Business ,  , Finance]"
        expected = {
            'summary': "Details follow.",
            'categories': ["Business", "Finance"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_removes_the_category_string_correctly_even_if_it_appears_in_the_middle_of_the_summary(self):
        input_data = "Beginning of summary. Categories: [Art, Design] Continuation of summary."
        expected = {
            'summary': "Beginning of summary. Continuation of summary.",
            'categories': ["Art", "Design"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)
if __name__ == '__main__':
    unittest.main()