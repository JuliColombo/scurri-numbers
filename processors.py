from abc import ABC


class Processor(ABC):
    number: int

    def matches(self, number) -> bool:
        pass

    def execute(self, number):
        pass


class PrintIntegerProcessor(Processor):
    def matches(self, number) -> bool:
        return True

    def execute(self, number):
        print(number)


class PrintStringProcessor(Processor):
    multiple_numbers = []
    result = str

    def __init__(self, result, *multiple_numbers):
        self.multiple_numbers = multiple_numbers
        self.result = result

    def is_multiple(self, multiple_number, number):
        return number % multiple_number == 0

    def all_are_multiples(self, number) -> bool:
        return all(self.is_multiple(multiple_number, number) for multiple_number in self.multiple_numbers)

    def matches(self, number):
        return self.all_are_multiples(number)

    def execute(self, number):
        print(self.result)

