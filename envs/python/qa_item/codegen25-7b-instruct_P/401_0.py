i
m
p
o
r
t
 
r
e




d
e
f
 
f
i
n
d
_
p
l
a
c
e
h
o
l
d
e
r
s
(
t
e
x
t
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
a
n
d
 
r
e
t
u
r
n
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
p
l
a
c
e
h
o
l
d
e
r
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
a
t
 
{
{
 
p
l
a
c
e
h
o
l
d
e
r
 
}
}
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
i
n
p
u
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
 
p
o
t
e
n
t
i
a
l
 
p
l
a
c
e
h
o
l
d
e
r
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
 
m
a
t
c
h
i
n
g
 
p
l
a
c
e
h
o
l
d
e
r
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
 
r
e
.
f
i
n
d
a
l
l
(
r
'
{
{
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
}
}
'
,
 
t
e
x
t
)




d
e
f
 
f
i
n
d
_
p
l
a
c
e
h
o
l
d
e
r
s
_
w
i
t
h
_
a
t
t
r
i
b
u
t
e
s
(
t
e
x
t
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
a
n
d
 
r
e
t
u
r
n
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
p
l
a
c
e
h
o
l
d
e
r
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
a
t
 
{
{
 
p
l
a
c
e
h
o
l
d
e
r
.
a
t
t
r
i
b
u
t
e
 
}
}
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
i
n
p
u
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
 
p
o
t
e
n
t
i
a
l
 
p
l
a
c
e
h
o
l
d
e
r
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
 
m
a
t
c
h
i
n
g
 
p
l
a
c
e
h
o
l
d
e
r
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
 
r
e
.
f
i
n
d
a
l
l
(
r
'
{
{
\
s
*
(
[
^
\
s
}
.
]
*
)
\
s
*
\
.
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
}
}
'
,
 
t
e
x
t
)




d
e
f
 
f
i
n
d
_
p
l
a
c
e
h
o
l
d
e
r
s
_
w
i
t
h
_
a
t
t
r
i
b
u
t
e
s
_
a
n
d
_
v
a
l
u
e
s
(
t
e
x
t
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
a
n
d
 
r
e
t
u
r
n
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
p
l
a
c
e
h
o
l
d
e
r
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
a
t
 
{
{
 
p
l
a
c
e
h
o
l
d
e
r
.
a
t
t
r
i
b
u
t
e
 
=
 
v
a
l
u
e
 
}
}
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
i
n
p
u
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
 
p
o
t
e
n
t
i
a
l
 
p
l
a
c
e
h
o
l
d
e
r
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
 
m
a
t
c
h
i
n
g
 
p
l
a
c
e
h
o
l
d
e
r
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
 
r
e
.
f
i
n
d
a
l
l
(
r
'
{
{
\
s
*
(
[
^
\
s
}
.
]
*
)
\
s
*
\
.
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
=
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
}
}
'
,
 
t
e
x
t
)




d
e
f
 
f
i
n
d
_
p
l
a
c
e
h
o
l
d
e
r
s
_
w
i
t
h
_
a
t
t
r
i
b
u
t
e
s
_
a
n
d
_
v
a
l
u
e
s
_
a
n
d
_
f
i
l
t
e
r
s
(
t
e
x
t
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
 
a
n
d
 
r
e
t
u
r
n
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
p
l
a
c
e
h
o
l
d
e
r
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
a
t
 
{
{
 
p
l
a
c
e
h
o
l
d
e
r
.
a
t
t
r
i
b
u
t
e
 
=
 
v
a
l
u
e
 
|
 
f
i
l
t
e
r
 
}
}
 
f
r
o
m
 
t
h
e
 
i
n
p
u
t
 
t
e
x
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
e
x
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
 
i
n
p
u
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
 
p
o
t
e
n
t
i
a
l
 
p
l
a
c
e
h
o
l
d
e
r
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
 
m
a
t
c
h
i
n
g
 
p
l
a
c
e
h
o
l
d
e
r
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
 
r
e
.
f
i
n
d
a
l
l
(
r
'
{
{
\
s
*
(
[
^
\
s
}
.
]
*
)
\
s
*
\
.
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
=
\
s
*
(
[
^
\
s
}
]
*
)
\
s
*
\
|
\
s
import unittest


class TestFindPlaceholders(unittest.TestCase):

    def test_multiple_placeholders(self):
        """Test string with multiple placeholders."""
        input_text = "Here are some placeholders: {{ placeholder1 }}, {{ placeholder2 }}, and {{ placeholder3 }}."
        expected_output = ['placeholder1', 'placeholder2', 'placeholder3']
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_no_placeholders(self):
        """Test string with no placeholders."""
        input_text = "This string has no placeholders."
        expected_output = []
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_single_placeholder(self):
        """Test string with a single placeholder."""
        input_text = "The only placeholder is {{ singlePlaceholder }}."
        expected_output = ['singlePlaceholder']
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_placeholder_with_spaces(self):
        """Test string with placeholders that have extra spaces."""
        input_text = "Placeholders with spaces: {{  placeholder_with_spaces  }} and {{ placeholder2 }}."
        expected_output = ['placeholder_with_spaces', 'placeholder2']
        self.assertEqual(find_placeholders(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()