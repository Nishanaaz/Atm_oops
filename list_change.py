def change(L):
    print(id(L))
    L.append(5)
    print(id(L))
    print(L)
l1=[1,2,3,4]
change(l1)
# change1(l1[:])   it will not change the real one as we are sending with colon;
print(id(l1))
print(l1)

#it means through pass by reference  if we send mutable datatype it will change the original list also 
#that is why al id are same.

def change1(L2):
    print(id(L2))
    L2=L2+(4,5)
    print(id(L2))
    print(L2)
l2=[1,2,3,4]
change1(l2)
print(id(l2))
print(l2)
#it means if the pass by reference datatype is immutable it will not change the original one 
# will create another one.