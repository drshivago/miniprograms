x = int(input('Enter in a number'))
for n in range(2, x):
    for x in range(2, n):   #because it is 2 to n it doesn't run the first time
        #print('n= ',n, 'x= ', x, 'n % x', n%x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
