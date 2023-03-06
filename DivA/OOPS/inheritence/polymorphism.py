class Calculator:

    def add_values(self, *args):
        # if isinstance(args[0], int):
        #     return sum(args)
        # else:
        #     new_string = ""
        #     for arg in args:
        #         new_string += arg
        #     return new_string

        if type(args[0]) == int:
            pass
        elif type(args[0]) == float:
            pass
        elif type(args[0]) == str:
            pass


calculator = Calculator()
print(calculator.add_values(10, 20, 30))
print(calculator.add_values("Hello ", "How are you? ", "I'm fine"))
