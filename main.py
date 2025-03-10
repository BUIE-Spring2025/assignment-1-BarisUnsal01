def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    # 1 -> I  5 -> V  10 -> X  50 -> L  100 -> C  500 -> D  1000 -> M
   
    values = [1000, 500, 100, 50, 10, 5, 1]
    letters = ["M", "D", "C", "L", "X", "V", "I"]
    
    while num >= values:
        num = num - values[0]
