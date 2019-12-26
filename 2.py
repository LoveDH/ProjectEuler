#피보나치 수열에서 짝수이면서 4백만 이하인 모든항을 더하면?

sum = 0

fib = list()
i=0
while True :
    if i == 0 :
        fib.append(1)
    elif i == 1 :
        fib.append(2)
    else :
        fib.append(fib[i-1]+fib[i-2])

    if fib[i] % 2 == 0 and fib[i] < 4000000 :
        sum += fib[i]
    elif fib[i] > 4000000:
        break;
    i+=1

print (sum)
