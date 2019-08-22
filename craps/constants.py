
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
CRAPS_FIRST_BOARD = "Point: None\nDice: None\nMoney: 1000"
BET_PLACED_SUCCESFULLY = "Your bet was placed successfully: PASS_BET"
CRAPS_SHOW_BET = "Point: None\n" \
    "Dice: None\n" \
    "Bet:\n" \
    "Bet type: PassBet\n" \
    "Amount bet: 200\n" \
    "Amount payed: 0\n" \
    "Bet state: Bet in progress\n" \
    "Money: 800" \

CRAPS_DICE = 'Point: None\nDice: (3, 4)\nBet:\nBet type: PassBet\nAmount bet: 200\nAmount payed: 400\nBet state: Payed\nMoney: 1200'
