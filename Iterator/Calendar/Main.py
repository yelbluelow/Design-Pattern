from Calendar import Calendar
from Plan import Plan


def main():
    calendar = Calendar()
    calendar.appendPlan(Plan('剣道', '2019/10/26 9:00', '2019/10/26 12:00'))
    calendar.appendPlan(Plan('友達と遊ぶ', '2019/10/26 11:00', '2019/10/26 22:00'))
    calendar.appendPlan(Plan('本を読む', '2019/10/27 13:00', '2019/10/27 19:00'))
    it = calendar.iterator()
    while it.hasNext():
        plan = it.next()
        print('----------------------')
        print(plan.getName())
        print(plan.getStartDate())
        print(plan.getEndDate())

if __name__ == '__main__':
    main()
