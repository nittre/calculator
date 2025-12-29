def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def main():
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Invalid operator.")
        exit()

    if isinstance(result, str):  # 예외 메시지 반환 시
        print(result)
    else:
        # 정수 결과일 때는 정수로 출력
        if result.is_integer():
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()