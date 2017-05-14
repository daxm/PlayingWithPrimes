from miscfunctions import calc_factors

pow2 = 1
count = 10
while count > 0:
    pow2 = pow2<<1
    testnum = pow2 - 1
    print("Number: %s has %s as factors." % (testnum, calc_factors(testnum)))
    count -= 1

