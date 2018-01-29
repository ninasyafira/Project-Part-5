class Goals():
    def __init__(self,user,type,name,goal):
        self.__user = user
        self.__type = type
        self.__name = name
        self.__goal = goal

    def get_user(self):
        return self.__user
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_goal(self):
        return self.__goal

    def set_user(self,user):
        self.__user = user
    def set_type(self,type):
        self.__type = type
    def set_name(self,name):
        self.__name = name
    def set_goal(self,goal):
        self.__goal = goal