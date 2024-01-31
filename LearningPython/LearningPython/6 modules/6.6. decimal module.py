# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.10")
# number = number * 3
# print(number)
from decimal import Decimal, ROUND_FLOOR
number = Decimal("10.026")
number = number.quantize(Decimal("1.00"), ROUND_FLOOR)
print(number)