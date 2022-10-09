n=int(input())
p=1
s=0
while n:
    r=n%10
    p*=r
    s+=r
    n=n//10
d=p-s
print(d)
    