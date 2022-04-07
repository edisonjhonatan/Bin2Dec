

class Bin2Dec:
    
    def __init__(self, binary_number):
        self.binary_number = binary_number
        
        self.check_invalid_digits()
        self.check_eight_digit_limit()
        self.convert_binary_to_decimal()
        
    def get_number(self):
        return self.binary_number
    
    def check_invalid_digits(self):
        number = str(self.get_number())
        
        for caracter in number:
            print(caracter)
            if caracter != "0" and caracter != "1":
                raise ValueError
            
    def check_eight_digit_limit(self):
        number_of_digits = len(str(self.get_number()))
        
        if number_of_digits > 8:
            raise ValueError
        
    def convert_binary_to_decimal(self):
        binary_number = str(self.get_number())
        return int(binary_number, 2)
    