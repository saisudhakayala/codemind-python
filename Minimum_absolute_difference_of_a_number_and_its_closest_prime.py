n=int(input())
prevprime=n
while True:
    fc=0
    for i in range(1,prevprime+1):
        if prevprime%i==0:
            fc+=1
    if fc==2:
        break
    prevprime-=1
nextprime=n
while True:
     fc=0
     for i in range(1,nextprime+1):
         if nextprime%i==0:
             fc+=1
     if fc==2:
        break
     nextprime+=1
n1=n-prevprime
n2=nextprime-n
if n1<=n2:
    print(n1)
elif n2<=n1:
    print(n2)
else:
    print(0)
