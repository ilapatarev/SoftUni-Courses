import math
record=float(input())
distance=float(input())
time_for_one_m_climb=float(input())

time_for_climb=distance*time_for_one_m_climb+((math.floor(distance/50))*30)
if time_for_climb<record:
    print(f'Yes! The new record is {time_for_climb:.2f} seconds.')
else:
    diff=abs(record-time_for_climb)
    print(f'No! He was {diff:.2f} seconds slower.')