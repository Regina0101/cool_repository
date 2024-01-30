from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.5"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        '''Сheck how many days until your birthday'''
        users_birthday = datetime(today.year, birthday_this_year.month, birthday_this_year.day).date()
        if users_birthday < today:
            '''If the birthday has already passed in the current year'''
            users_birthday = datetime(today.year + 1, birthday_this_year.month, birthday_this_year.day).date()


        days_left = (users_birthday - today).days

        if days_left < 7:
            ''' Check if your birthday falls on a weekend'''
            day_of_the_week = users_birthday.weekday()

            if day_of_the_week in [5, 6]:
                '''We extend congratulations to Monday'''
                next_birthday = users_birthday + timedelta(days=(7 - day_of_the_week))
            else:
                next_birthday = users_birthday

            '''We write down the birthday in the dictionary'''
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)

for birthday in upcoming_birthdays:
    print("Список привітань на цьому тижні:")
    print("Name:", birthday["name"])
    print("Date:", birthday["congratulation_date"])
