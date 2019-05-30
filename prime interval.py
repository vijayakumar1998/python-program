N,Q=input().split()
N=int(N)
Q=int(Q)
for num in range(N+1,Q):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print(num)
