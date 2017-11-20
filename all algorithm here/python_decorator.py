class MytestClass(object):
    def __init__(self,n,m,p):
        self.a=n
        self.b=m
        self.c=p


    def go_and_check(self,a,*args,**kwargs):
        for i in args:
            print(i)
        for i in kwargs:
            print(i)
class DriveClass(MytestClass):
    def __init__(self,*args,**kwargs):
        super(DriveClass,self).__init__(*args,**kwargs)

obj=DriveClass(n=20,m=20,p=21)
print(obj.a)