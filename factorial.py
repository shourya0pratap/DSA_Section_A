def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

    # shortcut expression
    # return 1 if n in range(0,2) else n * factorial(n-1)
    
def main():
    n = 5
    print(f"Factorial of {n} is {factorial(n)}")
    
if __name__ == "__main__":
    main()