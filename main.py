def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    # 1 -> I  5 -> V  10 -> X  50 -> L  100 -> C  500 -> D  1000 -> M
    thousands = 0
    five_hundreds = 0
    hundreds = 0
    fifties = 0
    tens = 0
    fives = 0
    ones = 0
    
    while num > 1000:
        num = num - 1000
        thousands += 1
    while num > 500:
        num = num - 500
        five_hundreds += 1
    while num > 100:
        num = num - 100
        hundreds += 1
    while num > 50:
        num = num - 50
        fifties += 1
    while num > 10:
        num = num - 10
        tens += 1
    while num > 5:
        num = num - 5
        fives += 1
    while num > 1:
        num = num - 1
        ones += 1
    
    
