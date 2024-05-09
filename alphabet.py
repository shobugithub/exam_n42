# alphabet nomle class yozing, class obyektlarini iteeratsiya qilish inkoni bo'lsin(iterator), obyektni 
# for sikli orqali iteratsiya qilinsa 26ta allifbo xarflari chiqsin


#creating class
class Alphabet:
    def __init__ (self):
        self.index = 0
        self.letter = 'abcdefghijklmnopqrstuvwxyz'
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self.index < len(self.letter):
            letter = self.letter[self.index]
            self.index += 1
            return letter 
        
        else:
            raise StopIteration
        
alphabets = Alphabet()

for letter in alphabets:
    print(letter)