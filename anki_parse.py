# -*- coding: utf-8 -*-
# <ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>
# 食[た]べ物[もの]

old_format = "食[た]べ物[もの]"

left_side = [pos for pos, char in enumerate(old_format) if char == "["]


for match in reversed(left_side):
    old_format = old_format[:match-3] + "<ruby>" + old_format[match-3:]

right_side = [pos for pos, char in enumerate(old_format) if char == "]"]
for match in reversed(right_side):
    old_format = old_format[:match+1] + "</ruby>" + old_format[match+1:]


old_format = old_format.replace("[", "<rt>")
old_format = old_format.replace("]", "</rt>")

print old_format
