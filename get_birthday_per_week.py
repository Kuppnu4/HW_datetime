from datetime import datetime
from datetime import date

def get_birthdays_per_week(users):
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
                
    print(users_congrat_dict)
            


    
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



users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Alex Voit", "birthday": datetime(1988, 9, 20).date()},
        {"name": "Denis Stena", "birthday": datetime(1980, 12, 7).date()},
        {"name": "Roman Ramon", "birthday": datetime(1990, 1, 4).date()},
        {"name": "Jeka Bratuha", "birthday": datetime(1987, 3, 10).date()},
        {"name": "Mister Test", "birthday": datetime(1987, 12, 9).date()},
        {"name": "Kostia Babnik", "birthday": datetime(1987, 12, 9).date()}
        ]

get_birthdays_per_week(users)
