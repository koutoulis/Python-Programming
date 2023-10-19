
import array
from random import randint

############ basikes sunarthseis ############
positions = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
board=[[" "," "," "],[" "," "," "],[" "," "," "]]

def player_mark(x): #gia na dinei ston paixth x h o 
    if x==1:
        return "x"
    elif x==2:
        return "o"

def player_switch(x):#gia na enallasei tous xrhstes
    if x==1:
        return 2
    elif x==2:
        return 1
def print_board(): #ektypwsh toy board
    print("  1   2   3")
    print("A "+board[0][0]+"---"+board[0][1]+"---"+board[0][2])
    print("  |\  |  /|")
    print("  | \ | / |")
    print("  |  \|/  |")
    print("B "+board[1][0]+"---"+board[1][1]+"---"+board[1][2])
    print("  |  /|\  |")
    print("  | / | \ |")
    print("  |/  |  \|")
    print("C "+board[2][0]+"---"+board[2][1]+"---"+board[2][2])

def is_winner(): #dinei shma true an uparxei nikh
    
    #rows
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]=="x" or board[i][0]==board[i][1]==board[i][2]=="o":
            win=True

            return win
    
    #columns
    for i in range(0,3):
        if board[0][i]==board[1][i]==board[2][i]=="x" or board[0][i]==board[1][i]==board[2][i]=="o":
            win=True
            return win
        
    
    #diagonal
    if board[0][0]==board[1][1]==board[2][2]=="x" or board[0][2]==board[1][1]==board[2][0]=="x" or board[0][0]==board[1][1]==board[2][2]=="o" or board[0][2]==board[1][1]==board[2][0]=="o":
            win=True
            return win

############ Prwto meros: Afethria ############
def place_mark(string, player_num): #sunarthsh pou ejetazei kathe periptwsh gia na balei sto board ta 3 pionia tou kathe paixth sthn afethria
    
    if (len(string)==2) and (string in positions):
        if string=="A1" and board[0][0]==" ":
            board[0][0] = player_mark(player_num)
            while is_winner():
                board[0][0] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="A2" and board[0][1]==" ":
            board[0][1] = player_mark(player_num)
            while is_winner():
                board[0][1] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="A3" and board[0][2]==" ":
            board[0][2] = player_mark(player_num)
            while is_winner():
                board[0][2] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="B1" and board[1][0]==" ":
            board[1][0] = player_mark(player_num)
            while is_winner():
                board[1][0] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="B2" and board[1][1]==" ":
            board[1][1] = player_mark(player_num)
            while is_winner():
                board[1][1] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="B3" and board[1][2]==" ":
            board[1][2] = player_mark(player_num)
            while is_winner():
                board[1][2] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="C1" and board[2][0]==" ":
            board[2][0] = player_mark(player_num)
            while is_winner():
                board[2][0] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="C2" and board[2][1]==" ":
            board[2][1] = player_mark(player_num)
            while is_winner():
                board[2][1] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        elif string=="C3" and board[2][2]==" ":
            board[2][2] = player_mark(player_num)
            while is_winner():
                board[2][2] = " "
                print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                return False
            return True
        else:
            print("Position taken by another peg. Please re-enter.")
            return False
    
    else:
        print("Invalid position. Not a board position. Please re-enter.")
        return False

def initialize(player_num): #ta bhmata pou prepei na ginoun gia na balei enas paixths pionia sthn afethria
    for i in range(1,4):
        move=str(input("Player "+str(player_num)+" peg no. "+ str(i)+". Enter the board position to put your peg: "))
        
        while place_mark(move, player_num)== False:
            move=str(input("Player "+str(player_num)+" peg no. "+ str(i)+". Enter the board position to put your peg: "))
        print_board()

def set_places(player_num): #odhgies afethrias
    initialize(player_num)
    player_num=player_switch(player_num)
    initialize(player_num)
    player_num=player_switch(player_num)

############ Deutero meros: Paixnidi ###########
def get_board_place(input):
    if input=="A1":
        return board[0][0]
    elif input=="B1":
        return board[1][0]
    elif input=="C1":
        return board[2][0]
    elif input=="A2":
        return board[0][1]
    elif input=="B2":
        return board[1][1]
    elif input=="C2":
        return board[2][1]
    elif input=="A3":
        return board[0][2]
    elif input=="B3":
        return board[1][2]
    elif input=="C3":
        return board[2][2]


def check_valid_move(makemove): #elegxei an h kinhsh pou dinei o xrhsths einai egkyrh elegxontas kathe periptwsh kai ektuponwntas to antistoixo mhnyma
    origin=makemove[0:2]
    destination=makemove[2:4]
    if len(makemove)==4 and ((origin in positions) and (destination in positions)) and origin!=destination:
        if is_connected(origin, destination):
            origins_mark=get_board_place(origin)
            destinations_mark=get_board_place(destination)
            if origins_mark==" " or origins_mark!=player_mark(player_num):
                print("Invalid move. Origin is not occupied by player's "+str(player_num)+" peg")
                return False
            elif destinations_mark!=" ":
                print("Invalid move. Destination position is not empty. Please re-enter move.")
                return False
            else:
                
                move_mark(origin, destination, player_num)
                return True
        else:
            print("Invalid move. Destination position is not connected to origin position. Please re-enter move.")
            return False
    else:
        print("Invalid move. Enter origin and destination positions in 4 characters, e.g., A2B1")
        return False
        
def is_connected(origin, destination): #elegxei an origin k destination einai theseis sundedemenes
    if origin=="A1" and (destination=="B1" or destination=="A2" or destination=="B2"):
        return True
    elif origin=="A2" and (destination=="A1" or destination=="B2" or destination=="A3"):
        return True
    elif origin=="A3" and (destination=="A2" or destination=="B2" or destination=="B3"):
        return True
    elif origin=="B1" and (destination=="A1" or destination=="B2" or destination=="C1"):
        return True
    elif origin=="B2":
        return True
    elif origin=="B3" and (destination=="A3" or destination=="B2" or destination=="C3"):
        return True
    elif origin=="C1" and (destination=="B1" or destination=="C2" or destination=="B2"):
        return True
    elif origin=="C2" and (destination=="C1" or destination=="B2" or destination=="C3"):
        return True
    elif origin=="C3" and (destination=="B3" or destination=="C2" or destination=="B2"):
        return True

def move_mark(origin, destination, player_num): # sunarthsh pou metakinei ta pionia, bazontas to pioni tou paixth sto destination kai katharizontas to origin
    
    if destination=="A1":
        board[0][0] = player_mark(player_num)
    elif destination=="A2":
        board[0][1] = player_mark(player_num)
    elif destination=="A3":
        board[0][2] = player_mark(player_num)
    elif destination=="B1":
        board[1][0] = player_mark(player_num)
    elif destination=="B2":
        board[1][1] = player_mark(player_num)
    elif destination=="B3":
        board[1][2] = player_mark(player_num)
    elif destination=="C1":
        board[2][0] = player_mark(player_num)
    elif destination=="C2":
        board[2][1] = player_mark(player_num)
    elif destination=="C3":
        board[2][2] = player_mark(player_num)
    
    
    if origin=="A1":
        board[0][0] = " "
    elif origin=="A2":
        board[0][1] = " "
    elif origin=="A3":
        board[0][2] = " "
    elif origin=="B1":
        board[1][0] = " "
    elif origin=="B2":
        board[1][1] = " "
    elif origin=="B3":
        board[1][2] = " "
    elif origin=="C1":
        board[2][0] = " "
    elif origin=="C2":
        board[2][1] = " "
    elif origin=="C3":
        board[2][2] = " "

def print_winner(): #ektypwsh tou nikhth
    
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]=="x" :
            print("Player 1 wins!")
            
        elif board[i][0]==board[i][1]==board[i][2]=="o":
            print("Player 2 wins!")
            
        elif board[0][i]==board[1][i]==board[2][i]=="x":
            print("Player 1 wins!")
            
        elif board[0][i]==board[1][i]==board[2][i]=="o":
            print("Player 2 wins!")
        
    if board[0][0]==board[1][1]==board[2][2]=="x" or board[0][2]==board[1][1]==board[2][0]=="x":
        print("Player 1 wins!")
    elif board[0][0]==board[1][1]==board[2][2]=="o" or board[0][2]==board[1][1]==board[2][0]=="o":
        print("Player 2 wins!")


### KLHSH PAIXNIDIOU
play_again="y"
while play_again=="Y" or play_again=="y" or play_again=="yes":

    player_num=randint(1,2)
    
    print("Player "+str(player_num)+" starts first.")

    
    
    print_board()
    
    ##prwto meros: dialegoume tuxaia prwto paixth,
    ##zhtame na balei ta 3 pionia sthn afethria, elegxontas thn egkyrothta, allazoume ton paixth kai epanalambanetai
    
    set_places(player_num)
    
    ##deutero meros: ksekinaei to paixnidi, oi paixtes bazoun egkyres kinhseis mexri na bgei nikh gia kapoion##
    while is_winner()!=True:
        
        makemove=str(input("Player "+str(player_num)+" enter your move: "))	
        while check_valid_move(makemove)==False:
            makemove=str(input("Player "+str(player_num)+" enter your move: "))
        print_board()
        
        player_num=player_switch(player_num)
        
        
        
      
    
    
    ##trito meros: ektypwnoume nikhth, 'katharizoume' to board kai rwtame an theloun na paijoun jana## 
    print_winner() 
    board=[[" "," "," "],[" "," "," "],[" "," "," "]] #katharismos tou board
    play_again=str(input("Type 'Y' or 'y' to play again: ")) #erwthsh an thelei na janapaijei o xrhsths




   



    








