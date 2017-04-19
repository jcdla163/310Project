from socket import *

#argv = sys.argv
#host = argv[1]
host = 'localhost'
#port = int(argv[2])
port = int(6958)
clientSocket = socket(AF_INET,SOCK_DGRAM)
count = 0

def help():
    print("The available methods are:\nlogin: It takes 1 argument which is used as the User ID.\nplace: It takes 1 argument which issues a move for an unoccupied position.\nexit: player exits the server at any time.")

def login(name):
    clientSocket.sendto(name.encode(),(host,port))

def place(number):
    clientSocket.sendto(number.encode(),(host,port))

def exit():
    clientSocket.close()


while True:
    action = str(input("What would you like to do? "))
    if action == "help":
        help()
        continue
    elif action == "login":
        login(str(input("Enter User ID: ")))
        break

message, address = clientSocket.recvfrom(1024)
message = message.decode()
print(message)

while True:
     if count <= 9:
        place(input("Where would you like to go? "))
     else:
         False
