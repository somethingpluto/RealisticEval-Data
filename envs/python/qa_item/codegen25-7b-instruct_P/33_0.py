i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d






d
e
f
 
p
a
r
s
e
_
x
m
l
_
t
o
_
d
a
t
a
f
r
a
m
e
(
x
m
l
_
f
i
l
e
:
 
s
t
r
)
 
-
>
 
p
d
.
D
a
t
a
F
r
a
m
e
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
 
t
h
e
 
X
M
L
 
f
i
l
e
 
i
n
t
o
 
a
 
p
a
n
d
a
s
 
D
a
t
a
F
r
a
m
e
,
 
w
h
e
r
e
 
e
a
c
h
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g
 
i
s
 
t
r
e
a
t
e
d
 
a
s
 
a
 
r
o
w
 
r
e
c
o
r
d
 
i
n
 
t
h
e
 
X
M
L
,


 
 
 
 
a
n
d
 
t
h
e
 
t
a
g
 
a
n
d
 
t
e
x
t
 
c
o
n
t
e
n
t
 
o
f
 
e
a
c
h
 
s
u
b
-
e
l
e
m
e
n
t
 
a
r
e
 
t
r
e
a
t
e
d
 
a
s
 
c
o
l
u
m
n
s
 
o
f
 
t
h
e
 
D
a
t
a
F
r
a
m
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
m
l
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
X
M
L
 
f
i
l
e
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
p
d
.
D
a
t
a
F
r
a
m
e
:
 
D
a
t
a
F
r
a
m
e
 
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
 
d
a
t
a
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
X
M
L
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
x
m
l
.
e
t
r
e
e
.
E
l
e
m
e
n
t
T
r
e
e
 
a
s
 
E
T




 
 
 
 
t
r
e
e
 
=
 
E
T
.
p
a
r
s
e
(
x
m
l
_
f
i
l
e
)


 
 
 
 
r
o
o
t
 
=
 
t
r
e
e
.
g
e
t
r
o
o
t
(
)




 
 
 
 
#
 
G
e
t
 
a
l
l
 
t
h
e
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g
s


 
 
 
 
s
e
q
u
e
n
c
e
s
 
=
 
r
o
o
t
.
f
i
n
d
a
l
l
(
"
s
e
q
u
e
n
c
e
"
)




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
w
h
e
r
e
 
e
a
c
h
 
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
r
e
s
e
n
t
s
 
a
 
s
i
n
g
l
e
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g


 
 
 
 
r
e
c
o
r
d
s
 
=
 
[
]


 
 
 
 
f
o
r
 
s
e
q
u
e
n
c
e
 
i
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
:


 
 
 
 
 
 
 
 
r
e
c
o
r
d
 
=
 
{
}


 
 
 
 
 
 
 
 
f
o
r
 
e
l
e
m
e
n
t
 
i
n
 
s
e
q
u
e
n
c
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
c
o
r
d
[
e
l
e
m
e
n
t
.
t
a
g
]
 
=
 
e
l
e
m
e
n
t
.
t
e
x
t


 
 
 
 
 
 
 
 
r
e
c
o
r
d
s
.
a
p
p
e
n
d
(
r
e
c
o
r
d
)




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
 
i
n
t
o
 
a
 
p
a
n
d
a
s
 
D
a
t
a
F
r
a
m
e


 
 
 
 
d
f
 
=
 
p
d
.
D
a
t
a
F
r
a
m
e
(
r
e
c
o
r
d
s
)




 
 
 
 
r
e
t
u
r
n
 
d
f






d
e
f
 
p
a
r
s
e
_
x
m
l
_
t
o
_
d
a
t
a
f
r
a
m
e
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
x
m
l
_
f
i
l
e
:
 
s
t
r
)
 
-
>
 
p
d
.
D
a
t
a
F
r
a
m
e
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
 
t
h
e
 
X
M
L
 
f
i
l
e
 
i
n
t
o
 
a
 
p
a
n
d
a
s
 
D
a
t
a
F
r
a
m
e
,
 
w
h
e
r
e
 
e
a
c
h
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g
 
i
s
 
t
r
e
a
t
e
d
 
a
s
 
a
 
r
o
w
 
r
e
c
o
r
d
 
i
n
 
t
h
e
 
X
M
L
,


 
 
 
 
a
n
d
 
t
h
e
 
t
a
g
 
a
n
d
 
t
e
x
t
 
c
o
n
t
e
n
t
 
o
f
 
e
a
c
h
 
s
u
b
-
e
l
e
m
e
n
t
 
a
r
e
 
t
r
e
a
t
e
d
 
a
s
 
c
o
l
u
m
n
s
 
o
f
 
t
h
e
 
D
a
t
a
F
r
a
m
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
x
m
l
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
X
M
L
 
f
i
l
e
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
p
d
.
D
a
t
a
F
r
a
m
e
:
 
D
a
t
a
F
r
a
m
e
 
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
 
d
a
t
a
 
e
x
t
r
a
c
t
e
d
 
f
r
o
m
 
t
h
e
 
X
M
L
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
x
m
l
.
e
t
r
e
e
.
E
l
e
m
e
n
t
T
r
e
e
 
a
s
 
E
T




 
 
 
 
t
r
e
e
 
=
 
E
T
.
p
a
r
s
e
(
x
m
l
_
f
i
l
e
)


 
 
 
 
r
o
o
t
 
=
 
t
r
e
e
.
g
e
t
r
o
o
t
(
)




 
 
 
 
#
 
G
e
t
 
a
l
l
 
t
h
e
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g
s


 
 
 
 
s
e
q
u
e
n
c
e
s
 
=
 
r
o
o
t
.
f
i
n
d
a
l
l
(
"
s
e
q
u
e
n
c
e
"
)




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
,
 
w
h
e
r
e
 
e
a
c
h
 
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
r
e
s
e
n
t
s
 
a
 
s
i
n
g
l
e
 
<
s
e
q
u
e
n
c
e
>
 
t
a
g


 
 
 
 
r
e
c
o
r
d
s
 
=
 
[
]


 
 
 
 
f
o
r
 
s
e
q
u
e
n
c
e
 
i
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
:


 
 
 
 
 
 
 
 
r
e
c
o
r
d
 
=
 
{
}


 
 
 
 
 
 
 
 
f
o
r
 
e
l
e
m
e
n
t
 
i
n
 
s
e
q
u
e
n
c
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
c
o
r
d
[
e
l
e
m
e
n
t
import unittest
import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET

class TestXmlToDataFrame(unittest.TestCase):
    def test_single_sequence(self):
        xml_data = """<root>
                        <sequence>
                            <name>John</name>
                            <age>30</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'John', 'age': '30'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_multiple_sequences(self):
        xml_data = """<root>
                        <sequence>
                            <name>Alice</name>
                            <age>25</age>
                        </sequence>
                        <sequence>
                            <name>Bob</name>
                            <age>22</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': '22'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_empty_sequence(self):
        xml_data = """<root>
                        <sequence></sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{}])
        pd.testing.assert_frame_equal(df, expected)

    def test_mixed_content(self):
        xml_data = """<root>
                        <sequence>
                            <name>Chris</name>
                        </sequence>
                        <sequence>
                            <age>28</age>
                        </sequence>
                      </root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame([{'name': 'Chris', 'age': None}, {'name': None, 'age': '28'}])
        pd.testing.assert_frame_equal(df, expected)

    def test_no_sequences(self):
        xml_data = """<root></root>"""
        xml_input = StringIO(xml_data)
        df = parse_xml_to_dataframe(xml_input)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(df, expected)

if __name__ == '__main__':
    unittest.main()