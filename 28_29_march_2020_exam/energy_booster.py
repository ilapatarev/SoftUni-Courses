fruit=input()
size=input()
count=int(input())
price=0
if fruit =='Watermelon':
    if size =='small':
        price=56*2
    else:
        price=28.7*5
elif fruit=='Mango':
    if size =='small':
        price=36.66*2
    else:
        price=19.6*5
elif fruit=='Pineapple':
    if size =='small':
        price=42.1*2
    else:
        price=24.8*5
else:
    if size =='small':
        price=20*2
    else:
        price=15.2*5

sum=price*count
if sum>=400 and sum<=1000:
    sum*=0.85
elif sum >1000:
    sum*=0.5

print(f'{sum:.2f} lv.')