
def calc_factors(numbertofactor):
    """
    This function takes a number and creats a list of its factors
    :param numbertofactor: 
    :return: list of factors
    """

    factors = []
    factoringnumber = 2
    originalnumber = numbertofactor
    while factoringnumber * factoringnumber <= numbertofactor:
        if numbertofactor % factoringnumber == 0:
            factors.append(factoringnumber)
            numbertofactor = int(numbertofactor // factoringnumber)
        else:
            factoringnumber += 1
    if numbertofactor != originalnumber:
        factors.append(numbertofactor)
    return factors
