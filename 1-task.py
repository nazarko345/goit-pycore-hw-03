import datetime

def get_days_from_today(date):
    try:
        specific_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        todays_date = datetime.datetime.today().date()
        delta = todays_date - specific_date
        return delta.days
    except AttributeError:
        return None
    
get_days_from_today("2023-06-01") # приклад використання функції