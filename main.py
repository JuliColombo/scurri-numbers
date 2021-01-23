from processors import PrintStringProcessor, PrintIntegerProcessor

integer_processor = PrintIntegerProcessor()
three_processor = PrintStringProcessor('Three', 3)
five_processor = PrintStringProcessor('Five', 5)
three_five_processor = PrintStringProcessor('ThreeFive', 3, 5)

processors = [three_five_processor, three_processor, five_processor, integer_processor]

for number in range(1, 100):
    processor = next(processor for processor in processors if processor.matches(number))
    processor.execute(number)
