def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    str1 = str(num1)
    str2 = str(num2)
    if set(str1) != set(str2) or len(str1) != len(str2):
        return False
    for num in set(str1):
        if str1.count(num) != str2.count(num):
            return False
    return True
    