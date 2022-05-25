walk_min=int(input())
walk_per_day=int(input())
calories=int(input())

calories_burn=walk_min*walk_per_day*5

if calories_burn>=calories*0.5:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.')