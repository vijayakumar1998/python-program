N,Q=input().split()
N=int(N)
Q=int(Q)
if(N,Q<=100000):
    for i in range (N+1,Q):
        if i%2==1:
            print(i)
