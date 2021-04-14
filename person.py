class Person:
    def __init__(self):
        self._full_name = None
        self._money = None
        self._sleepmood = None
        self._healthRate = None

#Attribute setters & getters
#----------------------------
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter   
    def full_name(self, full_name):
        self._full_name = full_name

#money
#---------------------------------
    @property
    def money(self):
        return self._money

    @money.setter   
    def money(self, money):
        self._money = money

#sleepmood
#----------------------------------
    @property
    def sleepmood(self):
        return self._sleepmood

    @sleepmood.setter   
    def sleepmood(self, sleepmood):
        self._sleepmood = sleepmood

#healthRate
#------------------------------------
    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter   
    def healthRate(self, healthRate):
        if healthRate >= 0 and healthRate <= 100:
            self._healthRate = healthRate

#Person sleep method
#--------------------

    def sleep(self,hours):
        pass

#Person eat method
#--------------------

    def eat(self,meals):
        pass

#Person buy method
#--------------------

    def buy(self,items):
        pass





