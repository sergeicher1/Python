from datetime import datetime

# yesterday = datetime.date(2024, 1, 28)
# print(yesterday)

# today = datetime.now()
# # print(today)
# print("{} {} {} {}:{}".format(today.day, today.month, today.year, today.hour, today.minute))

# future_time = datetime(2024, 2, 10)
# print(future_time)
time = datetime.strptime("22/05/2024", "%d/%m/%Y")
print(time)