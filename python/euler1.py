class Divisor(object):
    def __init__(self, number):
        if not isinstance(number, int):
            raise ValueError("Argument must be of type {}".format(int))
        self.number = number

    def evenlyDivides(self, quotient):
        if quotient % self.number == 0:
            return True
        return False

class Divisors(object):
    def __init__(self, *divisors):
        self.divisors = []
        for divisor in divisors:
            if not isinstance(divisor, Divisor):
                divisor = Divisor(divisor)
            self.divisors.append(divisor)

    def anyEvenlyDivide(self, quotient):
        for divisor in self.divisors:
            if divisor.evenlyDivides(quotient):
                return True
        return False

class NumberRange(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def multiplesOfDivisors(self, divisors):
        numbers = []
        for number in range(self.start, self.stop):
            if divisors.anyEvenlyDivide(number):
                numbers.append(number)
        return numbers

    def sumMultiplesOfDivisors(self, divisors):
        numbers = self.multiplesOfDivisors(divisors)
        return sum(numbers)

## actually perform calculations
divisors = Divisors(3, 5)
number_range = NumberRange(1, 1000)
total = number_range.sumMultiplesOfDivisors(divisors)
