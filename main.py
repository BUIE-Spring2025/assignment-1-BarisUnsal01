def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    # 1 -> I  5 -> V  10 -> X  50 -> L  100 -> C  500 -> D  1000 -> M
   
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ["M", "DM", "D", "CD", "C", "LC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman = ""
    for i in range(len(values)):
        while num >= values[i]:
            num = num - values[i]
            roman += letters[i]

    return roman

a = int_to_roman(3999)
print(a)