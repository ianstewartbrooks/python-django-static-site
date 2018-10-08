import datetime

def namer():
    today = datetime.datetime.now()
    return "Hello, this is my home page. Today's date is " + today.strftime('%d.%m.%Y')