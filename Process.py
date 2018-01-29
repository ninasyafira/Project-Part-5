from Users import Users
from SpendingLimit import SpendingLimit

def processUser(name,todayMonth,todayYear):
    usersList = []
    print(todayMonth)
    print(todayYear)
    print(name)
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0]==name and int(list[5])==todayMonth and int(list[6])==todayYear:
            goal = float(list[4])
            save = float(list[3])
            left = goal - save
            l = '%.2f' %left
            monthly = 0.05 / 12
            convert = monthly / 100
            interest = save * convert
            i = '%.2f' %interest
            s = Users(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],l,i)
            usersList.append(s)
    return usersList


def limit(name,todayMonth,todayYear):
    limitList = []
    limit_file = open('file/spendingLimit.txt', 'r')
    for limitlist in limit_file:
        list = limitlist.split(',')
        if list[0]==name and int(list[2])==todayMonth and int(list[3])==todayYear:
            s = SpendingLimit(list[0],list[1],list[2],list[3],list[4],list[5])
            limitList.append(s)
    return limitList

def over(name,todayMonth,todayYear):
    o_file = open('file/spendingLimit.txt','r')
    for ofile in o_file:
        list = ofile.split(',')
        if list[0]==name and int(list[2])==todayMonth and int(list[3])==todayYear:
            limit = float(list[4])
            spend = float(list[5])
            spend -= limit
            o = '%.2f' %spend
            return o

def interest(name,todayMonth,todayYear):
    i_file = open('file/users.txt','r')
    for ilist in i_file:
        list = ilist.split(',')
