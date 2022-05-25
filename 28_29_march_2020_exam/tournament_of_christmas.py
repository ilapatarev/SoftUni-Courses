days=int(input())
games_won_dailly=0
games_lost_dailly=0
money_raised=0
days_winner=0
days_loser=0
days_money=0
tournament_won=False
for day in range(1,days+1):
    sport=input()
    while sport!='Finish':
        result=input()
        if result=='win':
            days_money+=20
            games_won_dailly+=1
        else:
            games_lost_dailly+=1

        sport=input()
    if games_won_dailly>games_lost_dailly:
        days_winner+=1
        days_money*=1.1
    else:
        days_loser+=1
    money_raised+=days_money
    days_money=0
    games_won_dailly=0
    games_lost_dailly=0

if days_winner>days_loser:
    tournament_won=True
    money_raised*=1.2
if tournament_won:
    print(f'You won the tournament! Total raised money: {money_raised:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money_raised:.2f}')