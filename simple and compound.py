p=int(input("enter principal amt"))
t=int(input("enter the time"))
r=int(input("enter the time"))
si=p*t*r/100
ci=p*((1+r/100)**t)-p
print("simple interst is",si)
print("compound interest is",ci)