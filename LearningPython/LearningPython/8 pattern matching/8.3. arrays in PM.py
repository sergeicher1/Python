def print_people(people):
    match people:
        case ["Tom", "Sam", "Bob"] | ["Tomas", "Sam", "Bob"]:
            print("Tom/Tomas, Sam, Bob")



print_people(["Tomas","Sam", "Bob"])
