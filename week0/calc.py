def main():
    x = input("What's x? ")
    y = input("What's y? ")
    answer = calculate_sum(x, y)
    print(answer)
    a = input("What's a? ")
    b = input("What's b? ")
    div_answer = calculate_div(a, b)
    print(f"{div_answer:.2f} using f strings")
    print(round(div_answer, 2), "using round")

def calculate_sum(x, y):
    try:
        # if x and y are numbers, print the sum and exit program
        sum = float(x) + float(y)
        # print(sum)
        # print("Rounded to nearest int", round(sum))
        # print("Formatted", f"{sum:,}")
        # print("Rounded to 2 decimals", f"{round(sum, 2):,}")
        return f"{round(sum, 2):,}"
    except:
        return "Make sure to enter numbers!"

def calculate_div(a, b):
    try:
        answer = float(a) / float(b)
        return answer
    except:
        return "Make sure to enter numbers!"

main()