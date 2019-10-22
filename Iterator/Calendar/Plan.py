import datetime


class Plan:

    def __init__(self, name, startDate, endDate):
        self.__name = name
        self.startDate = datetime.datetime.strptime(startDate, '%Y/%m/%d %H:%M')
        self.endDate = datetime.datetime.strptime(endDate, '%Y/%m/%d %H:%M')

    def getName(self):
        return self.__name

    def getStartDate(self):
        return self.startDate.strftime('%Y-%m-%d %H:%M')

    def getEndDate(self):
        return self.endDate.strftime('%Y-%m-%d %H:%M')
