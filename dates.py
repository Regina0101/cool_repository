# Option 1
# from datetime import datetime

# def get_days_from_today(date):
#     while True:
#         try:
#             user_datetime=input("Enter the date of your registration: 'YYYY-MM-DD' ")
#             user_date=datetime.strptime(user_datetime, '%Y-%m-%d')
#             if date>user_date:
#                 duration_days=date-user_date
#                 print(f"{duration_days.days} days ago")
#                 break
#             else:
#                 print("The date can't be latter than the current date")
#         except Exception:
#             print("Please enter in format 'YYYY-MM-DD'")


# get_days_from_today(datetime.today())

# Option2
from datetime import datetime

def get_days_from_today(date_str):
    user_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    today_date = datetime.today().date()
    duration_days = (today_date - user_date).days
    return duration_days

result = get_days_from_today('2022-12-22')
print(result)
