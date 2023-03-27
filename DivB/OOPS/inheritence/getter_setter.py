# property
# private members
# setter

class Employee:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        print("Someone is trying to get name")
        return self.__name

    @name.setter
    def name(self, name):
        print(f"previous name {self.__name} that will change to {name}")
        self.__name = name


akshit = Employee("akshit")

akshit.name = "viral"

print(akshit.name)
