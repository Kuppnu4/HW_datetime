from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    start_day = date.today()
    start_stamp = datetime.combine(start_day, datetime.min.time()).timestamp()
    SECONDS_IN_WEEK = 60 * 60 * 24 * 7
    stop_stamp = start_stamp + SECONDS_IN_WEEK
    users_congrat_dict = {}

    for u in users:
        
        user_next_birthday = get_user_next_birthday(u)
       
        if start_stamp < user_next_birthday.timestamp() < stop_stamp:
            user_name = u['name'].split(' ')[0]
            week_day = user_next_birthday.strftime('%A')
            users_congrat_dict = check_day_in_dict(week_day, users_congrat_dict)
            

            if week_day == 'Saturday' or week_day == 'Sunday':
                del users_congrat_dict[week_day]
                users_congrat_dict = check_day_in_dict('Monday', users_congrat_dict)
                users_congrat_dict['Monday'].append(user_name)
            else:
                users_congrat_dict[week_day].append(user_name)
                
    users = users_congrat_dict
    
    return users


def get_user_next_birthday(user):
    
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
    
    if not week_day in days_in_dict:
        days_in_dict[week_day] = []

    return days_in_dict




if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
