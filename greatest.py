a1,a2,a3= input().split()
a1=int(a1)
a2=int(a2)
a3=int(a3)
if a1>=a2 and a1>=a3:
    print(a1)
elif a2>=a1 and a2>=a3:
    print(a2)
else:
    print(a3)
