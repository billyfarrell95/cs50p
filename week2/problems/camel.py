def main():
    camel_case = input("Enter camelCase variable name: ")
    snake_case = convert_to_snake_case(camel_case)
    print("In snake case:", snake_case)

def convert_to_snake_case(camel_case_string):
    snake_case = ""
    for letter in camel_case_string:
        if (letter.lower() != letter):
            snake_case += f"_{letter.lower()}"
        else:
            snake_case += letter.lower()
    return snake_case

main()

# PASS
# check50 --local cs50/problems/2022/python/camel