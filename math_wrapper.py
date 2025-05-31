class MyMath:
    def __init__(self, num: int):
        self.value = num
    
    def add(self ,number : int ):
        self.value += number
        return self
    
    def subtract(self, number : int):
        self.value -=number
        return self
    
    def multiply(self, number : int):
        self.value *= number
        return self
    
    def divide(self, number : int):
        self.value //= number #assuming integer divison rn
        return self
    
    def Value(self):
        return self.value
    




