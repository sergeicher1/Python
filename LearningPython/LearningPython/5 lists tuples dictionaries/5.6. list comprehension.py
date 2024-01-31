# numbers = [-3, -2, -1, 0, 1, 2, 3]
# positive_numbers = [i for i in numbers if i > 0]
# # positive_numbers = []
# # for i in numbers:
# #     if i > 0:
# #         positive_numbers.append(i)
# print(positive_numbers)

# print([n for n in range(10)])
dictionary = {"red": "red", "blue":"blue", "green":"green"}
words = [f"{key}: {dictionary[key]}" for key in dictionary if len(key) > 3]
print(words)
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# doubled_only_positive_numbers = [i * 2 if i > 0 else i for i in numbers]
# print(doubled_only_positive_numbers)
