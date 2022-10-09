a=int(input())
c1=0
c2=0
while a:
    r=a%10
    if r%2==0:
        c1+=1
    else:
        c2+=1
    a=a//10
if c1==0:
    print("Odd")
elif c2==0:
    print("Even")
else:
    print("Mixed")