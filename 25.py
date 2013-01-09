fib1 = 1
fib2 = 1
fibNext = 2
fibCount= 2
while True:
    fibNext = fib1 + fib2
    fibCount += 1
    if len(str(fibNext)) >= 1000:
        print fibCount
        break
    fib1 = fib2
    fib2 = fibNext
