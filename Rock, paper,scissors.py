def gameplay(userinput1,userinput2):
    if userinput1 == 'Rock' and userinput2 == 'Scissors':
        print('Player 1 win')
    elif userinput1 == 'Rock' and userinput2 == 'Paper':
        print('Player 2 win')
    elif userinput1 == 'Rock' and userinput2 == 'Rock':
        print('Tie')
    elif userinput1 == 'Paper' and userinput2 == 'Rock':
        print('Player 1 win')
    elif userinput1 =='Paper' and userinput2 == 'Scissors':
        print('Player 2 win')
    elif userinput1 =='Paper' and userinput2 == 'Paper':
        print('Tie')
    elif userinput1 == 'Scissors' and userinput2 == 'Paper':
        print('Player 1 win')
    elif userinput1 == 'Scissors' and userinput2 == 'Rock':
        print('Player 2 win')
    elif userinput1 =='Scissors' and  userinput2 == 'Scissors':
        print('Tie')

def replay():
    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')

while True:
    userinput1 = str(input('Your are player1, Enter Rock, Scissors or Paper :'))
    userinput2 = str(input('Your are player2,Enter Rock, Scissors or Paper :'))
    gameplay(userinput1,userinput2)
    if replay() == False:
        break






