# function to find n-th term of fibonacci series using naive approach
def fibonacci(n: int) -> int:
    # -- base cases --
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # -- recursive case --
    return fibonacci(n-1) + fibonacci(n-2)
    
    # shortcut expression
    # return 0 if n==0 else 1 if n==1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    n = 10
    print(f"Fibonacci Series up to {n} is: ")
    print("i\tTerm")
    for i in range(n):
        print(f"{i}\t{fibonacci(i)}") # print i-th term of series
        
if __name__ == "__main__":
    main()