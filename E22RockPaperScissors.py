def rpsWinner(P1,P2):
    if P1 == P2: 
        return 'tie'
    
    if P1 == 'rock' and P2 == 'scissors':
        return 'player one'
   
    elif P1 == 'paper' and P2 == 'scissors':
        return 'player two'
    
    elif P1 == 'scissors' and P2 =='rock':
        return 'player two'
    
    elif P1 =='paper' and P2 == 'rock':
        return 'player one'
    
    elif P1 == 'rock' and P2 == 'paper':
        return 'player two'
    
    elif P1 =='scissors' and P2 == 'paper':
        return 'player one'
    

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'