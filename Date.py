import list
def getDate():#to get date
    import datetime
    dateForToday=datetime.datetime.now
    return str(dateForToday().date())



def getTime():#to get time
    import datetime
    now=datetime.datetime.now
    return str(now().time())

