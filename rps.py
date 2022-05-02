from random import choice 

move = ['rock', 'paper', 'scissors']
player_previous_moves = [] 
wins = 0
loss = 0
draw = 0
total_games = 0

while True:
    # Pick Computer move
    computer_move = None
    if total_games == 0:
        computer_move == "paper"
    else:
        # Computer move = choice(moves) 
        rock_count = player_previous_moves.count("rock")
        paper_count = player_previous_moves.count("paper")
        scissors_count = player_previous_moves.count("scissors")
        # print(f"rocks: {rock_count} papers: {paper_count} scissors: {scissors_count}")
        
        if rock_count > paper_count and rock_count > scissors_count:
            computer_move = "paper"
            
        elif paper_count > scissors_count and paper_count > scissors_count:
            computer_move = "scissors"
            
        elif scissors_count > paper_count and scissors_count > rock_count:
            computer_move = "rock"
        
        else:
            computer_move = "rock"
        
    # Get player move
    player_move = str(input("Enter move (rock, paper, or scissors: "))
    print("Computer chose " + str((computer_move)))
    while player_move not in move:
        print("Sorry. " + player_move + " is not a valild move:")
    assert player_move in move, f"{player_move} is not in moves"
    player_previous_moves.append(player_move)
    total_games += 1 
    if player_move == "rock":
        
        if computer_move == "paper":
            print("Computer Wins")
            wins += 1
            
        elif computer_move == "rock":
            print("Draw")
            draw += 1 
            
        elif computer_move == "scissors":
            print("Player wins")
            loss += 1 
            
    elif player_move == "paper":
        if computer_move == "paper":
            print("Draw")
            draw += 1 
            
        elif computer_move == "rock":
            print("player wins")
            loss += 1 
            
        elif computer_move == "scissors":
            print("Computer wins")
            wins += 1 
            
    elif player_move == "scissors":
        if computer_move == "paper":
            print("Player Wins")
            loss += 1 
            
        elif computer_move == "rock":
            print("Computer Wins")
            wins += 1 
            
        elif computer_move == "scissors":
            print("Draw")
            draw += 1 
    print("Wins: " + str(wins) + " Loss: " + str(loss) + " Draw: " + str(draw))
    print("Computer win rate: " + str(wins/total_games))
    print(f"Previous moves: {player_previous_moves}")
    