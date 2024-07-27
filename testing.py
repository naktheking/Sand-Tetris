class test():
    def __init__(self, name):
        self.name = name
    def getit(self):
        return len(self.name)
    
a = test('steven')

print(a.getit())