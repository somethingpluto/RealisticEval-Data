d
e
f
 
c
o
n
v
e
r
t
_
y
a
m
l
_
t
o
_
j
s
o
n
(
y
a
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
,
 
j
s
o
n
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
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
y
a
m
l
 
f
o
r
m
a
t
 
f
i
l
e
s
 
t
o
 
j
s
o
n
 
f
o
r
m
a
t
 
f
i
l
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
a
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
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
Y
A
M
L
 
f
i
l
e
.


 
 
 
 
 
 
 
 
j
s
o
n
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
 
p
a
t
h
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
J
S
O
N
 
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
y
a
m
l
_
f
i
l
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
y
a
m
l
_
d
a
t
a
 
=
 
y
a
m
l
.
s
a
f
e
_
l
o
a
d
(
f
)


 
 
 
 
w
i
t
h
 
o
p
e
n
(
j
s
o
n
_
f
i
l
e
,
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
j
s
o
n
.
d
u
m
p
(
y
a
m
l
_
d
a
t
a
,
 
f
,
 
i
n
d
e
n
t
=
2
)






d
e
f
 
c
o
n
v
e
r
t
_
j
s
o
n
_
t
o
_
y
a
m
l
(
j
s
o
n
_
f
i
l
e
:
 
s
t
r
,
 
y
a
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
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
j
s
o
n
 
f
o
r
m
a
t
 
f
i
l
e
s
 
t
o
 
y
a
m
l
 
f
o
r
m
a
t
 
f
i
l
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
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
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
J
S
O
N
 
f
i
l
e
.


 
 
 
 
 
 
 
 
y
a
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
 
p
a
t
h
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
Y
A
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
j
s
o
n
_
f
i
l
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
j
s
o
n
_
d
a
t
a
 
=
 
j
s
o
n
.
l
o
a
d
(
f
)


 
 
 
 
w
i
t
h
 
o
p
e
n
(
y
a
m
l
_
f
i
l
e
,
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
y
a
m
l
.
d
u
m
p
(
j
s
o
n
_
d
a
t
a
,
 
f
,
 
i
n
d
e
n
t
=
2
)






d
e
f
 
c
o
n
v
e
r
t
_
j
s
o
n
_
t
o
_
c
s
v
(
j
s
o
n
_
f
i
l
e
:
 
s
t
r
,
 
c
s
v
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
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
j
s
o
n
 
f
o
r
m
a
t
 
f
i
l
e
s
 
t
o
 
c
s
v
 
f
o
r
m
a
t
 
f
i
l
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
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
 
p
a
t
h
 
t
o
 
t
h
e
 
i
n
p
u
t
 
J
S
O
N
 
f
i
l
e
.


 
 
 
 
 
 
 
 
c
s
v
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
 
p
a
t
h
 
t
o
 
t
h
e
 
o
u
t
p
u
t
 
C
S
V
 
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
j
s
o
n
_
f
i
l
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
j
s
o
n
_
d
a
t
a
 
=
 
j
s
o
n
.
l
o
a
d
(
f
)


 
 
 
 
w
i
t
h
 
o
p
e
n
(
c
s
v
_
f
i
l
e
,
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
w
r
i
t
e
r
 
=
 
c
s
v
.
w
r
i
t
e
r
(
f
)


 
 
 
 
 
 
 
 
w
r
i
t
e
r
.
w
r
i
t
e
r
o
w
(
j
s
o
n
_
d
a
t
a
[
0
]
.
k
e
y
s
(
)
)


 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
j
s
o
n
_
d
a
t
a
:


 
 
 
 
 
 
 
 
 
 
 
 
w
r
i
t
e
r
.
w
r
i
t
e
r
o
w
(
r
o
w
.
v
a
l
u
e
s
(
)
)






d
e
f
 
c
o
n
v
e
r
t
_
c
s
v
_
t
o
_
j
s
o
n
(
c
s
v
_
f
i
l
e
:
 
s
t
r
,
 
j
s
o
n
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
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
c
s
v
 
f
o
r
m
a
t
 
f
i
l
e
s
 
t
o
 
j
s
o
n
 
f
o
r
m
a
t
 
f
i
l
e
s


 
 
 
 
A
r
g
s
import unittest
import os
import json
import yaml


class TestConvertYamlToJson(unittest.TestCase):

    def setUp(self):
        # Create temporary YAML files for testing
        self.simple_yaml = 'simple.yaml'
        self.nested_yaml = 'nested.yaml'
        self.empty_yaml = 'empty.yaml'
        self.list_yaml = 'list.yaml'
        self.invalid_yaml = 'invalid.yaml'

        with open(self.simple_yaml, 'w') as file:
            file.write("name: John Doe\nage: 30\n")

        with open(self.nested_yaml, 'w') as file:
            file.write("person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n")

        with open(self.empty_yaml, 'w') as file:
            file.write("")

        with open(self.list_yaml, 'w') as file:
            file.write("- item1\n- item2\n- item3\n")

        with open(self.invalid_yaml, 'w') as file:
            file.write("{ invalid: YAML: structure }\n")

    def tearDown(self):
        # Remove temporary files after testing
        os.remove(self.simple_yaml)
        os.remove(self.nested_yaml)
        os.remove(self.empty_yaml)
        os.remove(self.list_yaml)
        os.remove(self.invalid_yaml)

        if os.path.exists('output.json'):
            os.remove('output.json')

    def test_simple_yaml_conversion(self):
        convert_yaml_to_json(self.simple_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, {"name": "John Doe", "age": 30})

    def test_nested_yaml_conversion(self):
        convert_yaml_to_json(self.nested_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        expected_data = {
            "person": {
                "name": "Jane Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "zip": 10001
                }
            }
        }
        self.assertEqual(data, expected_data)

    def test_empty_yaml_conversion(self):
        convert_yaml_to_json(self.empty_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, None)  # YAML.safe_load() returns None for empty files

    def test_list_yaml_conversion(self):
        convert_yaml_to_json(self.list_yaml, 'output.json')
        with open('output.json', 'r') as jf:
            data = json.load(jf)
        self.assertEqual(data, ["item1", "item2", "item3"])

    def test_invalid_yaml_conversion(self):
        with self.assertRaises(yaml.YAMLError):
            convert_yaml_to_json(self.invalid_yaml, 'output.json')

if __name__ == '__main__':
    unittest.main()