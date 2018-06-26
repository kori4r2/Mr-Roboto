import datetime
class User:
    def __init__(id, lastUpdate=datetime.date.min, minTime=datetime.time(6), maxTime=datetime.time(22)):
        self.id = id
        self.lastUpdate = lastUpdate
        self.minTime = minTime
        self.maxTime = maxTime
class Event:
    def __init__(id, timeStart=datetime.time(0, 1), timeEnd=datetime.time(23, 59), priority=0):
        self.id = id
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.priority = priority
class Group:
    def __init__(id):
        self.id = id
class Voting:
    def __init__(id, creationDate=datetime.date.today(), limitDate=(datetime.date.today()+datetime.timedelta(2*7))):
        self.id = id
        self.creationDate = creationDate
        self.limitDate = limitDate
