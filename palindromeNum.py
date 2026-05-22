num = int(input("Enter a number: "))
copy = num
rev = 0

while copy > 0:
    rem = copy%10
    rev = rev*10 + rem
    copy //= 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")