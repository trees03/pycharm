n=int(input("enter the  number"))

if n==0:
    print("0")
elif n==1:
    print("1")
else:
    n-=1
    a=(1+5**0.5)/2
    b=(1-5**0.5)/2
    s=((a**n)-(b**n))/(5**0.5)
    print(round(s))