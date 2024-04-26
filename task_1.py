from datetime import datetime

def het_days_from_today(date):
    dr_day = datetime.strptime(date, "%Y.%m.%d").date()
    today = datetime.today().date()
    res = (today - dr_day).days
    return res
print(het_days_from_today(date='2020.10.09'))