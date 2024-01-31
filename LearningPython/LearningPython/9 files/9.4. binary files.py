import pickle

FILENAME = "users.dat"
users = [
    ["Tom", 28, True],
    ["Bob", 35, True],
    ["Sam", 20, False],

]
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Name: ", user[0], "Age: ", user[1], "Is married: ", user[2])
