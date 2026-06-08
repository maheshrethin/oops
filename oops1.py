class sam:
    def Add(self,a):
        print(a)
    def Add(self,a,b):
        print(a+b)
    def Add(self,a,b,c):
        print(a+b+c)
s=sam()
# s.Add(10)
# s.Add(10,20)
s.Add(10,20,30)

class Load:
    def loading(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
l=Load()
print("Add",l.loading(125))
print("Add",l.loading(125,125))
print("Add",l.loading(125,125,125))