def look(words):
    match words:
        case {"red": red, **rest}:
            print(f"red: {red}")
            for key in rest:
                print(f"{key}: {rest[key]}")



look({"red": "red", "blue": "blue", "green": "green"})
look({"red": "red", "green": "green"})
look({"blue": "blue", "green": "green"})
look({"green": "green"})
look("Yellow")
