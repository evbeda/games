SUCCESS_MESSAGE = 'Your bet was saved succesfully'
NOT_ENOUGH_CASH_MESSAGE = 'You do not have enough cash!'
INVALID_BET_MESSAGE = 'Your bet is invalid'
INVALID_BET_TYPE_MESSAGE = 'Your bet type is invalid'
BYE_MESSAGE = 'Bye'
END_GAME_COMMAND = 'END_GAME'
GO_COMMAND = 'GO'
GO_END_COMMAND = '\n' + GO_COMMAND + ',\n' + END_GAME_COMMAND
WON_MESSAGE = 'You won: '
LOST_MESSAGE = 'You lost'
EXAMPLE_BOARD = \
        "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
        "|00|03|06|09|12|15|18|21|24|27|30|33|36|\n" +\
        "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
        "|00|02|05|08|11|14|17|20|23|26|29|32|35|\n" +\
        "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
        "|00|01|04|07|10|13|16|19|22|25|28|31|34|\n" +\
        "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n"
EXAMPLE_SHOWN_BOARD_NO_BET = \
        EXAMPLE_BOARD +\
        "Player Money: $100\n" +\
        "Placed Bets: \n" +\
        "No bets" #+\
        # "STRAIGHT_BET, COLOR_BET, EVENODD_BET, LOWHIGH_BET, STREET_BET, SIXLINE_BET, DOUBLE_BET,\
        #         ONEDOZEN_BET, TWODOZEN_BET, TRIO_BET, QUADRUPLE_BET" +\
        # "GO,"
EXAMPLE_SHOWN_BOARD_BET = \
        EXAMPLE_BOARD +\
        "Player Money: $60\n" +\
        "Placed Bets: \n" +\
        "STRAIGHT_BET 20, bet $40" #+\
        # "STRAIGHT_BET, COLOR_BET, EVENODD_BET, LOWHIGH_BET, STREET_BET, SIXLINE_BET, DOUBLE_BET,\
        #         ONEDOZEN_BET, TWODOZEN_BET, TRIO_BET, QUADRUPLE_BET" +\
        # "GO,"
EXAMPLE_SHOWN_BOARD_WON_BET = \
        EXAMPLE_BOARD +\
        "Player Money: $1460\n" +\
        "Placed Bets: \n" +\
        "No bets" #+\
        # "STRAIGHT_BET, COLOR_BET, EVENODD_BET, LOWHIGH_BET, STREET_BET, SIXLINE_BET, DOUBLE_BET,\
        #         ONEDOZEN_BET, TWODOZEN_BET, TRIO_BET, QUADRUPLE_BET" +\
        # "GO,"
EXAMPLE_SHOW_BOARD_END_GAME = \
        EXAMPLE_BOARD +\
        "Player Money: $1460\n" +\
        "Placed Bets: \n" +\
        "No bets" #+\
        
