from __Iterator import __Iterator


class CalendarIterator(__Iterator):

    def __init__(self, calendar):
        self.__calendar = calendar
        self.__index = 0

    def hasNext(self):
        if (self.__index < self.__calendar.getLength()):
            return True
        else:
            return False

    def next(self):
        plan = self.__calendar.getPlanAt(self.__index)
        self.__index += 1
        return plan
