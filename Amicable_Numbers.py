a=int(input())
b=int(input())
p1=0
for i in range(1,a):
    if a%i==0:
        p1+=i
p2=0
for i in range(1,b):
    if b%i==0:
        p2+=i 
if p1==b and p2==a:
    print("Amicable")
else:
    print("Not Amicable")