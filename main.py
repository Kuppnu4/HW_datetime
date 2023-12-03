'''
This modul check birthdays of a list of ppeople and gives
as a result the list of persons birthdays for the following week
'''

from datetime import date, datetime

def get_birthdays_per_week(users):
    '''
    This method recieve the list of users with their names and birthday dates
    and return the list of users which havw birthday next week, with a specific
    day of the week
    '''
    start_day = date.today()
    start_stamp = datetime.combine(start_day, datetime.min.time()).timestamp()
    seconds_in_week = 60 * 60 * 24 * 7
    stop_stamp = start_stamp + seconds_in_week
    users_congrat_dict = {}

    for u in users:

        user_next_birthday = get_user_next_birthday(u)

        if start_stamp < user_next_birthday.timestamp() < stop_stamp:
            user_name = u['name'].split(' ')[0]
            week_day = user_next_birthday.strftime('%A')
            users_congrat_dict = check_day_in_dict(week_day, users_congrat_dict)


            if week_day in ('Saturday', 'Sunday'):
                del users_congrat_dict[week_day]
                users_congrat_dict = check_day_in_dict('Monday', users_congrat_dict)
                users_congrat_dict['Monday'].append(user_name)
            else:
                users_congrat_dict[week_day].append(user_name)

    users = users_congrat_dict

    return users


def get_user_next_birthday(user):
    '''
    this method recieve the borning dates of the persons
    and return their birthdays in this year or in the beggining of next year
    '''

    if user['birthday'].month == 1 and user['birthday'].day <= 7:
        user_next_birthday = datetime(
                                        year = datetime.now().year + 1,
                                        month = user['birthday'].month,
                                        day = user['birthday'].day
                                        )

    else:
        user_next_birthday = datetime(
                                        year = datetime.now().year,
                                        month = user['birthday'].month,
                                        day = user['birthday'].day
                                        )

    return user_next_birthday



def check_day_in_dict(week_day, days_in_dict):
    '''
    this method checks if the specific day of the week exists
    alredy in the list or not
    '''

    if not week_day in days_in_dict:
        days_in_dict[week_day] = []

    return days_in_dict




if __name__ == "__main__":

    persons = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(persons)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
