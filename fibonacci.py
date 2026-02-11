# function to find n-th term of fibonacci series using naive approach
def fibonacci(n: int) -> int:
    global calls
    calls += 1
    # -- base cases --
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # -- recursive case --
    return fibonacci(n-1) + fibonacci(n-2)
    
    # shortcut expression
    # return 0 if n==0 else 1 if n==1 else fibonacci(n-1) + fibonacci(n-2)

n = 50
calls = 0
print(f"Fibonacci Series up to {n} is: ")
print("i\tTerm\tCalls")
for i in range(n):
    calls = 0
    print(f"{i}\t{fibonacci(i)}\t{calls}") # print i-th term of series