def main():
    x = input("What's x? ")
    y = input("What's y? ")
    answer = calculate_sum(x, y)
    print(answer)

# print function with basic check if entered values are numbers
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

main()