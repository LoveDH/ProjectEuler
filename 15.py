#20x20 격자에서의 경로의 수

def factorial(N):
    value = 1
    for i in range(1,N+1):
        value = value * i
    return value


print(factorial(40)/(factorial(20)*factorial(20)))