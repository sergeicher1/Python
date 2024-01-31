from datetime import datetime

now = datetime.now()
deadline = datetime(2025, 1, 30)
if now > deadline:
    print("The deadline for the project has passed")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("The deadline is today")
else:
    period = deadline - now
    print(f"{period.days} days left")
