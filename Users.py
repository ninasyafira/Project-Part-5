class Users():
    def __init__(self,user,type,name,saving,goal,month,year,goalType,limit,left,interest):
        self.__user = user
        self.__type = type
        self.__name = name
        self.__saving = saving
        self.__goal = goal
        self.__month = month
        self.__year = year
        self.__goalType = goalType
        self.__limit = limit
        self.__left = left
        self.__interest = interest

    def get_user(self):
        return self.__user
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_saving(self):
        return self.__saving
    def get_goal(self):
        return self.__goal
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year
    def get_goalType(self):
        return self.__goalType
    def get_limit(self):
        return self.__limit
    def get_left(self):
        return self.__left
    def get_interest(self):
        return self.__interest


    def set_user(self, user):
        self.__user = user
    def set_type(self, type):
        self.__type = type
    def set_name(self, name):
        self.__name = name
    def set_saving(self,saving):
        self.__saving = saving
    def set_goal(self,goal):
        self.__goal = goal
    def set_month(self,month):
        self.__month = month
    def set_year(self,year):
        self.__year = year
    def set_goalType(self,goalType):
        self.__goalType = goalType
    def set_limit(self,limit):
        self.__limit = limit
    def set_left(self,left):
        self.__left = left
    def set_interest(self,interest):
        self.__interest = interest

