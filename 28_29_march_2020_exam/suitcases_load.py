trunk_capacity=float(input())
command=input()

space_occupied=0
suitcase_count=0
no_more_space=False

while command!='End':
    suitcase_volume=float(command)
    suitcase_count+=1
    if suitcase_count%3==0:
        suitcase_volume*=1.1
    space_occupied+=suitcase_volume
    if space_occupied>trunk_capacity:
        no_more_space=True
        suitcase_count-=1
        break

    command=input()
if no_more_space:
    print('No more space!')
else:
    print('Congratulations! All suitcases are loaded!')
print(f'Statistic: {suitcase_count} suitcases loaded.')