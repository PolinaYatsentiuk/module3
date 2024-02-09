from datetime import datetime

def get_days_from_today (date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    dif = current_date - date_object
    return dif.days

date = input("Input date: ")
dif = get_days_from_today (date)

print("Days: ", dif)