from tkinter import *

FONT_NAME = "Courier"
SCREEN_COLOR = "#94ebcd"
LABEL_COLOR = "#6ddccf"


def enable_btns():
    for row in range(3):
        for col in range(3):
            btns[row][col]["state"] = "normal"


def disable_btns():
    for row in range(3):
        for col in range(3):
            btns[row][col]["state"] = "disabled"


def is_won(player):
    # row wise
    for row in range(3):
        if btns[row][0]['text'] == player and btns[row][1]['text'] == player and btns[row][2]['text'] == player:
            return True

    # col wise
    for col in range(3):
        if btns[0][col]['text'] == player and btns[1][col]['text'] == player and btns[2][col]['text'] == player:
            return True

    # diagonal wise
    if btns[0][0]['text'] == player and btns[1][1]['text'] == player and btns[2][2]['text'] == player:
        return True
    if btns[0][2]['text'] == player and btns[1][1]['text'] == player and btns[2][0]['text'] == player:
        return True

    return False


def btn_clicked(a, b):
    global turn, count_moves
    if btns[a][b]["text"] == "":
        if turn:
            btns[a][b].config(text="X")
            if is_won("X"):
                winner.config(text="X won!")
                disable_btns()
        else:
            btns[a][b].config(text="O")
            if is_won("O"):
                winner.config(text="O won!")
                disable_btns()

        count_moves += 1
        turn = not turn

    if count_moves == 9:
        winner.config(text="Game is draw")
        disable_btns()


def restart():
    global turn, count_moves
    for row in range(3):
        for col in range(3):
            btns[row][col].config(text="")

    enable_btns()
    winner.config(text="Tic tac toe")
    turn = True
    count_moves = 0


# screen
screen = Tk()
screen.config(padx=50, pady=50, bg=SCREEN_COLOR)
screen.title("Tic tac toe")

# labels
winner = Label(text="Tic tac toe", font=(FONT_NAME, 35, "bold"), width=16, bg="#94ebcd")
winner.grid(row=0, column=0, columnspan=3, pady=2)


# buttons
btns = []
for i in range(3):
    temp = []
    for j in range(3):
        btn = Button(text=f"", font=(FONT_NAME, 35, "bold"), bg="white", width=5, height=2)
        btn.grid(row=i+1, column=j)
        temp.append(btn)
    btns.append(temp)

btns[0][0].config(command=lambda: btn_clicked(0, 0))
btns[0][1].config(command=lambda: btn_clicked(0, 1))
btns[0][2].config(command=lambda: btn_clicked(0, 2))
btns[1][0].config(command=lambda: btn_clicked(1, 0))
btns[1][1].config(command=lambda: btn_clicked(1, 1))
btns[1][2].config(command=lambda: btn_clicked(1, 2))
btns[2][0].config(command=lambda: btn_clicked(2, 0))
btns[2][1].config(command=lambda: btn_clicked(2, 1))
btns[2][2].config(command=lambda: btn_clicked(2, 2))

start_again_btn = Button(text="Restart", font=(FONT_NAME, 20, "bold"), width=10, command=restart, bg=LABEL_COLOR)
start_again_btn.grid(row=4, column=0, columnspan=3, pady=10)

turn = True
count_moves = 0

screen.mainloop()
