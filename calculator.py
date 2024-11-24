class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            b = 0-b
            for i in range(b):
                result = self.subtract(result, a)
        else:
            for i in range(b):
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        negative = 0
        if a < 0:
            a = 0 - a
            negative += 1
        if b < 0:
            b = 0 - b
            negative += 1
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        for i in range(negative):
            result = -result
        return result
    
    def modulo(self, a, b):
        original_b = b
        if b < 0:
            b = -b
        while a < 0:
            a += b
        
        while a >= b:
            a -= b

        if original_b < 0:
            a -= b 

        return a



# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))