class Calculator:

    def add(self, a, b):
        return int(a) + int(b)

    def subtract(self, a, b):
        return int(a) - int(b)

    def multiply(self, a, b):
        return int(a) * int(b)

    def divide(self, a, b):
        return int(a) / int(b)

    def simple_divide(self, a, b):
        quotient = int(a) // int(b)
        remainder = int(a) % int(b)

        if remainder == 0:
            return quotient
        else:
            return quotient, remainder