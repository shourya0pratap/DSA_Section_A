def precedence(op):
    match op:
        case '^':
            return 3
        case '*' | '/':
            return 2
        case '+' | '-':
            return 1
    return 0

def infix_to_postfix(expr : str):
    result = ""
    stack = []
    expr = "(" + expr + ")"
    for chr in expr:
        if chr.isalnum():
            result += chr
        elif chr == '(' or not stack:
            stack.append(chr)
        elif chr == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            if precedence(chr) > precedence(stack[-1]):
                stack.append(chr)
            else:
                while precedence(chr) <= precedence(stack[-1]):
                    result += stack.pop()
                stack.append(chr)
    print(result)

def main():
    expr = "A+B*(C^D-E)^(F+G*H)-I"
    infix_to_postfix(expr)
    
if __name__ == "__main__":
    main()