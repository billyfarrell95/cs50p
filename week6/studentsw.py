import csv

name = input("What's your name? ")
location = input("What are you from? ")

with open("studentsw.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "location"])
    writer.writerow({"name": name, "location": location})