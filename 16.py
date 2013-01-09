def sum(num):
    ret = 0
    for s in str(num):
        ret += int(s)
    return ret

import math

print sum(math.factorial(100))
