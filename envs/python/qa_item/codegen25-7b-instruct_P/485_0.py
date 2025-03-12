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
 
p
r
e
p
a
r
e
_
q
u
e
r
y
(
s
q
l
:
 
s
t
r
,
 
p
a
r
a
m
s
:
 
d
i
c
t
)
 
-
>
 
t
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
m
o
d
i
f
i
e
s
 
a
 
S
Q
L
 
q
u
e
r
y
 
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
 
n
a
m
e
d
 
p
a
r
a
m
e
t
e
r
s


 
 
 
 
(
l
i
k
e
 
$
n
a
m
e
,
 
$
a
g
e
)
 
i
n
t
o
 
a
 
f
o
r
m
a
t
 
c
o
m
p
a
t
i
b
l
e
 
w
i
t
h
 
l
i
b
r
a
r
i
e
s
 
t
h
a
t
 
r
e
q
u
i
r
e


 
 
 
 
p
o
s
i
t
i
o
n
a
l
 
p
a
r
a
m
e
t
e
r
s
 
(
l
i
k
e
 
$
1
,
 
$
2
,
 
e
t
c
.
)
,
 
s
u
c
h
 
a
s
 
a
s
y
n
c
p
g
.
 
I
t
 
r
e
t
u
r
n
s


 
 
 
 
a
 
t
u
p
l
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
 
m
o
d
i
f
i
e
d
 
S
Q
L
 
s
t
r
i
n
g
 
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
 
p
a
r
a
m
e
t
e
r
 
v
a
l
u
e
s


 
 
 
 
o
r
d
e
r
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
 
t
h
e
i
r
 
n
e
w
 
p
o
s
i
t
i
o
n
s
 
i
n
 
t
h
e
 
q
u
e
r
y
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


 
 
 
 
 
 
 
 
 
 
 
 
s
q
l
:
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
u
s
e
r
s
 
W
H
E
R
E
 
i
d
 
=
 
$
u
s
e
r
_
i
d
 
A
N
D
 
s
t
a
t
u
s
 
=
 
$
s
t
a
t
u
s


 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
a
m
s
:
 
{
'
u
s
e
r
_
i
d
'
:
 
4
2
,
'
s
t
a
t
u
s
'
:
 
'
a
c
t
i
v
e
'
}


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:


 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
u
s
e
r
s
 
W
H
E
R
E
 
i
d
 
=
 
$
1
 
A
N
D
 
s
t
a
t
u
s
 
=
 
$
2
,
[
4
2
,
 
'
a
c
t
i
v
e
'
]




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
q
l
 
(
s
t
r
)
:
 
T
h
e
 
o
r
i
g
i
n
a
l
 
S
Q
L
 
q
u
e
r
y
 
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
 
n
a
m
e
d
 
p
a
r
a
m
e
t
e
r
s
.


 
 
 
 
 
 
 
 
p
a
r
a
m
s
 
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
 
m
a
p
p
i
n
g
 
p
a
r
a
m
e
t
e
r
 
n
a
m
e
s
 
t
o
 
t
h
e
i
r
 
v
a
l
u
e
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


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
w
h
e
r
e
 
t
h
e
 
f
i
r
s
t
 
e
l
e
m
e
n
t
 
i
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
 
S
Q
L
 
q
u
e
r
y
 
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
 
p
o
s
i
t
i
o
n
a
l
 
p
a
r
a
m
e
t
e
r
s
,
 
a
n
d
 
t
h
e
 
s
e
c
o
n
d
 
e
l
e
m
e
n
t
 
i
s
 
a
 
l
i
s
t
 
o
f
 
p
a
r
a
m
e
t
e
r
 
v
a
l
u
e
s
 
s
o
r
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
 
t
h
e
 
o
r
d
e
r
 
o
f
 
t
h
e
 
p
o
s
i
t
i
o
n
a
l
 
p
a
r
a
m
e
t
e
r
s
.


 
 
 
 
"
"
"


 
 
 
 
#
 
G
e
t
 
t
h
e
 
n
a
m
e
d
 
p
a
r
a
m
e
t
e
r
s
 
f
r
o
m
 
t
h
e
 
S
Q
L
 
q
u
e
r
y


 
 
 
 
n
a
m
e
d
_
p
a
r
a
m
s
 
=
 
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
"
\
$
\
w
+
"
,
 
s
q
l
)


 
 
 
 
#
 
G
e
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
 
n
a
m
e
d
 
p
a
r
a
m
e
t
e
r
s
 
f
r
o
m
 
t
h
e
 
S
Q
L
 
q
u
e
r
y


 
 
 
 
n
a
m
e
d
_
p
a
r
a
m
s
_
l
i
s
t
 
=
 
[
p
a
r
a
m
[
1
:
]
 
f
o
r
 
p
a
r
a
m
 
i
n
 
n
a
m
e
d
_
p
a
r
a
m
s
]


 
 
 
 
#
 
G
e
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
 
p
a
r
a
m
e
t
e
r
s
 
f
r
o
m
 
t
h
e
 
S
Q
L
 
q
u
e
r
y


 
 
 
 
p
a
r
a
m
s
_
l
i
s
t
 
=
 
l
i
s
t
(
p
a
r
a
m
s
.
k
e
y
s
(
)
)


 
 
 
 
#
 
G
e
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
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
n
o
t
 
i
n
 
t
h
e
 
S
Q
L
 
q
u
e
r
y


 
 
 
 
m
i
s
s
i
n
g
_
p
a
r
a
m
s
 
=
 
s
e
t
(
p
a
r
a
m
s
_
l
i
s
t
)
 
-
 
s
e
t
(
n
a
m
e
d
_
p
a
r
a
m
s
_
l
i
s
t
)


 
 
 
 
#
 
R
a
i
s
e
 
a
n
 
e
r
r
o
r
 
i
f
 
t
h
e
r
e
 
a
r
e
 
m
i
s
s
i
n
g
 
p
a
r
a
m
e
t
e
r
s


 
 
 
 
i
f
 
m
i
s
s
i
n
g
_
p
a
r
a
m
s
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(


 
 
 
 
 
 
 
 
 
 
 
 
f
"
T
h
e
 
f
o
l
l
o
w
i
n
g
 
p
a
r
a
m
e
t
e
r
s
 
a
r
e
 
m
i
s
s
i
n
g
 
i
n
 
t
h
e
 
S
Q
L
 
q
u
e
r
y
:
 
{
m
i
s
s
i
n
g
_
p
a
r
a
m
s
}
"


 
 
 
 
 
 
 
 
)


 
 
 
 
#
 
G
e
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
 
p
a
r
a
m
e
t
e
r
s
 
t
h
a
t
 
a
r
e
 
i
n
 
b
o
t
h
 
t
h
e
 
S
Q
L
 
q
u
e
r
y
 
a
n
d
 
t
h
e
 
p
a
r
a
m
e
t
e
r
s


 
 
 
 
c
o
m
m
o
n
_
p
a
r
a
m
s
 
=
 
s
e
t
(
n
a
m
e
d
_
p
a
r
a
m
s
_
l
i
s
t
)
 
&
 
s
e
t
(
p
a
r
a
m
s
_
l
i
s
t
)


 
 
 
 
#
 
S
o
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
 
c
o
m
m
o
n
 
p
a
r
a
m
e
t
e
r
s
 
i
n
 
t
h
e
 
o
r
d
e
r
 
o
f
 
t
h
e
 
S
Q
L
 
q
u
e
r
y


 
 
 
 
c
o
m
m
o
n
_
p
a
r
a
m
s
 
=
 
s
o
r
t
e
d
(
c
o
m
m
o
n
_
p
a
r
a
m
s
,
 
k
e
y
=
n
a
m
e
d
_
p
a
r
a
m
s
_
l
i
s
t
.
i
n
d
e
x
)


 
 
 
 
#
 
G
e
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
import unittest


# Assuming the prepare_query function is defined above or imported

class TestPrepareQuery(unittest.TestCase):

    def test_valid_named_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status"
        parameters = {
            'user_id': 42,
            'status': 'active'
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2"
        expected_values = [42, 'active']

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_missing_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status"
        parameters = {
            'user_id': 42  # 'status' is missing
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2"
        expected_values = [42]  # 'status' is not included

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_no_parameters(self):
        sql_query = "SELECT * FROM users"
        parameters = {}  # No parameters provided
        expected_sql = "SELECT * FROM users"
        expected_values = []

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_multiple_same_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $user_id"
        parameters = {
            'user_id': 42
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $1"
        expected_values = [42]  # Only one value for 'user_id'

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_special_characters_in_parameters(self):
        sql_query = "INSERT INTO users (name, email) VALUES ($name, $email)"
        parameters = {
            'name': "John Doe",
            'email': "john.doe@example.com"
        }
        expected_sql = "INSERT INTO users (name, email) VALUES ($1, $2)"
        expected_values = ["John Doe", "john.doe@example.com"]

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)
if __name__ == '__main__':
    unittest.main()