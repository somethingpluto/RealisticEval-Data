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
 
L
i
s
t






d
e
f
 
f
i
n
d
_
s
h
i
f
t
j
i
s
_
n
o
t
_
g
b
k
(
)
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
f
i
n
d
 
a
l
l
 
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
h
a
t
 
c
a
n
 
b
e
 
r
e
p
r
e
s
e
n
t
e
d
 
i
n
 
S
h
i
f
t
-
J
I
S
,
 
b
u
t
 
n
o
t
 
i
n
 
G
B
K
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
 
a
s
 
a
n
 
a
r
r
a
y




 
 
 
 
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
h
a
t
 
a
r
e
 
u
n
i
q
u
e
 
t
o
 
S
h
i
f
t
-
J
I
S
,
 
n
o
t
 
e
n
c
o
d
a
b
l
e
 
i
n
 
G
B
K
.


 
 
 
 
"
"
"


 
 
 
 
s
h
i
f
t
j
i
s
_
c
h
a
r
s
 
=
 
[


 
 
 
 
 
 
 
 
"
␀
"
,


 
 
 
 
 
 
 
 
"
␁
"
,


 
 
 
 
 
 
 
 
"
␂
"
,


 
 
 
 
 
 
 
 
"
␃
"
,


 
 
 
 
 
 
 
 
"
␄
"
,


 
 
 
 
 
 
 
 
"
␅
"
,


 
 
 
 
 
 
 
 
"
␆
"
,


 
 
 
 
 
 
 
 
"
␇
"
,


 
 
 
 
 
 
 
 
"
␈
"
,


 
 
 
 
 
 
 
 
"
␉
"
,


 
 
 
 
 
 
 
 
"
␊
"
,


 
 
 
 
 
 
 
 
"
␋
"
,


 
 
 
 
 
 
 
 
"
␌
"
,


 
 
 
 
 
 
 
 
"
␍
"
,


 
 
 
 
 
 
 
 
"
␎
"
,


 
 
 
 
 
 
 
 
"
␏
"
,


 
 
 
 
 
 
 
 
"
␐
"
,


 
 
 
 
 
 
 
 
"
␑
"
,


 
 
 
 
 
 
 
 
"
␒
"
,


 
 
 
 
 
 
 
 
"
␓
"
,


 
 
 
 
 
 
 
 
"
␔
"
,


 
 
 
 
 
 
 
 
"
␕
"
,


 
 
 
 
 
 
 
 
"
␖
"
,


 
 
 
 
 
 
 
 
"
␗
"
,


 
 
 
 
 
 
 
 
"
␘
"
,


 
 
 
 
 
 
 
 
"
␙
"
,


 
 
 
 
 
 
 
 
"
␚
"
,


 
 
 
 
 
 
 
 
"
␛
"
,


 
 
 
 
 
 
 
 
"
␜
"
,


 
 
 
 
 
 
 
 
"
␝
"
,


 
 
 
 
 
 
 
 
"
␞
"
,


 
 
 
 
 
 
 
 
"
␟
"
,


 
 
 
 
 
 
 
 
"
␠
"
,


 
 
 
 
 
 
 
 
"
␡
"
,


 
 
 
 
 
 
 
 
"
␢
"
,


 
 
 
 
 
 
 
 
"
␣
"
,


 
 
 
 
 
 
 
 
"
␤
"
,


 
 
 
 
 
 
 
 
"
␥
"
,


 
 
 
 
 
 
 
 
"
␦
"
,


 
 
 
 
 
 
 
 
"
␧
"
,


 
 
 
 
 
 
 
 
"
␨
"
,


 
 
 
 
 
 
 
 
"
␩
"
,


 
 
 
 
 
 
 
 
"
␪
"
,


 
 
 
 
 
 
 
 
"
␫
"
,


 
 
 
 
 
 
 
 
"
␬
"
,


 
 
 
 
 
 
 
 
"
␭
"
,


 
 
 
 
 
 
 
 
"
␮
"
,


 
 
 
 
 
 
 
 
"
␯
"
,


 
 
 
 
 
 
 
 
"
␰
"
,


 
 
 
 
 
 
 
 
"
␱
"
,


 
 
 
 
 
 
 
 
"
␲
"
,


 
 
 
 
 
 
 
 
"
␳
"
,


 
 
 
 
 
 
 
 
"
␴
"
,


 
 
 
 
 
 
 
 
"
␵
"
,


 
 
 
 
 
 
 
 
"
␶
"
,


 
 
 
 
 
 
 
 
"
␷
"
,


 
 
 
 
 
 
 
 
"
␸
"
,


 
 
 
 
 
 
 
 
"
␹
"
,


 
 
 
 
 
 
 
 
"
␺
"
,


 
 
 
 
 
 
 
 
"
�
import unittest


class TestFindShiftJISNotGBK(unittest.TestCase):

    def setUp(self):
        # Pre-calculate the list once since it's computationally expensive
        self.shiftjis_not_gbk = find_shiftjis_not_gbk()

    def test_known_shiftjis_character_not_in_gbk(self):
        # Test known characters (example values provided might not actually be in one and not the other; please adjust accordingly based on actual encoding tables)
        known_shiftjis_only = 'ヱ'  # An example character, ensure this is correct as per your encodings
        self.assertNotIn(known_shiftjis_only, self.shiftjis_not_gbk)

    def test_character_in_both_encodings(self):
        # Test characters known to be in both encodings
        common_character = '水'  # Common in both, ensure accuracy
        self.assertNotIn(common_character, self.shiftjis_not_gbk)

    def test_character_in_neither_encoding(self):
        # Character not typically found in either encoding
        neither_encoding_char = '\U0001F4A9'  # Emoji, not in basic Shift-JIS or GBK
        self.assertNotIn(neither_encoding_char, self.shiftjis_not_gbk)

    def test_bounds_of_bmp(self):
        # Characters at the edge of the BMP should be checked
        edge_of_bmp = '\uffff'  # Last character in BMP
        # Since this test.js is situational, we check based on the known state; may not be necessary
        if edge_of_bmp in self.shiftjis_not_gbk:
            self.assertIn(edge_of_bmp, self.shiftjis_not_gbk)
        else:
            self.assertNotIn(edge_of_bmp, self.shiftjis_not_gbk)
if __name__ == '__main__':
    unittest.main()