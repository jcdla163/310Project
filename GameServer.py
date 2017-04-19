from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",6958))
player = []
busy = []

def currentGame(player1,player2):
    turn = 1
    print('6')
    field = ['.','.','.','.','.','.','.','.','.']
    serverSocket.sendto(('Opponent: ' + player1[0]).encode(),(player2[1]))
    print('7')
    serverSocket.sendto(('Opponent: ' + player2[0]).encode(),(player1[1]))
    print('8')
    while True:
        serverSocket.sendto((field[0]+field[1]+field[2]+"\n"+
                             field[3]+field[4]+field[5]+"\n"+
                             field[6]+field[7]+field[8]).encode(),player1[1])
        serverSocket.sendto((field[0]+field[1]+field[2]+"\n"+
                             field[3]+field[4]+field[5]+"\n"+
                             field[6]+field[7]+field[8]).encode(),player2[1])
        if turn == 1 or turn % 2 != 0:
            space, address = serverSocket.recvfrom(1024,(player1[1]))
            field.insert(space,"X")
            field.remove(space+1,"X")
            turn = turn + 1
        elif turn % 2 == 0:
            space, address = serverSocket.recvfrom(1024,(player2[1]))
            field.insert(space,"X")
            field.remove(space+1,"X")
            turn = turn + 1

while True:
    print('wait')
    temp, address = serverSocket.recvfrom(1024)
    temp = temp.decode()
    print("1")
    player.append((temp,address))
    if len(player) == 2:
        print("5")
        busy.append(player[0])
        busy.append(player[1])
        currentGame(player[0],player[1])
        busy.remove(player[0])
        busy.remove(player[1])
        print("9")
    elif len(player) == 1:
        print("2")
        serverSocket.sendto(("Waiting for player 2.").encode(),address)
        print("3")
        continue





