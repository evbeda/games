
# Commands
GO_COMMAND = 'GO'
NO_COMMAND = 'NO'

# Losing Scores
LOSING_SCORES = [2, 3, 12]
WINNING_SCORES = [7, 11]

# Game states
GAME_STARTED = 'GAME_STARTED'
GAME_IN_PROGRESS = 'GAME_IN_PROGRESS'
GAME_OVER = 'Game Over'
PLAYER_LOST = 'PLAYER_LOST'
PLAYER_WON = 'PLAYER_WON'

# Messages
WON_MESSAGE = 'You won. Do you want to keep playing?'
LOST_MESSAGE = 'You lost. Do you want to keep playing?'
BET_MESSAGE = '\nEnter a bet type, amount of bet and value of bet(optional)'
BET_PLACED = 'Your bet was placed successfully: '
INVALID_BET_TYPE = 'Invalid bet type'
OUT_OF_CASH = "You don't have enough money"
CAN_NOT_LEAVE = "You can't leave until the turn ends. "
INVALID_TURN_BET = "You can't make this bet in this turn"
SHOOT_DICE_MESSAGE = 'Write Go to shoot the dice'
BET_AGAIN_OR_GO = 'Bet again or go'
INVALID_INPUT = 'Invalid input, try again'

# Bet States
BET_IN_PROGRESS = 'Bet in progress'
BET_PAYED = 'Payed'
BET_LOST = 'Lost'

# Bet Names
PASS_BET = 'PASS_BET'
DO_NOT_PASS_BET = 'DO_NOT_PASS_BET'
DOUBLE_BET = 'DOUBLE_BET'
SEVEN_BET = 'SEVEN_BET'
CRAPS_BET = 'CRAPS_BET'
DOUBLE_SEVEN = 'DOUBLE_SEVEN'

# Integration Test
CRAPS_FIRST_BOARD = "\nPoint: -\nDice: No dices played\nMoney: 1000\n"
BET_PLACED_SUCCESFULLY = "Your bet was placed successfully: PASS_BET"
# CRAPS_SHOW_BET = '''
# Point: 0
# Dice: No dices played
# Bet:
# Bet type: PassBet
# Amount bet: 200
# Amount payed: 0
# Bet state: Bet in progress
# Money: 800
# '''
CRAPS_SHOW_BET = "\nPoint: -\nDice: No dices played\nBet:\n\tBet type: PassBet\n\tAmount bet: 200\n\tAmount payed: 0\n\tBet state: Bet in progress\nMoney: 800\n"
CRAPS_DICE = "\nPoint: -\nDice: (3, 4)\nBet:\n\tBet type: PassBet\n\tAmount bet: 200\n\tAmount payed: 400\n\tBet state: Payed\nMoney: 1200\n"
# CRAPS_DICE_FINISH = "\nPoint: 0\nDice: (3, 4)\nBet:\n\tBet type: PassBet\n\tAmount bet: 200\n\tAmount payed: 400\n\tBet state: Payed\nMoney: 1200\n"
