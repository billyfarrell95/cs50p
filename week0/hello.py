name = input("What's your name? ")

# F-strings (format string)
print(f"Hello 1, {name}.")

# 2 params
print("Hello 2,", name)

# Using sep and end
print("Hello", "3", sep='-' , end=':')
print(name) # prints on same line as above because end is : rather than default \n

# Escaping characters
print("Hello, \"friend\"")

# Cleaning up with str methods
print("Cleaning up name with str methods:")
name = name.strip().title()
print(name)
print("Split to first/last name")
first, last = name.split(" ")
print("First: ", first)
print("Last: ", last)

