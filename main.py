import os
import signal
import random

class AlarmException(Exception):
    pass
class Snake:
    def __init__(self):
        self.score = 0
        self.gameOver = False
        self.gameMap = [["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
        self.snakeHead = ">"
        self.snakePos = [0,5]
        self.currDir = "d"
        self.applePos = [6,8]
        self.appleEaten = False


    def alarmHandler(self, signum, frame):
        raise AlarmException


    def timedInput(self, prompt='', timeout=20):
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.alarm(timeout)
        try:
            text = input(prompt)
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return self.currDir
    
    def printMap(self):
        for i in range(len(self.gameMap)):
            for j in range(len(self.gameMap[i])):
                if i == self.snakePos[0] and j == self.snakePos[1]:
                    print(f"\033[1;32;40m{self.snakeHead}", end=" ", flush=True)
                elif i == self.applePos[0] and j == self.applePos[1]:
                    print("\033[1;31;40mo", end=" ", flush=True)
                else:
                    print(f"\033[1;37;40m{self.gameMap[i][j]}", end = " ", flush=True)
            print()
    
    def move(self, direction):
        if direction == "w" and self.currDir != "s":
            self.snakePos[0] -= 1
            self.snakeHead = "^"
            self.currDir = "w"
        elif direction == "s" and self.currDir != "w":
            self.snakePos[0] += 1
            self.snakeHead = "v"
            self.currDir = "s"
        elif direction == "a" and self.currDir != "d":
            self.snakePos[1] -= 1
            self.snakeHead = "<"
            self.currDir = "a"
        elif direction == "d" and self.currDir != "a":
            self.snakePos[1] += 1
            self.snakeHead = ">"
            self.currDir = "d"
        else:
            self.move(self.currDir)
    
    def checkForApple(self):
        if self.snakePos[0] == self.applePos[0] and self.snakePos[1] == self.applePos[1]:
            self.appleEaten = True
            self.score += 1
            self.placeApple()
    
    def placeApple(self):
        while True:
            x = random.randint(0, len(self.gameMap)-1)
            y = random.randint(0, len(self.gameMap[0])-1)
            if x != self.snakePos[0] and y != self.snakePos[1]:
                self.applePos = [x,y]
                break
    
    def detectEdgeCollision(self):
        if self.snakePos[0] > (len(self.gameMap) -1) or self.snakePos[0] < 0 or self.snakePos[1] > (len(self.gameMap[0]) -1) or self.snakePos[1] < 0:
            return True
        return False
    
    def detectCollision(self):
        if self.detectEdgeCollision():
            self.gameOver = True
    
    def playGame(self):
        while(not self.gameOver):
            os.system("printf '\33c\e[3J'")
            self.checkForApple()
            self.printMap()
            print(self.score)
            move = self.timedInput(timeout=1)
            self.move(move)
            self.detectCollision()
        print("\033[1;31;40mGame Over")

mySnake = Snake()
mySnake.playGame()