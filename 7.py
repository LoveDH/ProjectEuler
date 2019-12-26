#10001번째 소수

i=3
j=3
a = list([2])

while len(a)<10001 :
    if i%j != 0 :
        j += 2
    elif i==j :
        a.append(i)
        print(i)
        i+=2
        j=3
    else :
        i+=2
        j=3

print(a[-1])


