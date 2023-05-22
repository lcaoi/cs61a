# Q4
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4 * 1
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    temp = n
    counter = 1
    if k > 0:
        while counter < k:
            temp = temp*(n-counter)
            counter += 1
        print(temp)
    else:
        print(1)


# Q5
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while y>0:
        result = result + y%10   # to get the unit digit
        y = y//10   # to decrease digit (三位數to兩位數)
    return result


# Q7
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    

