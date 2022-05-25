days=int(input())
food=float(input())

cat_all_food=0
dog_all_food=0
biscuits_eaten=0

for day in range(1,days+1):
    dog_eaten_food = float(input())
    cat_eaten_food=float(input())

    cat_all_food+=cat_eaten_food
    dog_all_food+=dog_eaten_food
    if day%3==0:
        biscuits_eaten+=(dog_eaten_food+cat_eaten_food)*0.1


all_eaten_food=cat_all_food+dog_all_food
all_food_perc=all_eaten_food/food*100
cat_all_eaten_food_perc=cat_all_food/all_eaten_food*100
dog_all_eaten_food_perc=dog_all_food/all_eaten_food*100
biscuits=round(biscuits_eaten)

print(f'Total eaten biscuits: {biscuits}gr.')
print(f'{all_food_perc:.2f}% of the food has been eaten.')
print(f'{dog_all_eaten_food_perc:.2f}% eaten from the dog.')
print(f'{cat_all_eaten_food_perc:.2f}% eaten from the cat.')

