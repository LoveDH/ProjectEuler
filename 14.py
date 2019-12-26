#가장 긴 과정을 거치는 백만이하의 우박수


def cal(N) :
    if N==1:
        return 0
    elif N%2==0:
        return 1+cal(N//2)
    else:
        return 1+cal(3*N+1)

max_number = 0
max_count = 0

for i in range(3,1000000):

    number = cal(i)
    if max_count < number:
        max_count = number
        max_number = i
        print(max_number, max_count)

