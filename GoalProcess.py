from Goals import Goals

def goalsUser(name,todayMonth,todayYear):
    goalsList = []
    print(todayMonth)
    print(todayYear)
    print(name)
    goal_list = open('file/goal.txt', 'r')
    for glist in goal_list:
        list = glist.split(',')
        if list[0]==name and int(list[5])==todayMonth and int(list[6])==todayYear:
            a = Goals(list[0],list[1],list[2],list[3])
            goalsList.append(a)
    return goalsList