from collections import OrderedDict
import requests
from time import sleep
from colorama import Fore
from os import system


def main():
    try:
        system("cls")
        board = loadBoard()
        printBoard(board)
        print("~~~~~~~~")
        while True:
            ans = getAlerts()
            if (type(ans) != bool):
                for alert in ans["data"]:
                    if (alert == "שהם"):
                        print(Fore.RED + alert[::-1] + Fore.RESET)
                    else:
                        print(alert[::-1])
                    for item in range(len(board)):
                        if (alert in board[item]):
                            board[item][alert] = "1"
                updateFile(board)
                print("~~~~~~~~~~")
                printBoard(board)    
            sleep(0.2)
    except Exception as e:
        print("Error!", e) 

def updateFile(board):
    fil = open("board.txt", 'r+', encoding='utf-8')
    fil.seek(fil.seek(0, 2) - 15, 0)
    for line in board:
        fil.write("\n" + "".join(line.values()))
    fil.close()


def loadBoard():
    fil = open("board.txt", 'r', encoding='utf-8')
    board = fil.read()
    fil.close()
    boolBoard = board[board.find("\n\n"):].split()
    cityBoard = board[:board.find("\n\n")].split('\n')
    board = []
    for i in range(len(cityBoard)):
        board += [OrderedDict()]
        for city in range(len(cityBoard[i].split("#"))):
            board[i][cityBoard[i].split('#')[city]] = list(boolBoard[i])[city]
    return board


def printBoard(board):
    for item in board:
        toPrint = ""
        for city, check in item.items():
            if (check == '0'):
                toPrint += Fore.RED
            else:
                toPrint += Fore.GREEN
            toPrint += city[::-1] + "   "
        print(toPrint + Fore.RESET)


def getOldAlerts(): 
    newAlerts = []
    server = "https://www.oref.org.il/WarningMessages/History/AlertsHistory.json"
    ans = requests.get(server).json()
    newAlerts = []
        
    lastAns = ans[0]
    while True:  # looping :)
        ans = requests.get(server).json()
        if (ans[0] != lastAns):
            i = 0
            while (lastAns != ans[i]):  # adding new alerts
                newAlerts += [ans[i]]
                i += 1
            lastAns = ans[0]  # reset last alert
            for i in newAlerts:
                print(i["data"][::-1])
            
            print("~~~~~~~~~~")
        
        sleep(0.2)

def getAlerts():
    url = 'https://www.oref.org.il/WarningMessages/alert/alerts.json'
    headers = {'Referer': 'https://www.oref.org.il/', 'X-Requested-With': 'XMLHttpRequest'}
    ans = requests.get(url, headers=headers)
    if (ans.text.strip() != ""):
        return ans.json()
    return False


if __name__ == "__main__":
    main()
