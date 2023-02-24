class Emp:
    __emp_id = 0
    new_id = 0

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        print("you are using me")
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class NewEmp(Emp):
    def kuch_bhi(self):
        self.__emp_id = 100
        print(self.__emp_id)


akshit = Emp('Akshit', 20)
print(akshit.name)

# akshit.name = "No one"
# print(akshit.name)

akshit.name = "no"
print(akshit.name)

heyy = NewEmp('Heyy', 20)
heyy.kuch_bhi()
