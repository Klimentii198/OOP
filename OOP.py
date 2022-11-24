if __name__ == "__main__":
   print("Hello python")
class Massive:
    def __init__(self, a=None, b=None):
        if a is None:
            a = []
        self.a = a
        self.b = b
    def appent(self, a = None, b=None):
        a = a.extend(b)
        print(a)
    def lem(self, a = None):
        print(sum(1 for char in a)
    def index(self, a=None, b=None):
        print(a.index(b))
    def srez(self, a =None, b = None, c = None):
        s = slice(b, c)
        print(a[s]
a = Massive
b = Massive
print(a.appent([1,2,3,4,5,6], 3))