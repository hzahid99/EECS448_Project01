from tkinter import *
import tkinter.font as Font
from functools import partial
#import placeShip
#import placeShipStart
import random

# def board_window():
#     newWindow1 = Toplevel(root)
#     newWindow1.title("")
#     newWindow1.geometry("500x500")
#     entry1 = Entry(newWindow1, justify='center' , font=("Arial", 12), fg="Grey")
#     entry1.pack()
#     newWindow1.mainloop()

    # display = Tk()
    # display.wm_title("BATTLESHIPS")
    # display.configure(background='black')
    # board_font = Font.Font(size=12, weight='normal')
    # label_font = Font.Font(size=11, weight='normal')
    # cell_style ={
    #     "ship_txt": "S",
    #     "ship_color": "red",
    #
    #     "Hit_txt": "X",
    #     "Hit_txt": "red",
    #
    #     "nonHIT_txt": "O",
    #     "nonship_color": "white",
    #
    #     "init_txt": " ",
    #     "init_color": "orange",
    # }
    # global player1_show, player1_play, player2_show, player2_play
    # showlabel()
    #
    # sampleShip_x1 = random.randint(1, 10)
    # sampleShip_y1 = random.randint(1, 10)
    # sampleShip_x2 = random.randint(1, 10)
    # sampleShip_y2 = random.randint(1, 10)
    # demo()
#def get_value():



# create label for each cell
isTurn = True
def player_turn():
    global isTurn
    global player1_show, player1_play, player2_show, player2_play
    if isTurn == True:
        isTurn = False
        for i in range(11):
            for j in range(11):
                if i == 0:
                    player1_show[i][j].configure(fg="black")
                    player1_play[i][j].configure(fg="black")
                    player2_show[i][j].configure(fg="white")
                    player2_play[i][j].configure(fg="white")
                elif j == 0:

                    player1_show[i][j].configure(fg="black")
                    player1_play[i][j].configure(fg="black")
                    player2_show[i][j].configure(fg="white")
                    player2_play[i][j].configure(fg="white")
                else:
                    player1_show[i][j].configure(text=" ", fg="black", bg="black")
                    player1_play[i][j].configure(text=" ", fg="black", bg="black",state = "disable")
                    player2_show[i][j].configure(text="O", fg="black", bg="Orange")
                    player2_play[i][j].configure(text="O", fg="black", bg="Orange",state = "normal")
    else:
        isTurn = True
        for i in range(11):
            for j in range(11):
                if i == 0:
                    player1_show[i][j].configure(fg="white")
                    player1_play[i][j].configure(fg="white")
                    player2_show[i][j].configure(fg="black")
                    player2_play[i][j].configure(fg="black")
                elif j == 0:
                    player1_show[i][j].configure(fg="white")
                    player1_play[i][j].configure(fg="white")
                    player2_show[i][j].configure(fg="black")
                    player2_play[i][j].configure(fg="black")
                else:
                    player1_show[i][j].configure(text="O", fg="black", bg="Orange")
                    player1_play[i][j].configure(text="O", fg="black", bg="Orange",state = "normal")
                    player2_show[i][j].configure(text=" ", fg="black", bg="black")
                    player2_play[i][j].configure(text=" ", fg="black", bg="black",state = "disable")

def Hit_ship(s_x,s_y):
    player_turn()
    global isTurn
    if isTurn == False:
        if  s_x == sampleShip_x1 and s_y == sampleShip_y1:
            player1_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x2 and s_y == sampleShip_y2:
            player1_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x3 and s_y == sampleShip_y3:
            player1_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x4 and s_y == sampleShip_y4:
            player1_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x5 and s_y == sampleShip_y5:
            player1_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        else:
            player1_play[s_x][s_y].configure(text="N", fg="black", bg="Wihte",state = "disable")
    else:
        if  s_x == sampleShip_x6 and s_y == sampleShip_y6:
            player2_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x7 and s_y == sampleShip_y7:
            player2_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x8 and s_y == sampleShip_y8:
            player2_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x9 and s_y == sampleShip_y9:
            player2_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")
        elif s_x == sampleShip_x10 and s_y == sampleShip_y10:
            player2_play[s_x][s_y].configure(text="X", fg="black", bg="Red",state = "disable")

        else:
            player2_play[s_x][s_y].configure(text="N", fg="black", bg="Wihte",state = "disable")
def create_label(lb,txt,x,y):
    if lb == "label":
        label = Label(display, text = txt, width=2, height=1, font=label_font, fg="White", bg="black")
    else:
        label = Button(display, text = txt, width=2, height=1, font=label_font, fg="black", bg="Orange",command = partial(Hit_ship,x,y))
    return label

#
# def test():
#     global player1_show
#     player1_show[9][9].configure(fg="pink",bg="pink")

# build label for each player pannel
def build_bd_axis():
    p1_showboard = []
    p1_playboard = []
    p2_showboard = []
    p2_playboard = []
    for i in range(11):
        #text="A B C D E F G H I J"
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        for j in range(11):
            if i == 0 and j == 0:
                player1_show = create_label("label",' ',i,j)
                player1_play = create_label("label",' ',i,j)
                player2_show = create_label("label",' ',i,j)
                player2_play = create_label("label",' ',i,j)
            elif i == 0:
                player1_show = create_label("label",str(chr(96+j).upper()),i,j)
                player1_play = create_label("label",str(chr(96+j).upper()),i,j)
                player2_show = create_label("label",str(chr(96+j).upper()),i,j)
                player2_play = create_label("label",str(chr(96+j).upper()),i,j)
            elif j == 0:
                player1_show = create_label("label",str(i),i,j)
                player1_play = create_label("label",str(i),i,j)
                player2_show = create_label("label",str(i),i,j)
                player2_play = create_label("label",str(i),i,j)
            else:
                player1_show = create_label("button"," ",i,j)
                player1_show.configure(state = "disable")
                player1_play = create_label("button"," ",i,j)
                player2_show = create_label("button"," ",i,j)
                player2_show.configure(state = "disable")
                player2_play = create_label("button"," ",i,j)
            row1.append(player1_show)
            row2.append(player1_play)
            row3.append(player2_show)
            row4.append(player2_play)
        p1_showboard.append(row1)
        p1_playboard.append(row2)
        p2_showboard.append(row3)
        p2_playboard.append(row4)

    for i in range(11):
        #text="A B C D E F G H I J"
        for j in range(11):
            if i == 0 and j == 0:
                # player1_show, player1_play, player2_show, player2_play  = build_bd_axis(' ', i, j)
                p1_showboard[i][j].grid(row=3 + i, column=4 + j)
                p1_playboard[i][j].grid(row=110 + i, column=4 + j)
                p2_showboard[i][j].grid(row=3 + i, column=17 + j)
                p2_playboard[i][j].grid(row=110 + i, column=17 + j)
            elif i == 0:
                # player1_show, player1_play, player2_show, player2_play  = build_bd_axis(str(chr(96+j).upper()), i, j)
                p1_showboard[i][j].grid(row=3 + i, column=4 + j)
                p1_playboard[i][j].grid(row=110 + i, column=4 + j)
                p2_showboard[i][j].grid(row=3 + i, column=17 + j)
                p2_playboard[i][j].grid(row=110 + i, column=17 + j)
            elif j == 0:
                # player1_show, player1_play, player2_show, player2_play  = build_bd_axis(str(i), i, j)
                p1_showboard[i][j].grid(row=3 + i, column=4 + j)
                p1_playboard[i][j].grid(row=110 + i, column=4 + j)
                p2_showboard[i][j].grid(row=3 + i, column=17 + j)
                p2_playboard[i][j].grid(row=110 + i, column=17 + j)
            else:
                p1_showboard[i][j].grid(row=3 + i, column=4 + j)
                p1_playboard[i][j].grid(row=110 + i, column=4 + j)
                p2_showboard[i][j].grid(row=3 + i, column=17 + j)
                p2_playboard[i][j].grid(row=110 + i, column=17 + j)
    return p1_showboard, p1_playboard, p2_showboard, p2_playboard

def showlabel():
    # title
    label_p1 = Label(display, text="Player 1", font=label_font, fg="white", bg="red")
    label_p1.grid(row=0, column=4, columnspan=10)
    label_p2 = Label(display, text="Player 2", font=label_font, fg="white", bg="blue")
    label_p2.grid(row=0, column=17, columnspan=10)
    # board
    global player1_show, player1_play, player2_show, player2_play
    player1_show, player1_play, player2_show, player2_play  = build_bd_axis()


def placingship_ship(playerboard,s_x,s_y):
    for i in range(1,11):
        for j in range(1,11):
            if i == s_x and j == s_y:

                playerboard[s_x][s_y].configure(textvariable=cell_style, fg="black", bg="Red")
def demo():

    placingship_ship(player1_show,sampleShip_x1,sampleShip_y1)
    placingship_ship(player1_show, sampleShip_x2, sampleShip_y2)
    placingship_ship(player1_show, sampleShip_x3, sampleShip_y3)
    placingship_ship(player1_show, sampleShip_x4, sampleShip_y4)
    placingship_ship(player1_show, sampleShip_x5, sampleShip_y5)

    placingship_ship(player2_show,sampleShip_x6,sampleShip_y6)
    placingship_ship(player2_show, sampleShip_x7, sampleShip_y7)
    placingship_ship(player2_show, sampleShip_x8, sampleShip_y8)
    placingship_ship(player2_show, sampleShip_x9, sampleShip_y9)
    placingship_ship(player2_show, sampleShip_x10, sampleShip_y10)


if __name__ == '__main__':
    display = Tk()
    display.wm_title("BATTLESHIPS")
    display.configure(background='black')
    board_font = Font.Font(size=12, weight='normal')
    label_font = Font.Font(size=11, weight='normal')
    cell_style ={
        "ship_txt": "S",
        "ship_color": "red",

        "Hit_txt": "X",
        "Hit_txt": "red",

        "nonHIT_txt": "O",
        "nonship_color": "white",

        "init_txt": " ",
        "init_color": "orange",
    }
    global player1_show, player1_play, player2_show, player2_play
    showlabel()

    sampleShip_x1 = random.randint(1, 10)
    sampleShip_y1 = random.randint(1, 10)
    sampleShip_x2 = random.randint(1, 10)
    sampleShip_y2 = random.randint(1, 10)
    sampleShip_x3 = random.randint(1, 10)
    sampleShip_y3 = random.randint(1, 10)
    sampleShip_x4 = random.randint(1, 10)
    sampleShip_y4 = random.randint(1, 10)
    sampleShip_x5 = random.randint(1, 10)
    sampleShip_y5 = random.randint(1, 10)
    sampleShip_x6 = random.randint(1, 10)
    sampleShip_y6 = random.randint(1, 10)
    sampleShip_x7 = random.randint(1, 10)
    sampleShip_y7 = random.randint(1, 10)
    sampleShip_x8 = random.randint(1, 10)
    sampleShip_y8 = random.randint(1, 10)
    sampleShip_x9 = random.randint(1, 10)
    sampleShip_y9 = random.randint(1, 10)
    sampleShip_x10 = random.randint(1, 10)
    sampleShip_y10 = random.randint(1, 10)
    demo()

    display.mainloop()
