class Calculator:
    def add_numbers(self, *args):
        if type(args[0]) == int:
            return sum(args)

        if type(args[0]) == str:
            new_string = ""
            for arg in args:
                new_string += arg

            return new_string


calculator = Calculator()

print(calculator.add_numbers(10, 20))
print(calculator.add_numbers("10", "20"))
