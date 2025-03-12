i
m
p
o
r
t
 
c
s
v


i
m
p
o
r
t
 
o
s






d
e
f
 
c
s
v
_
t
o
_
s
q
l
_
i
n
s
e
r
t
(
c
s
v
_
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
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
a
 
c
s
v
 
f
i
l
e
 
i
n
t
o
 
a
n
 
S
Q
L
 
i
n
s
e
r
t
 
s
t
a
t
e
m
e
n
t
 
w
i
t
h
 
a
 
t
a
b
l
e
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
s
u
f
f
i
x
 
r
e
m
o
v
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
s
v
_
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
 
c
s
v
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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
 
p
a
r
s
e
d
 
s
q
l
 
s
t
r


 
 
 
 
"
"
"


 
 
 
 
t
a
b
l
e
_
n
a
m
e
 
=
 
o
s
.
p
a
t
h
.
b
a
s
e
n
a
m
e
(
c
s
v
_
f
i
l
e
_
p
a
t
h
)
.
r
e
p
l
a
c
e
(
"
.
c
s
v
"
,
 
"
"
)


 
 
 
 
s
q
l
_
s
t
r
 
=
 
f
"
I
N
S
E
R
T
 
I
N
T
O
 
{
t
a
b
l
e
_
n
a
m
e
}
 
V
A
L
U
E
S
 
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
c
s
v
_
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
 
c
s
v
_
f
i
l
e
:


 
 
 
 
 
 
 
 
c
s
v
_
r
e
a
d
e
r
 
=
 
c
s
v
.
r
e
a
d
e
r
(
c
s
v
_
f
i
l
e
)


 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
c
s
v
_
r
e
a
d
e
r
:


 
 
 
 
 
 
 
 
 
 
 
 
s
q
l
_
s
t
r
 
+
=
 
f
"
(
{
'
,
'
.
j
o
i
n
(
r
o
w
)
}
)
,
"


 
 
 
 
s
q
l
_
s
t
r
 
=
 
s
q
l
_
s
t
r
[
:
-
1
]
 
+
 
"
;
"


 
 
 
 
r
e
t
u
r
n
 
s
q
l
_
s
t
r






d
e
f
 
c
s
v
_
t
o
_
s
q
l
_
i
n
s
e
r
t
_
w
i
t
h
_
h
e
a
d
e
r
(
c
s
v
_
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
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
a
 
c
s
v
 
f
i
l
e
 
i
n
t
o
 
a
n
 
S
Q
L
 
i
n
s
e
r
t
 
s
t
a
t
e
m
e
n
t
 
w
i
t
h
 
a
 
t
a
b
l
e
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
s
u
f
f
i
x
 
r
e
m
o
v
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
s
v
_
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
 
c
s
v
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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
 
p
a
r
s
e
d
 
s
q
l
 
s
t
r


 
 
 
 
"
"
"


 
 
 
 
t
a
b
l
e
_
n
a
m
e
 
=
 
o
s
.
p
a
t
h
.
b
a
s
e
n
a
m
e
(
c
s
v
_
f
i
l
e
_
p
a
t
h
)
.
r
e
p
l
a
c
e
(
"
.
c
s
v
"
,
 
"
"
)


 
 
 
 
s
q
l
_
s
t
r
 
=
 
f
"
I
N
S
E
R
T
 
I
N
T
O
 
{
t
a
b
l
e
_
n
a
m
e
}
 
V
A
L
U
E
S
 
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
c
s
v
_
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
 
c
s
v
_
f
i
l
e
:


 
 
 
 
 
 
 
 
c
s
v
_
r
e
a
d
e
r
 
=
 
c
s
v
.
r
e
a
d
e
r
(
c
s
v
_
f
i
l
e
)


 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
c
s
v
_
r
e
a
d
e
r
:


 
 
 
 
 
 
 
 
 
 
 
 
s
q
l
_
s
t
r
 
+
=
 
f
"
(
{
'
,
'
.
j
o
i
n
(
r
o
w
)
}
)
,
"


 
 
 
 
s
q
l
_
s
t
r
 
=
 
s
q
l
_
s
t
r
[
:
-
1
]
 
+
 
"
;
"


 
 
 
 
r
e
t
u
r
n
 
s
q
l
_
s
t
r






d
e
f
 
c
s
v
_
t
o
_
s
q
l
_
i
n
s
e
r
t
_
w
i
t
h
_
h
e
a
d
e
r
_
a
n
d
_
i
n
d
e
x
(
c
s
v
_
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
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
a
 
c
s
v
 
f
i
l
e
 
i
n
t
o
 
a
n
 
S
Q
L
 
i
n
s
e
r
t
 
s
t
a
t
e
m
e
n
t
 
w
i
t
h
 
a
 
t
a
b
l
e
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
s
u
f
f
i
x
 
r
e
m
o
v
e
d
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
s
v
_
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
import unittest
import os


class TestCsvToSqlInsert(unittest.TestCase):

    def setUp(self):
        # Create sample CSV files for testing
        self.test_files = {
            'test1.csv': 'id,name,age\n1,Alice,30\n2,Bob,25',
            'test2.csv': 'product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49',
            'test3.csv': 'user_id,email\n3,test@example.com\n4,user@domain.com',
            'test4.csv': 'order_id,order_date,total\n1001,2024-09-01,59.99',
            'test5.csv': 'quote_id,quote\n1,"It\'s a beautiful day."\n2,"She said, ""Hello!"""'
        }
        # Create the files on disk
        for filename, content in self.test_files.items():
            with open(filename, 'w') as f:
                f.write(content)

    def tearDown(self):
        # Remove the test files after tests
        for filename in self.test_files:
            os.remove(filename)

    def test_simple_csv(self):
        expected_sql = (
            "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n"
            "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');"
        )
        result = csv_to_sql_insert('test1.csv')
        self.assertEqual(result, expected_sql)

    def test_product_csv(self):
        expected_sql = (
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n"
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');"
        )
        result = csv_to_sql_insert('test2.csv')
        self.assertEqual(result, expected_sql)

    def test_email_csv(self):
        expected_sql = (
            "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n"
            "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');"
        )
        result = csv_to_sql_insert('test3.csv')
        self.assertEqual(result, expected_sql)

    def test_date_and_decimal_csv(self):
        expected_sql = (
            "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');"
        )
        result = csv_to_sql_insert('test4.csv')
        self.assertEqual(result, expected_sql)
if __name__ == '__main__':
    unittest.main()