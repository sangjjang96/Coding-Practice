fb1 = []
fb2 = []

def fib(n):
    if n == 1 or n == 2:
        fb1.append(0)
        return 1
    else:
        return (fib(int(n)-1) + fib(int(n)-2))
    
def fibonacci(n):
    f = []
    f.append(0)
    f.append(1)     # f[1]
    f.append(1)     # f[2]
    for i in range(3, int(n)):
        fb2.append(0)
        f.append(f[i-1] + f[i-2])
        
n = input()
ans1 = fib(int(n))
ans2 = fibonacci(int(n))

ret = ""

ret += str(len(fb1))
ret += " "
ret += str(len(fb2)+1)

print(ret)