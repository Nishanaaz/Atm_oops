class a:
    def m1(self):
        return 20
class b(a):
    def m1(self):
        return 30
    def m2(self):
        return 40
class c(b):
    def m2(self):
        return 20
obj1=a()
obj2=b()
obj3=c()
print(obj1.m1()+obj3.m1()+obj3.m2())


# keypoints:
# 1-child will accesshis parent method it is not there go to dada
# 2-overriding agar uske pass available hoga to