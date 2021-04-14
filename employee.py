import re
import person

class Employee(person.Person):
    def __init__(self):
        super().__init__()
        self._id = None
        self._email = None
        self._workmood = None
        self._salary = None
        self._is_manager = None
        self._office_name = None

#id attribute setter & getter
#-------------------------------
    @property
    def id(self):
        return self._id

    @id.setter   
    def id(self, id):
        self._id = id

#email attribute setter & getter
#--------------------------------
    @property
    def email(self):
        return self._email

    @email.setter   
    def email(self, email):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if (re.search(regex, email)):
            self._email = email

#workmood attribute setter & getter
#-----------------------------------

    @property
    def workmood(self):
        return self._workmood

    @workmood.setter   
    def workmood(self, workmood):
        self._workmood = workmood

#salary attribute setter & getter
#----------------------------------

    @property
    def salary(self):
        return self._salary

    @salary.setter   
    def salary(self, salary):
        if salary > 1000:
            self._salary = salary


#is_manager attribute setter & getter
#------------------------------------

    @property
    def is_manager(self):
        return self._is_manager

    @is_manager.setter   
    def is_manager(self, is_manager):
        self._is_manager = is_manager

#is_manager attribute setter & getter
#------------------------------------

    @property
    def office_name(self):
        return self._office_name

    @office_name.setter   
    def office_name(self, office_name):
        self._office_name = office_name

#Employee work method
#-----------------------

    def work(self, hours):
        if hours == 8:
            self.workmood = "happy"
        elif hours > 0 and hours < 8:
            self.workmood = "lazy"
        elif hours > 8 and hours <= 24:
            self.workmood = "tired"
        else:
            self.workmood = None


#Employee sendEmail method
#--------------------------

    def sendEmail(self, to, subject, body):
        validto=''
        f = open("email.txt","a")
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if (re.search(regex, to)):
            validto = to
        mailto = "To: " + str(validto) + "\n"
        f.write(mailto)
        mailsuject = "Subject: " + str(subject) + "\n"
        f.write(mailsuject)
        mailbody = "Body: " + str(body) + "\n"
        f.write(mailbody)
        f.write("=======================================")
        f.close()

    def sleep(self,hours):
        if hours == 7:
            self.sleepmood = "happy"
        elif hours > 0 and hours < 7:
            self.sleepmood = "tired"
        elif hours > 7 and hours <= 24:
            self.sleepmood = "lazy"
        else:
            self.sleepmood = "none"

#Person eat method
#--------------------

    def eat(self,meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

#Person buy method
#--------------------

    def buy(self,items):
        self.money = self.money - (10 * items)

