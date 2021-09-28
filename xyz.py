# def getFactors(n):
#     factors = [ ]
#     for num in range(1, n+1):# num is a possible factor
#         if n % num == 0:
#             factors.append(num)
#     return factors
# print(getFactors(6))

gameBoard = [ ["X", " ", "O"], [" ", "X", " "], [" ", " ", "O"] ]
for row in range(len(gameBoard)): # each row is a list
    boardString = ""
    for col in range(len(gameBoard[row])): # each col is a string
        boardString = boardString + gameBoard[row][col]
    print(boardString) # separate rows on separate lines
