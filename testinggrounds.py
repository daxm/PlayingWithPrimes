from miscfunctions import calc_factors

pow2 = 1
count = 1000
while count > 0:
    pow2 = pow2<<1
    testnum = pow2 - 1
    results = calc_factors(testnum)
    if len(results) > 0:
        print("Number: %s has %s as factors." % (testnum, results))
    else:
        print("Number: %s is prime!." % (testnum))
    count -= 1

