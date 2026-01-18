import re

def f(dates):
    pattern = r'\d{4}-\d{2}-\d{2}'
    date_list = re.findall(pattern, dates)
    return date_list
