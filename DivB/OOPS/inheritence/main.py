class Employee:
    # class variable
    raise_amount = 1.10

    def __init__(self, first_name: str, last_name: str, salary: float):
        # instance variable
        self.first_name = first_name
        self.last_name = last_name
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

    def __init__(self, first_name: str, last_name: str, salary: float, skill: str = "Java developer"):
        super().__init__(first_name, last_name, salary)
        self.skill = skill

    def display_details(self):
        super().display_details()
        print(f"Skill: {self.skill}")


class Manager(Employee):
    raise_amount = 1.50

    def __init__(self, first_name: str, last_name: str, salary: float, employees=None):
        super().__init__(first_name, last_name, salary)
        self.employees = employees


if __name__ == "__main__":
    akshit = Developer("Akshit", "Mithaiwala", 10000)
    rajan = Developer("Rajan", "Mourya", 20000, "Python developer")

    # akshit.display_details()
    # akshit.raise_salary()
    # akshit.display_details()

    # help(Developer)

    viral = Manager("Viral", "Shastri", 50000, [akshit, rajan])

    print(viral.email)
    for employee in viral.employees:
        print("- ", employee.email)
