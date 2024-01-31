import shelve

FILENAME = "file"
# d = shelve.open(FILENAME)
# d.close()



with shelve.open(FILENAME) as file:
    file.clear()
with shelve.open(FILENAME) as file:
    for key in file:
        print(key, "-", file[key])
