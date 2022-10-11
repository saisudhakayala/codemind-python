t=int(input())
for s in range(t):
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
        for j in range(1,nextprime+1):
            if nextprime%j==0:
                fc+=1
        if fc==2:
            break
        nextprime+=1
    if n-prevprime<=nextprime-n:
        print(prevprime)
    else:
        print(nextprime)
    