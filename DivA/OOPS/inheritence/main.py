# The method of inheriting the properties of parent class into a
# child class is known as inheritance.

# Employee class
# - raise_amount
# email
# Manager class
# Developer class
# - raise_amount
# - lang

# Why inheritence?

# Empty child class

# help


class Employee:
    # class variable
    raise_amount = 1.40

    def __init__(self, first_name: str, last_name: str, salary: float):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        # instance variable
        self.email = f"{first_name.lower()}.{last_name.lower()}@google.com"
        self.salary = salary

    def raise_salary(self):
        self.salary = self.salary * self.raise_amount

    def display_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    raise_amount = 1.25

    def __init__(self, first_name: str, last_name: str, salary: float, skill: str):
        super().__init__(first_name, last_name, salary)
        # Employee.__init__(self, first_name, last_name, salary)
        self.skill = skill

    def display_details(self):
        super().display_details()
        print("Skill: " + self.skill)


class Manager(Employee):
    raise_amount = 1.70

    def __init__(self, first_name: str, last_name: str, salary: float, employees: list = None):
        super().__init__(first_name, last_name, salary)

        self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def display_details(self):
        pass


if __name__ == "__main__":
    akshit = Developer("Akshit", "Mithaiwala", 10000, "Python Developer")
    rajan = Developer("Rajan", "Mourya", 20000, "Flutter Developer")

    viral = Manager("Viral", "Mithaiwala", 50000, [akshit])

    print(viral.email)

    viral.add_employee(rajan)

    for emp in viral.employees:
        print("- ", emp.email)
    # help(Developer)


# Create Phone class - Parent class
# Android and IOS class - Child class
# - Default values to be passed to constructor
# - Default data type to be passed to constructor and functions
# - Count number of android and ios devices
# - Display all android devices
# - Display all ios devices
# - Add discount to phones
# - Different discount for android and ios devices
