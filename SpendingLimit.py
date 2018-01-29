class SpendingLimit():
    def __init__(self,name,type,month,year,limit,spend):
        self.__name = name
        self.__type = type
        self.__month = month
        self.__year = year
        self.__limit = limit
        self.__spend = spend

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year
    def get_limit(self):
        return self.__limit
    def get_spend(self):
        return self.__spend

    def set_name(self,name):
        self.__name = name
    def set_type(self,type):
        self.__type = type
    def set_month(self,month):
        self.__month = month
    def set_year(self,year):
        self.__year = year
    def set_limit(self,limit):
        self.__limit = limit
    def set_spend(self,spend):
        self.__spend = spend