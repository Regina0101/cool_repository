from datetime import datetime

def get_days_from_today(date):
    while True:
        try:
            user_datetime=input("Enter the date of your registration: 'YYYY-MM-DD' ")
            user_date=datetime.strptime(user_datetime, '%Y-%m-%d')
            if date>user_date:
                duration_days=date-user_date
                print(f"{duration_days.days} days ago")
                break
            else:
                print("The date can't be latter than the current date")
        except Exception:
            print("Please enter in format 'YYYY-MM-DD'")


get_days_from_today(datetime.today())
