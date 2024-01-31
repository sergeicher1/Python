import csv

FILENAME = "users2.csv"
users = [
    {"name": "Tom", "age": 18},
    {"name": "Alice", "age": 28},
    {"name": "Sam", "age": 30}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)
    user = {"name": "Bob", "age": 50}
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], " - ", row["age"])
