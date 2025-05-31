class CharacterLiteral:
    def __init__(self):
        self.index = 0
    
    def Next(self):
        val  = chr(65+self.index)
        self.index = (self.index+1)%26
        return val
