# numbers1 = []
# numbers2 = list()
# objects = [1, 2.5, "hello", True]

# numbers = [1, 2, 3, 4, 5]
# people = ["Tom", "Sam", "Bob"]
# print(numbers)
# print(people)

# numbers2 = list(numbers)
# print(numbers2)
# letters = list("Hello")
# print(letters)

# numbers = [5] * 6
# print(numbers)
# people = ["Tom"] * 3
# print(people)
# print(students[0])
# students[0] = "Mike"
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[-1])
# print(students[-2])
# print(students[-3])
# print(students[-4])
# students = ["Bob", "Sam", "Tom", "Alice"]
# bob, sam, tom, alice = students
# print(bob)
# print(sam)
# for student in students:
#     print(student)
# i = 0
# while i < len(students):
#     print(students[i])
#     i += 1
# numbers1 = [1, 2, 3]
# numbers2 = [1, 2, 3]
# if numbers1 == numbers2:
#     print("Equal")
# else:
#     print("Not equal")
# slice1 = students[:2]
# print(slice1)
# slice2 = students[1:4]
# print(slice2)
# slice3 = students[1:4:2]
# print(slice3)
# if "Alice" in students:
#     print("Alice in students")
# students.append("John")
# print(students)
# students.insert(1, "Bill")
# print(students)
# students.extend(["Mike", "Marley"])
# print(students)
# index_of_tom = students.index("Tom")
# print(index_of_tom)
# students.pop()
# print(students)
# students.remove("Alice")
# print(students)
# students.clear()
# print(students)

# students = ["Bob", "Sam", "Tom", "Alice"]
# del students[1]
# print(students)
# nums = [10,20,30,40]
# nums[1:3] = [11,22]
# print(nums)
# students = ["Bob", "Sam", "Tom", "Alice"]
# # student_count = students.count("Tom")
# # print(student_count)
# # students.sort()
# # print(students)
# # students.reverse()
# # print(students)
# # sorted(students)
# print(sorted(students))
# nums = [1,50, 100, 200, 500, 0]
# print(min(nums))
# print(max(nums))
# students = ["Bob", "Sam", "Tom", "Alice"]
# students2 = ["Bob", "Sam", "Tom", "Alice"]
# students3 = students + students2
# print(students3)

people = [
    ["Tom", 24],
    ["Bob", 43],
    ["Sam", 30]
]
for person in people:
    for item in person:
        print(item, end="|")

