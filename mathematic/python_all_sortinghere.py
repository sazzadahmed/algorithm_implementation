class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.number)

    def __cmp__(self, other):
        if hasattr(other, 'number'):
            return self.number.__cmp__(other.number)


customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)
]
a=sorted(customlist)
for b in a:
    print(b.number)


s=[[1,2,3,4,5],(45,24,2,42),[3,4,23,4,234]]

def cmpr(data):
    return data[0]
d=sorted(s,key=cmpr)
for b in d:
    print(b)


