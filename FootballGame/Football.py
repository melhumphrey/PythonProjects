import random

players = {"Brett  " : 0, "Marilyn" : 0, "Mel    " : 0, "Joe    " : 0, "Maddie " : 0, "Marcus " : 0}
board = list(range(10))
limit = 100 // len(list(players.keys()))
print(limit)
remainder = 100 % len(list(players.keys()))
print(remainder)
for col in range(10):
    board[col] = list(range(10))
    for row in range(10):
        choice = random.choice(list(players.keys()))
        board[col][row] = choice
        players[choice] += 1
        if ((players[choice] == limit + 1) or (players[choice] == limit and len(list(players.keys())) > remainder)):
            del players[choice]
for col in range(10):
    row_str = ""
    for row in range(10):
        row_str += str(board[col][row])  + "  "
    print(row_str)
