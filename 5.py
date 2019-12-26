#1~20사이의 어떤 수로도 나누어 떨어지는 가장 작은수
def pp(a):
    b = list()
    i=2
    while True:
        if a%i == 0 :
            b.append(i)
            a/=i
        elif a == 1 :
            break
        else:
            i+=1
    return b
value = 1
c=list()
p=list()
for i in range(2,21):
    c.append(pp(i))
for i in range(2, 21):
    for j in range(0,19):
        p.append(c[j].count(i))
    value = value*(i**max(p))
    p=list()

print(value)