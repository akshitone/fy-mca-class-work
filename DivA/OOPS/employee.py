from datetime import datetime


class Employee:
    # class variable
    no_of_employees = 0
    raise_amount = 1.05

    def __init__(self, name, salary):
        # instance variable
        self.name = name
        self.salary = salary

        Employee.no_of_employees += 1

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        salary = float(salary)
        return cls(name, salary)

    @classmethod
    def from_list(cls, data):
        name, salary = data
        return cls(name, salary)

    @staticmethod
    def is_holiday(day):
        if day.weekday() in [5, 6]:
            return True
        return False

    def raise_salary(self):
        self.salary = self.salary*Employee.raise_amount

    def display_details(self):
        self.raise_salary()
        print(f"Name: {self.name}, Salary: {self.salary}")


akshit = Employee("Akshit", 10000)
viral = Employee("Viral", 20000)

# akshit.display_details()
# viral.display_details()

rajan_data = "Rajan-50000"
ashwini_data = "Ashwini-25000"

rajan = Employee.from_string(rajan_data)
ashwini = Employee.from_string(ashwini_data)

nikunj_list_data = ["Nikunj", 50000]
anand_list_data = ["Anand", 25000]


rajan.display_details()

print(Employee.no_of_employees)

nikunj = Employee.from_list(nikunj_list_data)
anand = Employee.from_list(anand_list_data)

anand.display_details()


print(Employee.is_holiday(datetime(2023, 2, 24)))
