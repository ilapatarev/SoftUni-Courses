food_bought=int(input())

food_left=food_bought*1000
eaten_food=0
command=input()
while command!='Adopted':
    dailly_eaten=int(command)
    eaten_food+=dailly_eaten

    command=input()

diff=abs(food_left-eaten_food)
if food_left>=eaten_food:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')
