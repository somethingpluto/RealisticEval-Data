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
 
D
i
c
t






d
e
f
 
r
d
f
_
j
s
o
n
l
d
_
t
o
_
n
g
s
i
l
d
(
r
d
f
_
j
s
o
n
l
d
:
 
s
t
r
)
 
-
>
 
D
i
c
t
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
 
t
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
 
i
n
 
R
D
F
 
J
S
O
N
-
L
D
 
f
o
r
m
a
t
 
t
o
 
N
G
S
I
-
L
D
 
f
o
r
m
a
t


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
d
f
_
j
s
o
n
l
d
 
(
s
t
r
)
:
 
R
D
F
 
J
S
O
N
-
L
D
 
f
o
r
m
a
t
t
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
s
 
a
 
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


 
 
 
 
 
 
 
 
D
a
t
a
 
f
o
r
m
a
t
t
e
d
 
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
 
N
G
S
I
-
L
D
 
s
p
e
c
i
f
i
c
a
t
i
o
n
s
.


 
 
 
 
"
"
"


 
 
 
 
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
s
(
r
d
f
_
j
s
o
n
l
d
)


 
 
 
 
e
n
t
i
t
i
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
e
n
t
i
t
y
 
i
n
 
d
a
t
a
[
"
@
g
r
a
p
h
"
]
:


 
 
 
 
 
 
 
 
e
n
t
i
t
y
_
i
d
 
=
 
e
n
t
i
t
y
[
"
@
i
d
"
]


 
 
 
 
 
 
 
 
e
n
t
i
t
y
_
t
y
p
e
 
=
 
e
n
t
i
t
y
[
"
@
t
y
p
e
"
]


 
 
 
 
 
 
 
 
e
n
t
i
t
y
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
 
=
 
{
}


 
 
 
 
 
 
 
 
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
 
e
n
t
i
t
y
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
k
e
y
 
n
o
t
 
i
n
 
[
"
@
i
d
"
,
 
"
@
t
y
p
e
"
]
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
n
t
i
t
y
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
[
k
e
y
]
 
=
 
v
a
l
u
e


 
 
 
 
 
 
 
 
e
n
t
i
t
i
e
s
.
a
p
p
e
n
d
(


 
 
 
 
 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
i
d
"
:
 
e
n
t
i
t
y
_
i
d
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
t
y
p
e
"
:
 
e
n
t
i
t
y
_
t
y
p
e
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
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
"
:
 
e
n
t
i
t
y
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
,


 
 
 
 
 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
{
"
e
n
t
i
t
i
e
s
"
:
 
e
n
t
i
t
i
e
s
}


import unittest
import json


class TestRDFJSONLDToNGSILDConversion(unittest.TestCase):
    def test_basic_conversion(self):
        """Test a basic and correct conversion from JSON-LD to NGSI-LD."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "@id": "urn:ngsi-ld:Vehicle:A123",
            "@type": "Vehicle",
            "speed": {"value": 60, "unitCode": "KMH"}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:Vehicle:A123",
            "type": "Vehicle",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "speed", "value": {"value": 60, "unitCode": "KMH"}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_missing_id_and_type(self):
        """Test conversion when @id and @type are missing."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "speed": {"value": 60, "unitCode": "KMH"}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:unknown:id",
            "type": "UnknownType",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "speed", "value": {"value": 60, "unitCode": "KMH"}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_with_nested_objects(self):
        """Test conversion with nested objects."""
        rdf_jsonld = json.dumps({
            "@context": "http://schema.org/",
            "@id": "urn:ngsi-ld:Vehicle:A123",
            "@type": "Vehicle",
            "location": {"latitude": 48.8566, "longitude": 2.3522}
        })
        expected_ngsild = {
            "id": "urn:ngsi-ld:Vehicle:A123",
            "type": "Vehicle",
            "@context": "http://schema.org/",
            "attributes": [
                {"type": "Property", "name": "location", "value": {"latitude": 48.8566, "longitude": 2.3522}}
            ]
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

    def test_invalid_json_input(self):
        """Test the function's response to invalid JSON input."""
        rdf_jsonld = "This is not a valid JSON"
        with self.assertRaises(json.JSONDecodeError):
            rdf_jsonld_to_ngsild(rdf_jsonld)

    def test_empty_jsonld(self):
        """Test the conversion of an empty JSON-LD document."""
        rdf_jsonld = json.dumps({})
        expected_ngsild = {
            "id": "urn:ngsi-ld:unknown:id",
            "type": "UnknownType",
            "@context": "https://schema.lab.fiware.org/ld/context",
            "attributes": []
        }
        result = rdf_jsonld_to_ngsild(rdf_jsonld)
        self.assertEqual(result, expected_ngsild)

if __name__ == '__main__':
    unittest.main()