def main():
    input_exp = input("Expression: ")
    input_list = input_exp.split(" ")
    answer = calc(float(input_list[0]), input_list[1], float(input_list[2]))
    print(round(answer, 1))

def calc(num1, operation, num2):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            print("Invalid operation. Use: +, -, *, or /")
main()

# PASS
# check50 --local cs50/problems/2022/python/interpreter