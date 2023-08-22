class a:
    def m1(self):
        return 20
class b(a):
    def m1(self):
        val=super().m1()+30
        return val
    def m2(self):
        return 40
class c(b):
    def m1(self):
        val=self.m1()+20
        return val
# obj1=a()
# obj2=b()
obj3=c()
print(obj3.m1())

# # keypoints:
# 1-jab obj3.m1 ko call karega tab class c m jaega and then
# aur vhaa par self.m1 ko baar baar call kr rha hai to recursion ban gya
# kyonki koi vbase condition nahin hai.