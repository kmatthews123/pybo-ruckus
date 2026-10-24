class board:
    def __init__(self, name: str, boardsize: tuple):
        self.name = name
        self.boardx = boardsize[0]
        self.boardy = boardsize[1]
    
    def check_on_board(boardsize: board, position: list) -> bool:
        #give this function the board and the bots position
        print( boardsize.boardx, position[1])
        onboard = True
        if position[0] > boardsize.boardx:
            onboard = False
            #print("fell off board")
        if position[1] > boardsize.boardy:
            onboard = False
            #print("fell off board")
        return onboard



class bot:
    def __init__(self, name: str, position: list, health: int, direction: int):
        self.name = name
        self.position =  position
        self.direction = direction
        self.health = health

    def returnbot(inbot: bot) -> dict:
        out = {"name": inbot.name, "position": inbot.position, "health": inbot.health, "direction": inbot.direction}
        return out

    # block below defines movements of bots
    def fwdMv(inbot: bot, distance: int) -> dict:
        if inbot.direction is 0:
            inbot.position[1] += distance
        elif inbot.direction is 1:
            inbot.poition[0] += distance
        elif inbot.direction is 2:
            inbot.position[1] -= distance
        elif inbot.direction is 3:
            inbot.position[0] -= distance
        else:
            raise Exception("thats not a valid direction")
        return inbot

    def rotate(inbot: bot, increment: int) -> dict:    
        return inbot
    
    # def rotate(inbot: bot) -> dict:
    #     pass
    #     #return outbot
    
    # def UTurn(inbot: bot) -> dict:
    #     pass
    #     #return outbot
    
    # def backupOne(inbot: bot) -> dict:
    #     pass
    #     #return outbot

def main():
    gameboard = board("basic", (10, 10))
    jeffbot = bot("gobert", [1,7], 10, 0)
    craigbot = bot("beeboop", [1,7], 10, 5)
    print(bot.returnbot(jeffbot))
    bot.fwdMv(jeffbot, 1)
    bot.fwdMv(jeffbot, 2)
    print(bot.returnbot(jeffbot))
    print(board.check_on_board(gameboard, jeffbot.position))
    bot.fwdMv(jeffbot, 1)
    bot.fwdMv(jeffbot, 1)
    print(jeffbot.position)
    bot.fwdMv(jeffbot, 1)
    bot.fwdMv(jeffbot, 1)
    print(bot.returnbot(jeffbot))
    print(board.check_on_board(gameboard, jeffbot.position))
    #print(bot.returnbot(craigbot))
    #bot.fwdMv(craigbot, 1)

main()