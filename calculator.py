def priority(x):
    if x == "^":
        return 3
    if x == "*" or x == "/":
        return 2
    if x == "+" or x == "-":
        return 1
    
def main():
    operators = []
    values = []
    x = "2+1-2"
    for i in x:
        # print(values,operators)
        if i.isnumeric():
            values.append(i)
        elif len(operators) == 0:
            operators.append(i)
        else:
            top = operators[-1]
            if priority(top) < priority(i): # type: ignore
                operators.append(i)
            else:   
                operators.pop()
                b = int(values.pop())
                a = int(values.pop())
                result = 0
                if top == "^":
                    result = a^b
                elif top == "*":
                    result = a*b
                elif top == "/":
                    result = a/b
                elif top == "+":
                    result = a+b
                elif top == "-":
                    result = a-b
                values.append(result)
                operators.append(i)
    while len(operators) > 0:
        top = operators.pop()
        b = int(values.pop())
        a = int(values.pop())
        result = 0
        if top == "^":
            result = a^b
        elif top == "*":
            result = a*b
        elif top == "/":
            result = a/b
        elif top == "+":
            result = a+b
        elif top == "-":
            result = a-b
        values.append(result)
    print(values.pop())
    
main()