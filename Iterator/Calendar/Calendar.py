from __Aggregate import __Aggregate
from CalendarIterator import CalendarIterator


class Calendar(__Aggregate):

    def __init__(self):
        self.__plans = []
        self.__last = 0

    def getPlanAt(self, index):
        return self.__plans[index]

    def appendPlan(self, plan):
        if self.validatePlan(plan):
            self.__plans.append(plan)
            self.__last += 1

    def getLength(self):
        return self.__last

    def validatePlan(self, plan):
        for __plan in self.__plans:
            if __plan.startDate < plan.startDate < __plan.endDate or __plan.startDate < plan.endDate < __plan.endDate:
                print('The plan "' + plan.getName() + '" overlaps with plan "' + __plan.getName() + '" !')
                return False
        return True

    def iterator(self):
        return CalendarIterator(self)
