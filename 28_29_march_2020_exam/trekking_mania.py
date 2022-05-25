groups_count=int(input())

mousala_count=0
monblan_count=0
kilimandjaro_count=0
k2_count=0
everest_count=0

for group in range(1, groups_count+1):
    people=int(input())
    if people<=5:
        mousala_count+=people
    elif people<=12:
        monblan_count+=people
    elif people<=25:
        kilimandjaro_count+=people
    elif people<=40:
        k2_count+=people
    else:
        everest_count+=people
all_people=monblan_count+mousala_count+k2_count+kilimandjaro_count+everest_count
mousala_perc=mousala_count/all_people*100
monblan_perc=monblan_count/all_people*100
kilimandjaro_perc=kilimandjaro_count/all_people*100
k2_perc=k2_count/all_people*100
everest_perc=everest_count/all_people*100

print(f'{mousala_perc:.2f}%')
print(f'{monblan_perc:.2f}%')
print(f'{kilimandjaro_perc:.2f}%')
print(f'{k2_perc:.2f}%')
print(f'{everest_perc:.2f}%')


        